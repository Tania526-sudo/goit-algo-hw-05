from __future__ import annotations

import re
from decimal import Decimal, getcontext
from typing import Callable, Generator, Iterable

# Точність для Decimal (достатньо для фінансових обчислень у межах ДЗ)
getcontext().prec = 28

# Числа мають бути чітко відокремлені пробілами з обох боків.
# (?<!\S)  — зліва немає не-пробільного символу (тобто або пробіл, або початок рядка)
# (?!\S)   — справа немає не-пробільного символу (тобто або пробіл, або кінець рядка)
_NUMBER_TOKEN = re.compile(r"(?<!\S)[+-]?\d+(?:\.\d+)?(?!\S)")


def generator_numbers(text: str) -> Generator[Decimal, None, None]:
    """
    Повертає генератор Decimal-чисел, виділених із тексту,
    які є окремими токенами (відокремлені пробілами з обох боків).

    Приклади матчів: '100', '-2', '27.45', '+0.99'
    Не матчить: '1000,50' (кома замість крапки), '10. ' (без цифр після крапки),
                'abc123', '123abc', '1,234.00' (роздільники тисяч)

    Parameters
    ----------
    text : str
        Вхідний рядок для аналізу.

    Yields
    ------
    Decimal
        Знайдене число у вигляді Decimal (безпечніше для фінансів, ніж float).
    """
    for m in _NUMBER_TOKEN.finditer(text):
        # Decimal точніше обробляє фінансові значення, ніж float
        yield Decimal(m.group(0))


def sum_profit(text: str, func: Callable[[str], Iterable[Decimal]]) -> Decimal:
    """
    Обчислює суму (загальний прибуток), використовуючи передану функцію-генератор чисел.

    Parameters
    ----------
    text : str
        Вхідний рядок з числами (докладні умови — див. generator_numbers).
    func : Callable[[str], Iterable[Decimal]]
        Функція, яка приймає текст і повертає ітерабельні Decimal-значення.

    Returns
    -------
    Decimal
        Сума всіх чисел з тексту.
    """
    total = Decimal("0")
    for value in func(text):
        total += value
    return total


if __name__ == "__main__":
    # Невелика демонстрація
    demo = (
        "Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів."
    )
    print(sum_profit(demo, generator_numbers))  # 1351.46
