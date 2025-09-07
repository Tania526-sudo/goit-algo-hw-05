from decimal import Decimal
import pytest

from src.task2_income_generator import generator_numbers, sum_profit


def test_example_from_task():
    text = (
        "Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів."
    )
    total = sum_profit(text, generator_numbers)
    assert total == Decimal("1351.46")


def test_separation_by_spaces_required():
    # Числа поряд з літерами не повинні матчитися
    text = "abc123 xyz - у тексті  5  є  10.50  і  -2 "
    vals = list(generator_numbers(text))
    # тільки токени, відокремлені пробілами
    assert vals == [Decimal("5"), Decimal("10.50"), Decimal("-2")]
    assert sum_profit(text, generator_numbers) == Decimal("13.50")


def test_edge_positions_start_end():
    text = "15 дещо 20.5 -7"
    vals = list(generator_numbers(text))
    assert vals == [Decimal("15"), Decimal("20.5"), Decimal("-7")]
    assert sum_profit(text, generator_numbers) == Decimal("28.5")


def test_no_numbers():
    assert list(generator_numbers("без чисел")) == []
    assert sum_profit("без чисел", generator_numbers) == Decimal("0")

