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
# obj_filename = 'assets/2.obj'

obj_filename = rc.resources.obj_primitives
obj_reader = rc.WavefrontReader(obj_filename)


# Create Mesh
cylinder = obj_reader.get_mesh("Cylinder", scale=.6)
cylinder.position.xyz = 0, 0, -2
cylinder.rotation.x = 40
# cylinder.speed = 5.
cylinder.uniforms['diffuse'] = 1., 1., 1.

# texture = rc.Texture.from_image(rc.resources.img_colorgrid)
# texture = rc.Texture.from_image('assets/uvgrid_bw.png')
texture = rc.Texture.from_image('assets/pict.png')
cylinder.textures.append(texture)
cylinder.speed = 0


vertname = glob(path.join(rc.resources.shader_path, 'default', '*.vert'))[0]
fragname = glob(path.join(rc.resources.shader_path, 'default', '*.frag'))[0]

shader = rc.Shader.from_file(vert = vertname, frag = fragname)


# Create Scene
scene = rc.Scene(meshes=[cylinder])

seq = [events.update_attribute(cylinder, 'speed', -2),
       events.wait_duration(10.),
       events.update_attribute(cylinder, 'speed', 2),]


clock = 0.
exp = events.chain_events(seq)
exp.next()


def update(dt):
    global clock
    clock += dt
    cylinder.rotation.y = cylinder.speed


@window.event
def on_draw():
    with rc.default_shader:
        pyglet.clock.schedule(exp.send)
        scene.draw()


pyglet.app.run()
