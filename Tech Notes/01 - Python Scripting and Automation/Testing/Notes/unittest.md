It is a built-in library.

- You put your tests into classes as methods
- You use a series of special assertion methods in the `unittest.TestCase` class instead of the built-in `assert` statement

> A simple assertion test
```python ln:False
>>> assert sum([1,1,1]) == 6, "Should be 6"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: Should be 6
```

Converting the above assert test to a `unittest`
```python title:test_sum_unittest.py
import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()
```

```bash ln:False
$ python test_sum_unittest.py
.F
======================================================================
FAIL: test_sum_tuple (__main__.TestSum)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_sum_unittest.py", line 9, in test_sum_tuple
    self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
AssertionError: Should be 6

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)
```

## Assertions

|Method|Equivalent to|
|---|---|
|`.assertEqual(a, b)`|`a == b`|
|`.assertTrue(x)`|`bool(x) is True`|
|`.assertFalse(x)`|`bool(x) is False`|
|`.assertIs(a, b)`|`a is b`|
|`.assertIsNone(x)`|`x is None`|
|`.assertIn(a, b)`|`a in b`|
|`.assertIsInstance(a, b)`|`isinstance(a, b)`|

> [!example] 
> [[Anagram Example using unittest|Checkout Unittest for an Anagram check Program]]


