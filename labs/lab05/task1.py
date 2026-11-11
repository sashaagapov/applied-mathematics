from sympy import integrate, solve, symbols
import matplotlib.pyplot as plt
import numpy as np

x = symbols("x", real=True)
parabola = x**2 - 2 * x - 1
line = 3 * x / 2 - 1

intersections = solve(parabola - line, x)
area = integrate(line - parabola, (x, intersections[0], intersections[1]))

print("Точки перетину:", intersections)
print(f"Площа: {area} ≈ {float(area):.4f}")

x_values = np.linspace(float(intersections[0]), float(intersections[1]), 400)
parabola_values = x_values**2 - 2 * x_values - 1
line_values = 3 * x_values / 2 - 1

plt.plot(x_values, parabola_values, label="y = x² − 2x − 1")
plt.plot(x_values, line_values, label="y = 3x/2 − 1")
plt.fill_between(x_values, parabola_values, line_values, alpha=0.3, label="Шукана площа")
plt.scatter([float(value) for value in intersections], [float(parabola.subs(x, value)) for value in intersections])
plt.title("Завдання 8.1.1 — площа фігури")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()
