import matplotlib.patches as patches
from matplotlib.path import Path
import matplotlib.pyplot as plt
import matplotlib.patheffects as patheffects

fig, ax = plt.subplots(figsize=(6, 6))
path = Path.unit_circle()
patch = patches.PathPatch(
    path, facecolor="none", lw=2,
    path_effects=[patheffects.withTickedStroke(angle=-90, spacing=10, length=1)],
)

ax.add_patch(patch)
ax.axis("equal")
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

plt.show()
