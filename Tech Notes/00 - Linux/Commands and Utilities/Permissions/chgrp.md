
</br>

Used to change the group ownership of files and directories.

### Basic Syntax

```shell ln:False
chgrp [OPTIONS] GROUP FILE...
```

- **<mark style="background: #FFB86CA6; color: black;">GROUP</mark>**: The name of the new group or the group ID (GID).
- **<mark style="background: #FFB86CA6; color: black;">FILE</mark>**: The name of one or more files or directories.

### Examples

1. **<mark style="background: #FFB86CA6; color: black;">Change the group of a single file</mark>**:
    
    ```shell ln:False
    chgrp www-data filename
    ```
    
2. **<mark style="background: #FFB86CA6; color: black;">Change the group of multiple files</mark>**:
    
    ```shell ln:False
    chgrp www-data file1 file2 dir1
    ```
    
3. **<mark style="background: #FFB86CA6; color: black;">Change the group using a numeric GID</mark>**:
    
    ```shell ln:False
    chgrp +1000 filename
    ```
    

### Options

- **<mark style="background: #FFB86CA6; color: black;">-R</mark>**: Recursively change the group ownership of all files and directories under a given directory.
    
    ```shell ln:False
    chgrp -R www-data /path/to/directory
    ```
    
- **<mark style="background: #FFB86CA6; color: black;">-h</mark>**: Change the group ownership of symbolic links themselves, rather than the files they point to.
    
    ```shell ln:False
    chgrp -h www-data symlink1
    ```
    
- **<mark style="background: #FFB86CA6; color: black;">-v</mark>**: Verbose mode, which shows the files being processed.
    
    ```shell ln:False
    chgrp -v www-data file1 file2
    ```
    

### When to use

- Regular users can change the group of a file only if they own the file and are members of the new group.
- Administrative users can change the group ownership of any file.