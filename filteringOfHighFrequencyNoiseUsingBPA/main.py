import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

data = [
[2.0, 3.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0],
[4.0, 1.0, 2.0, 2.0, 3.0, 0.0, 6.0, 0.0],
[2.0, 2.0, 3.0, 2.0, 3.0, 3.0, 4.0, 5.0],
[2.0, 1.0, 3.0, 2.0, 1.0, -1.0, 3.0, 0.0],
[0.0, 2.0, 9.0, 3.0, 2.0, -3.0, 2.0, 4.0],
[0.0, 5.0, 2.0, 2.0, 0.0, 3.0, 0.0, 5.0],
[8.0, 0.0, 7.0, 0.0, 6.0, 0.0, 6.0, 0.0],
[7.0, 4.0, 4.0, 5.0, 0.0, 5.0, 0.0, 4.0]
]

data = np.array(data)
length = data.shape[0]
width = data.shape[1]
x, y = np.meshgrid(np.arange(length), np.arange(width))
fig = plt.figure()

ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.plot_surface(x, y, data, cmap=cm.coolwarm)
ax.view_init(azim=-140, elev=40)
plt.show()
