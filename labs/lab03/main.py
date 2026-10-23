from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


VARIANT = 1
RESULTS_DIR = Path(__file__).parent / "results"


def build_task1_figure() -> plt.Figure:
    """Будує одну 3D-сцену з шістьма геометричними об’єктами."""
    fig = plt.figure(figsize=(13, 9))
    ax = fig.add_subplot(projection="3d")

    hemisphere_color = "#4C78A8"
    arrow_color = "#E45756"
    pyramid_color = "#F58518"
    ellipse_color = "#B279A2"
    parallelepiped_color = "#54A24B"
    cone_color = "#72B7B2"

    angle = np.linspace(0, 2 * np.pi, 60)
    polar_angle = np.linspace(0, np.pi / 2, 30)

    angle_grid, polar_angle_grid = np.meshgrid(angle, polar_angle)
    hemisphere_radius = 1.5
    hemisphere_x = -5 + hemisphere_radius * np.cos(angle_grid) * np.sin(polar_angle_grid)
    hemisphere_y = 4 + hemisphere_radius * np.sin(angle_grid) * np.sin(polar_angle_grid)
    hemisphere_z = hemisphere_radius * np.cos(polar_angle_grid)

    ax.plot_surface(
        hemisphere_x,
        hemisphere_y,
        hemisphere_z,
        color=hemisphere_color,
        alpha=0.78,
        edgecolor="none",
    )

    arrow_start = (-6, -4, 0.6)
    arrow_direction = (2.5, 1.2, 1.4)
    ax.quiver(
        *arrow_start,
        *arrow_direction,
        color=arrow_color,
        linewidth=2.8,
        arrow_length_ratio=0.16,
    )

    pyramid_vertices = np.array(
        [
            [-1.5, 2.5, 0],
            [1.5, 2.5, 0],
            [1.5, 5.5, 0],
            [-1.5, 5.5, 0],
            [0, 4, 3],
        ]
    )

    pyramid_faces = [
        [pyramid_vertices[index], pyramid_vertices[(index + 1) % 4], pyramid_vertices[4]]
        for index in range(4)
    ]
    pyramid_faces.append([pyramid_vertices[index] for index in range(4)])

    ax.add_collection3d(
        Poly3DCollection(
            pyramid_faces,
            facecolors=pyramid_color,
            edgecolors="black",
            linewidths=0.8,
            alpha=0.78,
        )
    )

    ellipse_parameter = np.linspace(0, 2 * np.pi, 200)
    ellipse_x = 2.1 * np.cos(ellipse_parameter)
    ellipse_y = -3 + 1.2 * np.sin(ellipse_parameter)
    ellipse_z = np.full_like(ellipse_parameter, 1.2)

    ax.plot(ellipse_x, ellipse_y, ellipse_z, color=ellipse_color, linewidth=3)

    parallelepiped_vertices = np.array(
        [
            [4, 3, 0], [6.8, 3, 0], [6.8, 5.4, 0], [4, 5.4, 0],
            [4, 3, 2.4], [6.8, 3, 2.4], [6.8, 5.4, 2.4], [4, 5.4, 2.4],
        ]
    )

    parallelepiped_faces = [
        [parallelepiped_vertices[index] for index in face]
        for face in ([0, 1, 2, 3], [4, 5, 6, 7], [0, 1, 5, 4],
                     [1, 2, 6, 5], [2, 3, 7, 6], [3, 0, 4, 7])
    ]
    ax.add_collection3d(
        Poly3DCollection(
            parallelepiped_faces,
            facecolors=parallelepiped_color,
            edgecolors="black",
            linewidths=0.8,
            alpha=0.72,
        )
    )

    cone_angle = np.linspace(0, 2 * np.pi, 60)
    cone_height_values = np.linspace(0, 3, 30)
    cone_angle_grid, cone_height_grid = np.meshgrid(cone_angle, cone_height_values)
    cone_radius = 1.45 * (1 - cone_height_grid / 3)
    cone_x = 5 + cone_radius * np.cos(cone_angle_grid)
    cone_y = -3 + cone_radius * np.sin(cone_angle_grid)
    cone_z = cone_height_grid
    ax.plot_surface(cone_x, cone_y, cone_z, color=cone_color, alpha=0.78, edgecolor="none")
    ax.plot(5 + 1.45 * np.cos(cone_angle), -3 + 1.45 * np.sin(cone_angle), 0, color="black")

    legend_items = [
        Patch(color=hemisphere_color, label="Півсфера"),
        Patch(color=arrow_color, label="3D-стрілка"),
        Patch(color=pyramid_color, label="Чотирикутна піраміда"),
        Patch(color=ellipse_color, label="Плоский еліпс"),
        Patch(color=parallelepiped_color, label="Прямокутний паралелепіпед"),
        Patch(color=cone_color, label="Конус"),
    ]
    ax.legend(handles=legend_items, loc="upper left", bbox_to_anchor=(1.02, 1))
    ax.set_title("Лабораторна робота №3 — Завдання 1: 3D геометричні об’єкти", pad=20)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_xlim(-8, 8)
    ax.set_ylim(-6.5, 6.5)
    ax.set_zlim(0, 4.5)
    ax.set_box_aspect((16, 13, 5))
    ax.view_init(elev=25, azim=-55)
    fig.subplots_adjust(right=0.78)

    return fig


