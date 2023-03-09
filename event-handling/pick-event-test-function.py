import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand

# Fixing random state for reproducibility
np.random.seed(19680801)


def line_picker(line, mouseevent):
    """
    Find the points within a certain distance from the mouseclick in
    data coords and attach some extra attributes, pickx and picky
    which are the data points that were picked.
    """
    if mouseevent.xdata is None:
        return False, dict()
    xdata = line.get_xdata()
    ydata = line.get_ydata()
    maxd = 0.05
    d = np.sqrt(
        (xdata - mouseevent.xdata)**2 + (ydata - mouseevent.ydata)**2)

    ind, = np.nonzero(d <= maxd)
    if len(ind):
        pickx = xdata[ind]
        picky = ydata[ind]
        props = dict(ind=ind, pickx=pickx, picky=picky)
        return True, props
    else:
        return False, dict()


def onpick(event):
    print("onpick line:", event.pickx, event.picky)


fig, ax = plt.subplots()
ax.set_title("custom picker for line data")
line, = ax.plot(rand(100), rand(100), "o", picker=line_picker)
fig.canvas.mpl_connect("pick_event", onpick)
plt.show()
