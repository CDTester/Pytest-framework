# Pytest-framework
Python, Pytest, db


## Install 
Install PyTest and PyTest-Mock.
Install Requests for API requests

```bash
pip install pytest
pip install pytest-mock
pip install requests
```

Then install the project from `pyproject.toml`
```bash
pip install -e .
```


## Running tests
Running the following will run all files with the naming convention `test_*.py` or `*_test.py`

```bash
pytest
```

The following with run in quiet mode:
```bash
pytest -q
```

Specific tests can be run:
```bash
pytest tests/unit/test_main.py
```

Or you can run tests by keyword expressions:
```bash
pytest -k "mock and not weather"
```
This will run [test_db_sqlite_mock.py](./tests/unit/test_db_sqlite_mock.py) but not [test_mockWeather.py](./tests/unit/test_mockWeather.py).

> [!NOTE]
> Keywords require "double quotes" on Windows, 'single quotes' on Linux.


Tests can be given custom marks, similar to tags. The markers are added to the test as a decoration:
```py
@pytest.mark.smoke
def test_divide():
```


Custom marks should be set up in the pytet.ini configuration file :
```ini
[pytest]
markers = 
  smoke: marks tests as smoke (deselect with -m "not smoke")
  slow
```

This will stop any warning messages when running
```bash
pytest -m smoke
```

Vebose test results output can be set by using:
```bash
pytest -v
```

## Debugging Tests
By default, pytest supresses stdout and stderr messages to keep the output clean. If you want to debug tests with print() statements then the tests will need to be run using:
```bash
pytest -s
```


## Fixtures
Fixtures gives the ability to define a generic setup step that can be reused over and over, just like a normal function would be used. Two different tests can request the same fixture and have pytest give each test their own result from that fixture.

### Fixture scopes
Fixtures are created when first requested by a test, and are destroyed based on their scope:
- function: the default scope, the fixture is destroyed at the end of the test.
- class: the fixture is destroyed during teardown of the last test in the class.
- module: the fixture is destroyed during teardown of the last test in the module.
- package: the fixture is destroyed during teardown of the last test in the package where the fixture is defined, including sub-packages and sub-directories within it.
- session: the fixture is destroyed at the end of the test session.

### Fixture Params
Fixture functions can be parametrized in which case they will be called multiple times, each time executing the set of dependent tests, i.e. the tests that depend on this fixture. 


### Fixtures that can be used across multiple test files
The `conftest.py` is a special pytest file that acts as a local plugin for your test suite. pytest automatically discovers and loads it before running tests — you never import it manually. Without conftest.py, fixtures defined in one test file can't be used in another. Putting them in conftest.py makes them available to all tests in the same directory 

Find out what kind of builtin pytest fixtures exist with the command:
```bash
pytest --fixtures
```

## Test Markers
By using the `pytest.mark` helper you can easily set metadata on your test functions.

Here are some of the builtin markers:
- usefixtures - use fixtures on a test function or class
- filterwarnings - filter certain warnings of a test function
- skip - always skip a test function
- skipif - skip a test function if a certain condition is met
- xfail - produce an “expected failure” outcome if a certain condition is met
- parametrize - perform multiple calls to the same test function.

Custom marks should be set up in the pytet.ini configuration file :
```ini
[pytest]
markers = 
  smoke: marks tests as smoke (deselect with -m "not smoke")
  slow
```

This will stop any warning messages when running
```bash
pytest -m smoke
```

