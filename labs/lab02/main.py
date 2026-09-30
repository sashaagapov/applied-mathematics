from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon, Rectangle, Wedge


VARIANT = 1
GROUP_COUNT = VARIANT + 5
SECTOR_COUNT = VARIANT + 5
POINT_COUNT = VARIANT + 50

RESULTS_DIR = Path(__file__).parent / "results"


def build_stacked_bar_chart() -> plt.Figure:
    groups = [f"Група {number}" for number in range(1, GROUP_COUNT + 1)]
    x = np.arange(GROUP_COUNT)

    segments = {
        "Сегмент 1": [18, 22, 15, 24, 20, 17],
        "Сегмент 2": [12, 16, 19, 14, 18, 21],
        "Сегмент 3": [21, 13, 17, 20, 15, 18],
        "Сегмент 4": [9, 14, 11, 16, 13, 12],
    }
    colors = ["#4C78A8", "#F58518", "#54A24B", "#E45756"]

    fig, ax = plt.subplots(figsize=(10, 6))
    bottom = np.zeros(GROUP_COUNT)

    for (label, values), color in zip(segments.items(), colors):
        values = np.array(values)
        ax.bar(
            x,
            values,
            bottom=bottom,
            label=label,
            color=color,
            edgecolor="white",
            linewidth=0.8,
        )
        bottom += values

    ax.set_title("Стовпчаста діаграма для варіанта 1", fontsize=15, pad=12)
    ax.set_xlabel("Групи", fontsize=11)
    ax.set_ylabel("Значення", fontsize=11)
    ax.set_xticks(x, groups)
    ax.grid(axis="y", linestyle="--", alpha=0.35)
    ax.legend(title="Кольорові сегменти")
    fig.tight_layout()

    return fig


def build_pie_chart() -> plt.Figure:
    labels = [f"Сектор {number}" for number in range(1, SECTOR_COUNT + 1)]
    values = np.array([18, 12, 20, 15, 22, 13])
    colors = ["#4C78A8", "#F58518", "#E45756", "#72B7B2", "#54A24B", "#B279A2"]

    explode = [0.08 if number % 3 == 0 else 0 for number in range(1, SECTOR_COUNT + 1)]

    fig, ax = plt.subplots(figsize=(8, 7))
    ax.pie(
        values,
        labels=labels,
        colors=colors,
        explode=explode,
        autopct="%1.1f%%",
        startangle=90,
        counterclock=False,
        wedgeprops={"edgecolor": "white", "linewidth": 1.2},
        textprops={"fontsize": 10},
    )
    ax.set_title("Кругова діаграма з виділеними секторами", fontsize=15, pad=18)
    ax.axis("equal")
    fig.tight_layout()

    return fig


def build_scatter_chart() -> plt.Figure:
    generator = np.random.default_rng(seed=VARIANT)
    x = generator.uniform(0, 100, POINT_COUNT)
    y = 0.65 * x + generator.normal(0, 8, POINT_COUNT)

    markers = ["o", "s", "^", "D", "P", "X"]
    colors = ["#4C78A8", "#F58518", "#54A24B", "#E45756", "#B279A2", "#FF9DA6"]

    fig, ax = plt.subplots(figsize=(10, 6))

    for group_number, start in enumerate(range(0, POINT_COUNT, 10)):
        finish = min(start + 10, POINT_COUNT)
        ax.scatter(
            x[start:finish],
            y[start:finish],
            marker=markers[group_number],
            color=colors[group_number],
            s=58,
            alpha=0.85,
            edgecolors="white",
            linewidths=0.7,
            label=f"Точки {start + 1}–{finish}",
        )

    ax.set_title("Діаграма розсіювання для 51 випадкової точки", fontsize=15, pad=12)
    ax.set_xlabel("Вісь X", fontsize=11)
    ax.set_ylabel("Вісь Y", fontsize=11)
    ax.grid(True, linestyle="--", alpha=0.35)
    ax.legend(title="Групи точок", ncol=2)
    fig.tight_layout()

    return fig


