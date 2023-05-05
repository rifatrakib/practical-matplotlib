import numpy as np
import matplotlib.cbook as cbook
import matplotlib.dates as dates
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt

# Load some financial data; Google's stock price
r = (cbook.get_sample_data("goog.npz", np_load=True)["price_data"].view(np.recarray))
r = r[-250:]  # get the last 250 days

fig, ax = plt.subplots()
ax.plot(r.date, r.adj_close)

ax.xaxis.set_major_locator(dates.MonthLocator())
# 16 is a slight approximation since months differ in number of days.
ax.xaxis.set_minor_locator(dates.MonthLocator(bymonthday=16))

ax.xaxis.set_major_formatter(ticker.NullFormatter())
ax.xaxis.set_minor_formatter(dates.DateFormatter("%b"))

# Remove the tick lines
ax.tick_params(axis="x", which="minor", tick1On=False, tick2On=False)

# Align the minor tick label
for label in ax.get_xticklabels(minor=True):
    label.set_horizontalalignment("center")

imid = len(r) // 2
ax.set_xlabel(str(r.date[imid].item().year))

plt.show()
