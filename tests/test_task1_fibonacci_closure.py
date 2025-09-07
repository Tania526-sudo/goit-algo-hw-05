import pytest
from src.task1_fibonacci_closure import caching_fibonacci

def test_base_cases():
    fib = caching_fibonacci()
    assert fib(0) == 0
    assert fib(1) == 1

def test_known_values():
    fib = caching_fibonacci()
    assert fib(10) == 55
    assert fib(15) == 610
    assert fib(20) == 6765

def test_validation():
    fib = caching_fibonacci()
    with pytest.raises(ValueError):
        fib(-1)
    with pytest.raises(TypeError):
        fib(3.14)  # type: ignore
