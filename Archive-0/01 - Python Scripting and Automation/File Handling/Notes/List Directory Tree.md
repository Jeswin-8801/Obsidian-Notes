
- using [[Getting a Directory Listing#`os.listdir()`|os.listdir()]]

```python
import os

def directory_tree(path, level = 0):
	print('\t' * level, path, sep = '')
	for entry in os.listdir(path):
	    if os.path.isdir(os.path.join(path, entry)):
	        directory_tree(os.path.join(path, entry), level + 1)
```

```python ln:False
>>> directory_tree('./')
./
        ./Commands and Utilities
                ./Commands and Utilities\Changing Process Priorities
                ./Commands and Utilities\Compression And Archiving
                ./Commands and Utilities\Create, Monitor and Terminate Processes
                ./Commands and Utilities\Others
                ./Commands and Utilities\Process Text Streams
                ./Commands and Utilities\Regular Expressions
                ./Commands and Utilities\Using Streams
        ./File System Heirarchy
                ./File System Heirarchy\Directories and Files
                        ./File System Heirarchy\Directories and Files\⁄etc
                        ./File System Heirarchy\Directories and Files\⁄proc
                ./File System Heirarchy\How To
                ./File System Heirarchy\Useful Information
        ./Images
```

- using [[Getting a Directory Listing#`os.scandir()`|os.scandir()]]

```python
import os

def directory_tree(path, level = 0):
	print('\t' * level, path if level == 0 else path.name, sep = '')
	with os.scandir(path) as entries:
	    for entry in entries:
	        if entry.is_dir():
		        directory_tree(entry, level + 1)
```

```python ln:False
>>> directory_tree('./')
./
        Commands and Utilities
                Changing Process Priorities
                Compression And Archiving
                Create, Monitor and Terminate Processes
                Others
                Process Text Streams
                Regular Expressions
                Using Streams
        File System Heirarchy
                Directories and Files
                        ⁄etc
                        ⁄proc
                How To
                Useful Information
        Images
```

## Comparing [[Getting a Directory Listing#`os.listdir()`|os.listdir()]] and [[Getting a Directory Listing#`os.scandir()`|os.scandir()]]

> Checkout [[cProfile]]

> [[List Directory Tree|directory_tree()]]

```python ln:False
# os.scandir()
>>> cProfile.run('directory_tree("./")')
./
        Commands and Utilities
                Changing Process Priorities
                Compression And Archiving
                Create, Monitor and Terminate Processes
                Others
                Process Text Streams
                Regular Expressions
                Using Streams
        File System Heirarchy
                Directories and Files
                        ⁄etc
                        ⁄proc
                How To
                Useful Information
        Images
         137 function calls (122 primitive calls) in 0.005 seconds
...(truncated)

# os.listdir()
>>> cProfile.run('directory_tree("./")')
./
        ./Commands and Utilities
                ./Commands and Utilities\Changing Process Priorities
                ./Commands and Utilities\Compression And Archiving
                ./Commands and Utilities\Create, Monitor and Terminate Processes
                ./Commands and Utilities\Others
                ./Commands and Utilities\Process Text Streams
                ./Commands and Utilities\Regular Expressions
                ./Commands and Utilities\Using Streams
        ./File System Heirarchy
                ./File System Heirarchy\Directories and Files
                        ./File System Heirarchy\Directories and Files\⁄etc
                        ./File System Heirarchy\Directories and Files\⁄proc
                ./File System Heirarchy\How To
                ./File System Heirarchy\Useful Information
        ./Images
         1366 function calls (1351 primitive calls) in 0.011 seconds
```