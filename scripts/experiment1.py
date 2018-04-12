import pyglet
import ratcave as rc
import events
import cfg

from glob import glob
from os import path
from numpy import random

# Create Window
window = pyglet.window.Window()

def update(dt):
    pass
pyglet.clock.schedule(update)

# Insert filename into WavefrontReader.
obj_filename = 'scripts/assets/2.obj'  # hollow cylinder
obj_reader = rc.WavefrontReader(obj_filename)


# Create Mesh
cylinder = obj_reader.get_mesh("hollow_Cylinder", scale=.6)
cylinder.position.xyz = cfg.CYLINDER_POSITION
cylinder.rotation.x = cfg.CYLINDER_ROTATION_X
cylinder.uniforms.diffuse = 1., 1., 1.

texture = rc.Texture.from_image(cfg.CYLINDER_TEXTURE)
cylinder.textures.append(texture)
cylinder.speed = 0


# Shader
vertname = glob(path.join(rc.resources.shader_path, 'default', '*.vert'))[0]
fragname = glob(path.join(rc.resources.shader_path, 'default', '*.frag'))[0]
shader = rc.Shader.from_file(vert=vertname, frag=fragname)


# Create Scene
scene = rc.Scene(meshes=[cylinder])
scene.gl_states = scene.gl_states[:-1]
scene.bgColor = (0., 0., 0.)


# Build experiment event sequence
seq = [events.update_attribute(cylinder, 'visible', False),
       events.wait_duration(cfg.START_TIME)]

for speed in random.permutation(cfg.CYLINDER_SPEEDS * 2):
    for direction in [1, -1]:
        phase_seq = [
            events.update_attribute(cylinder, 'visible', True),
            events.update_attribute(cylinder, 'speed', speed * direction),
            events.wait_duration(cfg.PHASE_DURATION_SECS),
            events.update_attribute(cylinder, 'visible', False),
            events.wait_duration(cfg.WAIT_DURATION_SECS),
        ]
        seq.extend(phase_seq)

def rotate_cylinder(dt):
    global cylinder
    cylinder.rotation.y += cylinder.speed * dt
pyglet.clock.schedule(rotate_cylinder)


exp = events.chain_events(seq)
next(exp)

@window.event
def on_draw():
    with rc.default_shader:
        scene.draw()


pyglet.clock.schedule(exp.send)
pyglet.app.run()
