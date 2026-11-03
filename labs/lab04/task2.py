import matplotlib.pyplot as plt


def calculate_surface():
    return


def update(frame):
    return


def build_figure():
    figure = plt.figure(figsize=(9, 7))
    axes = figure.add_subplot(projection="3d")
    axes.set_title("Лабораторна №4 — Завдання 2: 3D-поверхня")
    axes.set_xlabel("X")
    axes.set_ylabel("Y")
    axes.set_zlabel("Z")
    figure.tight_layout()
    return figure, axes


def run() -> None:
    build_figure()
    plt.show()


if __name__ == "__main__":
    run()
