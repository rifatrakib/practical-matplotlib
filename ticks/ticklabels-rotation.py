import matplotlib.pyplot as plt


x = [1, 2, 3, 4]
y = [1, 4, 9, 6]
labels = ["Frogs", "Hogs", "Bogs", "Slogs"]

plt.plot(x, y)
plt.xticks(x, labels, rotation="vertical")
plt.margins(0.2)
plt.subplots_adjust(bottom=0.15)

plt.show()
