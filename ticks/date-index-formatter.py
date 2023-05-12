import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.lines as ml
from matplotlib.dates import DateFormatter, DayLocator
from matplotlib.ticker import Formatter


class MyFormatter(Formatter):
    def __init__(self, dates, fmt="%a"):
        self.dates = dates
        self.fmt = fmt

    def __call__(self, x, pos=0):
        """Return the label for time x at position pos."""
        try:
            return self.dates[round(x)].item().strftime(self.fmt)
        except IndexError:
            pass


def format_date(x, _):
    try:
        # convert datetime64 to datetime, and use datetime"s strftime:
        return r.date[round(x)].item().strftime("%a")
    except IndexError:
        pass


r = cbook.get_sample_data("goog.npz", np_load=True)["price_data"].view(np.recarray)
r = r[:9]  # get the first 9 days

fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(6, 6), layout="constrained")
fig.get_layout_engine().set(hspace=0.15)

# First we"ll do it the default way, with gaps on weekends
ax1.plot(r.date, r.adj_close, "o-")

# Highlight gaps in daily data
gaps = np.flatnonzero(np.diff(r.date) > np.timedelta64(1, "D"))
for gap in r[["date", "adj_close"]][np.stack((gaps, gaps + 1)).T]:
    ax1.plot(gap.date, gap.adj_close, "w--", lw=2)
ax1.legend(handles=[ml.Line2D([], [], ls="--", label="Gaps in daily data")])

ax1.set_title("Plot y at x Coordinates")
ax1.xaxis.set_major_locator(DayLocator())
ax1.xaxis.set_major_formatter(DateFormatter("%a"))

# Create an index plot (x defaults to range(len(y)) if omitted)
ax2.plot(r.adj_close, "o-")

ax2.set_title("Plot y at Index Coordinates Using Custom Formatter")
ax2.xaxis.set_major_formatter(format_date)  # internally creates FuncFormatter
ax2.xaxis.set_major_formatter(MyFormatter(r.date, "%a"))

plt.show()
