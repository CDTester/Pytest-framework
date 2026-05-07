import pytest
import src.api.MockApi as MockApi
import src.db.MockDb as MockDb
from pathlib import Path
import os

class MockResponse():
  """Mock response object to mimic requests.Response."""
  status_code = 200

  @staticmethod
  def json():
    """Return the JSON data."""
    return {"mock_key": "mock_response"}


def getssh():
  """Simple function to return expanded homedir ssh path."""
  return Path.home() / ".ssh"

def mockreturn():
  return Path("/abc")

def get_os_user_lower():
  """Simple retrieval function.
  Returns lowercase USER or raises OSError."""
  username = os.getenv("USER")
  print(f"Retrieved USER environment variable: {username}")
  if username is None:
    raise OSError("USER environment is not set.")
  return username.lower()

def mock_get(*args, **kwargs):
  resp = MockResponse()
  resp.status_code = 307
  print(f"Mock GET called with args: {args}, kwargs: {kwargs}")
  print(f"Returning mock response with JSON: {resp.json()}")
  return resp

# TESTS

# Monkey Patching functions
def test_getssh(monkeypatch):
  print(f"Path.cwd(): {Path.cwd()}")
  print(f"Path.home(): {Path.home()}")
  # Application of the monkeypatch to replace Path.home
  monkeypatch.setattr(Path, "home", mockreturn)
  print(f"After monkeypatch Path.home() returns: {Path.home()}")

  # Calling getssh() will use mockreturn in place of Path.home
  # for this test with the monkeypatch.
  x = getssh()
  print(f"getssh() returns: {x}")
  assert x == Path("/abc/.ssh")


# Monkey Patching returned objects from API calls
def test_get_json(monkeypatch):
  """Test the get_json function with a mocked response."""
  # Mock the requests.get method to return a MockResponse object
  monkeypatch.setattr(MockApi.requests, "get", mock_get)
  
  # Call the get_json function, which will use the mocked requests.get
  result = MockApi.get_json("http://fakeurl.com/api/data")
  
  # Assert that the result is as expected from the MockResponse
  print(f"Result from get_json: {result}")
  assert result["mock_key"] == "mock_response"

# Monkey Patching environment variables
def test_upper_to_lower(monkeypatch):
  """Set the USER env var to assert the behavior."""
  print(f"Original USER environment variable: {os.getenv('USER')}")
  monkeypatch.setenv("USER", "TestingUser")
  print(f"After monkeypatch USER environment variable: {os.getenv('USER')}")
  assert get_os_user_lower() == "testinguser"

# Monkey Patching environment variables
def test_raise_exception(monkeypatch):
  """Remove the USER env var and assert OSError is raised."""
  print(f"Original USER environment variable: {os.getenv('USER')}")
  monkeypatch.delenv("USER", raising=False)
  print(f"After delenv USER environment variable: {os.getenv('USER')}")
  
  with pytest.raises(OSError):
    _ = get_os_user_lower()

# Monkey Patching dictionary values
def test_connection(monkeypatch):
  # Patch the values of DEFAULT_CONFIG to specific
  # testing values only for this test.
  print(f"Original MockDb.DEFAULT_CONFIG: {MockDb.DEFAULT_CONFIG}")
  monkeypatch.setitem(MockDb.DEFAULT_CONFIG, "user", "test_user")
  monkeypatch.setitem(MockDb.DEFAULT_CONFIG, "database", "test_db")

  # expected result based on the mocks
  expected = "User Id=test_user; Location=test_db;"

  # the test uses the monkeypatched dictionary settings
  result = MockDb.create_connection_string()
  assert result == expected

def test_missing_user(monkeypatch):
  # patch the DEFAULT_CONFIG to be missing the 'user' key
  print(f"Original MockDb.DEFAULT_CONFIG: {MockDb.DEFAULT_CONFIG}")
  monkeypatch.delitem(MockDb.DEFAULT_CONFIG, "user", raising=False)
  print(f"After delitem MockDb.DEFAULT_CONFIG: {MockDb.DEFAULT_CONFIG}")

  # Key error expected because a config is not passed, and the
  # default is now missing the 'user' entry.
  with pytest.raises(KeyError):
    _ = MockDb.create_connection_string()