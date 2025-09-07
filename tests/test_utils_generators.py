import itertools
import pytest
from src.utils.generators import fib_generator, window

def test_fib_generator_first_values():
    gen = fib_generator()
    vals = list(itertools.islice(gen, 10))
    assert vals == [0,1,1,2,3,5,8,13,21,34]

def test_window_basic():
    data = [1,2,3,4,5]
    assert list(window(data, 3)) == [(1,2,3),(2,3,4),(3,4,5)]

def test_window_invalid():
    with pytest.raises(ValueError):
        list(window([1,2,3], 0))
