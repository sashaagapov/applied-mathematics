from sympy import asin, diff, integrate, simplify, sqrt, symbols
import matplotlib.pyplot as plt
import numpy as np

x = symbols("x", real=True)
y = sqrt(1 - x**2) + asin(x)
derivative = diff(y, x)
integrand = sqrt(2 / (1 + x))
length = simplify(integrate(integrand, (x, 0, 1)))

print("Довжина:", length)
print(f"Приблизно: {float(length):.4f}")
print("Похідна:", derivative)

x_values = np.linspace(0, 1, 400)
y_values = np.sqrt(1 - x_values**2) + np.arcsin(x_values)

plt.plot(x_values, y_values, label="y = √(1 − x²) + arcsin(x)")
plt.title("Завдання 8.4.1 — довжина кривої")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()
