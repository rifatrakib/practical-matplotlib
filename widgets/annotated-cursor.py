import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
from matplotlib.backend_bases import MouseEvent


class AnnotatedCursor(Cursor):
    def __init__(
        self, line, numberformat="{0:.4g};{1:.4g}", offset=(5, 5),
        dataaxis="x", textprops=None, **cursorargs,
    ):
        if textprops is None:
            textprops = {}
        # The line object, for which the coordinates are displayed
        self.line = line
        # The format string, on which .format() is called for creating the text
        self.numberformat = numberformat
        # Text position offset
        self.offset = np.array(offset)
        # The axis in which the cursor position is looked up
        self.dataaxis = dataaxis

        # First call baseclass constructor.
        # Draws cursor and remembers background for blitting.
        # Saves ax as class attribute.
        super().__init__(**cursorargs)

        # Default value for position of text.
        self.set_position(self.line.get_xdata()[0], self.line.get_ydata()[0])
        # Create invisible animated text
        self.text = self.ax.text(
            self.ax.get_xbound()[0],
            self.ax.get_ybound()[0],
            "0, 0",
            animated=bool(self.useblit),
            visible=False, **textprops)
        # The position at which the cursor was last drawn
        self.lastdrawnplotpoint = None

    def onmove(self, event):
        """
        Overridden draw callback for cursor. Called when moving the mouse.
        """

        # Leave method under the same conditions as in overridden method
        if self.ignore(event):
            self.lastdrawnplotpoint = None
            return
        if not self.canvas.widgetlock.available(self):
            self.lastdrawnplotpoint = None
            return

        # If the mouse left drawable area, we now make the text invisible.
        # Baseclass will redraw complete canvas after, which makes both text
        # and cursor disappear.
        if event.inaxes != self.ax:
            self.lastdrawnplotpoint = None
            self.text.set_visible(False)
            super().onmove(event)
            return

        # Get the coordinates, which should be displayed as text,
        # if the event coordinates are valid.
        plotpoint = None
        if event.xdata is not None and event.ydata is not None:
            # Get plot point related to current x position.
            # These coordinates are displayed in text.
            plotpoint = self.set_position(event.xdata, event.ydata)
            # Modify event, such that the cursor is displayed on the
            # plotted line, not at the mouse pointer,
            # if the returned plot point is valid
            if plotpoint is not None:
                event.xdata = plotpoint[0]
                event.ydata = plotpoint[1]

        # If the plotpoint is given, compare to last drawn plotpoint and
        # return if they are the same.
        # Skip even the call of the base class, because this would restore the
        # background, draw the cursor lines and would leave us the job to
        # re-draw the text.
        if plotpoint is not None and plotpoint == self.lastdrawnplotpoint:
            return

        # Baseclass redraws canvas and cursor. Due to blitting,
        # the added text is removed in this call, because the
        # background is redrawn.
        super().onmove(event)

        # Check if the display of text is still necessary.
        # If not, just return.
        # This behaviour is also cloned from the base class.
        if not self.get_active() or not self.visible:
            return

        # Draw the widget, if event coordinates are valid.
        if plotpoint is not None:
            # Update position and displayed text.
            # Position: Where the event occurred.
            # Text: Determined by set_position() method earlier
            # Position is transformed to pixel coordinates,
            # an offset is added there and this is transformed back.
            temp = [event.xdata, event.ydata]
            temp = self.ax.transData.transform(temp)
            temp = temp + self.offset
            temp = self.ax.transData.inverted().transform(temp)
            self.text.set_position(temp)
            self.text.set_text(self.numberformat.format(*plotpoint))
            self.text.set_visible(self.visible)

            # Tell base class, that we have drawn something.
            # Baseclass needs to know, that it needs to restore a clean
            # background, if the cursor leaves our figure context.
            self.needclear = True

            # Remember the recently drawn cursor position, so events for the
            # same position (mouse moves slightly between two plot points)
            # can be skipped
            self.lastdrawnplotpoint = plotpoint
        # otherwise, make text invisible
        else:
            self.text.set_visible(False)

        # Draw changes. Cannot use _update method of baseclass,
        # because it would first restore the background, which
        # is done already and is not necessary.
        if self.useblit:
            self.ax.draw_artist(self.text)
            self.canvas.blit(self.ax.bbox)
        else:
            # If blitting is deactivated, the overridden _update call made
            # by the base class immediately returned.
            # We still have to draw the changes.
            self.canvas.draw_idle()

    def set_position(self, xpos, ypos):
        # Get plot line data
        xdata = self.line.get_xdata()
        ydata = self.line.get_ydata()

        # The dataaxis attribute decides, in which axis we look up which cursor
        # coordinate.
        if self.dataaxis == "x":
            pos = xpos
            data = xdata
            lim = self.ax.get_xlim()
        elif self.dataaxis == "y":
            pos = ypos
            data = ydata
            lim = self.ax.get_ylim()
        else:
            raise ValueError(
                f"The data axis specifier {self.dataaxis} should be 'x' or 'y'"
            )

        # If position is valid and in valid plot data range.
        if pos is not None and lim[0] <= pos <= lim[-1]:
            # Find closest x value in sorted x vector.
            # This requires the plotted data to be sorted.
            index = np.searchsorted(data, pos)
            # Return none, if this index is out of range.
            if index < 0 or index >= len(data):
                return None
            # Return plot point as tuple.
            return (xdata[index], ydata[index])

        # Return none if there is no good related point for this x position.
        return None

    def clear(self, event):
        """
        Overridden clear callback for cursor, called before drawing the figure.
        """

        # The base class saves the clean background for blitting.
        # Text and cursor are invisible,
        # until the first mouse move event occurs.
        super().clear(event)
        if self.ignore(event):
            return
        self.text.set_visible(False)

    def _update(self):
        """
        Overridden method for either blitting or drawing the widget canvas.

        Passes call to base class if blitting is activated, only.
        In other cases, one draw_idle call is enough, which is placed
        explicitly in this class (see *onmove()*).
        In that case, `~matplotlib.widgets.Cursor` is not supposed to draw
        something using this method.
        """

        if self.useblit:
            super()._update()


