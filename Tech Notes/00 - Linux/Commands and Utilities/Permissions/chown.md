</br>

Used to change the ownership of files and directories.

It allows you to set a new owner and/or group for a given file, directory, or symbolic link.

> [!note] 
> Alternatively, we can change just the owner group using [[chgrp]]

### Basic Syntax

```bash ln:False
chown [OPTIONS] USER[:GROUP] FILE(s)
```

- **<mark style="background: #FFB86CA6; color: black;">USER</mark>**: The username or user ID (UID) of the new owner.
- **<mark style="background: #FFB86CA6; color: black;">GROUP</mark>**: The new group’s name or group ID (GID).
- **<mark style="background: #FFB86CA6; color: black;">FILE(s)</mark>**: The name of one or more files, directories, or links.

### Examples

1. **<mark style="background: #FFB86CA6; color: black;">Change the Owner of a File</mark>**:
    
    ```bash ln:False
    chown newowner filename
    ```
    
    This command changes the owner of `filename` to `newowner`.
    
2. **<mark style="background: #FFB86CA6; color: black;">Change the Owner and Group of a File</mark>**:
    
    ```bash ln:False
    chown newowner:newgroup filename
    ```
    
    This command changes both the owner and the group of `filename`.
    
3. **<mark style="background: #FFB86CA6; color: black;">Change the Group of a File</mark>**:
    
    ```bash ln:False
    chown :newgroup filename
    ```
    
    This command changes only the group of `filename`.
    
4. **<mark style="background: #FFB86CA6; color: black;">Change Ownership Recursively</mark>**:
    
    ```bash ln:False
    chown -R newowner:newgroup /path/to/directory
    ```
    
    The `-R` option changes the ownership of the directory and all its contents recursively.
    
5. **<mark style="background: #FFB86CA6; color: black;">Using Numeric IDs</mark>**:
    
    ```bash ln:False
    chown 1001:1001 filename
    ```
    
    This command changes the owner and group of `filename` to the user and group with UID and GID 1001.