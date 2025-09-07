from __future__ import annotations

import re
from decimal import Decimal, getcontext
from typing import Callable, Generator, Iterable

# Precision for Decimal
getcontext().prec = 28

# Numbers should be clearly separated by spaces on both sides.
# (?<!\S)  — there is no non-whitespace character on the left (i.e. either a space or the beginning of a line)
# (?!\S)   — there is no non-whitespace character on the right (i.e. either a space or the end of a line)
_NUMBER_TOKEN = re.compile(r"(?<!\S)[+-]?\d+(?:\.\d+)?(?!\S)")


def generator_numbers(text: str) -> Generator[Decimal, None, None]:
    """
    Returns a generator of Decimal numbers extracted from text,
    which are separate tokens (separated by spaces on both sides).

    Examples of matches: '100', '-2', '27.45', '+0.99'
    Does not match: '1000,50' (comma instead of dot), '10. ' (no digits after dot),
                    'abc123', '123abc', '1,234.00' (thousand separators)

    Parameters
    ----------
    text : str
        Input string to parse.

    Yields
    ------
    Decimal
        Found number as Decimal (safer for financials than float).
    """
    for m in _NUMBER_TOKEN.finditer(text):
        # Decimal handles financial values ​​more accurately than float
        yield Decimal(m.group(0))


def sum_profit(text: str, func: Callable[[str], Iterable[Decimal]]) -> Decimal:
    """
    Calculates the sum (total profit) using the provided number generator function.

    Parameters
    ----------
    text : str
        Input string with numbers (detailed conditions — see generator_numbers).
    func : Callable[[str], Iterable[Decimal]]
        Function that takes text and returns iterable Decimal values.

    Returns
    -------
    Decimal
        Sum of all numbers from the text.
    """
    total = Decimal("0")
    for value in func(text):
        total += value
    return total


if __name__ == "__main__":
    # Small demonstration
    demo = (
        "An employee's total income consists of several parts: "
        "1000.01 as the main income, supplemented by additional revenues "
        "27.45 and 324.00 dollars."
    )
    print(sum_profit(demo, generator_numbers))  # 1351.46
