"""A simple in-memory database implementation."""

class MemoryDatabase:
  """A simple in-memory database implementation."""
  def __init__(self):
    self.data = {}

  def add_user(self, user_id: int, name: str):
    """Adds a new user to the database. Raises ValueError if the user already exists."""
    if user_id in self.data:
      raise ValueError("User already exists!")
    self.data[user_id] = name

  def get_user(self, user_id: int) -> str | None:
    """Retrieves a user's name by their ID. Returns None if the user is not found."""
    return self.data.get(user_id, None)

  def delete_user(self, user_id: int):
    """Deletes a user from the database. Raises ValueError if the user is not found."""
    if user_id in self.data:
      del self.data[user_id]
    else:
      raise ValueError("User not found!")
