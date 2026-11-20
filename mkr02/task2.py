# МКР №2 | Завдання №2 (4.1.1)
# Дано: поверхня G: z = √(x² + y²), обмежена площинами z = 0 і z = 2.
# Знайти: зобразити проєкцію поверхні на площину xOy із заповненням області.

import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2 * np.pi, 300)
x = 2 * np.cos(theta)
y = 2 * np.sin(theta)

fig, ax = plt.subplots(figsize=(6, 6))

ax.fill(x, y, color="skyblue", alpha=0.6, label="D: x² + y² ≤ 4")
ax.plot(x, y, color="navy")

ax.set_title("Проєкція поверхні на площину xOy")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_aspect("equal")
ax.grid(True)
ax.legend()

plt.tight_layout()
plt.show()
