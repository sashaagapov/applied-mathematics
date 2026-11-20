# Лабораторна №6 | Завдання №4
# Дано: подвійний інтеграл від f(x, y) = x + 2y + 1 по області D, обмеженій лініями y = x² та y = 1.
# Знайти: значення інтеграла та побудувати область D.
from sympy import symbols, integrate, pprint, solve, Eq, Integer
import numpy as np
import matplotlib.pyplot as plt

x, y = symbols("x y", real=True)

f = x + 2*y + 1

curve1 = x**2
curve2 = Integer(1)

intersections = solve(Eq(curve1, curve2), x)
x_left, x_right = sorted(intersections)

midpoint = (x_left + x_right) / 2

if curve1.subs(x, midpoint) < curve2.subs(x, midpoint):
    y_lower = curve1
    y_upper = curve2
else:
    y_lower = curve2
    y_upper = curve1

inner_integral = integrate(f, (y, y_lower, y_upper))

print("Межі за x:")
pprint((x_left, x_right))

print("Межі за y:")
pprint((y_lower, y_upper))

print("Внутрішній інтеграл:")
pprint(inner_integral)


result = integrate(inner_integral, (x, x_left, x_right))

print("Результат подвійного інтеграла:")
pprint(result)

x_values = np.linspace(float(x_left), float(x_right), 400)

y_lower_values = np.array([float(y_lower.subs(x, value)) for value in x_values])
y_upper_values = np.array([float(y_upper.subs(x, value)) for value in x_values])

plt.figure(figsize=(8, 6))

plt.plot(x_values, y_lower_values, label="Нижня межа")
plt.plot(x_values, y_upper_values, label="Верхня межа")

plt.fill_between(x_values, y_lower_values, y_upper_values, alpha=0.3)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Область D")
plt.grid(True)
plt.legend()

plt.show()
