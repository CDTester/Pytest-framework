"""Documentation for the main module."""

def get_temperature(temp: int) -> str:
  """get_temperature returns a string message based on the input temperature."""
  if temp >= 20:
    return "It's warm outside!"
  return "It's cold outside!"

def add(a: int, b: int) -> int:
  """add returns the sum of two integers."""
  return a + b

def divide(a: int, b: int) -> float:
  """divide returns the quotient of two ints. Raises ValueError if the second int is zero."""
  if b == 0:
    raise ValueError("Cannot divide by zero!")
  return a / b

def is_prime(n: int) -> bool:
  """is_prime returns True if the input integer is a prime number, False otherwise."""
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True
