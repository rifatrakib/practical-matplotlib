import matplotlib.pyplot as plt
import matplotlib.lines as lines
import matplotlib.text as text
import numpy as np

from basic_units import cm

fig, ax = plt.subplots()
ax.xaxis.set_units(cm)
ax.yaxis.set_units(cm)

# Fixing random state for reproducibility
np.random.seed(19680801)

# test a plain-ol-line
line = lines.Line2D([0 * cm, 1.5 * cm], [0 * cm, 2.5 * cm], lw=2, color="black", axes=ax)
ax.add_line(line)

t = text.Text(3 * cm, 2.5 * cm, "text label", ha="left", va="bottom", axes=ax)
ax.add_artist(t)

ax.set_xlim(-1 * cm, 10 * cm)
ax.set_ylim(-1 * cm, 10 * cm)
# ax.xaxis.set_units(inch)
ax.grid(True)
ax.set_title("Artists with units")

plt.show()
