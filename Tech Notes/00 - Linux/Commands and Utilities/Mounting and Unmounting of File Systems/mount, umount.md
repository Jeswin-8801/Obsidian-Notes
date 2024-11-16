
</br>

# <mark style="background: #ABF7F7A6;">mount</mark>

> Checkout [[Mounting]]

```bash ln:False
mount [options] <device> <directory>
```

- **`<device>`**: The device or partition you want to mount (e.g., `/dev/sda1`).
- **`<directory>`**: The directory where the file system will be attached (e.g., `/mnt`).

</br>

- **<mark style="background: #FFB86CA6; color: black;">-t <type></mark>**: Specifies the file system type (e.g., `ext4`, `xfs`, `vfat`).

	```bash ln:False
	sudo mount -t ext4 /dev/sdb1 /home/jeswins
	```
	> the partition `/dev/sdb1`(device file) of type `ext4` is mounted on mount point `/home/jeswins`
    
- **<mark style="background: #FFB86CA6; color: black;">-o <options></mark>**: Specifies mount options (e.g., `ro` for read-only, `rw` for read-write).
    
    ```bash ln:False
    sudo mount -o ro /dev/sda1 /mnt
    ```
    
- **<mark style="background: #FFB86CA6; color: black;">-a</mark>**: Mounts all file systems listed in `/etc/fstab`.
    
    ```bash ln:False
    sudo mount -a
    ```

---

</br>

# <mark style="background: #ABF7F7A6;">umount</mark>

Used to unmount/detach a filesystem.

```bash ln:False
umount [options] <device|mount_point>
```

</br>

- **<mark style="background: #FFB86CA6; color: black;">-a</mark>**: Unmount all file systems listed in `/etc/fstab`, except those marked as requiring separate unmount.
    
    ```bash ln:False
    sudo umount -a
    ```
    
- **<mark style="background: #FFB86CA6; color: black;">-f</mark>**: Force unmount, even if the device is busy. Use with caution as it may cause data loss.
    
    ```bash ln:False
    sudo umount -f /mnt
    ```
    
- **<mark style="background: #FFB86CA6; color: black;">-l</mark>**: Perform a lazy unmount. Detaches the file system now and cleans up references later.
    
    ```bash ln:False
    sudo umount -l /mnt
    ```
    
- **<mark style="background: #FFB86CA6; color: black;">-r</mark>**: If unmounting fails, try to remount the file system as read-only.
    
    ```bash ln:False
    sudo umount -r /mnt
    ```
    
- **<mark style="background: #FFB86CA6; color: black;">-v</mark>**: Verbose mode.
    
    ```bash ln:False
    sudo umount -v /mnt
    ```