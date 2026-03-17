</br>

## File Ownership

Each file and directory in Linux has three types of owners:

1. **<mark style="background: #FFB86CA6; color: black;">User</mark>**: The owner of the file. Typically, the user who created the file.
2. **<mark style="background: #FFB86CA6; color: black;">Group</mark>**: A set of users who share the same permissions for the file.
3. **<mark style="background: #FFB86CA6; color: black;">Others</mark>**: All other users on the system.

## File Permissions

Permissions are divided into three categories for each type of owner:

- **<mark style="background: #FFB86CA6; color: black;">Read (r)</mark>**
- **<mark style="background: #FFB86CA6; color: black;">Write (w)</mark>**
- **<mark style="background: #FFB86CA6; color: black;">Execute (x)</mark>**

</br>

```bash ln:False
$ ln -l
total 36
drwxr-x--- 4 jeswins jeswins 4096 Nov 16 13:12 ./
drwxr-xr-x 3 root    root    4096 Nov 13 06:09 ../
-rw------- 1 jeswins jeswins  973 Nov 16 16:31 .bash_history
-rw-r--r-- 1 jeswins jeswins  220 Mar 31  2024 .bash_logout
```

> Alternatively can use <mark style="background: #D2B3FFA6;">ll</mark> (shorthand for <mark style="background: #D2B3FFA6;">ln -al</mark>)

```bash ln:False
-rw-r--r-- 1 user group 1234 Nov 16 18:12 filename
```

- The very first character can take on the following values:
	- <mark style="background: #FFB86CA6; color: black;">d</mark> for directory
	- <mark style="background: #FFB86CA6; color: black;">-</mark> for file
	- <mark style="background: #FFB86CA6; color: black;">l</mark> for link
- `rw-r--r--`
	- <mark style="background: #FFB86CA6; color: black;">rw-</mark>: permissions for ==user/owner==.
	- <mark style="background: #FFB86CA6; color: black;">r--</mark>: permissions for ==group==.
	- <mark style="background: #FFB86CA6; color: black;">r--</mark>: permissions for ==others==.
- `1`: The number of hard links.
- `user`: The owner of the file.
- `group`: The group associated with the file.
- `1234`: The size of the file in bytes.
- `Nov 16 18:12`: The last modification date and time.
- `filename`: The name of the file.

---

</br>

## Other Permissions

Beyond the standard read (`r`), write (`w`), and execute (`x`) permissions, there are several special permissions that provide additional control over files and directories. These include the sticky bit (`t`), setuid (`s`), setgid (`s`), and their uppercase counterparts (`T`, `S`, `S`).

- <mark style="background: #FFB86CA6; color: black;">4</mark> - setuid
- <mark style="background: #FFB86CA6; color: black;">2</mark> - setgid
- <mark style="background: #FFB86CA6; color: black;">1</mark> - sticky bit

```bash ln:False
$ chmod 7111 stat.sh
$ ll stat.sh
---s--s--t 1 jeswins jeswins 946 Nov 20 10:52 stat.sh*
$ chmod 7000 stat.sh
$ ll stat.sh
---S--S--T 1 jeswins jeswins 946 Nov 20 10:52 stat.sh
```

### Setuid (`s` and `S`)

- **<mark style="background: #FFB86CA6; color: black;">s</mark>**: When set on an executable file, it allows the file to be executed with the permissions of the file owner. This is useful for programs that need elevated privileges.
    
    ```bash ln:False
    chmod u+s /path/to/file
    ```
    
    <mark style="background: #BBFABBA6;">Example</mark>: `-rwsr-xr-x` (the `s` in the user permissions indicates setuid is set).
    
- **<mark style="background: #FFB86CA6; color: black;">S</mark>**: Similar to `s`, but indicates that the execute (`x`) permission is not set for the user.
    
    ```bash ln:False
    chmod 4755 /path/to/file
    ```
    
    <mark style="background: #BBFABBA6;">Example</mark>: `-r-Sr-xr-x` (the `S` in the user permissions indicates setuid is set without execute permission).
    

### Setgid (`s` and `S`)

- **<mark style="background: #FFB86CA6; color: black;">s</mark>**: When set on a directory, new files created within the directory inherit the group ID of the directory, rather than the primary group ID of the user who created the file. When set on an executable file, it allows the file to be executed with the permissions of the file’s group.
    
    ```bash ln:False
    chmod g+s /path/to/directory
    ```
    > *OR*
    ```bash ln:False
    chmod 2745 /path/to/directory
    ```
    
    <mark style="background: #BBFABBA6;">Example</mark>: `drwxrwsr-x` (the `s` in the group permissions indicates <mark style="background: #D2B3FFA6;">setgid</mark> is set).
    
- **<mark style="background: #FFB86CA6; color: black;">S</mark>**: Similar to `s`, but indicates that the execute (`x`) permission is not set for the group.

    <mark style="background: #BBFABBA6;">Example</mark>: `drwxr-Sr-x` (the `S` in the group permissions indicates <mark style="background: #D2B3FFA6;">setgid</mark> is set without execute permission).

### Sticky Bit (`t` and `T`)

The sticky bit is a special type of permission in Linux that is primarily used on directories. When the sticky bit is set on a directory, it ensures that only the owner of a file within that directory, the directory owner, or the root user can delete or rename the file.

> This is particularly useful in directories like `/tmp`, where many users have write access

To check if a directory has the sticky bit set, you can use the <mark style="background: #FFB86CA6; color: black;">ls -ld</mark> or <mark style="background: #FFB86CA6; color: black;">stat</mark> command.

```bash ln:False
$ ls -ld /tmp
drwxrwxrwt 15 root root 4096 Nov 20 07:42 /tmp/
```

- **<mark style="background: #FFB86CA6; color: black;">t</mark>**: Indicates that the sticky bit is set.

	To set the sticky bit on a directory, you can use the `chmod` command:

	```bash ln:False
	chmod +t /path/to/directory
	```
	> *OR*

    ```bash ln:False
    chmod 1776 /path/to/directory
    ```
	
	- to remove it:
	
	```bash ln:False
	chmod -t /path/to/directory
	```
    
- **<mark style="background: #FFB86CA6; color: black;">T</mark>**: Similar to `t`, but indicates that the execute (`x`) permission is not set for others.
    
	```bash ln:False
	~$ ll stat.sh
	-rwxr--r-- 1 jeswins jeswins 946 Nov 20 10:52 stat.sh*
	$ chmod +t stat.sh
	$ ll stat.sh
	-rwxr--r-T 1 jeswins jeswins 946 Nov 20 10:52 stat.sh*
	```
    
    <mark style="background: #BBFABBA6;">Example</mark>: `drwxrwxrwT` (the `T` at the end indicates the sticky bit is set without execute permission).