
```python
>>> import mod
>>> mod.__file__
'C:\\Users\\john\\mod.py'
```

- `__file__` shows the location of the module file

- Can also import specific functions or Classes from a module using `from`

```python
from mod import f, c, Foo
```

- Import everything inside mod. 

```python
from mod import *
```

- Refer to module by an alternate name

```python
import mod as my_mod
```

## `dir()` function

Returns a list of defined names in a namespace

```python
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
'__package__', '__spec__']
```

```python
>>> import mod
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
'__package__', '__spec__', 'mod']
```

- list the names inside module

```python
>>> import mod
>>> dir(mod)
['Foo', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
'__name__', '__package__', '__spec__', 'f', 'c']
```