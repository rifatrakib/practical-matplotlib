import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def format_fn(tick_val, tick_pos):
    if int(tick_val) in xs:
        return labels[int(tick_val)]
    else:
        return ""


fig, ax = plt.subplots()
xs = range(26)
ys = range(26)
labels = list("abcdefghijklmnopqrstuvwxyz")


# A FuncFormatter is created automatically.
ax.xaxis.set_major_formatter(format_fn)
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.plot(xs, ys)
plt.show()
