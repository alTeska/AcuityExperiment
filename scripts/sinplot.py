import numpy as np
import matplotlib.pyplot as plt
import cfg

v = np.linspace(0, np.pi * cfg.SCALE, num=cfg.SIZE)
m = np.repeat(np.sin(v)[np.newaxis, :], cfg.SIZE, axis=0)

fig = plt.imshow(m, cmap='gray')
plt.axis('off')
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)
plt.savefig(cfg.CYLINDER_TEXTURE, bbox_inches='tight', pad_inches=0, dpi=cfg.DPI, transparent=True)
