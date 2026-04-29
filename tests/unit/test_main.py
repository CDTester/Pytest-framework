from main import get_temperature, add, divide
import pytest

def test_get_temperature():
    assert get_temperature(25) == "It's warm outside!"
    assert get_temperature(15) == "It's cold outside!"

def test_add():
    assert add(2, 3) == 5, "Expected add(2, 3) to be 5"
    assert add(-1, 1) == 0, "Expected add(-1, 1) to be 0"
    assert add(0, 0) == 0, "Expected add(0, 0) to be 0"

def test_divide():
    assert divide(10, 2) == 5, "Expected divide(10, 2) to be 5"
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(10, 0)
