
# `os.listdir()`

```python ln:False
>>> entries = os.listdir('./')
>>> for entry in entries:
...     print(entry)
...
Desktop
Documents
Downloads
Favorites
GitHub
...(truncated)
```

---
# `os.scandir()`

For modern python.
As opposed to returning a list for `os.listdir()`, `os.scandir()` returns an iterator.

```python ln:False
>>> import os
>>> entries = os.scandir('my_directory/')
>>> entries
<posix.ScandirIterator object at 0x7f5b047f3690>
```

```python
import os

with os.scandir('./') as entries:
    for entry in entries:
        print(entry.name)
```

---

> Checkout [[List Directory Tree|Show directory tree usong os.listdir() and os.scandir()]]

___



