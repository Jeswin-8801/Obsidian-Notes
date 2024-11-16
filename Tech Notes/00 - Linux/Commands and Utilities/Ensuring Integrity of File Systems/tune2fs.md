
</br>

The <mark style="background: #D2B3FFA6;">tune2fs</mark> command in Linux is used to adjust various tunable parameters of ==ext2==, ==ext3==, and ==ext4== file systems.

It allows system administrators to modify file system attributes, optimize performance, and manage file system behavior.

> [!info] 
> Similarly we can modify file system attributes for <mark style="background: #D2B3FFA6;">xfs file systems</mark> using <mark style="background: #ABF7F7A6;">[[xfs_repair, xfs_db, xfs_fsr#`xfs_repair`|xfs_repair -n]]</mark>

</br>

## Basic Usage

```bash ln:False
$ sudo tune2fs -l /dev/sda2
tune2fs 1.47.0 (5-Feb-2023)
Filesystem volume name:   <none>
Last mounted on:          /boot
Filesystem UUID:          e28f5bc5-7f07-4255-9449-eb8c4b5ffc3e
Filesystem magic number:  0xEF53
... (Truncated)
```

This command lists the current parameters of the file system on the specified device.

---

</br>

## Common Options

- <mark style="background: #FFB86CA6; color: black;">-l</mark>: List the contents of the file system superblock.
    
    ```bash ln:False
    sudo tune2fs -l /dev/sdX1
    ```
    
- <mark style="background: #FFB86CA6; color: black;">-c</mark>: Set the maximum number of mounts before a file system check. (<mark style="background: #FF5582A6;">IMP</mark>)
    
    ```bash ln:False
    $ sudo tune2fs -c 20 /dev/sda2
	tune2fs 1.47.0 (5-Feb-2023)
	Setting maximal mount count to 20
    ```
    
- <mark style="background: #FFB86CA6; color: black;">-i</mark>: Set the interval between file system checks. (<mark style="background: #FF5582A6;">IMP</mark>)
    
    ```bash ln:False
    $ sudo tune2fs -i 2d /dev/sda2
	tune2fs 1.47.0 (5-Feb-2023)
	Setting interval between checks to 172800 seconds
    ```
    
- <mark style="background: #FFB86CA6; color: black;">-L</mark>: Set the volume label.
    
    ```bash ln:False
    sudo tune2fs -L MyVolume /dev/sdX1
    ```
    
- <mark style="background: #FFB86CA6; color: black;">-m</mark>: Set the percentage of reserved blocks for the super-user.
    
    ```bash ln:False
    sudo tune2fs -m 1 /dev/sdX1
    ```
    
- <mark style="background: #FFB86CA6; color: black;">-e</mark>: Change the behavior of the file system when errors are detected (e.g., continue, remount-ro, panic).
    
    ```bash ln:False
    sudo tune2fs -e remount-ro /dev/sdX1
    ```
    
- <mark style="background: #FFB86CA6; color: black;">-r</mark>: Set the number of reserved blocks.
    
    ```bash ln:False
    sudo tune2fs -r 1000 /dev/sdX1
    ```
    
- <mark style="background: #FFB86CA6; color: black;">-C</mark>: Set the number of times the file system has been mounted.
    
    ```bash ln:False
    sudo tune2fs -C 0 /dev/sdX1
    ```
    
- <mark style="background: #FFB86CA6; color: black;">-U</mark>: Set the UUID of the file system.
    
    ```bash ln:False
    sudo tune2fs -U random /dev/sdX1
    ```

---

</br>

## Advanced Options

- <mark style="background: #FFB86CA6; color: black;">-E</mark>: Set extended options for the file system.
    
    ```bash ln:False
    sudo tune2fs -E stride=16,stripe-width=64 /dev/sdX1
    ```
    
- <mark style="background: #FFB86CA6; color: black;">-O</mark>: Enable or disable specific file system features.
    
    ```bash ln:False
    sudo tune2fs -O ^has_journal /dev/sdX1
    ```

---

</br>

## Practical Examples

1. **<mark style="background: #FFB86CA6; color: black;">List File System Parameters</mark>**:
    
    ```bash ln:False
    sudo tune2fs -l /dev/sdX1
    ```
    
2. **<mark style="background: #FFB86CA6; color: black;">Set Volume Label</mark>**:
    
    ```bash ln:False
    sudo tune2fs -L MyData /dev/sdX1
    ```
    
3. **<mark style="background: #FFB86CA6; color: black;">Change Reserved Blocks Percentage</mark>**:
    
    ```bash ln:False
    sudo tune2fs -m 2 /dev/sdX1
    ```
    
4. **<mark style="background: #FFB86CA6; color: black;">Schedule File System Check</mark>**:
    
    ```bash ln:False
    sudo tune2fs -c 30 /dev/sdX1
    ```