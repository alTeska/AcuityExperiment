import pyglet
import ratcave as rc
import events

from glob import glob
from os import path


# Create Window
window = pyglet.window.Window()

def update(dt):
    pass
pyglet.clock.schedule(update)

# Insert filename into WavefrontReader.
# obj_filename = rc.resources.obj_primitives
obj_filename = 'assets/2.obj'  # hollow cylinder
obj_reader = rc.WavefrontReader(obj_filename)


# Create Mesh
cylinder = obj_reader.get_mesh("hollow_Cylinder", scale=.6)
cylinder.dynamic = True
cylinder.position.xyz = 0, 0, -2
cylinder.rotation.x = 90
cylinder.uniforms['diffuse'] = 1., 1., 1.



texture = rc.Texture.from_image('assets/pict.png')
cylinder.textures.append(texture)
cylinder.speed = 0


vertname = glob(path.join(rc.resources.shader_path, 'default', '*.vert'))[0]
fragname = glob(path.join(rc.resources.shader_path, 'default', '*.frag'))[0]
shader = rc.Shader.from_file(vert = vertname, frag = fragname)


# Create Scene
scene = rc.Scene(meshes=[cylinder])
scene.gl_states = scene.gl_states[:-1]

# Create Sequence
seq = [events.update_attribute(cylinder, 'speed', -20),
       events.wait_duration(5.),
       events.update_attribute(cylinder, 'speed', 20),
       events.wait_duration(5.),
       ]

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
