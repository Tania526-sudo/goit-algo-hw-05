from decimal import Decimal
import pytest

from src.task2_income_generator import generator_numbers, sum_profit


def test_example_from_task():
    text = (
        "An employee's total income consists of several parts: "
        "1000.01 as base income, plus additional amounts "
        "27.45 and 324.00 dollars."
    )
    total = sum_profit(text, generator_numbers)
    assert total == Decimal("1351.46")


def test_separation_by_spaces_required():
    # Numbers adjacent to letters should not be matched
    text = "abc123 xyz - in the text  5  are  10.50  and  -2 "
    vals = list(generator_numbers(text))
    # only tokens delimited by spaces
    assert vals == [Decimal("5"), Decimal("10.50"), Decimal("-2")]
    assert sum_profit(text, generator_numbers) == Decimal("13.50")


def test_edge_positions_start_end():
    text = "15 something 20.5 -7"
    vals = list(generator_numbers(text))
    assert vals == [Decimal("15"), Decimal("20.5"), Decimal("-7")]
    assert sum_profit(text, generator_numbers) == Decimal("28.5")


def test_no_numbers():
    assert list(generator_numbers("no numbers")) == []
    assert sum_profit("no numbers", generator_numbers) == Decimal("0")


