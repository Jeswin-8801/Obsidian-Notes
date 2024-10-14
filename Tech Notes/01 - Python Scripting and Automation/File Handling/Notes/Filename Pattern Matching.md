
| Function                             | Description                                                                     |
| ------------------------------------ | ------------------------------------------------------------------------------- |
| `startswith()`                       | Tests if a string starts with a specified pattern and returns `True` or `False` |
| `endswith()`                         | Tests if a string ends with a specified pattern and returns `True` or `False`   |
| `fnmatch.fnmatch(filename, pattern)` | Tests whether the filename matches the pattern and returns `True` or `False`    |
| `glob.glob()`                        | Returns a list of filenames that match a pattern within the current directory   |

#### Print all files in directory that matches regex

```python
import fnmatch
for filename in os.listdir('.'):
    if os.path.isfile(filename) and fnmatch.fnmatch(filename, '[0-9][0-9]th*'):
        print(filename)
```

> [!note] 
> `fnmatch` and `glob` has reduced support for regex (cannot use `+` or `{}`) and [[Regular Expressions|re]] is preferred for more advanced matching.
> This is because they use wildcard matching.

```python
import glob, os
def glob_list():
	for filename in glob.glob('[0-9]*th*'):
	    if os.path.isfile(filename):
	        print(filename)
```

```text title:output ln:False
10th_CertificateOfMigration.pdf
10th_HallTicket.pdf
12th_fee_reciept.pdf
12th_HallTicket.pdf
```

- search recursively using `iglob`
```python
import glob
for file in glob.iglob('**/*.py', recursive=True):
	print(file)
```

- using [[Regular Expressions|re]]
```python ln:False
>>> import os, re
>>> print('\n'.join([f for f in os.listdir('.') if os.path.isfile(f) and re.compile(r'^[0-9]{2}th*').match(f)]))
```
 also gives the same output
