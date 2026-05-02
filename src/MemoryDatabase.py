class MemoryDatabase:
  """A simple in-memory database implementation."""
  def __init__(self):
    self.data = {}

  def add_user(self, user_id: int, name: str):
    if user_id in self.data:
      raise ValueError("User already exists!")
    self.data[user_id] = name

  def get_user(self, user_id: int) -> str | None:
    return self.data.get(user_id, None)
  
  def delete_user(self, user_id: int):
    if user_id in self.data:
      del self.data[user_id]
    else:
      raise ValueError("User not found!")