fig_1, ax_1= plt.subplots(figsize=(8, 6))
ax_1.set_title("Cursor Tracking x Position")

x = np.linspace(-5, 5, 1000)
y = x ** 2

line, = ax_1.plot(x, y)
ax_1.set_xlim(-5, 5)
ax_1.set_ylim(0, 25)

cursor_1 = AnnotatedCursor(
    line=line, numberformat="{0:.2f}\n{1:.2f}", dataaxis="x", offset=[10, 10],
    textprops={"color": "blue", "fontweight": "bold"},
    ax=ax_1, useblit=True, color="red", linewidth=2,
)

# Simulate a mouse move to (-2, 10), needed for online docs
t = ax_1.transData
MouseEvent("motion_notify_event", ax_1.figure.canvas, *t.transform((-2, 10)))._process()

fig_2, ax_2 = plt.subplots(figsize=(8, 6))
ax_2.set_title("Cursor Tracking y Position")

line, = ax_2.plot(x, y)
ax_2.set_xlim(-5, 5)
ax_2.set_ylim(0, 25)

cursor_2 = AnnotatedCursor(
    ax=ax_2, line=line, numberformat="{0:.2f}\n{1:.2f}", dataaxis="y", offset=[10, 10],
    textprops={"color": "blue", "fontweight": "bold"}, useblit=True, color="red", linewidth=2,
)

# Simulate a mouse move to (-2, 10), needed for online docs
t = ax_2.transData
MouseEvent("motion_notify_event", ax_2.figure.canvas, *t.transform((-2, 10)))._process()

plt.show()
