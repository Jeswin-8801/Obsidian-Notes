
Allows you to interact with the ==Python runtime environment==, ==access command line arguments==, ==manipulate the Python path==, ==handle exceptions==, and much more.

## Accessing Command Line Arguments

```python title:example.py
import sys

arguments = sys.argv
print(arg)
```

```bash ln:False
$ python example.py text1 1 2 3
['example.py', 'text1', '1', '2', '3']
```

- for programs that require arguments
```python
import sys  
  
# Check if at least one argument is provided  
if len(sys.argv) < 2:  
	print("No arguments provided. Exiting.")  
	sys.exit()
```

> Checkout [[argparse vs sys.argv]]

---
## Customizing Python's Runtime Environment

By manipulating the `sys.path` list, you can control which directories Python searches for modules.

- add and remove a directory to the `sys.path` list
```python
import sys

sys.path.append('/path/to/directory')  # Add directory to sys.path
sys.path.remove('/path/to/directory')  # Remove directory from sys.path
```

---
## Working with ==Standard Input==, ==Output== and ==Error==

- `sys.stdin`: Standard input
- `sys.stdout`: Standard output
- `sys.stderr`: Standard error

- Standard Input
```python
import sys

name = input("Enter your name: ")
print("Hello, " + name)
```

```python
import sys

name = sys.stdin.readline().strip()
print("Hello, " + name)
```

- redirecting the standard output
```python
import sys  
  
# Save the original standard output  
original_stdout = sys.stdout  
  
# Redirect standard output to a file  
with open('output.txt', 'w') as f:  
	sys.stdout = f 
	print("This will be written to the file.")  
  
# Restore the original standard output  
sys.stdout = original_stdout  
print("This will be printed on the console.")
```

- Standard Error
```python ln:False
import sys

print("This will be printed to standard error", file = sys.stderr)
```

---
## Exiting the Program

```python ln:False
sys.exit(0) # Exit the program with exit code 0
```

---
## Understanding System-specific Parameters

```python ln:False
>>> print("Python Version:", sys.version)
Python Version: 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)]
```

```python ln:False
>>> print("Platform:", sys.platform)
Platform: win32
```

- return size of Objects
```python
import sys

size = sys.getsizeof('Hello, World!')
print("Size:", size, "bytes")
```

```bash title:output ln:False
Size: 62 bytes
```

