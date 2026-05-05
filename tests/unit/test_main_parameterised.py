"""Parameterised Unit tests for the is_prime function in main.py."""
import pytest
from src.main import is_prime

# pytest.mark.paramaterize uses a list of tuples to specify multiple sets of
# input and expected output for the test function.
@pytest.mark.parametrize("n, expected", [
  (1, False),  # 1 is not prime
  (2, True),   # 2 is prime
  (3, True),   # 3 is prime
  (4, False),  # 4 is not prime
  (5, True),   # 5 is prime
  (17, True),  # 17 is prime
  (18, False), # 18 is not prime
  (19, True),  # 19 is prime
  (25, False), # 25 is not prime
])

def test_is_prime(n, expected):
  """Tests the is_prime function with multiple inputs."""
  assert is_prime(n) == expected, f"Expected is_prime({n}) to be {expected}"
