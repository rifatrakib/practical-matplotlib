import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.units as munits
import numpy as np

base = datetime.datetime(2005, 2, 1)
dates = [base + datetime.timedelta(hours=(2 * i)) for i in range(732)]
N = len(dates)
np.random.seed(19680801)
y = np.cumsum(np.random.randn(N))

fig_1, axs = plt.subplots(3, 1, layout="constrained", figsize=(6, 6))
lims = [
    (np.datetime64("2005-02"), np.datetime64("2005-04")),
    (np.datetime64("2005-02-03"), np.datetime64("2005-02-15")),
    (np.datetime64("2005-02-03 11:00"), np.datetime64("2005-02-04 13:20")),
]

for nn, ax in enumerate(axs):
    ax.plot(dates, y)
    ax.set_xlim(lims[nn])

    # rotate_labels...
    for label in ax.get_xticklabels():
        label.set_rotation(40)
        label.set_horizontalalignment("right")

axs[0].set_title("Default Date Formatter")

fig_2, axs = plt.subplots(3, 1, layout="constrained", figsize=(6, 6))

for nn, ax in enumerate(axs):
    locator = mdates.AutoDateLocator(minticks=3, maxticks=7)
    formatter = mdates.ConciseDateFormatter(locator)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)

    ax.plot(dates, y)
    ax.set_xlim(lims[nn])

axs[0].set_title("Concise Date Formatter")

converter = mdates.ConciseDateConverter()
munits.registry[np.datetime64] = converter
munits.registry[datetime.date] = converter
munits.registry[datetime.datetime] = converter

fig_3, axs = plt.subplots(3, 1, figsize=(6, 6), layout="constrained")

for nn, ax in enumerate(axs):
    ax.plot(dates, y)
    ax.set_xlim(lims[nn])

axs[0].set_title("Concise Date Formatter")

plt.show()
