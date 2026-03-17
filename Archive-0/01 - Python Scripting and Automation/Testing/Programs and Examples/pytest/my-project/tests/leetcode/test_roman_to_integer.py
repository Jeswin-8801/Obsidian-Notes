import pytest


@pytest.mark.leetcode
class TestRomanToInt:

    def test_invalid_input(self, leetcode):
        with pytest.raises(TypeError):
            leetcode.roman_to_int(23)
    
    def test_case1(self, leetcode):
        expected_output = 3
        result = leetcode.roman_to_int("III")
        if expected_output != result:
            raise ValueError(f'Expected {expected_output} = {result}')
    
    def test_case2(self, leetcode):
        expected_output = 58
        result = leetcode.roman_to_int("LVIII")
        if expected_output != result:
            raise ValueError(f'Expected {expected_output} = {result}')
    
    def test_case3(self, leetcode):
        expected_output = 1994
        result = leetcode.roman_to_int("MCMXCIV")
        if expected_output != result:
            raise ValueError(f'Expected {expected_output} = {result}')
    
    def test_fail(self, leetcode):
        output = 10
        result = leetcode.roman_to_int("I")
        if output == result:
            raise ValueError(f'Expected {output} != {result} on failure')
