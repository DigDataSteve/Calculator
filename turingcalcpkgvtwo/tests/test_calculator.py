import pytest
from src.turingcalcpkgvtwo.calculator import Calculator

# python -m pytest test/test_calculator.py

def test_add():
  calc = Calculator()
  assert calc.add(2) == 2
  assert calc.add(3.1) == 5.1
  assert calc.add(-1) == 4.1

def test_subtract():
  calc = Calculator()
  assert calc.subtract(-3) == -3
  assert calc.subtract(-7.1) == -10.1
  assert calc.subtract(5) == -5.1

def test_multiply():
  calc = Calculator()
  assert calc.multiply(3) == 0
  assert calc.multiply(4) == 0
  assert calc.add(5) == 5
  assert calc.multiply(5) == 25

def test_divide():
  calc = Calculator()
  assert calc.divide(3) == 0
  assert calc.divide(4) == 0
  assert calc.add(15) == 5
  assert calc.divide(5) == 3