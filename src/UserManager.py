"""UserManager is a simple class to manage user data in memory."""
class UserManager:
  """UserManager provides methods to add and retrieve users from an in-memory database."""
  def __init__(self):
    self.users = {}

  def add_user(self, username: str, email: str) -> bool:
    """Adds a new user to the database. Raises ValueError if the user already exists."""
    if username in self.users:
      raise ValueError("Username already exists!")
    self.users[username] = email
    return True

  def get_user(self, username: str) -> str | None:
    """Retrieves the email of a user by their username. Returns None if the user does not exist."""
    return self.users.get(username)
