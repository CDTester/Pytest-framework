"""Unit tests for the MemoryDatabase class."""
import pytest
from src.MemoryDatabase import MemoryDatabase


# Instead of returning s new instance, we use yield to provide the fixture value to the test
# and then perform cleanup after the test runs. This is useful for more complex fixtures that
# require setup and teardown logic, such as database connections or file handling.
# In this case, we clear the data after each test, although it's not strictly necessary since
# we're creating a new instance for each test.
@pytest.fixture
def db():
  """Creates a fresh instance of MemoryDatabase for each test and cleans up after the test."""
  database = MemoryDatabase()
  yield database # Provide the fixture value to the test
  database.data.clear() # Clean up after test, not needed as a new instance but good practice for real db

def test_add_user(db):
  """Tests adding a new user."""
  db.add_user(1, "Alice")
  assert db.get_user(1) == "Alice", (
    "Expected get_user(1) to return 'Alice' after adding the user"
  )
  print("\ntest_add_user passed")

def test_add_existing_user(db):
  """Tests adding a user that already exists."""
  db.add_user(1, "Alice")
  with pytest.raises(ValueError, match="User already exists!") as excinfo:
    db.add_user(1, "Bob")
    assert str(excinfo.value) == "User already exists!", (
      "Expected exception message to be 'User already exists!'"
    )
  assert "User already exists!" in str(excinfo.value) # or you can test error message this way
  print("\ntest_add_existing_user passed")

def test_delete_user(db):
  """Tests deleting a user."""
  db.add_user(2, "Bob")
  db.delete_user(2)
  assert db.get_user(2) is None, "Expected get_user(2) to return None after deletion"
  print("\ntest_delete_user passed")
