import argparse
import sys
from src.task3_log_analyzer import (
    load_logs,
    count_logs_by_level,
    filter_logs_by_level,
    display_log_counts,
    VALID_LEVELS,
)

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Аналізатор лог-файлів: статистика за рівнями та фільтрація."
    )
    parser.add_argument("file_path", help="Шлях до лог-файлу")
    parser.add_argument(
        "level",
        nargs="?",
        help="(опційно) Рівень логування для виводу деталей: info|debug|error|warning",
    )
    args = parser.parse_args(argv)

    try:
        logs = load_logs(args.file_path)
    except FileNotFoundError:
        print(f"Помилка: файл '{args.file_path}' не знайдено.", file=sys.stderr)
        return 1
    except OSError as e:
        print(f"Помилка читання файлу: {e}", file=sys.stderr)
        return 1

    # Показати агреговану статистику
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    # Якщо вказано рівень — показати деталі
    if args.level:
        level = args.level.upper()
        if level not in VALID_LEVELS:
            print(
                f"\nПопередження: невідомий рівень '{args.level}'. "
                f"Доступні: {', '.join(sorted(VALID_LEVELS))}.",
                file=sys.stderr,
            )
            return 2

        filtered = filter_logs_by_level(logs, level)
        print(f"\nДеталі логів для рівня '{level}':")
        if not filtered:
            print("(записів не знайдено)")
        else:
            for item in filtered:
                # Формат за прикладом: YYYY-MM-DD HH:MM:SS - message
                print(f"{item['date']} {item['time']} - {item['message']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
