import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 1.0, 0.01)
y1 = np.sin(2 * np.pi * x)
y2 = np.sin(4 * np.pi * x)
lines = plt.plot(x, y1, x, y2)
l1, l2 = lines
plt.setp(lines, linestyle="--")       # set both to dashed
plt.setp(l1, linewidth=2, color="r")  # line1 is thick and red
plt.setp(l2, linewidth=1, color="g")  # line2 is thinner and green

print("Line setters")
plt.setp(l1)
print("Line getters")
plt.getp(l1)

print("Rectangle setters")
plt.setp(plt.gca().patch)
print("Rectangle getters")
plt.getp(plt.gca().patch)

t = plt.title("Hi mom")
print("Text setters")
plt.setp(t)
print("Text getters")
plt.getp(t)

plt.show()
