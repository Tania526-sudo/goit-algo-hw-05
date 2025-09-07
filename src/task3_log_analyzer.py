from __future__ import annotations

import sys
from collections import Counter
from typing import Dict, List

# Supported log levels (upper case)
VALID_LEVELS = {"INFO", "ERROR", "DEBUG", "WARNING"}


def parse_log_line(line: str) -> Dict[str, str]:
    """
    Parses a single log line in the format:
      YYYY-MM-DD HH:MM:SS LEVEL Message...

    Returns a dict:
      {"date": str, "time": str, "level": str, "message": str}

    Raises ValueError if the format is invalid or the level is unknown.
    """
    raw = line.strip()
    if not raw:
        raise ValueError("Empty line")

    parts = raw.split(maxsplit=3)  # expect 4 tokens
    if len(parts) < 4:
        raise ValueError("Invalid log format (expected 4 tokens)")

    date, time, level, message = parts
    level = level.upper()
    if level not in VALID_LEVELS:
        raise ValueError(f"Unknown log level: {level}")

    return {"date": date, "time": time, "level": level, "message": message}


def load_logs(file_path: str) -> List[Dict[str, str]]:
    """
    Reads the file and returns a list of log-record dicts.
    Skips malformed lines and prints warnings to stderr.
    """
    logs: List[Dict[str, str]] = []
    with open(file_path, "r", encoding="utf-8") as fh:
        for lineno, line in enumerate(fh, start=1):
            try:
                rec = parse_log_line(line)
            except ValueError as e:
                print(f"[WARN] Line {lineno} skipped: {e}", file=sys.stderr)
                continue
            logs.append(rec)
    return logs


def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    """
    Returns only records of the given level (case-insensitive).
    Uses a functional programming element: filter + lambda.
    """
    level_up = level.upper()
    return list(filter(lambda rec: rec["level"] == level_up, logs))


def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Returns a dict: level -> count.
    Ensures presence of all known levels (including zeros).
    """
    ctr = Counter(rec["level"] for rec in logs)
    # Ensure keys for all levels
    return {lvl: ctr.get(lvl, 0) for lvl in ("INFO", "DEBUG", "ERROR", "WARNING")}


def display_log_counts(counts: Dict[str, int]) -> None:
    """
    Prints a simple table with per-level statistics.
    """
    # Match the example order: INFO, DEBUG, ERROR, WARNING
    rows = [("Log Level", "Count"), ("----------------", "-----")]
    for lvl in ("INFO", "DEBUG", "ERROR", "WARNING"):
        rows.append((lvl, str(counts.get(lvl, 0))))

    # Dynamic column widths
    col1 = max(len(r[0]) for r in rows)
    col2 = max(len(r[1]) for r in rows)
    for i, (c1, c2) in enumerate(rows):
        if i == 1:  # separator row — print as is
            print(f"{c1:<{col1}} | {c2:<{col2}}")
        else:
            print(f"{c1:<{col1}} | {c2:<{col2}}")

