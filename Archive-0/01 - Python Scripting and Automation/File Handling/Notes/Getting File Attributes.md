---
tags:
  - File-Properties
  - Time-Format
---

using `os.stat()`, `os.scandir()`, or `pathlib.Path()`

-  the `st_mtime` attribute shows the time the content of the file was last modified.
```python ln:False
>>> import os
>>> with os.scandir('./') as dir_contents:
...     for entry in dir_contents:
...         info = entry.stat()
...         print(info.st_mtime)
...
1539032199.0052035
1539032469.6324475
1538998552.2402923
1540233322.4009316
1537192240.0497339
1540266380.3434134
```

- using `pathlib`
```python ln:False
>>> from pathlib import Path
>>> current_dir = Path('my_directory')
>>> for path in current_dir.iterdir():
...     info = path.stat()
...     print(info.st_mtime)
```

- format time
```python
from datetime import datetime
from os import scandir

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

def get_files(path):
    for entry in scandir(path):
        if entry.is_file():
            info = entry.stat()
            print(f'{entry.name:40}\t Last Modified: {convert_date(info.st_mtime)}')
```
> `entry.name` has a maximum of 40 characters
```python ln:False
>>> get_files('01 - Python Scripting and Automation/')
APIs and Web Requests.md                         Last Modified: 13 Oct 2024
Environment Management.md                        Last Modified: 13 Oct 2024
Logging.md                                       Last Modified: 13 Oct 2024
Regular Expressions.md                           Last Modified: 13 Oct 2024
```


