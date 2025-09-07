# Algorithmic Homework #5

Homework #5 from the course "Algorithms and Data Structures" in Python.  
The main goal is to deepen knowledge about:

- recursion;
- closures;
- generators;
- functional programming;
- using decorators;
- log analysis;
- creating CLI bots;
- testing and automation via GitHub Actions.

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

## Repository Structure

```bash
goit-algo-hw-05/
├── README.md
├── ЛІЦЕНЗІЯ
├── pyproject.toml
├── .gitignore
├── .pre-commit-config.yaml         
├── .github/
│   └── workflows/
│       └── ci.yml                  # GitHub Actions (Tests + Linters)
├── data/
│   └── sample.log                  # sample log file for Task 3
├── examples/
│   ├── benchmark_fib.py           # Fibonacci test
│   ├── cli.py                     # CLI for task 1 (list/value)
│   └── parse_income.py            # CLI for task 2
├── src/
│   ├── __init__.py
│   ├── task1_fibonacci_closure.py # Task 1
│   ├── task2_income_generator.py  # Task 2
│   ├── task3_log_analyzer.py      # Task 3
│   └── task4_console_bot.py       # Task 4
├── utils/
│   ├── __init__.py
│   ├── decorators.py              # generic @safe 
│   ├── generators.py              # fib_generator(), window()
│   ├── functional.py              # functions as arguments
│   ├── main.py                    # CLI for task 3
│   └── bot.py                     # CLI for task 4
├── tests/
│   ├── test_task1_fibonacci_closure.py
│   ├── test_task2_income_generator.py
│   ├── test_task3_log_analyzer.py
│   └── test_task4_console_bot.py
