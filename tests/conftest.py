import time, pytest
from unittest import result

# timer fixture
@pytest.fixture(scope="session", autouse=True)
def session_timer():
  print("\nStarting session timer fixture...")
  start_time = time.time()
  yield
  end_time = time.time()
  print(f"\nExecution time for session using fixture: {end_time - start_time:.4f} seconds")
