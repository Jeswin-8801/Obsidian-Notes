
Adds behavior to a function or class. (`@decorator`)

```python
def some_decorator(f):
    def wraps(*args):
        print(f"Calling function '{f.__name__}'")
        return f(args)
    return wraps

@some_decorator
def decorated_function(x):
    print(f"With argument '{x}'")
```

```bash
Calling function 'decorated_function'
With argument 'Python'
```

## Example

```python
# Defining a decorator
def trace(f):
    def wrap(*args, **kwargs):
        print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")
        return f(*args, **kwargs)
	
    return wrap

# Applying decorator to a function
@trace
def add_two(x):
    return x + 2

# Calling the decorated function
add_two(3)

# Applying decorator to a lambda
print((trace(lambda x: x ** 2))(3))
```

```python
>>> add_two(3)
[TRACE] func: add_two, args: (3,), kwargs: {}
5
>>> print((trace(lambda x: x ** 2))(3))
[TRACE] func: <lambda>, args: (3,), kwargs: {}
9
```


