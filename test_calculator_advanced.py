# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 13:52:00 2025

@author: saani
"""

# test_calculator_advanced.py
import pytest
from calculator_advanced import Calculator, CalculatorError

calc = Calculator()

def test_add():
    assert calc.add(5, 3) == 8

def test_subtract():
    assert calc.subtract(10, 4) == 6

def test_multiply():
    assert calc.multiply(6, 7) == 42

def test_divide():
    assert calc.divide(20, 5) == 4

def test_divide_by_zero():
    with pytest.raises(CalculatorError):
        calc.divide(10, 0)