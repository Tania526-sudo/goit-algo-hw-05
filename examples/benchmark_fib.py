import argparse
import time
from functools import lru_cache
from src.task1_fibonacci_closure import caching_fibonacci

def fib_naive(n: int) -> int:
    if n < 2:
        return n
    return fib_naive(n-1) + fib_naive(n-2)

@lru_cache(maxsize=None)
def fib_lru(n: int) -> int:
    if n < 2:
        return n
    return fib_lru(n-1) + fib_lru(n-2)

def time_call(fn, *args):
    t0 = time.perf_counter()
    val = fn(*args)
    dt = time.perf_counter() - t0
    return val, dt

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=35)
    args = ap.parse_args()

    n = args.n
    fib = caching_fibonacci()

    val1, t1 = time_call(fib_naive, n)
    val2, t2 = time_call(fib, n)
    val3, t3 = time_call(fib_lru, n)

    print(f"n={n}")
    print(f"naive: {val1} in {t1:.6f}s")
    print(f"closure+cache: {val2} in {t2:.6f}s")
    print(f"functools.lru_cache: {val3} in {t3:.6f}s")

if __name__ == "__main__":
    main()
