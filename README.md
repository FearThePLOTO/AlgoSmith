<div align="center">
  <img src="assets/LOGO.jpg"/>
</div>

A desktop application that analyzes the time complexity of Python algorithms. Paste your code, run it, and get the Big-O class detected automatically backed by curve fitting, static AST analysis, and an AI explanation.

---

<!--
---

## Project Structure

```
AlgoSmith/
├── main.py
├── web/                  # Eel frontend (HTML/CSS/JS)
├── engine/
│   ├── executor.py       # Code execution + threading
│   ├── timer.py          # Precision timing
│   └── analyzer.py       # Curve fitting + AST analysis
├── ai/
│   ├── explainer.py      # AI complexity explanation
│   └── optimizer.py      # AI code optimizer
├── algorithms/           # Built-in algorithm library
├── assets/
└── .env                  # API keys (never committed)
```

---
-->

## Setup

```bash
git clone https://github.com/your-repo/AlgoSmith.git
cd AlgoSmith
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in the root:

```
ANTHROPIC_API_KEY=your_key_here
MODEL_NAME=claude-sonnet-4-20250514
MAX_TOKENS=1000
```

Then run:

```bash
python main.py
```
