# Лабораторна №6 | Завдання №1 (3.3.1)
# Дано: y'' - 2y' + y = x*e^x
# Знайти: загальний розв'язок диференціального рівняння.
from sympy import symbols, Function, Eq, diff, exp, dsolve, checkodesol, pprint, expand

x = symbols("x", real=True)
y = Function("y")

equation = Eq(
    diff(y(x), x, 2) - 2 * diff(y(x), x) + y(x),
    x * exp(x)
)

solution = dsolve(equation, y(x))

pretty_solution = Eq(
    y(x),
    exp(x) * expand(solution.rhs / exp(x))
)

verification = checkodesol(equation, solution)

print("\n" + "=" * 55)
print("ЛАБОРАТОРНА №6 | ЗАВДАННЯ №1")
print("=" * 55)

print("\nПочаткове диференціальне рівняння:")
pprint(equation, use_unicode=True)

print("\nЗагальний розв'язок:")
pprint(pretty_solution, use_unicode=True)

print("\nПеревірка:")
if verification == (True, 0):
    print("Успішно — розв'язок задовольняє рівняння.")
else:
    print("Результат перевірки:", verification)

print("=" * 55)