def task1() -> None:
    """Зберігає результат побудови Завдання 1 у PNG-файл."""
    RESULTS_DIR.mkdir(exist_ok=True)
    figure = build_task1_figure()
    output_path = RESULTS_DIR / "task1_3d_shapes.png"
    figure.savefig(output_path, dpi=150, bbox_inches="tight")

    print("Лабораторна робота №3 — Завдання 1")
    print(f"Варіант: {VARIANT}")
    print(f"Результат збережено в: {output_path}")


def build_task2_prism() -> plt.Figure:
    """Будує трикутну призму з ребрами у вигляді 3D-стрілок."""
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(projection="3d")

    prism_vertices = np.array(
        [
            [-2.0, -1.2, 0.0],
            [2.0, -1.2, 0.0],
            [0.0, 2.0, 0.0],
            [-2.0, -1.2, 3.0],
            [2.0, -1.2, 3.0],
            [0.0, 2.0, 3.0],
        ]
    )

    prism_faces = [
        [prism_vertices[index] for index in face]
        for face in ([0, 1, 2], [3, 4, 5], [0, 1, 4, 3],
                     [1, 2, 5, 4], [2, 0, 3, 5])
    ]

    ax.add_collection3d(
        Poly3DCollection(
            prism_faces,
            facecolors="#72B7B2",
            edgecolors="none",
            alpha=0.48,
        )
    )

    prism_edges = [
        (0, 1), (1, 2), (2, 0),
        (3, 4), (4, 5), (5, 3),
        (0, 3), (1, 4), (2, 5),
    ]
    for start_index, end_index in prism_edges:
        start = prism_vertices[start_index]
        end = prism_vertices[end_index]

        direction = end - start
        ax.quiver(
            *start,
            *direction,
            color="#1F4E79",
            linewidth=2.0,
            arrow_length_ratio=0.12,
        )

    ax.text(0, -0.05, 1.45, "Variant 1", color="#111111", fontsize=13, ha="center")
    ax.set_title("Лабораторна робота №3 — Завдання 2: трикутна призма", pad=18)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_xlim(-3, 3)
    ax.set_ylim(-2, 3)
    ax.set_zlim(-0.3, 3.6)
    ax.set_box_aspect((6, 5, 4))
    ax.view_init(elev=24, azim=-55)
    fig.tight_layout()

    return fig


def task2() -> None:
    """Зберігає результат побудови Завдання 2 у PNG-файл."""
    RESULTS_DIR.mkdir(exist_ok=True)
    figure = build_task2_prism()
    output_path = RESULTS_DIR / "task2_3d_prism.png"
    figure.savefig(output_path, dpi=150, bbox_inches="tight")

    print("Лабораторна робота №3 — Завдання 2")
    print(f"Варіант: {VARIANT}")
    print(f"Результат збережено в: {output_path}")


