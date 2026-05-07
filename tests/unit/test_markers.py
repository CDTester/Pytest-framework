import pytest

@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
def test_eval(test_input, expected):
  print(f"Testing: {test_input} == {expected}")
  assert eval(test_input) == expected

@pytest.mark.xfail(reason="This test is expected to fail because the expected value is incorrect.")
def test_xfail():
  print("Testing: This is an expected failure.")
  assert False, "This test should fail but is marked as xfail."


@pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])
class TestClass:
  def test_simple_case(self, n, expected):
    print(f"Testing: {n} + 1 == {expected}")
    assert n + 1 == expected

  def test_weird_simple_case(self, n, expected):
    print(f"Testing: ({n} * 1) + 1 == {expected}")
    assert (n * 1) + 1 == expected
