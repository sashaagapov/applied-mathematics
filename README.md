# Applied Mathematics

Лабораторні роботи з прикладної математики: обчислення з NumPy та SymPy і візуалізація за допомогою Matplotlib. Приклади реалізовано для варіанта 1.

## Роботи

| Робота | Зміст | Результат |
| --- | --- | --- |
| [Lab 01](labs/lab01/README.md) | Матричні рівняння, системи лінійних рівнянь і векторна алгебра | Консольні обчислення; [звіт](labs/lab01/Lab1_Report.docx) |
| [Lab 02](labs/lab02/README.md) | Діаграми, геометричні фігури та криві | Графіки в `labs/lab02/results/` |
| [Lab 03](labs/lab03/README.md) | 3D-об'єкти, поверхні, стовпці та мозаїка | Сім графіків у `labs/lab03/results/` |

Приклад lab 03: поверхня `z = xy`.

![Сідлоподібна поверхня z = xy з lab 03](docs/lab03/task3-surface.png)

## Встановлення

Потрібен Python 3. Команди виконуються з кореня репозиторію.

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Запуск

From the repository root:

```bash
python labs/lab01/main.py
python labs/lab02/main.py
python labs/lab03/main.py
```

Lab 01 виводить обчислення в консоль; lab 02 і lab 03 зберігають PNG та відкривають графіки. Каталоги результатів ігноруються Git, тому повний набір зображень потрібно створити локально запуском скрипту. Приклади та список семи побудов наведено в [описі lab 03](labs/lab03/README.md).
