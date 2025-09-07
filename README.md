Homework **HW-05**: locking, recursion, caching (memoization), generators, functional approach and decorators + optional CLI tasks.

---

## Table of Contents
- [Завдання 1 — кешування Фібоначчі (замикання + рекурсія)](#завдання-1--кешування-фібоначчі-замикання--рекурсія)
- [Завдання 2 — generator_numbers та sum_profit (генератори)](#завдання-2--generator_numbers-та-sum_profit-генератори)
- [Завдання 3 — Аналізатор журналів (CLI, необов'язково)](#завдання-3--аналізатор-журналів-cli-необовязково)
- [Завдання 4 — Консольний бот з декоратором input_error](#завдання-4--консольний-бот-з-декоратором-input_error)

```bash
goit-algo-hw-05/
├── README.md
├── ЛІЦЕНЗІЯ
├── pyproject.toml
├── .gitignore
├── .pre-commit-config.yaml         # (необов'язково)
├── .github/
│   └── workflows/
│       └── ci.yml                  # Дії GitHub (тести + лінтери)
├── data/
│   └── sample.log                  # зразок файлу журналу для Завдання 3
├── examples/
│   ├── benchmark_fib.py           # Тест Фібоначчі
│   ├── cli.py                     # CLI для завдання 1 (список/значення)
│   └── parse_income.py            # CLI для завдання 2
├── src/
│   ├── __init__.py
│   ├── task1_fibonacci_closure.py # Завдання 1
│   ├── task2_income_generator.py  # Завдання 2
│   ├── task3_log_analyzer.py      # Завдання 3
│   └── task4_console_bot.py       # Завдання 4
├── utils/
│   ├── __init__.py
│   ├── decorators.py              # generic @safe (не обов'язково)
│   ├── generators.py              # fib_generator(), window()
│   ├── functional.py              # функції як аргументи (приклад)
│   ├── main.py                    # CLI для завдання 3
│   └── bot.py                     # CLI для завдання 4
├── tests/
│   ├── test_task1_fibonacci_closure.py
│   ├── test_task2_income_generator.py
│   ├── test_task3_log_analyzer.py
│   └── test_task4_console_bot.py
```