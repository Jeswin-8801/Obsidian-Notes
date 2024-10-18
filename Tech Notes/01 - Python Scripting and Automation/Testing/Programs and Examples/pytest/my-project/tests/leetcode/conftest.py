import pytest

from src.my_project.leetcode import LeetCode


@pytest.fixture
def leetcode():
    return LeetCode()
