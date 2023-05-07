import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.units as munits
import numpy as np

base = datetime.datetime(2005, 2, 1)
dates = [base + datetime.timedelta(hours=(2 * i)) for i in range(732)]
lims = [
    (np.datetime64("2005-02"), np.datetime64("2005-04")),
    (np.datetime64("2005-02-03"), np.datetime64("2005-02-15")),
    (np.datetime64("2005-02-03 11:00"), np.datetime64("2005-02-04 13:20")),
]
N = len(dates)
np.random.seed(19680801)
y = np.cumsum(np.random.randn(N))

fig_1, axs = plt.subplots(3, 1, layout="constrained", figsize=(6, 6))

for nn, ax in enumerate(axs):
    locator = mdates.AutoDateLocator()
    formatter = mdates.ConciseDateFormatter(locator)
    formatter.formats = [
        "%y",  # ticks are mostly years
        "%b",       # ticks are mostly months
        "%d",       # ticks are mostly days
        "%H:%M",    # hrs
        "%H:%M",    # min
        "%S.%f",  # secs
    ]
    # these are mostly just the level above...
    formatter.zero_formats = [""] + formatter.formats[:-1]
    # ...except for ticks that are mostly hours, then it is nice to have
    # month-day:
    formatter.zero_formats[3] = "%d-%b"

    formatter.offset_formats = [
        "", "%Y", "%b %Y", "%d %b %Y", "%d %b %Y", "%d %b %Y %H:%M",
    ]
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)

    ax.plot(dates, y)
    ax.set_xlim(lims[nn])

axs[0].set_title("Concise Date Formatter")

formats = [
    "%y",          # ticks are mostly years
    "%b",     # ticks are mostly months
    "%d",     # ticks are mostly days
    "%H:%M",  # hrs
    "%H:%M",  # min
    "%S.%f",  # secs
]

# these can be the same, except offset by one level....
zero_formats = [""] + formats[:-1]
# ...except for ticks that are mostly hours, then it's nice to have month-day
zero_formats[3] = "%d-%b"
offset_formats = ["", "%Y", "%b %Y", "%d %b %Y", "%d %b %Y", "%d %b %Y %H:%M"]

converter = mdates.ConciseDateConverter(
    formats=formats,
    zero_formats=zero_formats,
    offset_formats=offset_formats,
)

munits.registry[np.datetime64] = converter
munits.registry[datetime.date] = converter
munits.registry[datetime.datetime] = converter

fig_2, axs = plt.subplots(3, 1, layout="constrained", figsize=(6, 6))

for nn, ax in enumerate(axs):
    ax.plot(dates, y)
    ax.set_xlim(lims[nn])

axs[0].set_title("Concise Date Formatter registered non-default")

plt.show()
