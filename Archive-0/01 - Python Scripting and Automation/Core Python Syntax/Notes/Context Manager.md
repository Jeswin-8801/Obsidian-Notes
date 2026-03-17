
A context manager in Python is a way to manage resources efficiently using the `with` statement.

It ensures that resources like ==files==, ==locks==, ==network connections==, or ==database connections== are properly acquired and released, even if an error occurs.

#### Key Components:

1. `__enter__` **method**: Acquires the resource.
2. `__exit__` **method**: Releases the resource.

##### Custom Context Manger
```python
class MyContext:
    def __enter__(self):
        print("Entering context")
        return self
	
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")
```
> Using the context manager
```python ln:False
>>> with MyContext() as context:
...     print("Inside context")
...
Entering context
Inside context
Exiting context
```

---

### Problems that can occur when managing resources

- When a program keeps creating new connections without releasing or reusing them, the database backend can stop accepting new connections. This might require an admin to log in and manually kill those stale connections to make the database usable again.

- Writing text to files is usually a buffered operation. This means that calling `.write()` on a file won’t immediately result in writing text to the physical file but to a temporary buffer. Sometimes, when the buffer isn’t full and developers forget to call `.close()`, part of the data can be lost forever.

- When your application runs into errors or exceptions that cause the control flow to bypass the code responsible for releasing the resource at hand.
  For the example given below, the implementation doesn’t guarantee the file will be closed if an exception occurs during the `.write()` call.
```python title:example.py
file = open("hello.txt", "w")
file.write("Hello, World!")
file.close()
```

> Solution (using `try...finally`)

```python title:example.py
# Safely open the file
file = open("hello.txt", "w")

try:
    file.write("Hello, World!")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")
finally:
    # Make sure to close the file after using it
    file.close()
```

Checkout [[Exception Handling]]

---

## The `with` Statement

The Python `with` statement creates a ==**runtime context**== that allows you to run a group of statements under the control of a context manager.

```python
with open("hello.txt", mode="w") as file:
    file.write("Hello, World!")
```

### Performing High Precision Calculations

```python ln:False
>>> from decimal import Decimal, localcontext

>>> with localcontext() as ctx:
...     ctx.prec = 42
...     Decimal("1") / Decimal("42")
...
Decimal('0.0238095238095238095238095238095238095238095')

>>> Decimal("1") / Decimal("42")
Decimal('0.02380952380952380952380952381')
```

`localcontext()` provides a context manager that creates a local decimal context and allows you to perform calculations using a custom precision

- precision is reset back to `28` places after the context code block is executed.

### Handling Locks in Multithreaded Programs

Use a `Lock` object as the context manager in a `with` statement to automatically acquire and release a given lock.

```python
import threading

balance_lock = threading.Lock()
```

- approach 1 (using `try...finally`)
```python
balance_lock.acquire()
try:
    # Update the account balance here ...
finally:
    balance_lock.release()
```

- approach 2 (using `with`)
```python
with balance_lock:
    # Update the account balance here ...
```