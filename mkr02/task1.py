# МКР №2 | Завдання №1 (4.1.1)
# Дано: поверхня G: z = √(x² + y²), обмежена площинами z = 0 і z = 2.
# Знайти: побудувати 3D-модель поверхні із зафарбовуванням.

import matplotlib.pyplot as plt
import numpy as np

r = np.linspace(0, 2, 50)
theta = np.linspace(0, 2 * np.pi, 100)
r_grid, theta_grid = np.meshgrid(r, theta)

x = r_grid * np.cos(theta_grid)
y = r_grid * np.sin(theta_grid)
z = r_grid

fig = plt.figure(figsize=(8, 7))
ax = fig.add_subplot(projection="3d")

ax.plot_surface(x, y, z, cmap="viridis", alpha=0.9)
ax.plot(2 * np.cos(theta), 2 * np.sin(theta), 2, color="red", label="z = 2")

ax.set_title("Поверхня z = √(x² + y²), 0 ≤ z ≤ 2")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.legend()

plt.tight_layout()
plt.show()
