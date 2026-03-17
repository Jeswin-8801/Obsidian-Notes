
# `*args`

- Stands for arguments.
- Allows you to pass a variable number of positional arguments to a function.
- Collects additional positional arguments as a tuple.

```python
def foo(*args):
    for arg in args:
        print(arg)

foo(1, 2, 3)
# Output:
# 1
# 2
# 3
```

---

# `**kwargs`

- Stands for keyword arguments.
- Allows you to pass a variable number of keyword arguments to a function.
- Collects additional keyword arguments as a dictionary.

```python
def foo(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')

foo(a=1, b=2, c=3)
# Output:
# a = 1
# b = 2
# c = 3
```