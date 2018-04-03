import pyglet
import ratcave as rc
from glob import glob
from os import path


# Create Window
window = pyglet.window.Window()

def update(dt):
    pass
pyglet.clock.schedule(update)

# Insert filename into WavefrontReader.
obj_filename = rc.resources.obj_primitives
obj_reader = rc.WavefrontReader(obj_filename)

# Create Mesh
cylinder = obj_reader.get_mesh("Cylinder", scale=.6)
cylinder.position.xyz = 0, 0, -2
cylinder.rotation.x = 40
cylinder.speed = 5.
cylinder.uniforms['diffuse'] = 1., 1., 1.

texture = rc.Texture.from_image(rc.resources.img_colorgrid)
cylinder.textures.append(texture)

vertname = glob(path.join(rc.resources.shader_path, 'default', '*.vert'))[0]
fragname = glob(path.join(rc.resources.shader_path, 'default', '*.frag'))[0]

shader = rc.Shader.from_file(vert = vertname, frag = fragname)



# Create Scene
scene = rc.Scene(meshes=[cylinder])

clock = 0.
def update(dt):
    global clock
    clock += dt
    cylinder.rotation.y += cylinder.speed * dt
    # virtual_scene.camera.position.xyz = monkey.position.xyz
    # screen.uniforms['playerPos'] = virtual_scene.camera.position.xyz
pyglet.clock.schedule(update)


@window.event
def on_draw():
    with rc.default_shader:
        # cylinder.rotation.y += cylinder.speed
        scene.draw()

pyglet.app.run()
