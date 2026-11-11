# Lab 05 — Calculus with SymPy

Eight tasks solved symbolically with SymPy and plotted with Matplotlib: areas between curves, arc lengths, complex roots, a Fourier series, and the sum of a series. Each `taskN.py` prints its result to the console and then opens a plot; the [report](Lab05_Report.docx) is included.

## Tasks and results

The values below are the console output of running each script.

| Task | Script | Result |
| --- | --- | --- |
| 1 | [`task1.py`](task1.py) | Area between two curves; they intersect at `x = 0` and `x = 7/2`; area = 343/48 ≈ 7.1458 |
| 2 | [`task2.py`](task2.py) | Area = π/4 + 2 ≈ 2.7854 |
| 3 | [`task3.py`](task3.py) | Parametric curve; parameters of intersection ±π/4; area = 3π/2 − 2 ≈ 2.7124 |
| 4 | [`task4.py`](task4.py) | Arc length = 4 − 2√2 ≈ 1.1716 |
| 5 | [`task5.py`](task5.py) | Parametric arc length = 2e^(2π) − 2 |
| 6 | [`task6.py`](task6.py) | The four complex roots of z⁴ = −16, √2·(±1 ± i), drawn in the complex plane |
| 7 | [`task7.py`](task7.py) | Fourier coefficients a₀ = −1, aₙ = 0, bₙ = ((−1)ⁿ − 1)/(πn), and a plotted partial sum |
| 8 | [`task8.py`](task8.py) | Series with general term (3ⁿ + 4ⁿ)/12ⁿ; sum S = 5/6 ≈ 0.8333 |

## Run

From the repository root, install the [dependencies](../../requirements.txt), then run any task:

```bash
python labs/lab05/task1.py
```
