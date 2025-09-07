from __future__ import annotations

import sys
from collections import Counter
from typing import Dict, List

# Допустимі рівні логування (у верхньому регістрі)
VALID_LEVELS = {"INFO", "ERROR", "DEBUG", "WARNING"}


def parse_log_line(line: str) -> Dict[str, str]:
    """
    Парсить один рядок логу формату:
      YYYY-MM-DD HH:MM:SS LEVEL Message...

    Повертає словник:
      {"date": str, "time": str, "level": str, "message": str}

    Генерує ValueError, якщо формат некоректний або рівень невідомий.
    """
    raw = line.strip()
    if not raw:
        raise ValueError("Порожній рядок")

    parts = raw.split(maxsplit=3)  # очікуємо 4 частини
    if len(parts) < 4:
        raise ValueError("Неправильний формат логу (очікується 4 токени)")

    date, time, level, message = parts
    level = level.upper()
    if level not in VALID_LEVELS:
        raise ValueError(f"Невідомий рівень логування: {level}")

    return {"date": date, "time": time, "level": level, "message": message}


def load_logs(file_path: str) -> List[Dict[str, str]]:
    """
    Зчитує файл та повертає список словників-логів.
    Пропускає некоректні рядки, виводячи попередження у stderr.
    """
    logs: List[Dict[str, str]] = []
    with open(file_path, "r", encoding="utf-8") as fh:
        for lineno, line in enumerate(fh, start=1):
            try:
                rec = parse_log_line(line)
            except ValueError as e:
                print(
                    f"[WARN] Рядок {lineno} пропущено: {e}",
                    file=sys.stderr,
                )
                continue
            logs.append(rec)
    return logs


def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    """
    Повертає записи лише заданого рівня (case-insensitive).
    Використано елемент функціонального програмування: filter + lambda.
    """
    level_up = level.upper()
    return list(filter(lambda rec: rec["level"] == level_up, logs))


def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Повертає словник: рівень -> кількість.
    Забезпечує наявність усіх відомих рівнів (у т.ч. з нулем).
    """
    ctr = Counter(rec["level"] for rec in logs)
    # Гарантуємо ключі для всіх рівнів
    return {lvl: ctr.get(lvl, 0) for lvl in ("INFO", "DEBUG", "ERROR", "WARNING")}


def display_log_counts(counts: Dict[str, int]) -> None:
    """
    Друкує просту таблицю зі статистикою за рівнями.
    """
    # Відповідаємо прикладу: порядок INFO, DEBUG, ERROR, WARNING
    rows = [("Рівень логування", "Кількість"),
            ("-----------------", "----------")]
    for lvl in ("INFO", "DEBUG", "ERROR", "WARNING"):
        rows.append((lvl, str(counts.get(lvl, 0))))

    # Динамічні ширини колонок
    col1 = max(len(r[0]) for r in rows)
    col2 = max(len(r[1]) for r in rows)
    for i, (c1, c2) in enumerate(rows):
        if i == 1:  # розділовий рядок — друкуємо як є
            print(f"{c1:<{col1}} | {c2:<{col2}}")
        else:
            print(f"{c1:<{col1}} | {c2:<{col2}}")