def build_task2_primitives() -> plt.Figure:
    fig, ax = plt.subplots(figsize=(10, 8))

    semicircle = Wedge((-4, 3), 1, 0, 180, facecolor="#4C78A8", edgecolor="black")
    triangle = Polygon([(-4, -3), (-2, -3), (-3, -1)], facecolor="#54A24B", edgecolor="black")
    sector = Wedge((0, -2), 1.3, 25, 135, facecolor="#B279A2", edgecolor="black")
    diamond = Polygon([(4, 4), (5, 3), (4, 2), (3, 3)], facecolor="#E45756", edgecolor="black")
    rectangle = Rectangle((3, -3.8), 2, 1.5, facecolor="#F58518", edgecolor="black")

    for figure in [semicircle, triangle, sector, diamond, rectangle]:
        ax.add_patch(figure)

    ax.annotate(
        "",
        xy=(0.5, 3.5),
        xytext=(-1.5, 3.5),
        arrowprops={"arrowstyle": "->", "color": "#72B7B2", "linewidth": 2.5},
    )

    ax.set_title("Лабораторна №2 — Завдання 2. Частина 1", fontsize=15, pad=12)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_xlim(-6, 6)
    ax.set_ylim(-5, 5)
    ax.set_aspect("equal", adjustable="box")
    fig.tight_layout()

    return fig


def build_task2_polygon() -> plt.Figure:
    fig, ax = plt.subplots(figsize=(8, 8))

    vertices = [(0, 3.5), (-3, -2), (3, -2)]
    polygon = Polygon(vertices, closed=True, facecolor="#72B7B2", edgecolor="none")
    ax.add_patch(polygon)

    for start, finish in zip(vertices, vertices[1:] + vertices[:1]):
        ax.annotate(
            "",
            xy=finish,
            xytext=start,
            arrowprops={"arrowstyle": "->", "color": "#1F4E79", "linewidth": 2.5},
        )

    ax.text(0, -0.2, "Варіант 1", ha="center", va="center", fontsize=14)
    ax.set_title("Лабораторна №2 — Завдання 2. Частина 2", fontsize=15, pad=12)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_xlim(-5, 5)
    ax.set_ylim(-4, 5)
    ax.set_aspect("equal", adjustable="box")
    fig.tight_layout()

    return fig


def build_task3_implicit_curve() -> plt.Figure:
    x = np.linspace(-6, 6, 400)
    y = np.linspace(-6, 6, 400)
    x_grid, y_grid = np.meshgrid(x, y)
    z = np.sin(x_grid) - np.cos(y_grid) - x_grid + y_grid

    fig, ax = plt.subplots(figsize=(8, 7))
    ax.contour(x_grid, y_grid, z, levels=[0], colors="#4C78A8", linewidths=2)
    ax.text(-5.7, 4.9, r"$\sin(x) - \cos(y) = x - y$", fontsize=13)
    ax.set_title("Лабораторна №2 — Завдання 3.1а", fontsize=15, pad=12)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.set_aspect("equal", adjustable="box")
    fig.tight_layout()

    return fig


def build_task3_parametric_curve() -> plt.Figure:
    parameter_left = np.linspace(-5, -1.2, 500)
    parameter_right = np.linspace(-0.8, 5, 500)

    x_left = 3 * parameter_left / (1 + parameter_left**3)
    y_left = 2 * parameter_left**2 / (1 + parameter_left**3)
    x_right = 3 * parameter_right / (1 + parameter_right**3)
    y_right = 2 * parameter_right**2 / (1 + parameter_right**3)

    fig, ax = plt.subplots(figsize=(8, 7))
    ax.plot(x_left, y_left, color="#F58518", linewidth=2)
    ax.plot(x_right, y_right, color="#F58518", linewidth=2)
    ax.text(-5.7, 3.3, r"$x(t)=\frac{3t}{1+t^3},\ y(t)=\frac{2t^2}{1+t^3}$", fontsize=12)
    ax.set_title("Лабораторна №2 — Завдання 3.1б", fontsize=15, pad=12)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_xlim(-6, 6)
    ax.set_ylim(-5, 4)
    ax.set_aspect("equal", adjustable="box")
    fig.tight_layout()

    return fig


