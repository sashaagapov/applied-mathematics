from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

coordinates = np.linspace(-1, 1, 400)
cosine = 0.45 * np.cos(2 * np.pi * coordinates)
u, v = np.meshgrid([-1, 1], [-1, 1])

figure = plt.figure(figsize=(9, 7))
axes = figure.add_subplot(projection="3d")

axes.plot_surface(u, v, np.full_like(u, -1), color="lightgray", alpha=0.08, shade=False)
axes.plot_surface(u, v, np.full_like(u, 1), color="lightgray", alpha=0.08, shade=False)
axes.plot_surface(u, np.full_like(u, -1), v, color="lightgray", alpha=0.08, shade=False)
axes.plot_surface(u, np.full_like(u, 1), v, color="lightgray", alpha=0.08, shade=False)
axes.plot_surface(np.full_like(u, -1), u, v, color="lightgray", alpha=0.08, shade=False)
axes.plot_surface(np.full_like(u, 1), u, v, color="lightgray", alpha=0.08, shade=False)

for x_value in (-1, 1):
    for y_value in (-1, 1):
        axes.plot([x_value, x_value], [y_value, y_value], [-1, 1], color="black", linewidth=1.5)

for x_value in (-1, 1):
    for z_value in (-1, 1):
        axes.plot([x_value, x_value], [-1, 1], [z_value, z_value], color="black", linewidth=1.5)

for y_value in (-1, 1):
    for z_value in (-1, 1):
        axes.plot([-1, 1], [y_value, y_value], [z_value, z_value], color="black", linewidth=1.5)

axes.plot(coordinates, cosine, np.full_like(coordinates, -1), color="crimson", linewidth=2, label="z = −1")
axes.plot(coordinates, cosine, np.full_like(coordinates, 1), color="royalblue", linewidth=2, label="z = 1")
axes.plot(coordinates, np.full_like(coordinates, -1), cosine, color="darkorange", linewidth=2, label="y = −1")
axes.plot(coordinates, np.full_like(coordinates, 1), cosine, color="seagreen", linewidth=2, label="y = 1")
axes.plot(np.full_like(coordinates, -1), coordinates, cosine, color="purple", linewidth=2, label="x = −1")
axes.plot(np.full_like(coordinates, 1), coordinates, cosine, color="teal", linewidth=2, label="x = 1")

axes.set_title("Завдання 2 — куб із косинусоїдами на гранях")
axes.set_xlabel("x")
axes.set_ylabel("y")
axes.set_zlabel("z")
axes.set_xlim(-1.2, 1.2)
axes.set_ylim(-1.2, 1.2)
axes.set_zlim(-1.2, 1.2)
axes.set_box_aspect((1, 1, 1))
axes.view_init(elev=24, azim=-48)
axes.legend(loc="upper left", fontsize=9)

figure.tight_layout()
figure.savefig(Path(__file__).with_name("task2_cube_cosines.png"), dpi=200)
plt.show()
