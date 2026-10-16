# Applied Mathematics

Laboratory work for the Applied Mathematics course. The repository contains Python programs using NumPy, SymPy, and Matplotlib.

## Structure

```text
labs/
├── lab01/    # linear and vector algebra
├── lab02/    # Matplotlib charts and curves
└── lab03/    # starter environment for the third laboratory work
```

Reports produced for the course are kept with their corresponding lab. Lecture and methodological materials are kept outside this public repository in the University materials review area until they are deliberately moved to shared storage.

## Setup

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

## Run a lab

From the repository root:

```bash
python labs/lab01/main.py
python labs/lab02/main.py
python labs/lab03/main.py
```

Lab 2 writes generated plots to `labs/lab02/results/`. That directory is intentionally ignored because the plots can be regenerated.
