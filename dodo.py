import numpy as np
import matplotlib.pyplot as plt
import cfg
from module import sinplot, experiment

def task_make_grid():
    return {
        'actions': [(sinplot.make_singrid, [], {
            'file' : cfg.CYLINDER_TEXTURE,
            'scale': cfg.SCALE,
            'sizex': cfg.SIZEX,
            'sizey': cfg.SIZEY,
            'dpi'  : cfg.DPI,})],
        'targets':['module/assets/sin.png'],
    }


def task_run_experiment():
    return {
        'actions': [(experiment.run_experiment, [], {
            'cfg': cfg,
            })
        ],
    }