def build_task3_surface() -> plt.Figure:
    """Будує сідлоподібну поверхню z = xy."""
    x = np.linspace(-4, 4, 100)
    y = np.linspace(-4, 4, 100)

    x_grid, y_grid = np.meshgrid(x, y)

    z_grid = x_grid * y_grid

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(projection="3d")

    surface = ax.plot_surface(
        x_grid,
        y_grid,
        z_grid,
        cmap="coolwarm",
        edgecolor="none",
        antialiased=True,
    )
    fig.colorbar(surface, ax=ax, shrink=0.68, pad=0.1, label="Значення z")

    ax.set_title(r"Лабораторна робота №3 — Завдання 3: $z = xy$", pad=18)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_zlim(-16, 16)
    ax.computed_zorder = False
    ax.quiver(-4, 0, 0, 8, 0, 0, color="red", arrow_length_ratio=0.08, linewidth=2, zorder=10)
    ax.quiver(0, -4, 0, 0, 8, 0, color="red", arrow_length_ratio=0.08, linewidth=2, zorder=10)
    ax.quiver(0, 0, -16, 0, 0, 32, color="red", arrow_length_ratio=0.08, linewidth=2, zorder=10)
    ax.set_box_aspect((8, 8, 6))
    ax.view_init(elev=28, azim=-45)
    fig.tight_layout()

    return fig


def task3() -> None:
    """Зберігає результат побудови Завдання 3 у PNG-файл."""
    RESULTS_DIR.mkdir(exist_ok=True)
    figure = build_task3_surface()
    output_path = RESULTS_DIR / "task3_surface.png"
    figure.savefig(output_path, dpi=150, bbox_inches="tight")

    print("Лабораторна робота №3 — Завдання 3")
    print(f"Варіант: {VARIANT}")
    print(f"Результат збережено в: {output_path}")


def build_task4_surface() -> plt.Figure:
    """Будує кольорову поверхню z = 3x + y - xy на заданій області."""
    x = np.linspace(0, 1, 100)
    y = np.linspace(0, 4, 100)

    x_grid, y_grid = np.meshgrid(x, y)

    z_grid = 3 * x_grid + y_grid - x_grid * y_grid

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(projection="3d")

    surface = ax.plot_surface(
        x_grid,
        y_grid,
        z_grid,
        cmap="viridis",
        edgecolor="none",
        antialiased=True,
    )
    fig.colorbar(surface, ax=ax, shrink=0.68, pad=0.1, label="Значення z")

    ax.set_title(r"Лабораторна робота №3 — Завдання 4: $z = 3x + y - xy$", pad=18)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 4)
    ax.set_zlim(0, 4)
    ax.set_box_aspect((2, 6, 4))
    ax.view_init(elev=28, azim=-55)
    fig.tight_layout()

    return fig


def task4() -> None:
    """Зберігає результат побудови Завдання 4 у PNG-файл."""
    RESULTS_DIR.mkdir(exist_ok=True)
    figure = build_task4_surface()
    output_path = RESULTS_DIR / "task4_colored_surface.png"
    figure.savefig(output_path, dpi=150, bbox_inches="tight")

    print("Лабораторна робота №3 — Завдання 4")
    print(f"Варіант: {VARIANT}")
    print(f"Результат збережено в: {output_path}")


