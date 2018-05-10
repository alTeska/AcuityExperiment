from glob import glob
from os   import path
from numpy import random
import pyglet
import ratcave as rc

from .events import update_attribute, chain_events, wait_duration


def rotate_cylinder(dt, cylinder):
    cylinder.rotation.y += cylinder.speed * dt


def update(dt):
    pass


def run_experiment(cfg):
    # Create Window
    window = pyglet.window.Window()
    pyglet.clock.schedule(update)

    # Insert filename into WavefrontReader.
    obj_filename = cfg.PATH + '2.obj'  # hollow cylinder
    obj_reader = rc.WavefrontReader(obj_filename)


    # Create Mesh
    cylinder = obj_reader.get_mesh("hollow_Cylinder", scale=.6)
    cylinder.position.xyz = cfg.CYLINDER_POSITION
    cylinder.rotation.x = cfg.CYLINDER_ROTATION_X
    cylinder.uniforms.diffuse = 1., 1., 1.

    texture = rc.Texture.from_image(cfg.CYLINDER_TEXTURE)
    # texture = rc.Texture.from_image('module/assets/uvgrid_bw2.png')

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

    if cfg.SEQ:
        # TODO: add cfg.SEQ interpreter
        seq = [cfg.SEQ]
    else:
        seq = [update_attribute(cylinder, 'visible', False),
                wait_duration(cfg.START_TIME)]

        for speed in random.permutation(cfg.CYLINDER_SPEEDS * 2):
            for direction in random.permutation([1, -1]):
                phase_seq = [
                update_attribute(cylinder, 'visible', True),
                update_attribute(cylinder, 'speed', speed * direction),
                wait_duration(cfg.PHASE_DURATION_SECS),
                update_attribute(cylinder, 'visible', False),
                wait_duration(cfg.WAIT_DURATION_SECS),
            ]
            seq.extend(phase_seq)

    pyglet.clock.schedule(rotate_cylinder, cylinder)


    exp = chain_events(seq)
    next(exp)

    @window.event
    def on_draw():
        with rc.default_shader:
            scene.draw()


    pyglet.clock.schedule(exp.send)
    pyglet.app.run()

    return 0
