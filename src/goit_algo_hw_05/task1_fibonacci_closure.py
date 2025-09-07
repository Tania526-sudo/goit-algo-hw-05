from typing import Callable, Dict
import sys

def caching_fibonacci() -> Callable[[int], int]:
    """
    Returns a function fibonacci(n) that computes the nth Fibonacci number with caching.
    The cache is stored in a closure (lexical environment) and persists between calls.

    Validation:
      - n must be a non-negative integer.

    Complexity:
      - Time: O(n) due to memoization.
      - Space: O(n) for the cache.
    """
    cache: Dict[int, int] = {0: 0, 1: 1}

    def fibonacci(n: int) -> int:
        if not isinstance(n, int):
            raise TypeError("n must be an int")
        if n < 0:
            raise ValueError("n must be >= 0")
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


def _main(argv: list[str]) -> None:
    """Simple launch via `python -m src.task1_fibonacci_closure 10 15`."""
    fib = caching_fibonacci()
    for arg in argv:
        n = int(arg)
        print(fib(n))


if __name__ == "__main__":
    _main(sys.argv[1:])
