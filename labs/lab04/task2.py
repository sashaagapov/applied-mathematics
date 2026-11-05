import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def calculate_surface():
    values = np.linspace(-2, 2, 65)
    x, y = np.meshgrid(values, values)
    z = x * y
    return x, y, z


def update(frame, axes):
    axes.view_init(elev=30, azim=frame)


def build_figure():
    figure = plt.figure(figsize=(9, 7))
    axes = figure.add_subplot(projection="3d")

    x, y, z = calculate_surface()
    axes.plot_surface(x, y, z, cmap="viridis")

    axes.set_title("ЛР №4 — Завдання 2: 3D-поверхня")
    axes.set_xlabel("X")
    axes.set_ylabel("Y")
    axes.set_zlabel("Z")

    axes.set_xlim(-2, 2)
    axes.set_ylim(-2, 2)
    axes.set_zlim(-4, 4)

    figure.tight_layout()
    return figure, axes


def run():
    figure, axes = build_figure()

    _animation = FuncAnimation(
        figure,
        update,
        frames=None,
        interval=40,
        fargs=(axes,),
        cache_frame_data=False,
    )

    plt.show()


if __name__ == "__main__":
    run()
