
## Create or Append contents to a File

```python
# Create and write to a file
with open("example.txt", "w") as file:
    file.write("This is the first line.\n")

# Append content to the same file
with open("example.txt", "a") as file:
    file.write("This is an appended line.\n")
```

---
## Deleting Files

`os.remove()` and `os.unlink()` both have the same function.

```python
import os

data_file = 'data.txt'
os.remove(data_file)
```

- error handling
```python
import os

data_file = 'Age Estimation_240410_153346.sdocx'

# Use exception handling
try:
    os.remove(data_file)
except (OSError, IsADirectoryError, PermissionError)  as e:
    print(f'Error: {data_file} : {e.strerror}')
```

---

## Deleting Directories

```python
import os

trash_dir = 'my_documents/bad_dir'

try:
    os.rmdir(trash_dir)
except OSError as e:
    print(f'Error: {trash_dir} : {e.strerror}')
```

---

## Copying Files

using `shutil.copy()`

```python
import shutil

src = 'path/to/file.txt'
dst = 'path/to/dest_dir'
shutil.copy(src, dst)
```

> [!note] 
> To preserve all file metadata (such as creation time, update time, etc) when copying, use `shutil.copy2()`

---

## Copying Directories

using `shutil.copytree()`

```python ln:False
>>> import shutil
>>> shutil.copytree('data_1', 'data1_backup')
'data1_backup'
```

---

## Moving Files and Directories

using `shutil.move()`

```python ln:False
>>> import shutil
>>> shutil.move('dir_1/', 'backup/')
'backup'
```

---

## Renaming Files and Directories

```python ln:False
>>> os.rename('first.zip', 'first_01.zip')
```
