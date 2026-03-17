</br>

==Hard links== and ==soft links== (also known as <mark style="background: #D2B3FFA6;">symbolic links</mark> or <mark style="background: #D2B3FFA6;">symlinks</mark>) are used to create references to files and directories. Here’s a breakdown of each type:

</br>

## Hard Links

A hard link is a direct reference to the physical data on the disk (==inode==).

> Multiple filenames can point to the same inode.

- **<mark style="background: #FFB86CA6; color: black;">Characteristics</mark>**:
    - **<mark style="background: #ABF7F7A6;">Same Inode</mark>**: Hard links share the same inode number as the original file.
    - **<mark style="background: #ABF7F7A6;">Broken Links</mark>**: Changes to the data in one hard link are reflected in all hard links pointing to the same inode.
    - **<mark style="background: #ABF7F7A6;">Flexibility</mark>**: The data is only deleted when the last hard link is removed. (i.e. the data is still accessible even when the original file has been deleted)
- **<mark style="background: #FFB86CA6; color: black;">Usage</mark>**:
    
    ```shell ln:False
    ln original_file hard_link
    ```

- **<mark style="background: #FFB86CA6; color: black;">Limitations</mark>**:
	- Cannot be used beyond the current filesystem. (i.e. we cannot create a hard link from one partition to another)
	- Cannot link to directories. The Restriction is in place because of:
		1. **<mark style="background: #ABF7F7A6;">Broken Links</mark>**:
			Allowing hard links to directories could create loops in the filesystem, making it difficult to traverse and manage.
		2. **<mark style="background: #ABF7F7A6;">Broken Links</mark>**:
			Hard links to directories could lead to inconsistencies and corruption, as the filesystem would struggle to maintain accurate references and counts.


### Soft Links (Symbolic Links)

A soft link is a special file that points to another file or directory by its path.

- **<mark style="background: #FFB86CA6; color: black;">Characteristics</mark>**:
    - **<mark style="background: #ABF7F7A6;">Broken Links</mark>**: Soft links have a different inode number from the original file.
    - **<mark style="background: #ABF7F7A6;">Broken Links</mark>**: They store the path to the target file or directory.
    - **<mark style="background: #ABF7F7A6;">Flexibility</mark>**: Can span across different filesystems and can link to directories.
    - **<mark style="background: #ABF7F7A6;">Broken Links</mark>**: If the target file is deleted, the soft link becomes a “broken link” or “dangling link.”
- **<mark style="background: #FFB86CA6; color: black;">Usage</mark>**:
    
    ```shell ln:False
    ln -s target_file soft_link
    ```

---

</br>

### <mark style="background: #BBFABBA6;">Example</mark>

```bash ln:False
$ ln stat.sh stat
$ ln -s stat.sh stats
$ ls -li stat*
526027 -rwxr--r-T 2 jeswins jeswins 946 Nov 20 10:52 stat
526025 lrwxrwxrwx 1 jeswins jeswins   7 Nov 20 16:28 stats -> stat.sh
526027 -rwxr--r-T 2 jeswins jeswins 946 Nov 20 10:52 stat.sh
```
- `line 1` creates a <mark style="background: #D2B3FFA6;">hard link</mark> to `stat.sh`
- `line 2` creates a <mark style="background: #D2B3FFA6;">soft link</mark> to `stat.sh`

> [!note] 
> - Note that both <mark style="background: #D2B3FFA6;">soft link</mark> and the original file(`stat.sh`) have the same inode number (`526027`).
> - <mark style="background: #D2B3FFA6;">soft link</mark> will have a different inode number and will point to original file(`stat.sh`) by its path.

##### `-i` flag in ==ls== shows the ==inode number==

```shell ln:False
$ ls -lid /usr/bin/
44 drwxr-xr-x 2 root root 36864 Nov 13 05:59 /usr/bin/
$ ls -lid /bin
12 lrwxrwxrwx 1 root root 7 Apr 22  2024 /bin -> usr/bin
```

---

</br>

### Practical Considerations

- **<mark style="background: #FFB86CA6; color: black;">Hard Links</mark>**:
	Useful for creating backups or multiple access points to the same data without duplicating the data itself.

</br>

- **<mark style="background: #FFB86CA6; color: black;">Soft Links</mark>**:
	Useful for creating shortcuts or aliases to files and directories, especially when they are located in different filesystems.