import app
import pytest

def test_add():
    assert app.add(2, 3) == 5

def test_subtract():
    assert app.subtract(10, 4) == 6

def test_multiply():
    assert app.multiply(3, 3) == 9

def test_divide():
    assert app.divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        app.divide(5, 0)
