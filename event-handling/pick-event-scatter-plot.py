import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand

# Fixing random state for reproducibility
np.random.seed(19680801)


def onpick(event):
    ind = event.ind
    print("onpick scatter:", ind, x[ind], y[ind])


x, y, c, s = rand(4, 100)

fig, ax = plt.subplots()
ax.scatter(x, y, 100 * s, c, picker=True)
fig.canvas.mpl_connect("pick_event", onpick)
plt.show()
