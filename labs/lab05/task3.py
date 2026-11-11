from sympy import Interval, cos, diff, integrate, pi, simplify, sin, solveset, sqrt, symbols
import matplotlib.pyplot as plt
import numpy as np

t = symbols("t", real=True)
x = 4 * sqrt(2) * cos(t)**3
y = 2 * sqrt(2) * sin(t)**3

parameters = solveset(x - 2, t, domain=Interval(-pi / 2, pi / 2))
left_parameter, right_parameter = sorted(parameters)
area = simplify(integrate((x - 2) * diff(y, t), (t, left_parameter, right_parameter)))

print("Параметри перетину:", parameters)
print(f"Площа: {area} ≈ {float(area):.4f}")

parameter_values = np.linspace(-np.pi, np.pi, 600)
x_values = 4 * np.sqrt(2) * np.cos(parameter_values)**3
y_values = 2 * np.sqrt(2) * np.sin(parameter_values)**3
filled_parameters = np.linspace(-np.pi / 4, np.pi / 4, 400)
filled_x = 4 * np.sqrt(2) * np.cos(filled_parameters)**3
filled_y = 2 * np.sqrt(2) * np.sin(filled_parameters)**3

plt.plot(x_values, y_values, label="Параметрична крива")
plt.axvline(2, color="black", linestyle="--", label="x = 2")
plt.fill_betweenx(filled_y, 2, filled_x, alpha=0.3, label="Шукана площа")
plt.title("Завдання 8.3.1 — площа параметричної фігури")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.show()
