from src.task3_log_analyzer import (
    parse_log_line,
    load_logs,
    filter_logs_by_level,
    count_logs_by_level,
)
from pathlib import Path

def test_parse_log_line_ok():
    line = "2024-01-22 09:00:45 ERROR Database connection failed."
    rec = parse_log_line(line)
    assert rec["date"] == "2024-01-22"
    assert rec["time"] == "09:00:45"
    assert rec["level"] == "ERROR"
    assert rec["message"].startswith("Database connection failed")

def test_count_and_filter(tmp_path: Path):
    p = tmp_path / "log.log"
    p.write_text(
        "2024-01-22 08:30:01 INFO Ok\n"
        "2024-01-22 08:45:23 DEBUG Debug1\n"
        "2024-01-22 09:00:45 ERROR Err\n"
        "2024-01-22 09:15:10 INFO Ok2\n"
        "2024-01-22 10:30:55 WARNING Warn\n",
        encoding="utf-8",
    )
    logs = load_logs(str(p))
    counts = count_logs_by_level(logs)
    assert counts == {"INFO": 2, "DEBUG": 1, "ERROR": 1, "WARNING": 1}

    errs = filter_logs_by_level(logs, "error")
    assert len(errs) == 1
    assert errs[0]["message"] == "Err"

