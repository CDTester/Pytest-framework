import pytest
from MemoryDatabase import MemoryDatabase

"""
Instead of returning s new instance, we use yield to provide the fixture value to the test
and then perform cleanup after the test runs. This is useful for more complex fixtures that 
require setup and teardown logic, such as database connections or file handling. 
In this case, we clear the data after each test, although it's not strictly necessary since 
we're creating a new instance for each test.
"""
@pytest.fixture
def db():
  """Creates a fresh instance of MemoryDatabase for each test and cleans up after the test."""
  db = MemoryDatabase()
  yield db # Provide the fixture value to the test
  db.data.clear() # Clean up after the test, not needed here since it's a fresh instance, but good practice for real db

def test_add_user(db):
  """Tests adding a new user."""
  print("test_add_user passed")
  db.add_user(1, "Alice")
  assert db.get_user(1) == "Alice"
  print("test_add_user passed")

def test_add_existing_user(db):
  """Tests adding a user that already exists."""
  db.add_user(1, "Alice")
  with pytest.raises(ValueError):
    db.add_user(1, "Bob")
    print("test_add_existing_user passed")

def test_delete_user(db):
  """Tests deleting a user."""
  db.add_user(2, "Bob")
  db.delete_user(2)
  assert db.get_user(2) is None
  print("test_delete_user passed")