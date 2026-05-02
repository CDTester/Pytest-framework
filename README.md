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
This will run [test_db_sqlite_mock.py](tests\unit\test_db_sqlite_mock.py) but not [test_mockWeather.py](tests\unit\test_mockWeather.py).

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


## Debugging Tests
By default, pytest supresses stdout and stderr messages to keep the output clean. If you want to debug tests with print() statements then the tests will need to be run using:
```bash
pytest -s
```


## Fixtures
Find out what kind of builtin pytest fixtures exist with the command:
```bash
pytest --fixtures
```


