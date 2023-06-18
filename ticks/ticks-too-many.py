import matplotlib.pyplot as plt
import numpy as np

fig_1, ax_1 = plt.subplots(1, 2, layout="constrained", figsize=(6, 2.5))
x = ["1", "5", "2", "3"]
y = [1, 4, 2, 3]
ax_1[0].plot(x, y, "d")
ax_1[0].tick_params(axis="x", color="r", labelcolor="r")
ax_1[0].set_xlabel("Categories")
ax_1[0].set_title("Ticks seem out of order / misplaced")

# convert to numbers:
x = np.asarray(x, dtype="float")
ax_1[1].plot(x, y, "d")
ax_1[1].set_xlabel("Floats")
ax_1[1].set_title("Ticks as expected")

fig_2, ax_2 = plt.subplots(1, 2, figsize=(6, 2.5))
x = [f"{xx}" for xx in np.arange(100)]
y = np.arange(100)
ax_2[0].plot(x, y)
ax_2[0].tick_params(axis="x", color="r", labelcolor="r")
ax_2[0].set_title("Too many ticks")
ax_2[0].set_xlabel("Categories")

ax_2[1].plot(np.asarray(x, float), y)
ax_2[1].set_title("x converted to numbers")
ax_2[1].set_xlabel("Floats")

fig_3, ax_3 = plt.subplots(1, 2, layout="constrained", figsize=(6, 2.75))
x = ["2021-10-01", "2021-11-02", "2021-12-03", "2021-09-01"]
y = [0, 2, 3, 1]
ax_3[0].plot(x, y, "d")
ax_3[0].tick_params(axis="x", labelrotation=90, color="r", labelcolor="r")
ax_3[0].set_title("Dates out of order")

# convert to datetime64
x = np.asarray(x, dtype="datetime64[s]")
ax_3[1].plot(x, y, "d")
ax_3[1].tick_params(axis="x", labelrotation=90)
ax_3[1].set_title("x converted to datetimes")

plt.show()
