from matplotlib.patches import BoxStyle
from matplotlib.path import Path
import matplotlib.pyplot as plt


class CustomStyle:
    def __init__(self, pad=0.3):
        self.pad = pad
        super().__init__()

    def __call__(self, x0, y0, width, height, mutation_size):
        # padding
        pad = mutation_size * self.pad
        # width and height with padding added
        width = width + 2.0 * pad
        height = height + 2.0 * pad
        # boundary of the padded box
        x0, y0 = x0 - pad, y0 - pad
        x1, y1 = x0 + width, y0 + height
        # return the new path
        return Path(
            [
                (x0, y0), (x1, y0), (x1, y1), (x0, y1),
                (x0 - pad, (y0 + y1) / 2), (x0, y0), (x0, y0),
            ],
            closed=True,
        )


def custom_box_style(x0, y0, width, height, mutation_size):
    # padding
    mypad = 0.3
    pad = mutation_size * mypad
    # width and height with padding added.
    width = width + 2 * pad
    height = height + 2 * pad
    # boundary of the padded box
    x0, y0 = x0 - pad, y0 - pad
    x1, y1 = x0 + width, y0 + height
    # return the new path
    return Path(
        [
            (x0, y0), (x1, y0), (x1, y1), (x0, y1),
            (x0 - pad, (y0 + y1) / 2), (x0, y0), (x0, y0),
        ],
        closed=True,
    )


fig_1, ax_1 = plt.subplots(figsize=(3, 3))
ax_1.text(
    0.5, 0.5, "Test", size=30, va="center", ha="center",
    rotation=30, bbox=dict(boxstyle=custom_box_style, alpha=0.2),
)

BoxStyle._style_list["angled"] = CustomStyle  # Register the custom style.

fig_2, ax_2 = plt.subplots(figsize=(3, 3))
ax_2.text(
    0.5, 0.5, "Test", size=30, va="center", ha="center",
    rotation=30, bbox=dict(boxstyle="angled,pad=0.5", alpha=0.2),
)

del BoxStyle._style_list["angled"]  # Unregister it.

plt.show()