def build_task5_bars() -> plt.Figure:
    """Будує три набори просторових стовпців для варіанта 1."""
    bar_count = VARIANT + 4
    x_positions = np.arange(bar_count) * 1.2
    bar_width = 0.55
    bar_depth = 0.16

    first_y_positions = np.full(bar_count, 1.0)
    second_y_positions = np.full(bar_count, 2.0)
    third_y_positions = np.linspace(0.05, 1.0, bar_count)

    third_x_positions = x_positions + 0.65


    first_heights = np.array([2.2, 3.4, 1.8, 4.0, 2.8])
    second_heights = np.array([1.6, 2.5, 3.6, 2.1, 3.1])
    third_heights = np.array([1.4, 2.8, 2.0, 3.3, 2.4])
    z_positions = np.zeros(bar_count)

    fig = plt.figure(figsize=(11, 8))
    ax = fig.add_subplot(projection="3d")

    ax.bar3d(
        x_positions,
        first_y_positions,
        z_positions,
        bar_width,
        bar_depth,
        first_heights,
        color="#4C78A8",
        alpha=0.82,
        shade=True,
    )
    ax.bar3d(
        x_positions,
        second_y_positions,
        z_positions,
        bar_width,
        bar_depth,
        second_heights,
        color="#F58518",
        alpha=0.82,
        shade=True,
    )
    ax.bar3d(
        third_x_positions,
        third_y_positions,
        z_positions,
        bar_width,
        bar_depth,
        third_heights,
        color="#54A24B",
        alpha=0.82,
        shade=True,
    )

    legend_items = [
        Patch(color="#4C78A8", label="Набір 1: y = 1"),
        Patch(color="#F58518", label="Набір 2: y = 2"),
        Patch(color="#54A24B", label="Набір 3: y від 0.05 до 1"),
    ]
    ax.legend(handles=legend_items, loc="upper left")
    ax.set_title("Лабораторна робота №3 — Завдання 5: просторові стовпці", pad=18)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z (висота)")
    ax.set_xlim(-0.3, 6.1)
    ax.set_ylim(0, 2.4)
    ax.set_zlim(0, 4.5)
    ax.set_box_aspect((7, 3, 4.5))
    ax.view_init(elev=24, azim=-58)
    fig.tight_layout()

    return fig


def task5() -> None:
    """Зберігає результат побудови Завдання 5 у PNG-файл."""
    RESULTS_DIR.mkdir(exist_ok=True)
    figure = build_task5_bars()
    output_path = RESULTS_DIR / "task5_3d_bars.png"
    figure.savefig(output_path, dpi=150, bbox_inches="tight")

    print("Лабораторна робота №3 — Завдання 5")
    print(f"Варіант: {VARIANT}, кількість стовпців у наборі: {VARIANT + 4}")
    print(f"Результат збережено в: {output_path}")


def build_task6_surface() -> plt.Figure:
    """Будує кольорову хвилясту поверхню z = sin(x) cos(y)."""
    x = np.linspace(-np.pi, np.pi, 120)
    y = np.linspace(-np.pi, np.pi, 120)

    x_grid, y_grid = np.meshgrid(x, y)

    z_grid = np.sin(x_grid) * np.cos(y_grid)

    fig = plt.figure(figsize=(11, 8))
    ax = fig.add_subplot(projection="3d")

    surface = ax.plot_surface(
        x_grid,
        y_grid,
        z_grid,
        cmap="turbo",
        edgecolor="none",
        antialiased=True,
    )

    ax.contourf(x_grid, y_grid, z_grid, zdir="z", offset=-1.2, cmap="turbo", alpha=0.7)
    fig.colorbar(surface, ax=ax, shrink=0.68, pad=0.1, label="Значення z")

    ax.text2D(0.02, 0.9, "Варіант 1", transform=ax.transAxes, fontsize=12, weight="bold")
    ax.set_title(r"Лабораторна робота №3 — Завдання 6: $z = \sin(x)\cos(y)$", pad=18)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_xlim(-np.pi, np.pi)
    ax.set_ylim(-np.pi, np.pi)
    ax.set_zlim(-1.2, 1.2)
    ax.set_box_aspect((7, 7, 3))
    #ax.view_init(elev=32, azim=-55)
    fig.tight_layout()

    return fig


def task6() -> None:
    """Зберігає результат побудови Завдання 6 у PNG-файл."""
    RESULTS_DIR.mkdir(exist_ok=True)
    figure = build_task6_surface()
    output_path = RESULTS_DIR / "task6_custom_surface.png"
    figure.savefig(output_path, dpi=150, bbox_inches="tight")

    print("Лабораторна робота №3 — Завдання 6")
    print(f"Варіант: {VARIANT}")
    print(f"Результат збережено в: {output_path}")


