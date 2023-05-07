import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from numpy.random import randn

# Fixing random state for reproducibility
np.random.seed(19680801)

fig_1, ax_1 = plt.subplots()

data = np.clip(randn(250, 250), -1, 1)

cax = ax_1.imshow(data, cmap=cm.coolwarm)
ax_1.set_title("Gaussian noise with vertical colorbar")

# Add colorbar, make sure to specify tick locations to match desired ticklabels
cbar = fig_1.colorbar(cax, ticks=[-1, 0, 1])
cbar.ax.set_yticklabels(["< -1", "0", "> 1"])  # vertically oriented colorbar

fig_2, ax_2 = plt.subplots()

data = np.clip(randn(250, 250), -1, 1)

cax = ax_2.imshow(data, cmap=cm.afmhot)
ax_2.set_title("Gaussian noise with horizontal colorbar")

cbar = fig_2.colorbar(cax, ticks=[-1, 0, 1], orientation="horizontal")
cbar.ax.set_xticklabels(["Low", "Medium", "High"])  # horizontal colorbar

plt.show()
