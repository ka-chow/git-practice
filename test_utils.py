import pytest
from utils import add, sub, div, pow, mod, floor_div, mul

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(5, 3) == 2

def test_div():
    assert div(10, 2) == 5

def test_div_by_zero():
    with pytest.raises(ValueError):
        div(10, 0)

def test_pow():
    assert pow(2, 3) == 8

def test_mod():
    assert mod(10, 3) == 1

def test_floor_div():
    assert floor_div(10, 3) == 3

def test_mul():
    assert mul(3, 4) == 12