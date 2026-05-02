import pytest
from UserManager import UserManager

# fixture to create a fresh UserManager instance for each test
@pytest.fixture
def user_manager() -> UserManager:
  """Creates a fresh instance of UserManager for each test."""
  return UserManager()

def test_add_user(user_manager: UserManager):
  """Tests adding a new user."""
  assert user_manager.add_user("alice", "alice@example.com") == True
  assert user_manager.get_user("alice") == "alice@example.com"

def test_add_existing_user(user_manager: UserManager):
  """Tests adding a user that already exists."""
  user_manager.add_user("alice", "alice@example.com")
  with pytest.raises(ValueError):
    user_manager.add_user("alice", "alice2@example.com")