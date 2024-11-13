
</br>

The ESP is a special partition on a data storage device (like a hard disk drive or solid-state drive) used by computers with <mark style="background: #D2B3FFA6;">UEFI firmware</mark>.

- <mark style="background: #FFB86CA6; color: black;">File System</mark>: It is typically formatted with a <mark style="background: #D2B3FFA6;">FAT32 file system</mark>.
- <mark style="background: #FFB86CA6; color: black;">Size</mark>: Usually ranges from 100MB to 200MB. (500MB recommended for modern desktop systems).

### Purpose and Function

- <mark style="background: #FFB86CA6; color: black;">Boot Process</mark>:
	The ESP contains the [[Bootloader|bootloader]] and other files necessary for the boot process. When the system starts, the UEFI firmware loads the bootloader from the ESP to boot the operating system.
- <mark style="background: #FFB86CA6; color: black;">Storage</mark>:
	It stores essential files such as boot loaders, device drivers, and system utilities needed during the boot process.
- <mark style="background: #FFB86CA6; color: black;">Multi-OS Support</mark>:
	The ESP can support multiple operating systems, each with its own bootloader stored in the partition.

### Key Features

- <mark style="background: #FFB86CA6; color: black;">OS Independence</mark>:
	The ESP is OS-independent, meaning it can be used by different operating systems like Windows, Linux, and macOS.
- <mark style="background: #FFB86CA6; color: black;">Redundancy and Recovery</mark>:
	It helps in system recovery and maintenance by providing a dedicated space for boot-related files, ensuring that the system can boot even if other parts of the disk are corrupted.