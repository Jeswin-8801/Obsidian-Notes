
</br>

The **<mark style="background: #D2B3FFA6;">Initial RAM Disk (initrd)</mark>** in Linux is a temporary root file system that is loaded into memory during the boot process.

It plays a crucial role in preparing the system before the actual root file system is mounted.

</br>

### Purpose of initrd

- **<mark style="background: #FFB86CA6; color: black;">Temporary Root File System</mark>**:
	Provides a temporary root file system that the kernel can use to load necessary drivers and modules before the real root file system is available.
- **<mark style="background: #FFB86CA6; color: black;">Hardware Initialization</mark>**:
	Helps in initializing hardware components and loading kernel modules that are required to access the root file system.

</br>

### Boot Process with initrd

1. **<mark style="background: #FFB86CA6; color: black;">Boot Loader</mark>**:
	The [[Bootloader|bootloader]] (like <mark style="background: #D2B3FFA6;">GRUB</mark>) loads the kernel and the <mark style="background: #D2B3FFA6;">initrd image</mark> into memory.
1. **<mark style="background: #FFB86CA6; color: black;">Kernel Initialization</mark>**:
	The kernel starts and mounts the initrd as the root file system.
1. **<mark style="background: #FFB86CA6; color: black;">Execution of init Scripts</mark>**:
	The initrd contains scripts and executables that perform necessary setup tasks, such as loading additional drivers and mounting the real root file system.
1. **<mark style="background: #FFB86CA6; color: black;">Switch to Real Root File System</mark>**:
	Once the real root file system is ready, the initrd transitions control to it, and the system continues booting normally.

</br>

### initrd vs initramfs

- **<mark style="background: #FFB86CA6; color: black;">initrd</mark>**:
	Traditionally uses a compressed file system image that is loaded into a RAM disk.
- **<mark style="background: #FFB86CA6; color: black;">initramfs</mark>**:
	A newer approach that uses a <mark style="background: #D2B3FFA6;">cpio archive</mark>, which is unpacked directly into a tmpfs (temporary file system) in memory. This method is more flexible and efficient.

</br>

### Practical Use

- **<mark style="background: #FFB86CA6; color: black;">Kernel Modules</mark>**:
	Essential for systems where the root file system resides on complex storage setups like ==RAID==, ==LVM==, or ==encrypted partitions==.
- **<mark style="background: #FFB86CA6; color: black;">System Recovery</mark>**:
	Useful in recovery scenarios where the main root file system is not accessible.