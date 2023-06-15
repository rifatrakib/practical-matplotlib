import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["ytick.right"] = plt.rcParams["ytick.labelright"] = True
plt.rcParams["ytick.left"] = plt.rcParams["ytick.labelleft"] = False

x = np.arange(10)

fig, (ax0, ax1) = plt.subplots(2, 1, sharex=True, figsize=(6, 6))

ax0.plot(x)
ax0.yaxis.tick_left()

ax1.plot(x)

plt.show()
