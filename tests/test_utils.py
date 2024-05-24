# tests/test_utils.py
from refactor_tool import utils

def test_run_tests():
    result = utils.run_tests()
    assert 'passed' in result