import pytest


@pytest.mark.leetcode
class TestShortestCompletingWord:

    def test_invalid_license_plate(self, leetcode):
        license_plate = 23
        words = ["Tempo", "car"]
        with pytest.raises(TypeError):
            leetcode.shortest_completing_word(license_plate, words)

    def test_invalid_words(self, leetcode):
        license_plate = "a1r sa2"
        words = ["Tempo", 2]
        with pytest.raises(TypeError):
            leetcode.shortest_completing_word(license_plate, words)
    
    def test_case1(self, leetcode):
        license_plate = "1s3 PSt"
        words = ["step","steps","stripe","stepple"]
        expected_output = "steps"
        result = leetcode.shortest_completing_word(license_plate, words)
        if expected_output != result:
            raise ValueError(f'Expected {expected_output} = {result}')

    def test_case2(self, leetcode):
        license_plate = "1s3 456"
        words = ["looks","pest","stew","show"]
        expected_output = "pest"
        result = leetcode.shortest_completing_word(license_plate, words)
        if expected_output != result:
            raise ValueError(f'Expected {expected_output} = {result}')

    def test_fail(self, leetcode):
        license_plate = "1s3 456"
        words = ["looks","pest","stew","show"]
        output = "show"
        result = leetcode.shortest_completing_word(license_plate, words)
        if output == result:
            raise ValueError(f'Expected {output} != {result} on failure')