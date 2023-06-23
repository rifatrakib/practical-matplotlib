from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import numpy as np
from PIL import Image

fig = Figure(figsize=(5, 4), dpi=100)
# A canvas must be manually attached to the figure (pyplot would automatically
# do it).  This is done by instantiating the canvas with the figure as
# argument.
canvas = FigureCanvasAgg(fig)

# Do some plotting.
ax = fig.add_subplot()
ax.plot([1, 2, 3])

# Option 1: Save the figure to a file; can also be a file-like object (BytesIO,
# etc.).
fig.savefig("embed-on-gui/assets/canvasagg/test.png")

# Option 2: Retrieve a memoryview on the renderer buffer, and convert it to a
# numpy array.
canvas.draw()
rgba = np.asarray(canvas.buffer_rgba())
# ... and pass it to PIL.
im = Image.fromarray(rgba)
# This image can then be saved to any format supported by Pillow, e.g.:
im.save("embed-on-gui/assets/canvasagg/test.bmp")
im.show()
