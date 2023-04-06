import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2*np.pi)
x = np.cos(theta - np.pi/2)
y = np.sin(theta - np.pi/2)
z = theta

fig_1, ax_1 = plt.subplots(subplot_kw=dict(projection="3d"))
ax_1.stem(x, y, z)

fig_2, ax_2 = plt.subplots(subplot_kw=dict(projection="3d"))
markerline_2, stemlines_2, baseline_2 = ax_2.stem(
    x, y, z, linefmt="grey", markerfmt="D", bottom=np.pi,
)
markerline_2.set_markerfacecolor("none")

fig_3, ax_3 = plt.subplots(subplot_kw=dict(projection="3d"))
markerline_3, stemlines_3, baseline_3 = ax_3.stem(x, y, z, bottom=-1, orientation="x")
ax_3.set(xlabel="x", ylabel="y", zlabel="z")

plt.show()
