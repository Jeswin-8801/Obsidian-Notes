
Using `re` module for pattern matching.

```python ln:False
>>> s = 'foo123bar'

>>> # One last reminder to import!
>>> import re

>>> re.search('123', s)
<_sre.SRE_Match object; span=(3, 6), match='123'>
```

using with Boolean constructs

```python ln:False
>>> if re.search('123', s):
...     print('Found a match.')
... else:
...     print('No match.')
...
Found a match.
```

```python ln:False
>>> regex = r'[0-9][0-9][0-9]'
>>> re.search(regex, 'foo456bar')
<_sre.SRE_Match object; span=(3, 6), match='456'>
```


```python ln:False
>>> re.search('x-{3}x', 'x---x')                      # Three dashes
<_sre.SRE_Match object; span=(0, 5), match='x---x'>

>>> print(re.search('x-{3}x', 'x----x'))              # Four dashes
None
```

with dynamic loops

```python
>>> for i in range(1, 6):
...     s = f"x{'-' * i}x"
...     print(f'{i}  {s:10}', re.search('x-{2,4}x', s))
...
1  x-x        None
2  x--x       <_sre.SRE_Match object; span=(0, 4), match='x--x'>
3  x---x      <_sre.SRE_Match object; span=(0, 5), match='x---x'>
4  x----x     <_sre.SRE_Match object; span=(0, 6), match='x----x'>
5  x-----x    None
```

capturing groups

```python ln:False
>>> m = re.search('(\w+),(\w+),(\w+)', 'foo,quux,baz')
>>> m
<_sre.SRE_Match object; span=(0, 12), match='foo:quux:baz'>
```

```python ln:False
>>> m.groups()
('foo', 'quux', 'baz')
>>> m.group(1)
'foo'
>>> m.group(2)
'quux'
>>> m.group(3)
'baz'
>>> m.group(1, 3)
('foo', 'baz')
```

## Example

> Find all files in current directory that are not dot files and contain only alphabets

Checkout [[Getting a Directory Listing]]

```python
import os
import re

def list_alpha_files(directory):
    # Regex pattern to match files with only alphabetic characters
    pattern = re.compile(r'^[A-Za-z]+$')
	
    # List files in the specified directory
    files = os.listdir(directory)
	
    # Filter files based on the regex pattern
    alpha_files = [f for f in files if pattern.match(f)]
	
    return alpha_files

alpha_files = list_alpha_files('./')
for file in alpha_files:
    print(file)

```

is the same as

```python ln:False
>>> print('\n'.join([f for f in os.listdir('./') if re.compile(r'^[A-Z][A-Za-z]+$').match(f)]))
AppData
Contacts
Cookies
Desktop
Documents
...(truncated)
```



