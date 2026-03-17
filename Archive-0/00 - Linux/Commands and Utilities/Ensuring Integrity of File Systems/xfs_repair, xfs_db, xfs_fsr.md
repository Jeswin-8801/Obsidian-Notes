---
tags: XFS
---

> [!important] 
> Key Features of the XFS filesystem
> - **<mark style="background: #FFB86CA6; color: black;">Scalable/Parallel I/O</mark>**:
> 	Efficiently handles multiple I/O operations in parallel, improving performance for large-scale applications.
> - **<mark style="background: #FFB86CA6; color: black;">Journaling</mark>**:
> 	Provides robust metadata journaling, which helps in quick recovery and maintaining consistency.
> - **<mark style="background: #FFB86CA6; color: black;">Delayed Allocation</mark>**:
> 	Reduces fragmentation and improves performance by delaying the allocation of disk space until data is actually written.
> - **<mark style="background: #FFB86CA6; color: black;">B+ Trees</mark>**:
> 	Uses B+ trees for directory contents and file allocation, enhancing performance and scalability.
> - **<mark style="background: #FFB86CA6; color: black;">Defragmentation</mark>**:
> 	Supports online defragmentation to optimize file system performance without downtime.

</br>

## <mark style="background: #ABF7F7A6;">xfs_repair</mark>

Repairs corrupt or damaged XFS filesystems.

```bash ln:False
sudo xfs_repair /dev/sdX1
```

- `-n` flag states that `xfs_repair` should not modify but should only scan the file system.
```bash ln:False
$ sudo xfs_repair -n /dev/sdb1
Phase 1 - find and verify superblock...
Phase 2 - using internal log
		- zero log...
		- scan filesystem free space and inode maps...
... (Truncated)
```

- the `-v`flag can be used to provide a more verbose output

> [!note] 
> The file system must be unmounted before using `xfs_repair`

---

</br>

## <mark style="background: #ABF7F7A6;">xfs_db</mark>

Debug the XFS file system.

```bash ln:False
$ sudo xfs_db /dev/sdb1
xfs_db> uuid
UUID = 906004c6b-892f-4f59-8305-bb6431018d34
xfs_db> frag
actual 0, ideal 0, fragmentation factor 0,00%
xfs_db> quit
```

> It provides an interactive cli.
> use `help` to see available options

> [!note] 
> The file system must be unmounted before using `xfs_db`

---

</br>

## <mark style="background: #ABF7F7A6;">xfs_fsr</mark>

It stands for <mark style="background: #D2B3FFA6;">XFS File System Reorganizer</mark> and is used to defragment files within the XFS file system.

```bash ln:False
sudo xfs_fsr /dev/sdX1
```

This command will defragment the XFS file system on the specified device `/dev/sdX1`.

- **<mark style="background: #FFB86CA6; color: black;">-v</mark>**: Verbose mode.
    
    ```bash ln:False
    sudo xfs_fsr -v /dev/sdX1
    ```
    
- **<mark style="background: #FFB86CA6; color: black;">-t seconds</mark>**: Specifies how long to run the reorganization process. The default is 7200 seconds (2 hours).
    
    ```bash ln:False
    sudo xfs_fsr -t 3600 /dev/sdX1
    ```
    
- **<mark style="background: #FFB86CA6; color: black;">-f leftoff</mark>**: Uses a specified file to read and store the state of where the reorganization left off.
    
    ```bash ln:False
    sudo xfs_fsr -f /var/tmp/.fsrlast_xfs /dev/sdX1
    ```
    
- **<mark style="background: #FFB86CA6; color: black;">-m mtab</mark>**: Uses a specified file for the list of file systems to reorganize. The default is `/etc/mtab`.
    
    ```bash ln:False
    sudo xfs_fsr -m /etc/mtab
    ```

> The file system does not need to be unmounted to use `xfs_fsr`

### How It Works

1. **<mark style="background: #FFB86CA6; color: black;">Reorganization Algorithm</mark>**:
    - `xfs_fsr` operates on one file at a time, compacting or improving the layout of the file extents. It copies the entire file to a temporary location and then swaps the data extents of the target and temporary files in an atomic manner.
2. **<mark style="background: #FFB86CA6; color: black;">Running Without Arguments</mark>**:
    - When invoked without arguments, `xfs_fsr` reorganizes all regular files in all mounted XFS file systems. It makes multiple passes over the file systems, each time selecting files with the largest number of extents and attempting to defragment the top 10% of these files.
3. **<mark style="background: #FFB86CA6; color: black;">State Management</mark>**:
    - The utility records the state of where it left off in a file (default is `/var/tmp/.fsrlast_xfs`). This allows it to resume from the same point in subsequent runs.

### Practical Considerations

- **<mark style="background: #FFB86CA6; color: black;">Disk Space</mark>**: 
	Ensure there is enough free disk space to copy files during the reorganization process.
- **<mark style="background: #FFB86CA6; color: black;">Performance Impact</mark>**:
	Running `xfs_fsr` can impact system performance, so it is often scheduled during off-peak hours.
- **<mark style="background: #FFB86CA6; color: black;">Regular Maintenance</mark>**: 
	Regularly running `xfs_fsr` can help maintain optimal file system performance.