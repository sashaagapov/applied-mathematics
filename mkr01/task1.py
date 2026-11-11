from pathlib import Path

import matplotlib.pyplot as plt
from sympy import Matrix, simplify

a = Matrix([-3, 0, 4])
b = Matrix([6, 2, -5])
c = 2 * a + b

length_a = a.norm()
dot_product = c.dot(a)
scalar_projection = simplify(dot_product / length_a)
vector_projection = simplify(dot_product / a.dot(a)) * a

print("a =", tuple(a))
print("b =", tuple(b))
print("c = 2a + b =", tuple(c))
print("|a| =", length_a)
print("c · a =", dot_product)
print("Скалярна проєкція пр_a(c) =", scalar_projection, "≈", float(scalar_projection))
print("Векторна проєкція proj_a(c) =", tuple(vector_projection))

figure = plt.figure(figsize=(9, 7))
axes = figure.add_subplot(projection="3d")

axes.plot([-4, 4], [0, 0], [0, 0], color="gray", linewidth=0.8)
axes.plot([0, 0], [-3, 3], [0, 0], color="gray", linewidth=0.8)
axes.plot([0, 0], [0, 0], [-1, 5], color="gray", linewidth=0.8)

axes.quiver(0, 0, 0, float(a[0]), float(a[1]), float(a[2]), color="royalblue", linewidth=2)
axes.quiver(0, 0, 0, float(c[0]), float(c[1]), float(c[2]), color="crimson", linewidth=2)
axes.quiver(0, 0, 0, float(vector_projection[0]), float(vector_projection[1]), float(vector_projection[2]), color="seagreen", linewidth=2)
axes.plot(
    [float(c[0]), float(vector_projection[0])],
    [float(c[1]), float(vector_projection[1])],
    [float(c[2]), float(vector_projection[2])],
    color="black",
    linestyle="--",
)

axes.plot([], [], [], color="royalblue", linewidth=2, label="a = (−3, 0, 4)")
axes.plot([], [], [], color="crimson", linewidth=2, label="c = 2a + b = (0, 2, 3)")
axes.plot([], [], [], color="seagreen", linewidth=2, label="proj_a(c) = (−36/25, 0, 48/25)")

axes.set_title("Завдання 1 — проєкція вектора c на вектор a")
axes.set_xlabel("x")
axes.set_ylabel("y")
axes.set_zlabel("z")
axes.set_xlim(-4, 4)
axes.set_ylim(-3, 3)
axes.set_zlim(-1, 5)
axes.set_box_aspect((8, 6, 6))
axes.view_init(elev=22, azim=-55)
axes.legend(loc="upper left")

figure.tight_layout()
figure.savefig(Path(__file__).with_name("task1_projection.png"), dpi=200)
plt.show()
