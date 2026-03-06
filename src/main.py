import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors


distribution_1 = np.random.normal(size=1000)
distribution_2 = np.random.normal(size=1000)

histogram, x_edge, y_edge = np.histogram2d(
    distribution_1,
    distribution_2,
    bins=10,
    density=True
)

# grid for bar3d
x, y = np.meshgrid(x_edge[:-1], y_edge[:-1])
xpos = x.ravel()
ypos = y.ravel()
zpos = np.zeros_like(xpos)

dx = dy = (x_edge[1] - x_edge[0]) * np.ones_like(xpos)
dz = histogram.ravel()

# color mapping
norm = colors.Normalize(dz.min(), dz.max())
bar_colors = cm.turbo(norm(dz))


fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=bar_colors, shade=True)
hist_x, edges_x = np.histogram(distribution_1, bins=10, density=True)
hist_y, edges_y = np.histogram(distribution_2, bins=10, density=True)

x_center = (edges_x[:-1] + edges_x[1:]) / 2
y_center = (edges_y[:-1] + edges_y[1:]) / 2

dx_hist = edges_x[1] - edges_x[0]
dy_hist = edges_y[1] - edges_y[0]


ax.bar(
    x_center,
    hist_x,
    zs=y_edge[0],
    zdir='y',
    width=dx_hist,
    alpha=0.6
)

ax.bar(
    y_center,
    hist_y,
    zs=x_edge[-1],
    zdir='x',
    width=dy_hist,
    alpha=0.6
)

ax.set_xlabel("distribution 1")
ax.set_ylabel("distribution 2")
ax.set_zlabel("Probability Density")

try:
    plt.show()

except KeyboardInterrupt:
    pass