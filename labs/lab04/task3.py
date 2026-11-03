import matplotlib.pyplot as plt


def calculate_polar_curve():
    return


def update(frame):
    return


def build_figure():
    figure, axes = plt.subplots(
        figsize=(8, 8),
        subplot_kw={"projection": "polar"},
    )
    axes.set_title("Лабораторна №4 — Завдання 3: полярна крива", pad=18)
    figure.tight_layout()
    return figure, axes


def run() -> None:
    build_figure()
    plt.show()


if __name__ == "__main__":
    run()
