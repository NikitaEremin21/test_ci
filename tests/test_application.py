import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from src.main import sum_two


def test_hello_thing():
    result = sum_two(1, 2)
    assert result == 3
