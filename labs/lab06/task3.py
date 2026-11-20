
# Лабораторна №6 | Завдання №3 (4.1.1)
# Дано: x'(t) = 4x(t) + 3y(t) + t
#       y'(t) = -2x(t) - y(t)
# Знайти: загальний розв'язок системи.

from sympy import symbols, Function, Eq, diff, dsolve, pprint, simplify

t = symbols("t", real=True)
x = Function("x")
y = Function("y")

eq1 = Eq(diff(x(t), t), 4*x(t) + 3*y(t) + t)
eq2 = Eq(diff(y(t), t), -2*x(t) - y(t))

solution = dsolve(
    [eq1, eq2],
    [x(t), y(t)]
)

x_formula = solution[0].rhs
y_formula = solution[1].rhs

left1 = diff(x_formula, t)
right1 = 4*x_formula + 3*y_formula + t
check1 = simplify(left1 - right1)

left2 = diff(y_formula, t)
right2 = -2*x_formula - y_formula
check2 = simplify(left2 - right2)

print("\n" + "=" * 55)
print("ЛАБОРАТОРНА №6 | ЗАВДАННЯ №3")
print("=" * 55)

print("\nПочаткова система:")
pprint(eq1, use_unicode=True)
pprint(eq2, use_unicode=True)

print("\nЗагальний розв'язок:")
for result in solution:
    pprint(result, use_unicode=True)

print("\nПеревірка першого рівняння:")
print("Ліва частина - права частина =", check1)

print("\nПеревірка другого рівняння:")
print("Ліва частина - права частина =", check2)

if check1 == 0 and check2 == 0:
    print("\nУспішно — обидва рівняння виконуються.")
else:
    print("\nПомилка перевірки.")

print("=" * 55)
