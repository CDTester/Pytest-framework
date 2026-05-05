"""Unit tests for the get_weather function in mockWeather.py using mocking."""
# import pytest
from mockWeather import get_weather

def test_get_weather(mocker):
  """Tests the get_weather function with a mocked API response."""
  # Mock the requests.get method to return a fake response
  mock_get = mocker.patch('mockWeather.requests.get')

  # set return values for the mock
  mock_get.return_value.status_code = 200
  mock_get.return_value.json.return_value = {"temperature": 25, "condition": "Sunny"}

  # Call the function and check the result
  result = get_weather("Dubai")
  assert result == {"temperature": 25, "condition": "Sunny"}, (
    "Expected get_weather to return the mocked response"
  )

  # Verify that the mock was called with the correct URL
  mock_get.assert_called_once_with("https://api.weather.com/v1/Dubai")
