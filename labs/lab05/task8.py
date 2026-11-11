from sympy import oo, simplify, summation, symbols
import matplotlib.pyplot as plt
import numpy as np

n = symbols("n", integer=True, positive=True)
k = symbols("k", integer=True, positive=True)
term = (3**n + 4**n) / 12**n
total_sum = simplify(summation(term, (n, 1, oo)))
partial_sum = simplify(summation(term, (n, 1, k)))

print("Загальний член ряду:", term)
print("Часткова сума S_k =", partial_sum)
print("Сума нескінченного ряду S =", total_sum)
print("Наближене значення =", total_sum.evalf())

indices = np.arange(1, 21)
partial_values = [float(partial_sum.subs(k, int(index))) for index in indices]

plt.plot(indices, partial_values, marker="o", label="Часткова сума Sₖ")
plt.axhline(float(total_sum), color="crimson", linestyle="--", label="S = 5/6")
plt.title("Завдання 8 — сума числового ряду")
plt.xlabel("Кількість членів k")
plt.ylabel("Сума")
plt.grid(True)
plt.legend()
plt.show()
