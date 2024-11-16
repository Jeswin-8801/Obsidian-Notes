The `/etc/fstab` file is a system configuration file in Linux and other Unix-like operating systems that ==contains information about disk drives and partitions==.

> An entry in `/etc/fstab` might look like this:
>
> ```text
> # <file system> <mount point>   <type>  <options>       <dump>  <pass>
> UUID=123e4567-e89b-12d3-a456-426614174000 /               ext4    defaults        1 1
> /dev/sda1		/mnt/data		ext4		defaults		0  2
> ```

It includes the following params:

- **<mark style="background: #FFB86CA6;color: black">Filesystem</mark>**
	The device or partition to be mounted, typically specified by its device node (e.g., `/dev/sda1`), UUID, or label.
    
- **<mark style="background: #FFB86CA6;color: black">Mount Point</mark>**
	The directory where the filesystem is to be mounted (e.g., `/mnt/data`).
    
- **<mark style="background: #FFB86CA6;color: black">Filesystem Type</mark>**
	The type of filesystem (e.g., `ext4`, `xfs`, `vfat`).
    
- **<mark style="background: #FFB86CA6;color: black">Options</mark>**
	Mount options (e.g., `defaults`, `noatime`, `ro`).
    
- **<mark style="background: #FFB86CA6;color: black">Dump</mark>**
	Used for backup operations (usually set to `0` or `1`).
    
- **<mark style="background: #FFB86CA6;color: black">Pass</mark>**
	- A number indicating the order in which the file systems should be checked by [[fsck]] at boot time. <mark style="background: #D2B3FFA6;">0</mark> means the file system is not checked, <mark style="background: #D2B3FFA6;">1</mark> is for the root file system, and <mark style="background: #D2B3FFA6;">2</mark> is for other file systems.


This file ensures that filesystems are mounted in a consistent manner whenever the system boots.

</br>

- **<mark style="background: #ABF7F7A6;">Editing <mark style="background: #D2B3FFA6;">/etc/fstab</mark></mark>**:
    
    - Always back up the file before making changes. Incorrect entries can prevent the system from booting properly.
    - Use a text editor with root privileges to edit the file (e.g., `sudo nano /etc/fstab`).

</br>

- **<mark style="background: #ABF7F7A6;">Testing Changes</mark>**:
    
    - After editing, you can test the changes without rebooting by using the `mount -a` command, which attempts to mount all file systems listed in `/etc/fstab`.