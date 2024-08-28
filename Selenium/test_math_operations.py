# test_math_operations.py

import pytest


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


@pytest.mark.smoke
def test_add():
    assert add(3, 2) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


@pytest.mark.regression
def test_subtract():
    assert subtract(3, 2) == 1
    assert subtract(2, 3) == -1
    assert subtract(0, 0) == 0


@pytest.mark.skip
def test_multiply():
    assert multiply(3, 2) == 6
    assert multiply(0, 5) == 0
    assert multiply(-1, 1) == -1


@pytest.mark.smoke
def test_divide():
    assert divide(6, 2) == 3
    assert divide(5, 2) == 2.5
    with pytest.raises(ValueError):
        divide(1, 0)


if __name__ == "__main__":
    pytest.main()
