
```python
import os

try:
    os.mkdir('example_directory/')
except FileExistsError as exc:
    print(exc)
```
> OR
```python
from pathlib import Path

p = Path('example_directory')
try:
    p.mkdir()
except FileExistsError as exc:
    print(exc)
```
Alternatively,
ignore the `FileExistsError` by passing `exist_ok=True`
```python
from pathlib import Path

p = Path('example_directory')
p.mkdir(exist_ok=True)
```

# Multiple directories

```python
import os

if not os.path.isdir('2018/'):
	os.makedirs('2018/10/05')
```
creates a nested directory structure
```text ln:False
.
|
└── 2018/
    └── 10/
        └── 05/
```



