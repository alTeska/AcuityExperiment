import numpy as np
import matplotlib.pyplot as plt
import cfg


def make_singrid(file, scale, sizex, sizey, dpi):
    m = np.array([np.sin(np.linspace(-scale*np.pi, scale*np.pi, sizex))]*sizey)

    fig = plt.imshow(m, cmap='gray')
    fig.axes.get_xaxis().set_visible(False)
    plt.axis('off')
    fig.axes.get_yaxis().set_visible(False)
    plt.savefig(file, bbox_inches='tight',
                pad_inches=0, dpi=dpi, transparent=True)
