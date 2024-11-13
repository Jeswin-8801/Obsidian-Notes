---
tags:
  - boot
---

</br>

Program that is responsible for loading the <mark style="background: #D2B3FFA6;">operating system kernel</mark> into memory and starting it.

> It acts as an interface between the firmware (BIOS or UEFI) and the operating system.

</br>

### Functions of a Bootloader

- <mark style="background: #FFB86CA6; color: black;">Initialization</mark>:
	After the system firmware initializes the hardware, the bootloader takes over to load the operating system.
- <mark style="background: #FFB86CA6; color: black;">Kernel Loading</mark>:
	It locates the kernel on the disk, loads it into memory, and starts it.
- <mark style="background: #FFB86CA6; color: black;">Multi-boot Support</mark>:
	Many bootloaders can manage multiple operating systems, allowing the user to choose which one to boot.
- <mark style="background: #FFB86CA6; color: black;">Configuration</mark>:
	Bootloaders can pass parameters to the kernel, such as specifying the root filesystem or enabling debugging options.

</br>

### Common Linux Bootloaders

- <mark style="background: #FFB86CA6; color: black;">GRUB (Grand Unified Bootloader)</mark>:
	The most widely used bootloader in Linux. It supports a variety of operating systems and provides a user-friendly interface with advanced features.
- <mark style="background: #FFB86CA6; color: black;">systemd-boot</mark>:
	A simple UEFI boot manager that is part of the systemd project.