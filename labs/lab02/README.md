# Lab 02 — 2D Visualization

[The script](main.py) builds 11 Matplotlib figures across three tasks. All 11 outputs are included below. The [lab report](Lab2_Report.docx) is also available.

| Task | Plots saved under `labs/lab02/results/` |
| --- | --- |
| 1 — Charts | `stacked_bar_chart.png` (six groups, four segments each), `pie_chart.png` (six sectors), `scatter_chart.png` (51 points). |
| 2 — Shapes | `task2_primitives.png`, `task2_polygon.png`. |
| 3 — Curves and functions | `task3_implicit_curve.png`, `task3_parametric_curve.png`, `task3_polar_curve.png`, `task3_colored_curve.png`, `task3_functions_subplots.png`, `task3_functions_combined.png`. The last plot marks the intersections also printed in the console. |

After [installing the dependencies](../../README.md#run), run from the repository root:

```bash
python labs/lab02/main.py
```

The script saves the PNG files and opens the figures in Matplotlib windows. The `results/` directory is ignored by Git; selected copies for documentation live in `docs/lab02/`.

## Gallery

### Task 1 — charts

![Stacked bar chart for six groups](../../docs/lab02/stacked_bar_chart.png)
![Pie chart with six sectors](../../docs/lab02/pie_chart.png)
![Scatter plot with 51 points](../../docs/lab02/scatter_chart.png)

### Task 2 — geometric shapes

![Geometric primitives and arrow](../../docs/lab02/task2_primitives.png)
![Polygon construction](../../docs/lab02/task2_polygon.png)

### Task 3 — curves and functions

![Implicit curve](../../docs/lab02/task3_implicit_curve.png)
![Parametric curve](../../docs/lab02/task3_parametric_curve.png)
![Polar curve](../../docs/lab02/task3_polar_curve.png)
![Colored curve with equation label](../../docs/lab02/task3_colored_curve.png)
![Function plots in separate panels](../../docs/lab02/task3_functions_subplots.png)
![Combined functions with marked intersections](../../docs/lab02/task3_functions_combined.png)
