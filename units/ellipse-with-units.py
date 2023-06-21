from matplotlib import patches
import matplotlib.pyplot as plt
import numpy as np

from basic_units import cm

xcenter, ycenter = 0.38 * cm, 0.52 * cm
width, height = 1e-1 * cm, 3e-1 * cm
angle = -30

theta = np.deg2rad(np.arange(0.0, 360.0, 1.0))
x = 0.5 * width * np.cos(theta)
y = 0.5 * height * np.sin(theta)

rtheta = np.radians(angle)
R = np.array([
    [np.cos(rtheta), -np.sin(rtheta)],
    [np.sin(rtheta),  np.cos(rtheta)],
])

x, y = np.dot(R, [x, y])
x += xcenter
y += ycenter

fig_1 = plt.figure()
ax_1 = fig_1.add_subplot(211, aspect="auto")
ax_1.fill(x, y, alpha=0.2, facecolor="yellow", edgecolor="yellow", linewidth=1, zorder=1)

e1 = patches.Ellipse(
    (xcenter, ycenter), width, height, angle=angle,
    linewidth=2, fill=False, zorder=2,
)

ax_1.add_patch(e1)

ax_2 = fig_1.add_subplot(212, aspect="equal")
ax_2.fill(x, y, alpha=0.2, facecolor="green", edgecolor="green", zorder=1)
e2 = patches.Ellipse(
    (xcenter, ycenter), width, height,
    angle=angle, linewidth=2, fill=False, zorder=2,
)

ax_2.add_patch(e2)

fig_2 = plt.figure()
ax_3 = fig_2.add_subplot(211, aspect="auto")
ax_3.fill(x, y, alpha=0.2, facecolor="yellow", edgecolor="yellow", linewidth=1, zorder=1)

e1 = patches.Arc(
    (xcenter, ycenter), width, height,
    angle=angle, linewidth=2, fill=False, zorder=2,
)

ax_3.add_patch(e1)

ax_4 = fig_2.add_subplot(212, aspect="equal")
ax_4.fill(x, y, alpha=0.2, facecolor="green", edgecolor="green", zorder=1)
e2 = patches.Arc(
    (xcenter, ycenter), width, height,
    angle=angle, linewidth=2, fill=False, zorder=2,
)

ax_4.add_patch(e2)

plt.show()
