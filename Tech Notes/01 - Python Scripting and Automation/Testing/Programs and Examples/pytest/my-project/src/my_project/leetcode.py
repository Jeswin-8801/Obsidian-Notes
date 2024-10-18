"""
    Solutions to Leetcode Problems
"""

from collections import Counter


class LeetCode:
    
    def __init__(self) -> None:
        """
        only needed for the roman numeral problem to test pytest.fixtures
        """
        self.roman_nums = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    
    def shortest_completing_word(self, license_plate: str, words: list[str]) -> str:
        letters = Counter(ltr.lower() for ltr in license_plate if ltr.isalpha())
        return min((word for word in words if not letters - Counter(word)), key=len)
    
    def roman_to_int(self, roman_str: str) -> int:
        ans = 0
        length = len(roman_str)
        for i, char in enumerate(roman_str):
            if i < length - 1:
                num_from_roman = self.roman_nums[roman_str[i+1]]
                if self.roman_nums[char] < num_from_roman:
                    ans -= self.roman_nums[char]
                else:
                    ans += self.roman_nums[char]
            else:
                ans += self.roman_nums[char]
        return ans
