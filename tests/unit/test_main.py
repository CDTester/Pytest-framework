"""Unit tests for the main module."""
import pytest
from src.main import get_temperature, add, divide
from utils.test_decorators import timer

@timer
def test_get_temperature():
  """Tests the get_temperature function with different temperature values."""
  assert get_temperature(25) == "It's warm outside!"
  assert get_temperature(15) == "It's cold outside!"

@timer
def test_add():
  """Tests the add function with different values."""
  assert add(2, 3) == 5, "Expected add(2, 3) to be 5"
  assert add(-1, 1) == 0, "Expected add(-1, 1) to be 0"
  assert add(0, 0) == 0, "Expected add(0, 0) to be 0"

@timer
@pytest.mark.smoke
def test_divide():
  """Test normal division"""
  assert divide(10, 2) == 5, "Expected divide(10, 2) to be 5"

@timer
def test_divide_error():
  """Test division by zero raises ValueError with correct message"""
  with pytest.raises(ValueError, match="Cannot divide by zero!"):
    divide(10, 0)

@timer
def test_approx():
  """pytest also provides a number of utilities to make writing tests easier. For example, 
  you can use pytest.approx() to compare floating-point values that may have small rounding errors:
  """
  assert (0.1 + 0.2) == pytest.approx(0.3)

@timer
def test_subtests(subtests):
  """Subtests are an alternative to parametrization, 
  particularly useful when the exact parametrization values are not known at collection time.
  """
  test_cases = [(1, 2, 3), (2, 3, 5), (3, 4, 7)]
  for a, b, expected in test_cases:
    with subtests.test(a=a, b=b):
      print(f"Testing subtest: add({a}, {b}) = {expected}")
      assert add(a, b) == expected
