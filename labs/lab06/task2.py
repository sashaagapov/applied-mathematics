# Лабораторна №6 | Завдання №2 (3.4.1)
# Дано: y'' + 4y' + 8y = sin(4x)
# Початкові умови: y(0) = 0, y'(0) = 1
# Знайти: загальний і частковий розв'язки, побудувати графік.
from sympy import symbols, Function, Eq, diff, sin, dsolve, checkodesol, pprint,lambdify
import numpy as np
import matplotlib.pyplot as plt

x = symbols("x", real=True)
y = Function("y")

equation = Eq(
    diff(y(x), x, 2) + 4 * diff(y(x), x) + 8 * y(x),
    sin(4 * x)
)
general_solution = dsolve(equation, y(x))

print("\nЗагальний розв'язок:")
pprint(general_solution, use_unicode=True)

initial_conditions = {
    y(0): 0,
    diff(y(x), x).subs(x, 0): 1
}
particular_solution = dsolve(
    equation,
    y(x),
    ics=initial_conditions
)
print("\nЧастковий розв'язок:")
pprint(particular_solution, use_unicode=True)
verification = checkodesol(equation, particular_solution)

value_at_zero = particular_solution.rhs.subs(x, 0)
print("y(0) =", value_at_zero)
derivative = diff(particular_solution.rhs, x)
value_at_zero_for_derative = derivative.subs(x,0)
print("y'(0) =", value_at_zero_for_derative)

x_values = np.linspace(-1, 6, 500)
numeric_function = lambdify(x, particular_solution.rhs, "numpy")
y_values = numeric_function(x_values)

plt.figure(figsize=(9, 5))
plt.plot(x_values, y_values, label="y(x)", linewidth=2)
plt.scatter(0, 0, color="red", label="y(0) = 0")

plt.title("Лабораторна №6 — Завдання №2")
plt.xlabel("x")
plt.ylabel("y(x)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

