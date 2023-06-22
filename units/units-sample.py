import matplotlib.pyplot as plt
import numpy as np

from basic_units import cm, inch

cms = cm * np.arange(0, 10, 2)

fig, axs = plt.subplots(2, 2, layout="constrained")

axs[0, 0].plot(cms, cms)

axs[0, 1].plot(cms, cms, xunits=cm, yunits=inch)

axs[1, 0].plot(cms, cms, xunits=inch, yunits=cm)
axs[1, 0].set_xlim(-1, 4)  # scalars are interpreted in current units

axs[1, 1].plot(cms, cms, xunits=inch, yunits=inch)
axs[1, 1].set_xlim(3*cm, 6*cm)  # cm are converted to inches

plt.show()
