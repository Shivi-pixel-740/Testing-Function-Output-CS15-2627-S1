

import pytest

def subtract(a: float, b: float) -> float:
    """Subtract b from a.

    :param a: The number to subtract from.
    :param b: The number to subtract.
    :return: The difference.
    """
    difference = a - b
    return difference


def test_subtract_positive_result():
    assert subtract(10, 4) == 6


def test_subtract_negative_result():
    assert subtract(3, 5) == -2


def square(a: float) -> float:
    """Square a number.

    :param a: The number to square.
    :return: The squared value.
    """
    result = a * a
    return result


def test_square_positive():
    assert square(4) == 16


def test_square_decimal():
    # 1.1 * 1.1 = 1.2100000000000002 due to floating point,
    # so we use approx to check against the expected 1.21.
    assert pytest.approx(1.21) == square(1.1)


def average(a: float, b: float) -> float:
    """Calculate the average of two numbers.

    :param a: First number.
    :param b: Second number.
    :return: The average of a and b.
    """
    result = (a + b) / 2
    return result


def test_average_whole_numbers():
    assert average(4, 6) == 5


def test_average_decimal():
    # 0.1 + 0.2 has floating point imprecision, so I approximate.
    assert pytest.approx(0.15) == average(0.1, 0.2)
