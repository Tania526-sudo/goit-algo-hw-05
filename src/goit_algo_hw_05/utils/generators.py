from collections import deque
from typing import Deque, Generator, Iterable, Tuple, TypeVar

T = TypeVar("T")

def fib_generator() -> Generator[int, None, None]:
    """
    Infinite Fibonacci number generator: 0, 1, 1, 2, 3, ...
    Space O(1).
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def window(iterable: Iterable[T], size: int) -> Generator[Tuple[T, ...], None, None]:
    """
    Sliding window over iterable source.
    Returns tuples of length `size`.
    """
    if size <= 0:
        raise ValueError("size must be > 0")
    it = iter(iterable)
    buf: Deque[T] = deque(maxlen=size)
    
    for _ in range(size):
        buf.append(next(it))
    yield tuple(buf)
    for x in it:
        buf.append(x)
        yield tuple(buf)
