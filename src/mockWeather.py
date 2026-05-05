"""Documentation for the mockWeather module."""
import requests

def get_weather(city: str):
  """get_weather fetches weather data for a given city from a hypothetical API."""
  response = requests.get(f"https://api.weather.com/v1/{city}", timeout=5)
  if response.status_code == 200:
    return response.json()
  raise ValueError("Could not fetch weather data!")