def build_task3_polar_curve() -> plt.Figure:
    phi = np.linspace(0, 2 * np.pi, 500)
    rho = 1 / (1 + (1 / 3) * np.sin(phi))

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={"projection": "polar"})
    ax.plot(phi, rho, color="#54A24B", linewidth=2)
    ax.text(np.pi / 2, 0.25, r"$\rho=\frac{1}{1+\frac{1}{3}\sin(\varphi)}$", ha="center", fontsize=13)
    ax.set_title("Лабораторна №2 — Завдання 3.2", fontsize=15, pad=18)
    fig.tight_layout()

    return fig


def build_task3_colored_curve() -> plt.Figure:
    y_left = np.linspace(-8, -2.7, 300)
    y_middle = np.linspace(-2.7, 2.7, 300)
    y_right = np.linspace(2.7, 8, 300)

    fig, ax = plt.subplots(figsize=(10, 6))

    for y_values, color in [
        (y_left, "#4C78A8"),
        (y_middle, "#F58518"),
        (y_right, "#54A24B"),
    ]:
        x_values = (y_values**2 - 10) / 2
        ax.plot(x_values, y_values, color=color, linewidth=2.5)

    ax.text(7, -4.5, r"$y^2 - 2x - 10 = 0$", rotation=204, fontsize=13)
    ax.set_title("Лабораторна №2 — Завдання 3.3", fontsize=15, pad=12)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_xlim(-6, 28)
    ax.set_ylim(-9, 9)
    ax.set_aspect("equal", adjustable="box")
    fig.tight_layout()

    return fig


def calculate_difference(x):
    return 2 / (x**2 - 1) - np.log(x)


def find_root(left, right):
    for _ in range(60):
        middle = (left + right) / 2

        if calculate_difference(left) * calculate_difference(middle) <= 0:
            right = middle
        else:
            left = middle

    return (left + right) / 2


def find_intersection_points():
    points = []

    for start, finish in [(0.01, 0.99), (1.01, 5)]:
        x_values = np.linspace(start, finish, 1000)

        for left, right in zip(x_values[:-1], x_values[1:]):
            if calculate_difference(left) * calculate_difference(right) < 0:
                x_value = find_root(left, right)
                points.append((x_value, np.log(x_value)))
                break

    return points


def build_task3_functions_subplots() -> plt.Figure:
    x_left = np.linspace(-5, -1.05, 400)
    x_middle = np.linspace(-0.95, 0.95, 400)
    x_right = np.linspace(1.05, 5, 400)
    x_logarithm = np.linspace(0.05, 5, 500)

    fig, (ax_f, ax_g) = plt.subplots(1, 2, figsize=(12, 5))

    for x_values in [x_left, x_middle, x_right]:
        ax_f.plot(x_values, 2 / (x_values**2 - 1), color="#5BC0EB", linewidth=2)

    ax_f.set_title(r"$f(x)=\frac{2}{x^2-1}$")
    ax_f.set_xlabel("X")
    ax_f.set_ylabel("Y")
    ax_f.set_xlim(-5, 5)
    ax_f.set_ylim(-10, 10)

    ax_g.plot(x_logarithm, np.log(x_logarithm), color="#E63946", linewidth=2)
    ax_g.set_title(r"$g(x)=\ln(x)$")
    ax_g.set_xlabel("X")
    ax_g.set_ylabel("Y")
    ax_g.set_xlim(0, 5)
    ax_g.set_ylim(-3.5, 2)

    fig.suptitle("Лабораторна №2 — Завдання 3.4.1", fontsize=15)
    fig.tight_layout()

    return fig


