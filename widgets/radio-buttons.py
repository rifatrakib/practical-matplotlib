import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons


def hzfunc(label):
    hzdict = {"1 Hz": s0, "2 Hz": s1, "4 Hz": s2}
    ydata = hzdict[label]
    l.set_ydata(ydata)
    fig.canvas.draw()


def colorfunc(label):
    l.set_color(label)
    fig.canvas.draw()


def stylefunc(label):
    l.set_linestyle(label)
    fig.canvas.draw()


axcolor = "lightgoldenrodyellow"
t = np.arange(0.0, 2.0, 0.01)
s0 = np.sin(2 * np.pi * t)
s1 = np.sin(4 * np.pi * t)
s2 = np.sin(8 * np.pi * t)

fig, ax = plt.subplots()
l, = ax.plot(t, s0, lw=2, color="red")
fig.subplots_adjust(left=0.3)

rax = fig.add_axes([0.05, 0.7, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ("1 Hz", "2 Hz", "4 Hz"))
radio.on_clicked(hzfunc)

rax = fig.add_axes([0.05, 0.4, 0.15, 0.15], facecolor=axcolor)
radio2 = RadioButtons(rax, ("red", "blue", "green"))
radio2.on_clicked(colorfunc)

rax = fig.add_axes([0.05, 0.1, 0.15, 0.15], facecolor=axcolor)
radio3 = RadioButtons(rax, ("-", "--", "-.", ":"))
radio3.on_clicked(stylefunc)

plt.show()
