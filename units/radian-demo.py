import matplotlib.pyplot as plt
import numpy as np

from basic_units import radians, degrees, cos

x = [val * radians for val in np.arange(0, 15, 0.01)]

fig, axs = plt.subplots(2)

axs[0].plot(x, cos(x), xunits=radians)
axs[1].plot(x, cos(x), xunits=degrees)

fig.tight_layout()
plt.show()
