from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 3, subplot_kw={"projection": "3d"})

# Get the test data
X, Y, Z = axes3d.get_test_data(0.05)

# Plot the data
for ax in axs:
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

# Set the orthographic projection.
axs[0].set_proj_type("ortho")  # FOV = 0 deg
axs[0].set_title('"ortho"\nfocal_length = ∞', fontsize=10)

# Set the perspective projections
axs[1].set_proj_type("persp")  # FOV = 90 deg
axs[1].set_title('"persp"\nfocal_length = 1 (default)', fontsize=10)

axs[2].set_proj_type("persp", focal_length=0.2)  # FOV = 157.4 deg
axs[2].set_title('"persp"\nfocal_length = 0.2', fontsize=10)

plt.show()
