
# Raising Exceptions

```python
number = 10
if number > 5:
    raise Exception(f"The number should not exceed 5. ({number=})")
print(number)
```

```bash
Traceback (most recent call last):
  File "./low.py", line 3, in <module>
    raise Exception(f"The number should not exceed 5. ({number=})")
Exception: The number should not exceed 5. (number=10)
```

# Assertions

```python
number = 10
assert (number < 5), f"The number should not exceed 5. ({number=})"
print(number)
```

```bash
Traceback (most recent call last):
  File "./low.py", line 2, in <module>
    assert (number < 5), f"The number should not exceed 5. ({number=})"
            ^^^^^^^^^^
AssertionError: The number should not exceed 5. (number=10)
```

> [!note]
> Don’t rely on assertions for catching crucial run conditions of your program in production.
  Because Python globally disables assertions when you run it in optimized mode using the `-O` (`python -O foo.py`)


# Handling Exceptions With the `try` and `except` Block

![[20241012161602_python_exception_handling.png]]

```python
# Filename: linux_interaction.py

def linux_interaction():
    import sys
    if "linux" not in sys.platform:
        raise RuntimeError("Function can only run on Linux systems.")
    print("Doing Linux things.")

try:
    linux_interaction()
except:
    print("Linux function wasn't executed.")
```

```bash
$ python linux_interaction.py
Linux function wasn't executed.
```

- catch exceptions

```python
# Filename: linux_interaction.py

# ...

try:
    linux_interaction()
except RuntimeError as error:
    print(error)
    print("The linux_interaction() function wasn't executed.")
```

```bash
$ python linux_interaction.py
Function can only run on Linux systems.
The linux_interaction() function wasn't executed.
```

- Example with open file

```python
try:
    with open("file.log") as file:
        read_data = file.read()
except:
    print("Couldn't open file.log")
```

- using `else` and `finally`
```python
# Filename: linux_interaction.py

# ...

try:
    linux_interaction()
except RuntimeError as error:
    print(error)
else: # executes if no exception
    try:
        with open("file.log") as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally: # executes in every scenario
    print("Cleaning up, irrespective of any exceptions.")
```

# Custom Exceptions

```python
# Filename: linux_interaction.py

class PlatformException(Exception):
    """Incompatible platform."""

def linux_interaction():
    import sys
    if "linux" not in sys.platform:
        raise PlatformException("Function can only run on Linux systems.")
    print("Doing Linux things.")
```

```bash
$ python linux_interaction.py
Traceback (most recent call last):
  ...
PlatformException: Function can only run on Linux systems.
```