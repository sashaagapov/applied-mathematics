# МКР №2 | Завдання №3 (4.1.1)
# Дано: інтеграл ∬ (x² + y² + z²) dσ по поверхні G: z = √(x² + y²), 0 ≤ z ≤ 2.
# Знайти: значення інтеграла за допомогою Python.

from sympy import symbols, sqrt, cos, sin, pi, diff, simplify, integrate, lambdify
import numpy as np

x, y, theta = symbols("x y theta", real=True)
r = symbols("r", positive=True)

z = sqrt(x**2 + y**2)
f = x**2 + y**2 + z**2
dsigma = simplify(sqrt(1 + diff(z, x)**2 + diff(z, y)**2))

integrand = simplify((f * dsigma).subs({x: r*cos(theta), y: r*sin(theta)}) * r)
result = integrate(integrate(integrand, (r, 0, 2)), (theta, 0, 2*pi))

n = 1000
r_values = (np.arange(n) + 0.5) * 2 / n
theta_values = (np.arange(n) + 0.5) * 2 * np.pi / n
r_grid, theta_grid = np.meshgrid(r_values, theta_values)
function = lambdify((r, theta), integrand, "numpy")
numeric = function(r_grid, theta_grid).sum() * (2 / n) * (2 * np.pi / n)

print("dσ =", dsigma, "dx dy")
print("Підінтегральна функція в полярних координатах:", integrand)
print("Інтеграл (sympy):", result, "≈", result.evalf(10))
print("Інтеграл (numpy):", numeric)
print("Різниця:", abs(float(result) - numeric))
