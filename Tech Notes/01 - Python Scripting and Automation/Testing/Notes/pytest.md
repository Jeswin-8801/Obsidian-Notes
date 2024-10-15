
A external testing library that adds onto the shortcomings of [[unittest]].
Provides a plugin based ecosystem.

### Sample Test Program

```python title:test_with_pytest.py
def test_always_passes():
    assert True

def test_always_fails():
    assert False
```
> running `pytest` from the top-level folder of your project:
```bash ln:False
(venv) $ pytest
============================= test session starts ==============================
platform linux -- Python 3.12.6, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/jeswins/Downloads/project
collected 2 items

test_with_pytest.py .F                                                   [100%]

=================================== FAILURES ===================================
______________________________ test_always_fails _______________________________
    def test_always_fails():
>       assert False
E       assert False

test_with_pytest.py:5: AssertionError
=========================== short test summary info ============================
FAILED test_with_pytest.py::test_always_fails - assert False
========================= 1 failed, 1 passed in 0.06s ==========================
```

The output then indicates the status of each test using a syntax similar to `unittest`:
```bash ln:False
test_with_pytest.py .F [ 50%]
test_with_unittest.py F. [100%]
```

- **A dot (`.`)** means that the test passed.
- **An `F`** means that the test has failed.
- **An `E`** means that the test raised an unexpected exception.
