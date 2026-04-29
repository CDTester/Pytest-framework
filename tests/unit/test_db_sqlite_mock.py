from db.sqlite import add_user

# mock a connection to the SQLite database for testing
def test_add_user(mocker):
  """Tests adding a user to the SQLite database."""
  mock_connection = mocker.patch('sqlite3.connect')
  mock_cursor = mock_connection.return_value.cursor.return_value

  add_user("John Doe", 30)
  # Verify that the correct SQL query was executed
  mock_connection.assert_called_once_with('users.db')
  mock_cursor.execute.assert_called_once_with('INSERT INTO users (name, age) VALUES (?, ?)', ("John Doe", 30))
