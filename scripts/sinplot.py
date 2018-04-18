import numpy as np
import matplotlib.pyplot as plt
import cfg

scale = cfg.SCALE*np.pi

m = np.array([np.sin(np.linspace(-scale, scale, cfg.SIZEX))]*cfg.SIZEY)

fig = plt.imshow(m, cmap='gray')
plt.axis('off')
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)
plt.savefig('scripts/assets/sin.png', bbox_inches='tight',
            pad_inches=0, dpi=cfg.DPI, transparent=True)
