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
        description="Log file analyzer: per-level statistics and filtering."
    )
    parser.add_argument("file_path", help="Path to the log file")
    parser.add_argument(
        "level",
        nargs="?",
        help="(optional) Log level to show details for: info|debug|error|warning",
    )
    args = parser.parse_args(argv)

    try:
        logs = load_logs(args.file_path)
    except FileNotFoundError:
        print(f"Error: file '{args.file_path}' not found.", file=sys.stderr)
        return 1
    except OSError as e:
        print(f"File read error: {e}", file=sys.stderr)
        return 1

    # Show aggregated statistics
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    # If a level was provided — show details
    if args.level:
        level = args.level.upper()
        if level not in VALID_LEVELS:
            print(
                f"\nWarning: unknown level '{args.level}'. "
                f"Available: {', '.join(sorted(VALID_LEVELS))}.",
                file=sys.stderr,
            )
            return 2

        filtered = filter_logs_by_level(logs, level)
        print(f"\nDetails for level '{level}':")
        if not filtered:
            print("(no records found)")
        else:
            for item in filtered:
                # Format like: YYYY-MM-DD HH:MM:SS - message
                print(f"{item['date']} {item['time']} - {item['message']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

