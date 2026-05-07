# contents of test_append.py
import pytest

# FIXTURES

@pytest.fixture
def first_entry():
  return "a"

@pytest.fixture
def second_entry():
  return 2

@pytest.fixture
def order():
  return []

@pytest.fixture
def orders(order, second_entry):
  order.append(second_entry)
  return order

@pytest.fixture
def expected_list():
  return ["a", 2, 3.0]

# This fixture will automatically run before each test function due to autouse=True
@pytest.fixture(autouse=True)
def append_first(order, first_entry):
  order.append(first_entry)
  return order

# This fixture can be invoked once by the module and used across all tests in the module due to scope="module"
# other options are function (default), class, packageand session
@pytest.fixture(scope="module")
def module_order():
  return []

# Example of using fixture for setup and teardown with yield
@pytest.fixture
def setup_and_teardown():
  # Setup code before the test runs
  print("\nSetting up resources for the test...")
  yield
  # Teardown code after the test runs
  print("\nCleaning up resources after the test...")

# Example of using params in fixture to run the same test with different data
@pytest.fixture(params=[1, 2, 3, pytest.param(4, marks=pytest.mark.skip(reason="Skipping this param"))])
def param_order(request):
  return request.param



# TESTS
def test_string(orders, expected_list):
  # Act
  orders.append(3.0)
  # Assert
  assert orders == expected_list

def test_string_only(order, first_entry):
  # Assert
  assert order == [first_entry]

def test_string_and_int(order, first_entry):
  order.append(2)
  assert order == [first_entry, 2]

def test_module_order_1(module_order, first_entry):
  # Module used first time houild only contain the first entry
  module_order.append(first_entry)
  print(f"module_order in test_module_order_1: {module_order}")
  assert module_order == [first_entry]
    
def test_module_order_2(module_order, first_entry,second_entry):
  # Module used second time should contain both entries since it's the same instance across the module
  module_order.append(second_entry)
  print(f"module_order in test_module_order_2: {module_order}")
  assert module_order == [first_entry, second_entry]

def test_with_setup_and_teardown(setup_and_teardown):
  # This test will run with setup and teardown logic defined in the fixture
  print("Running test_with_setup_and_teardown")
  assert True

def test_with_params(param_order):
  # test will run three times with param_order values 1, 2 and 3 due to the params in the fixture
  print(f"Running test_with_params with param_order: {param_order}")
  assert param_order in [1, 2, 3]