def build_task7_mosaic() -> plt.Figure:
    """Будує мозаїку з каркаса, 3D-точок і полярних контурів."""
    x = np.linspace(-3, 3, 50)
    y = np.linspace(-3, 3, 50)

    x_grid, y_grid = np.meshgrid(x, y)
    z_grid = x_grid * y_grid

    fig = plt.figure(figsize=(14, 12))
    wireframe_ax = fig.add_axes([0.06, 0.56, 0.4, 0.34], projection="3d")
    scatter_ax = fig.add_axes([0.54, 0.56, 0.4, 0.34], projection="3d")
    polar_ax = fig.add_axes([0.28, 0.08, 0.44, 0.36], projection="polar")


    wireframe_ax.plot_wireframe(
        x_grid,
        y_grid,
        z_grid,
        rstride=3,
        cstride=3,
        color="#1F4E79",
        linewidth=0.65,
    )
    wireframe_ax.set_title(r"Каркас поверхні $z = xy$", pad=10)
    wireframe_ax.set_xlabel("X")
    wireframe_ax.set_ylabel("Y")
    wireframe_ax.set_zlabel("Z")
    wireframe_ax.set_zlim(-9, 9)
    wireframe_ax.set_box_aspect((6, 6, 4.5))
    wireframe_ax.view_init(elev=25, azim=-50)


    scatter = scatter_ax.scatter(
        x_grid[::3, ::3],
        y_grid[::3, ::3],
        z_grid[::3, ::3],
        c=z_grid[::3, ::3],
        cmap="coolwarm",
        s=13,
        alpha=0.85,
        depthshade=True,
    )
    scatter_ax.set_title(r"Розсіяні 3D-точки $z = xy$", pad=10)
    scatter_ax.set_xlabel("X")
    scatter_ax.set_ylabel("Y")
    scatter_ax.set_zlabel("Z")
    scatter_ax.set_zlim(-9, 9)
    scatter_ax.set_box_aspect((6, 6, 4.5))
    scatter_ax.view_init(elev=25, azim=-50)
    fig.colorbar(scatter, ax=scatter_ax, shrink=0.55, pad=0.06, label="Z")

    phi = np.linspace(0, 2 * np.pi, 240)
    rho = np.linspace(0, 1.65, 160)

    phi_grid, rho_grid = np.meshgrid(phi, rho)
    field = rho_grid * (1 + np.sin(phi_grid) / 3)
    levels = np.linspace(0, 2, 17)
    polar_ax.contourf(phi_grid, rho_grid, field, levels=levels, cmap="YlGnBu")
    polar_ax.contour(phi_grid, rho_grid, field, levels=levels, colors="#355C7D", linewidths=0.45)

    target_curve = polar_ax.contour(
        phi_grid,
        rho_grid,
        field,
        levels=[1],
        colors="#C2185B",
        linewidths=2.6,
    )
    polar_ax.clabel(target_curve, fmt={1.0: "F = 1"}, fontsize=10)
    polar_ax.set_title(r"Полярні контури: $F(\rho, \varphi)$ та рівень $F = 1$", pad=18)
    polar_ax.set_rmax(1.65)
    polar_ax.set_rlabel_position(135)
    polar_ax.grid(alpha=0.45)

    fig.suptitle("Лабораторна робота №3 — Завдання 7: мозаїка графіків", fontsize=16, y=0.98)

    return fig


def task7() -> None:
    """Зберігає результат побудови Завдання 7 у PNG-файл."""
    RESULTS_DIR.mkdir(exist_ok=True)
    figure = build_task7_mosaic()
    output_path = RESULTS_DIR / "task7_mosaic.png"
    figure.savefig(output_path, dpi=150, bbox_inches="tight")

    print("Лабораторна робота №3 — Завдання 7")
    print(f"Варіант: {VARIANT}")
    print(f"Результат збережено в: {output_path}")


def main() -> None:
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
    task7()
    plt.show()


if __name__ == "__main__":
    main()
