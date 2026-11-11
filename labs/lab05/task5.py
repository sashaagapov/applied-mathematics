from sympy import cos, diff, exp, integrate, pi, simplify, sin, sqrt, symbols
import matplotlib.pyplot as plt
import numpy as np

t = symbols("t", real=True)
x = exp(t) * (cos(t) + sin(t))
y = exp(t) * (cos(t) - sin(t))
derivative_x = simplify(diff(x, t))
derivative_y = simplify(diff(y, t))
integrand = simplify(sqrt(derivative_x**2 + derivative_y**2))
length = simplify(integrate(integrand, (t, 0, 2 * pi)))

print("Похідна x:", derivative_x)
print("Похідна y:", derivative_y)
print("Підінтегральний вираз:", integrand)
print("Довжина:", length)
print(f"Приблизно: {float(length):.4f}")

parameter_values = np.linspace(0, 2 * np.pi, 1000)
x_values = np.exp(parameter_values) * (np.cos(parameter_values) + np.sin(parameter_values))
y_values = np.exp(parameter_values) * (np.cos(parameter_values) - np.sin(parameter_values))

plt.plot(x_values, y_values)
plt.title("Завдання 8.5.1 — параметрична крива")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.grid(True)
plt.show()
