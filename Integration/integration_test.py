g# import addition
# import multiplication
#
# def test_integration():
#     # Test multiplying the result of adding two numbers with another number
#     assert multiplication.multiply(addition.add(2, 3), 4) == 20

import calculator
import input_handler
import requests

def test_addition():
    assert calculator.add(2, 3) == 5

def test_subtraction():
    assert calculator.subtract(5, 3) == 2

def test_multiplication():
    assert calculator.multiply(2, 3) == 6

def test_division():
    assert calculator.divide(6, 3) == 2

def test_divide_by_zero():
    try:
        calculator.divide(6, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"
    else:
        assert False, "Expected ValueError"



