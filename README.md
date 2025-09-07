Homework **HW-05**: locking, recursion, caching (memoization), generators, functional approach and decorators + optional CLI tasks.

---

## Table of Contents
- [Repository Structure](#repository-structure)
- [Installation & Setup](#installation--setup)
- [Task 1 — caching_fibonacci (closure + recursion)](#task-1--caching_fibonacci-closure--recursion)
- [Task 2 — generator_numbers & sum_profit (generators)](#task-2--generator_numbers--sum_profit-generators)
- [Task 3 — Log Analyzer (CLI, optional)](#task-3--log-analyzer-cli-optional)
- [Task 4 — Console Bot with input_error decorator](#task-4--console-bot-with-input_error-decorator)
- [Tests & Linters](#tests--linters)
- [Notes](#notes)
- [License](#license)

---
goit-algo-hw-05/
├── README.md
├── LICENSE
├── pyproject.toml
├── .gitignore
├── .pre-commit-config.yaml # (optional)
├── .github/
│ └── workflows/
│ └── ci.yml # GitHub Actions (tests + linters)
├── data/
│ └── sample.log # sample log file for Task 3
├── examples/
│ ├── benchmark_fib.py # Fibonacci benchmark
│ ├── cli.py # CLI for Task 1 (list/value)
│ └── parse_income.py # CLI for Task 2
├── src/
│ ├── init.py
│ ├── task1_fibonacci_closure.py # Task 1
│ ├── task2_income_generator.py # Task 2
│ ├── task3_log_analyzer.py # Task 3
│ ├── task4_console_bot.py # Task 4
│ └── utils/
│ ├── init.py
│ ├── decorators.py # generic @safe (not required for HW)
│ ├── generators.py # fib_generator(), window()
│ └── functional.py # functions as arguments example
├── main.py # CLI for Task 3
├── bot.py # CLI for Task 4
└── tests/
├── test_task1_fibonacci_closure.py
├── test_task2_income_generator.py
├── test_task3_log_analyzer.py
└── test_task4_console_bot.py
---