import numpy as np
import sympy as sp


def print_task_header(number, title):
    print("\n" + "=" * 70)
    print(f"Завдання {number}. {title}")
    print("=" * 70)


def print_part(title):
    print(f"\n{title}:")


def task1():
    print_task_header(1, "Матричний поліном f(A)")

    A = np.array([
        [1, 2, -1],
        [3, 0, 1],
        [0, 1, 0],
    ])

    print_part("Умова")
    print("Знайти f(A), якщо f(x) = 2x^2 + 3x + 1.")
    print("Матриця A:")
    print(A)

    A_squared = A @ A
    I = np.eye(3, dtype=int)
    f_A = 2 * A_squared + 3 * A + I

    print_part("Обчислення")
    print("A^2:")
    print(A_squared)
    print("f(A) = 2A^2 + 3A + I")

    print_part("Результат")
    print(f_A)


def task2():
    print_task_header(2, "Матричне рівняння A * X = B")

    A = sp.Matrix([
        [3, 2],
        [1, 1],
    ])

    B = sp.Matrix([
        [1, 2, 7],
        [0, 4, 8],
    ])

    print_part("Умова")
    print("Розв'язати матричне рівняння A * X = B.")
    print("A =")
    sp.pprint(A)
    print("B =")
    sp.pprint(B)

    A_inverse = A.inv()
    X = A_inverse @ B

    print_part("Обчислення")
    print("A^(-1) =")
    sp.pprint(A_inverse)
    print("X = A^(-1) * B")

    print_part("Результат")
    sp.pprint(X)

    print_part("Перевірка")
    print("A * X =")
    sp.pprint(A @ X)


def task3():
    print_task_header(3, "Дослідження СЛАР на сумісність")

    A = sp.Matrix([
        [1, 1, -3, 0],
        [1, -1, 1, 2],
        [3, 3, -9, 0],
        [1, 2, -5, -1],
    ])

    b = sp.Matrix([2, -1, 6, 3])
    augmented = A.row_join(b)

    print_part("Умова")
    print("Дослідити систему, задану розширеною матрицею.")
    print("[A | b] =")
    sp.pprint(augmented)


    rank_A = A.rank()
    rank_augmented = augmented.rank()
    x1, x2, x3, x4 = sp.symbols("x1 x2 x3 x4")
    solution = sp.linsolve((A, b), (x1, x2, x3, x4))

    print_part("Обчислення")
    print("rank(A) =", rank_A)
    print("rank([A | b]) =", rank_augmented)

    print_part("Результат")
    if rank_A == rank_augmented:
        print("Система сумісна, бо ранги рівні.")
        print("Загальний розв'язок:")
        sp.pprint(solution)
    else:
        print("Система несумісна, бо rank(A) не дорівнює rank([A | b]).")
        print("Загального розв'язку не існує.")


def task4():
    print_task_header(4, "Скалярні обчислення з векторами")

    a, b = sp.symbols("a b")

    expression_a = sp.expand((4 * a + 7 * b) * (a - 2 * b))
    expression_b_squared = sp.expand((2 * a - 3 * b) ** 2)

    a_length = sp.Integer(2)
    print(a_length)
    b_length = sp.Integer(5)
    phi = sp.pi / 3

    print_part("Умова")
    print("Обчислити:")
    print("a) (4a + 7b) * (a - 2b)")
    print("б) |2a - 3b|")
    print(f"Дано: |a| = {a_length}, |b| = {b_length}, φ = π/3")


    dot_ab = a_length * b_length * sp.cos(phi)

    values = {
        a**2: a_length**2,
        a * b: dot_ab,
        b**2: b_length**2,
    }

    result_a = expression_a.subs(values)
    result_b = sp.sqrt(expression_b_squared.subs(values))

    print_part("Обчислення")
    print("a * b = |a| * |b| * cos(phi) =", dot_ab)
    print("(4a + 7b) * (a - 2b) =", expression_a)
    print("(2a - 3b)^2 =", expression_b_squared)

    print_part("Результат")
    print("a) (4a + 7b) * (a - 2b) =", result_a)
    print("б) |2a - 3b| =", result_b)
    print(f"Наближено: {float(result_b):.6f}")


def task5():
    print_task_header(5, "Площа грані та об'єм піраміди")

    A = np.array([1, -2, 3], dtype=int)
    B = np.array([2, 4, 7], dtype=int)
    C = np.array([-3, -4, 0], dtype=int)
    D = np.array([1, 0, 5], dtype=int)

    print_part("Умова")
    print("Обчислити площу грані ABC і об'єм піраміди ABCD.")
    print("A =", A)
    print("B =", B)
    print("C =", C)
    print("D =", D)

    AB = B - A
    AC = C - A
    AD = D - A

    cross_product = np.cross(AB, AC)
    area_exact = sp.sqrt(int(np.dot(cross_product, cross_product))) / 2
    area_approx = np.linalg.norm(cross_product) / 2
    mixed_product = int(np.dot(AD, cross_product))
    volume = sp.Rational(abs(mixed_product), 6)
    print_part("Обчислення")
    print("AB =", AB)
    print("AC =", AC)
    print("AD =", AD)
    print("AB x AC =", cross_product)
    print("AD * (AB x AC) =", mixed_product)

    print_part("Результат")
    print("Площа трикутника ABC = |AB x AC| / 2 =", area_exact)
    print(f"Площа наближено = {area_approx:.6f}")
    print("Об'єм піраміди ABCD = |AD * (AB x AC)| / 6 =", volume)


def main():
    print("Лабораторна робота №1")
    print("Варіант 1")
    print("Тема: застосування лінійної та векторної алгебри в Python")
    task1()
    task2()
    task3()
    task4()
    task5()


if __name__ == "__main__":
    main()
