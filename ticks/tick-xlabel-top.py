import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(range(10))
ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
ax.set_title("x-ticks moved to the top")

plt.show()
