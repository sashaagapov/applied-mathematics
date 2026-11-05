import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


DRAW_FRAMES = 180


def calculate_polar_curve():
    phi = np.linspace(0, 2 * np.pi, 500)
    rho = 1 / (1 + np.sin(phi) / 3)
    return phi, rho


def update(frame, line, phi, rho):
    if frame <= DRAW_FRAMES:
        count = max(
            1,
            int(len(phi) * frame / DRAW_FRAMES)
        )

        line.set_data(phi[:count], rho[:count])

    else:
        rotation = (frame - DRAW_FRAMES) * 0.015
        line.set_data(phi + rotation, rho)

    return line,


def build_figure():
    figure, axes = plt.subplots(
        figsize=(8, 8),
        subplot_kw={"projection": "polar"},
    )

    line, = axes.plot(
        [], [],
        color="purple",
        linewidth=2.5
    )

    axes.set_title(
        "ЛР №4 — Завдання 3: Полярна крива",
        pad=20
    )
    axes.set_ylim(0, 1.65)
    axes.grid(True)

    figure.tight_layout()
    return figure, axes, line


def run():
    figure, _, line = build_figure()
    phi, rho = calculate_polar_curve()

    _animation = FuncAnimation(
        figure,
        update,
        frames=None,
        interval=30,
        fargs=(line, phi, rho),
        cache_frame_data=False,
    )

    plt.show()


if __name__ == "__main__":
    run()