def build_task3_functions_combined(intersection_points) -> plt.Figure:
    x_left = np.linspace(0.05, 0.95, 400)
    x_right = np.linspace(1.05, 5, 400)
    x_logarithm = np.linspace(0.05, 5, 500)

    fig, ax = plt.subplots(figsize=(10, 7))
    ax.plot(x_left, 2 / (x_left**2 - 1), color="#5BC0EB", linewidth=2)
    ax.plot(x_right, 2 / (x_right**2 - 1), color="#5BC0EB", linewidth=2)
    ax.plot(x_logarithm, np.log(x_logarithm), color="#E63946", linewidth=3)

    for x_value, y_value in intersection_points:
        ax.scatter(x_value, y_value, color="#7B2CBF", s=55, zorder=3)
        ax.annotate(
            f"({x_value:.4f}, {y_value:.4f})",
            xy=(x_value, y_value),
            xytext=(10, 12),
            textcoords="offset points",
        )

    ax.axhline(0, color="black", linewidth=1)
    ax.axvline(0, color="black", linewidth=1)
    ax.text(0.3, -3.4, r"$f(x)=\frac{2}{x^2-1}$", color="#168AAD", fontsize=13)
    ax.text(3.1, 1.35, r"$g(x)=\ln(x)$", color="#E63946", fontsize=13)
    ax.set_title("Лабораторна №2 — Завдання 3.4.2", fontsize=15, pad=12)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_xlim(-0.25, 5)
    ax.set_ylim(-4, 4)
    fig.tight_layout()

    return fig


def task1() -> None:
    RESULTS_DIR.mkdir(exist_ok=True)

    figures = {
        "stacked_bar_chart.png": build_stacked_bar_chart(),
        "pie_chart.png": build_pie_chart(),
        "scatter_chart.png": build_scatter_chart(),
    }

    for filename, figure in figures.items():
        figure.savefig(RESULTS_DIR / filename, dpi=150, bbox_inches="tight")

    print(f"Варіант: {VARIANT}")
    print(f"Кількість груп: {GROUP_COUNT}")
    print(f"Кількість секторів: {SECTOR_COUNT}")
    print(f"Кількість точок: {POINT_COUNT}")
    print(f"Результати збережено в: {RESULTS_DIR}")

    plt.show()


def task2() -> None:
    RESULTS_DIR.mkdir(exist_ok=True)

    figures = {
        "task2_primitives.png": build_task2_primitives(),
        "task2_polygon.png": build_task2_polygon(),
    }

    for filename, figure in figures.items():
        figure.savefig(RESULTS_DIR / filename, dpi=150, bbox_inches="tight")

    print("Лабораторна №2 — Завдання 2")
    print(f"Результати збережено в: {RESULTS_DIR}")

    plt.show()


def task3() -> None:
    RESULTS_DIR.mkdir(exist_ok=True)
    intersection_points = find_intersection_points()

    figures = {
        "task3_implicit_curve.png": build_task3_implicit_curve(),
        "task3_parametric_curve.png": build_task3_parametric_curve(),
        "task3_polar_curve.png": build_task3_polar_curve(),
        "task3_colored_curve.png": build_task3_colored_curve(),
        "task3_functions_subplots.png": build_task3_functions_subplots(),
        "task3_functions_combined.png": build_task3_functions_combined(intersection_points),
    }

    for filename, figure in figures.items():
        figure.savefig(RESULTS_DIR / filename, dpi=150, bbox_inches="tight")

    print("Лабораторна №2 — Завдання 3")
    for x_value, y_value in intersection_points:
        print(f"Точка перетину: ({x_value:.6f}, {y_value:.6f})")
    print(f"Результати збережено в: {RESULTS_DIR}")

    plt.show()


def main() -> None:
    task1()
    task2()
    task3()


if __name__ == "__main__":
    main()
