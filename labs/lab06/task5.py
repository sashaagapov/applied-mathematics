
# Лабораторна №6 | Завдання №5 (1.3.1)
# Дано: x² + y² + 6x ≤ 0, y ≥ √3x, y ≤ 0.
# Знайти: площу області у декартових і полярних координатах, побудувати графіки.

from sympy import symbols, solve, sqrt, atan, atan2, sin, cos, integrate, simplify, lambdify
import numpy as np
import matplotlib.pyplot as plt

x, y, r, theta = symbols("x y r theta", real=True)

circle = x**2 + y**2 + 6*x
line = sqrt(3) * x

x_left, x_right = sorted(solve(circle.subs(y, 0), x))
x_cross = sorted(solve(circle.subs(y, line), x))[0]
circle_lower = solve(circle, y)[0]

area_xy = simplify(
    integrate(-circle_lower, (x, x_left, x_cross))
    + integrate(-line, (x, x_cross, x_right))
    
)

theta_start = atan2(0, x_left)
theta_end = theta_start + atan(line.coeff(x))

polar_circle = circle.subs({x: r*cos(theta), y: r*sin(theta)})
r_outer = solve(polar_circle, r)[1]

area_polar = simplify(
    integrate(r, (r, 0, r_outer), (theta, theta_start, theta_end))
)

print("Декартові координати:", area_xy, "≈", area_xy.evalf(10))
print("Полярні координати:", area_polar, "≈", area_polar.evalf(10))
print("Різниця:", simplify(area_xy - area_polar))

x_arc = np.linspace(float(x_left), float(x_cross), 300)
x_line = np.linspace(float(x_cross), float(x_right), 200)

y_arc = lambdify(x, circle_lower, "numpy")(x_arc)
y_line = lambdify(x, line, "numpy")(x_line)

angles = np.linspace(float(theta_start), float(theta_end), 400)
radii = lambdify(theta, r_outer, "numpy")(angles)

fig = plt.figure(figsize=(12, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2, projection="polar")

ax1.plot(x_arc, y_arc, label="Коло")
ax1.plot(x_line, y_line, label="Пряма")
ax1.axhline(0, color="black", label="y = 0")
ax1.fill_between(x_arc, y_arc, 0, alpha=0.3)
ax1.fill_between(x_line, y_line, 0, alpha=0.3)
ax1.set_title("Декартові координати")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_aspect("equal")
ax1.grid(True)
ax1.legend()

ax2.plot(angles, radii)
ax2.fill_between(angles, 0, radii, alpha=0.3)
ax2.set_title("Полярні координати")
ax2.grid(True)

plt.tight_layout()
plt.show()
