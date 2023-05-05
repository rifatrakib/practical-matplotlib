import matplotlib.pyplot as plt
import numpy as np
np.random.seed(19680801)

fig_1, ax_1 = plt.subplots()
dots = np.linspace(0.3, 1.2, 10)
X, Y = np.meshgrid(dots, dots)
x, y = X.ravel(), Y.ravel()
ax_1.scatter(x, y, c=x+y)

plt.rcParams["axes.autolimit_mode"] = "round_numbers"

fig_2, ax_2 = plt.subplots()
ax_2.scatter(x, y, c=x+y)

fig_3, ax_3 = plt.subplots()
ax_3.scatter(x, y, c=x+y)
ax_3.set_xmargin(0.8)

plt.show()
