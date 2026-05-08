# Pytest-framework
Python, Pytest, db


## Install 
Install PyTest and PyTest-Mock.
Install Requests for API requests

Install the project from `pyproject.toml`
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
pytest -v   # verbose, displays test names
pytest -vv  # more verbose
pytest -vvv # very verbose
```

### Debugging Tests
By default, pytest supresses stdout and stderr messages to keep the output clean. If you want to debug tests with print() statements then the tests will need to be run using:
```bash
pytest -s
```
or
```bash
pytest -rA
```
will report all tests with their print statements, this shows you what test produced the print statement.

other options are:
- -rf, failed
- -rE, error
- -rs, skipped
- -rx, xfailed
- -rX, xpassed
- -rp, passed
- -rP, passed with output
- -ra, all except passed
- -rA, all

Tests can be executed in a manner that allows you to fix them during the test execution using stepwise:
```bash
pytest --sw
```
The test suite will run until the first failure and then stop. At the next invocation, tests will continue from the last failing test and then run until the next failing test. 

Alternatively, you can use the python debugger:
```bash
pytest --pdb
```

### Re-Running tests
Tests that failed in the last run can be re-run using the following options:

```bash
pytest --lf # Re-runs the last failed tests
```


or
```bash
pytest --ff ## Re-runs the failures first, then runs the rest of the tests that previously passed
```

or 
```bash
pytest --nf # Runs new/updated tests first, then all the other tests. Organised by modified time.
```

The failed tests can be found in the cache using the following option:
```bash
pytest --cache-show
```

This cache can be cleared (recommended for CI servers) using:
```bash
pytest --cache-clear
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

## Reports

### JUnit
Pytest can create junit style test reports using:
```bash
pytest --junit-xml=/test_reports/junit.xml
```
This will create a file named `junit.xml` in the test_results folder. 

The test suite name can be set in the `pytest.ini` file.
```ini
junit_suite_name = my_test_suite
```


## PyTest-BDD
pytest-bdd implements a subset of the Gherkin language to enable automating project requirements testing and to facilitate behavioral driven development.

Unlike many other BDD tools, it does not require a separate runner and benefits from the power and flexibility of pytest. It enables unifying unit and functional tests, reduces the burden of continuous integration server configuration and allows the reuse of test setups.

Pytest fixtures written for unit tests can be reused for setup and actions mentioned in feature steps with dependency injection. This allows a true BDD just-enough specification of the requirements without maintaining any context object containing the side effects of Gherkin imperative declarations.

