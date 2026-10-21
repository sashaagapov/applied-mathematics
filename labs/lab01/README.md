# Lab 01 — Linear and Vector Algebra

[The script](main.py) works through five variant 1 tasks with NumPy and SymPy. It prints the intermediate calculations and answers to the console; it does not create plots. The submitted [report](Lab1_Report.docx) is also available.

| Task | Calculation |
| --- | --- |
| 1 | Evaluate the matrix polynomial `f(A) = 2A² + 3A + I`. |
| 2 | Solve `AX = B` and check the solution by multiplying `A` and `X`. |
| 3 | Compare the coefficient and augmented matrix ranks and solve the linear system. |
| 4 | Evaluate two expressions using vector lengths and the angle between the vectors. |
| 5 | Find the area of triangle `ABC` and the volume of pyramid `ABCD`. |

For Task 1, the script evaluates `f(A)` for `A = [[1, 2, -1], [3, 0, 1], [0, 1, 0]]` and prints:

```text
[[18  8 -1]
 [15 15 -3]
 [ 6  3  3]]
```

After [installing the dependencies](../../README.md#run), run from the repository root:

```bash
python labs/lab01/main.py
```

If Windows reports a `UnicodeEncodeError` for `φ` or `π`, set `$env:PYTHONIOENCODING = "utf-8"` in PowerShell before running the script.
