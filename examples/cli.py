import argparse
import itertools
from src.task1_fibonacci_closure import caching_fibonacci
from src.utils.generators import fib_generator

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--n", type=int, help="Calculate F(n)")
    p.add_argument("--list", dest="list_n", type=int, help="Display the first N Fibonacci numbers")
    args = p.parse_args()

    if args.n is not None:
        fib = caching_fibonacci()
        print(fib(args.n))

    if args.list_n is not None:
        gen = fib_generator()
        print(list(itertools.islice(gen, args.list_n)))

if __name__ == "__main__":
    main()
