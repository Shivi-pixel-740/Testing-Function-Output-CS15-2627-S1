import pytest

def area_rectangle(width: float, length: float):

    """Calculate the area of a rectangle.

    :param length: The length of the rectangle.
    :param width: The width of the rectangle.
    :return: the area of the rectangle."""

    area = width * length
    return area

def test_area_rectangle():
    assert area_rectangle(5, 3) == 15

def test_area_rectangle_2():
    assert area_rectangle(4, 3) == 12

def add_tax(price: float, tax: float):
    """Add tax to the price,
    :param price: The original grocery price
    :param tax: The new grocery tax"""
    tax = price*tax
    total = price + tax
    return total
def test_add_tax():
    assert add_tax(50,0.05) ==52.5
def test_add_tax_decimal():
    assert add_tax(25.50,0.05) == pytest.approx(26.775)

def celsius_to_fahrenheit(celsius:float):
    """Convert Celsius to Fahrenheit.
    :param celsius: The temperature to Celsius
    :return: the temperature in Fahrenheit"""

    fahrenheit = (celsius* 9/5) + 32
    return fahrenheit
def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
def test_celsius_to_fahrenheit_2():
    assert celsius_to_fahrenheit(20) == 68