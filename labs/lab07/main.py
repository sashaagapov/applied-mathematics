# STEM-проєкт | ІПЗ-21 | Варіант 1 | Завдання №1.11
#
# Дано:
# Еліпс, відстань між вершинами великої осі якого дорівнює 16,
# а відстань між фокусами - 10.
#
# Завдання:
# 1. Визначити параметри еліпса a, b, c.
# 2. Скласти канонічне рівняння еліпса.
# 3. Побудувати графік еліпса.
# 4. Позначити центр, вершини, фокуси та півосі.
# 5. Оформити графік і створити анімацію руху точки по еліпсу.
# 6. Продемонструвати сталість суми відстаней до фокусів.

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


a = 16 / 2
c = 10 / 2
b = np.sqrt(a**2 - c**2)

print("Велика піввісь a =", a)
print("Відстань від центра до фокуса c =", c)
print(f"Мала піввісь b = √{b**2:.0f} ≈ {b:.4f}")
print(f"Канонічне рівняння: x²/{a**2:.0f} + y²/{b**2:.0f} = 1")
print("Сума відстаней від точки еліпса до фокусів = 2a =", 2 * a)


t = np.linspace(0, 2 * np.pi, 400)
x_ellipse = a * np.cos(t)
y_ellipse = b * np.sin(t)

focus_1 = (-c, 0)
focus_2 = (c, 0)

fig, ax = plt.subplots(figsize=(10, 6.5))


ax.fill(x_ellipse, y_ellipse, color="tab:blue", alpha=0.08)
ax.plot(x_ellipse, y_ellipse, color="tab:blue", linewidth=2, label="Еліпс")
ax.plot(0, 0, "ko", label="Центр O(0; 0)")
ax.plot([-c, c], [0, 0], "o", color="tab:red", markersize=8,
        label=f"Фокуси F1(-{c:.0f}; 0), F2({c:.0f}; 0)")
ax.plot([-a, a], [0, 0], "s", color="tab:green", markersize=8,
        label=f"Вершини A1(-{a:.0f}; 0), A2({a:.0f}; 0)")


ax.plot([0, a], [0, 0], "--", color="gray", linewidth=1)
ax.plot([0, 0], [0, b], "--", color="gray", linewidth=1)
ax.text(a / 2, 0.3, f"a = {a:.0f}", ha="center")
ax.text(0.3, b + 0.55, f"b = √{b**2:.0f} ≈ {b:.2f}", va="center")



labels = [("O", (0, 0), (0, -16)), ("F1", focus_1, (0, -16)), ("F2", focus_2, (0, -16)),
          ("A1", (-a, 0), (-14, -16)), ("A2", (a, 0), (14, -16))]
for name, position, offset in labels:
    ax.annotate(name, position, textcoords="offset points", xytext=offset, ha="center")


point, = ax.plot([], [], "o", color="gold", markeredgecolor="black", markersize=10, label="Рухома точка M")
segment_1, = ax.plot([], [], color="tab:purple", linewidth=1.5, label="d1 - відстань до F1")
segment_2, = ax.plot([], [], color="tab:orange", linewidth=1.5, label="d2 - відстань до F2")
info = ax.text(0.02, 0.97, "", transform=ax.transAxes, va="top", family="monospace", fontsize=11,
               bbox=dict(boxstyle="round", facecolor="white", edgecolor="gray"))

ax.set_title(f"Еліпс x²/{a**2:.0f} + y²/{b**2:.0f} = 1")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_xlim(-10, 10)
ax.set_ylim(-8, 8)
ax.set_aspect("equal")
ax.grid(True, alpha=0.4)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=3)

frames = 240


def update(frame):

    angle = 2 * np.pi * frame / frames
    x = a * np.cos(angle)
    y = b * np.sin(angle)


    d1 = np.hypot(x - focus_1[0], y - focus_1[1])
    d2 = np.hypot(x - focus_2[0], y - focus_2[1])

    point.set_data([x], [y])
    segment_1.set_data([focus_1[0], x], [focus_1[1], y])
    segment_2.set_data([focus_2[0], x], [focus_2[1], y])
    info.set_text(f"d1      = {d1:5.2f}\nd2      = {d2:5.2f}\nd1 + d2 = {d1 + d2:5.2f}")
    return point, segment_1, segment_2, info



animation = FuncAnimation(fig, update, frames=frames, interval=40, blit=True)

plt.tight_layout()
plt.show()
