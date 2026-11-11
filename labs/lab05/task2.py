from sympy import cos, integrate, pi, symbols
import matplotlib.pyplot as plt
import numpy as np

phi = symbols("phi", real=True)
outer_radius = 1 + cos(phi)
inner_radius = 1

area = integrate((outer_radius**2 - inner_radius**2) / 2, (phi, -pi / 2, pi / 2))
print(f"Площа: {area} ≈ {float(area):.4f}")

angles = np.linspace(-np.pi / 2, np.pi / 2, 400)
outer_values = 1 + np.cos(angles)
inner_values = np.ones_like(angles)

figure, axis = plt.subplots(subplot_kw={"projection": "polar"})
axis.plot(angles, outer_values, label="ρ = 1 + cos(φ)")
axis.plot(angles, inner_values, label="ρ = 1")
axis.fill_between(angles, inner_values, outer_values, alpha=0.3, label="Шукана площа")
axis.set_title("Завдання 8.2.1\nплоща в полярних координатах", pad=20)
axis.legend(loc="lower left", bbox_to_anchor=(1.05, 0))
plt.show()
