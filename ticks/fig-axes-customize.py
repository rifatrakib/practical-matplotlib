import matplotlib.pyplot as plt

fig = plt.figure()
rect = fig.patch  # a rectangle instance
rect.set_facecolor("lightgoldenrodyellow")

ax1 = fig.add_axes([0.1, 0.3, 0.4, 0.4])
rect = ax1.patch
rect.set_facecolor("lightslategray")

ax1.tick_params(axis="x", labelcolor="tab:red", labelrotation=45, labelsize=16)
ax1.tick_params(axis="y", color="tab:green", size=25, width=3)

plt.show()
