from matplotlib.backend_bases import MouseButton
import matplotlib.pyplot as plt
import numpy as np


def on_move(event):
    if event.inaxes:
        print(
            f"data coords {event.xdata} {event.ydata},",
            f"pixel coords {event.x} {event.y}",
        )


def on_click(event):
    if event.button is MouseButton.LEFT:
        print("disconnecting callback")
        plt.disconnect(binding_id)


t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

binding_id = plt.connect("motion_notify_event", on_move)
plt.connect("button_press_event", on_click)

plt.show()
