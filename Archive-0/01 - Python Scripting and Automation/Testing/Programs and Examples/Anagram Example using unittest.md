
```python title:__init__.py
import re

def is_anagram(s, t):
    if not isinstance(s, str) or not isinstance(t, str):
        raise TypeError("Both inputs must be strings")
    
    s = s.lower()
    t = t.lower()
    if len(s) != len(t) or contains_number_or_space(s + t):
        return False
    
    freq = [0] * 26
    for i in range(len(s)):
        freq[ord(s[i]) - ord('a')] += 1
        freq[ord(t[i]) - ord('a')] -= 1
    
    for i in range(len(freq)):
        if freq[i] != 0:
            return False
    
    return True

def contains_number_or_space(s):
    return bool(re.search(r'\d|\s', s))
```
- `ord()` returns the Unicode code point for a given character (e.g. returns 65 for `A`)

> Directory Structure
```bash ln:False
project/
│
├── my_scripts/
│   └── __init__.py
|
└── test.py
```

```python title:test.py
import unittest

from my_scripts import is_anagram

class TestAnagram(unittest.TestCase):
    def test_lowercase_string(self):
        """
        Test for anagram using lowercase strings
        """
        original_string = "silent"
        test_string = "listen"
        self.assertTrue(is_anagram(original_string, test_string))
    
    def test_camelcase_string(self):
        """
        Test for anagram using camelcase strings
        """
        original_string = "Silent"
        test_string = "Listen"
        self.assertTrue(is_anagram(original_string, test_string))
    
    def test_withnumberorspace_string(self):
        """
        Test for anagram with string having a number or space
        """
        original_string = "sil4en t"
        test_string = "L isten"
        self.assertFalse(is_anagram(original_string, test_string))
    
    def test_badtype(self):
        not_a_string = 10
        test = "corn"
        with self.assertRaises(TypeError):
            is_anagram(not_a_string, test)

if __name__ == "__main__":
    unittest.main()
```
> Test
```bash ln:False
$ python -m unittest -v test
test_badtype (test.TestAnagram.test_badtype)
Test for input type other than string ... ok
test_camelcase_string (test.TestAnagram.test_camelcase_string)
Test for anagram using camelcase strings ... ok
test_lowercase_string (test.TestAnagram.test_lowercase_string)
Test for anagram using lowercase strings ... ok
test_withnumberorspace_string (test.TestAnagram.test_withnumberorspace_string)
Test for anagram with string having a number or space ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

