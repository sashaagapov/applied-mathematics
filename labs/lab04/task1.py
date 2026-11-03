import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

_animation: FuncAnimation | None = None

def calculate_curve():
    t = np.linspace(0, 2, 300)

    x = (2 * t**2) / (1 + t**3)
    y = (3 * t) / (1 + t**3)

    return x, y


def update(frame, line, x, y):
    left_shift = -2 - x.min()
    right_shift = 3 - x.max()

    travel_frames = 80
    phase = frame % (2 * travel_frames)

    if phase <= travel_frames:
        progress = phase / travel_frames
        shift = left_shift + (right_shift - left_shift) * progress
    else:
        progress = (phase - travel_frames) / travel_frames
        shift = right_shift - (right_shift - left_shift) * progress

    line.set_data(x + shift, y)

    if phase < 40:
        line.set_color("blue")
    elif phase < 80:
        line.set_color("red")
    elif phase < 120:
        line.set_color("green")
    else:
        line.set_color("purple")

    return line,


def build_figure():
    figure, axes = plt.subplots(figsize=(9, 6))
    x, y = calculate_curve()
    line, = axes.plot(x, y, color="blue", linewidth=2)
    axes.set_title("Лабораторна №4 — Завдання 1: 2D-крива")
    axes.set_xlabel("X")
    axes.set_ylabel("Y")
    axes.grid(True, linestyle="--", alpha=0.35)
    axes.set_xlim(-2, 3)
    axes.set_ylim(-0.2, 1.8)
    figure.tight_layout()
    return figure, axes, line, x, y


def run() -> None:
    global _animation

    figure, _axes, line, x, y = build_figure()

    _animation = FuncAnimation(
        figure,
        update,
        frames=None,
        interval=40,
        fargs=(line, x, y),
        cache_frame_data=False,
    )

    plt.show()


if __name__ == "__main__":
    run()
