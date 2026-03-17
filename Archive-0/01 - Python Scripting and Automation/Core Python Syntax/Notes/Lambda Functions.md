
```python
>>> (lambda x: x + 1)(2)
3
```

```python
>>> add_one = lambda x: x + 1
>>> add_one(2)
3
```

equivalent to

```python
def add_one(x):
    return x + 1
```

> A lambda function can’t contain any statements. In a lambda function, statements like `return`, `pass`, `assert`, or `raise` will raise a `SyntaxError` exception

```python
>>> (lambda x: assert x == 2)(2)
  File "<input>", line 1
    (lambda x: assert x == 2)(2)
                    ^
SyntaxError: invalid syntax
```

### Examples

```python
>>> (lambda x, y, z: x + y + z)(1, 2, 3)
6
>>> (lambda *args: sum(args))(1,2,3)
6
>>> (lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)
6
```

Learn more about [[args and kwargs]]
