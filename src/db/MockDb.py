DEFAULT_CONFIG = {"user": "user1", "database": "db1"}

def create_connection_string(config=None):
  """Creates a connection string from input or defaults."""
  config = config or DEFAULT_CONFIG
  print(f"Creating connection string with config: {config}")
  return f"User Id={config['user']}; Location={config['database']};"