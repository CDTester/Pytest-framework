from main import get_temperature, add, divide
import pytest

def test_get_temperature():
    assert get_temperature(25) == "It's warm outside!"
    assert get_temperature(15) == "It's cold outside!"

def test_add():
    assert add(2, 3) == 5, "Expected add(2, 3) to be 5"
    assert add(-1, 1) == 0, "Expected add(-1, 1) to be 0"
    assert add(0, 0) == 0, "Expected add(0, 0) to be 0"

@pytest.mark.smoke
def test_divide():
    """Test normal division"""
    assert divide(10, 2) == 5, "Expected divide(10, 2) to be 5"
    
    """Test division by zero raises ValueError with correct message"""
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(10, 0)


def test_approx():
    """pytest also provides a number of utilities to make writing tests easier. For example, 
    you can use pytest.approx() to compare floating-point values that may have small rounding errors:"""
    assert (0.1 + 0.2) == pytest.approx(0.3)