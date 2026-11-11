from sympy import cos, integrate, lambdify, pi, simplify, sin, symbols
import matplotlib.pyplot as plt
import numpy as np

x = symbols("x", real=True)
n = symbols("n", integer=True, positive=True)
a0 = integrate(-1, (x, 0, pi)) / pi
an = simplify(integrate(-cos(n * x), (x, 0, pi)) / pi)
bn = simplify(integrate(-sin(n * x), (x, 0, pi)) / pi)
harmonics = 10
fourier_sum = a0 / 2 + sum(
    an.subs(n, index) * cos(index * x) + bn.subs(n, index) * sin(index * x)
    for index in range(1, harmonics + 1)
)

print("a0 =", a0)
print("an =", an)
print("bn =", bn)
print("Розклад Фур'є:", simplify(fourier_sum))

x_values = np.linspace(-np.pi, np.pi, 2000)
function_values = np.where(x_values < 0, 0, -1)
fourier_values = np.asarray(lambdify(x, fourier_sum, "numpy")(x_values), dtype=float)

plt.step(x_values, function_values, where="post", label="Початкова функція")
plt.plot(x_values, fourier_values, label="Ряд Фур'є (10 гармонік)")
plt.scatter([0], [-0.5], color="black", zorder=3, label="Сума ряду в x = 0")
plt.title("Завдання 3.1.1 — наближення рядом Фур'є")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.ylim(-1.5, 0.5)
plt.grid(True)
plt.legend()
plt.show()
