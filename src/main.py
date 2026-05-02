def get_temperature(temp: int) -> str:
  if temp >= 20:
      return "It's warm outside!"
  else:
      return "It's cold outside!"
  
def add(a: int, b: int) -> int:
  return a + b

def divide(a: int, b: int) -> float:
  if b == 0:
      raise ValueError("Cannot divide by zero!")
  return a / b

def is_prime(n: int) -> bool:
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True