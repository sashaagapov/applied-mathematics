from sympy import im, re, simplify, solve, symbols
import matplotlib.pyplot as plt

z = symbols("z")
roots = solve(z**4 + 16, z)
real_parts = [float(re(root)) for root in roots]
imaginary_parts = [float(im(root)) for root in roots]

print("Корені рівняння z⁴ = −16:")
for index, root in enumerate(roots, 1):
    print(f"z{index} = {simplify(root)}")

print("\nКоординати коренів:")
for index, root in enumerate(roots, 1):
    print(f"z{index}: ({re(root)}, {im(root)})")

plt.scatter(real_parts, imaginary_parts, color="crimson", s=60)
for index, (real_part, imaginary_part) in enumerate(zip(real_parts, imaginary_parts), 1):
    plt.annotate(f"z{index}", (real_part, imaginary_part), xytext=(6, 6), textcoords="offset points")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.title("Корені рівняння z⁴ = −16")
plt.xlabel("Re(z)")
plt.ylabel("Im(z)")
plt.xlim(-2.5, 2.5)
plt.ylim(-2.5, 2.5)
plt.gca().set_aspect("equal", adjustable="box")
plt.grid(True)
plt.show()
