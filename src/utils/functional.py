from typing import Callable, Iterable, List, TypeVar

T = TypeVar("T")
U = TypeVar("U")

def apply_list(data: Iterable[T], fn: Callable[[T], U]) -> List[U]:
    """
    Demonstrates passing a function as an argument.
    Returns a list of results fn(x) for each x.
    """
    return [fn(x) for x in data]
