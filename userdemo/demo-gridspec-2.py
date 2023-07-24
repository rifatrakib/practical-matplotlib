import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


def annotate_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)


fig_1 = plt.figure()
fig_1.suptitle("Controlling subplot sizes with width_ratios and height_ratios")

gs1 = GridSpec(2, 2, width_ratios=[1, 2], height_ratios=[4, 1])
ax_1 = fig_1.add_subplot(gs1[0])
ax_2 = fig_1.add_subplot(gs1[1])
ax_3 = fig_1.add_subplot(gs1[2])
ax_4 = fig_1.add_subplot(gs1[3])

annotate_axes(fig_1)

fig_2 = plt.figure()
fig_2.suptitle("Controlling spacing around and between subplots")

gs2 = GridSpec(3, 3, left=0.05, right=0.48, wspace=0.05)
ax_5 = fig_2.add_subplot(gs2[:-1, :])
ax_6 = fig_2.add_subplot(gs2[-1, :-1])
ax_7 = fig_2.add_subplot(gs2[-1, -1])

gs3 = GridSpec(3, 3, left=0.55, right=0.98, hspace=0.05)
ax_8 = fig_2.add_subplot(gs3[:, :-1])
ax_9 = fig_2.add_subplot(gs3[:-1, -1])
ax_10 = fig_2.add_subplot(gs3[-1, -1])

annotate_axes(fig_2)

plt.show()
