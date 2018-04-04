import numpy as np
import matplotlib.pyplot as plt


size = 10000
scale = 50

a = np.linspace(0, np.pi * scale, num=size)
b = np.sin(a)
m = np.repeat(b[np.newaxis, :], size, axis=0)

print(m.shape)

fig = plt.matshow(m, cmap='gray')
fig = plt.imshow(m, cmap='gray')
plt.axis('off')
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)
plt.savefig('assets/pict.png', bbox_inches='tight', pad_inches=0, dpi=500, transparent=True)

# plt.show()
