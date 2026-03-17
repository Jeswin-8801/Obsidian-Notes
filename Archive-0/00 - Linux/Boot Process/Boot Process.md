---
tags:
  - boot
---

![[20241113155639_linux_boot_process.png]]

</br>

# 1. [[BIOS vs UEFI#**<mark style="background ABF7F7A6;">BIOS</mark>**|BIOS]]/[[BIOS vs UEFI#**<mark style="background ABF7F7A6;">UEFI (Unified Extensible Firmware Interface)</mark>**|UEFI]]

Once the system powers up, the [[BIOS vs UEFI#**<mark style="background ABF7F7A6;">BIOS</mark>**|BIOS]] or [[BIOS vs UEFI#**<mark style="background ABF7F7A6;">UEFI (Unified Extensible Firmware Interface)</mark>**|UEFI]] programs are executed.

> The BIOS or UEFI runs the <mark style="background: #D2B3FFA6;">power-on self-test (POST)</mark>. The POST does a series of tasks:
> 
> - verify the hardware components and peripherals
> - carry out tests to ensure that the computer is in proper working condition

</br>

# 2. [[Bootloader]]

Once the POST check has checked the state of the machine, **the BIOS/UEFI selects a boot device** depending on the system configuration.

The default boot order is as follows:
1. Hard drives
2. USB drives
3. CD drives

> [!note] 
> **A BIOS system has the boot loader located in the first sector of the boot device**; this is the MBR. It takes up the first 512 bytes on the disk. On the other hand, **a UEFI system stores all startup data in an _.efi_ file**. The file is on the EFI System Partition, which contains the boot loader.

> Checkout [[MBR vs GPT]], [[fdisk#Check Existing Partitions]]


</br>

# 3. GRUB2

Almost all modern Linux distributions use <mark style="background: #D2B3FFA6;">GRUB (GRand Unified Boot Loader)</mark> because it’s very feature-rich:

- ability to boot multiple operating systems
- boots both a graphical and a text-based interface
- allows ease of use over a serial cable
- strong command line interface for interactive configuration
- network-based diskless booting

Presently, <mark style="background: #D2B3FFA6;">GRUB2</mark> has replaced its past version (GRUB), which is now known as <mark style="background: #D2B3FFA6;">GRUB Legacy</mark>.

- Check the GRUB version in your system using the following command:
```shell ln:False
$ sudo grub-install -V
grub-install (GRUB) 2.12-1ubuntu7
```

#### Functions of GRUB2

1. takes over from BIOS or UEFI at boot time
2. loads itself
3. inserts both the Linux kernel and [[initrd (InitialRamDisk)]] into memory
4. turns over execution to the kernel

</br>

# 4. Kernel

After going through BIOS or UEFI, POST, and using a boot loader to initiate the kernel.

Once the kernel is loaded, it mounts the [[initrd (InitialRamDisk)|initrd]] as a temporary root file system that's specified in the `grub.conf` file.

The [[initrd (InitialRamDisk)|initrd]] contains essential scripts and executables that perform necessary setup tasks. These tasks include:
    - Loading additional kernel modules required to access the actual root file system.
    - Handling tasks like decryption if the root file system is encrypted.

**Switch to Real Root File System**:
After the necessary drivers and modules are loaded, the [[initrd (InitialRamDisk)|initrd]] mounts the real root file system and transitions control to it.

**The operating system now controls access to our computer resources**.

> The Linux kernel follows a predefined procedure:
> 
> 1. decompress itself in place
> 2. perform hardware checks
> 3. gain access to vital peripheral hardware
> 4. run the <mark style="background: #D2B3FFA6;">init</mark> process

Next, **init** process continues the system startup by running init scripts for the parent process.



</br>

# 5. Systemd

The kernel initiates the <mark style="background: #D2B3FFA6;">init</mark> process, which starts the parent process. Here, **the parent of all Linux processes** **is** [[SysVinit vs Upstart vs Systemd#Systemd|systemd]], which replaces the old [[SysVinit vs Upstart vs Systemd#SysVinit|SysVinit]] process.

Following the booting steps, <mark style="background: #D2B3FFA6;">Systemd</mark> performs a range of tasks:

- probe all remaining hardware
- mount filesystems
- initiate and terminate services
- manage essential system processes like user login
- run a desktop environment

Lastly, Systemd uses the `/etc/systemd/system/default.target` file to decide the ==state or target== the Linux system boots into.

</br>

# 6. Run Levels

**In Linux, the run level stands for the current state of the operating system**. Run levels define which system services are running. 

[[SysVinit vs Upstart vs Systemd#SysVinit|SysVinit]] identifies run levels by number, however, `.target` files now replace run levels in [[SysVinit vs Upstart vs Systemd#Systemd|systemd]].

Further, [[SysVinit vs Upstart vs Systemd#Systemd|systemd]] activates the <mark style="background: #D2B3FFA6;">_default.target_</mark> unit by default when the system boots. Let’s check our default target:

```bash ln:False
$ systemctl get-default
graphical.target
```

> ==targets== in systemd:
> 
> - _<mark style="background: #FFB86CA6; color: black;">poweroff.target (0)</mark>_: turn off (shut down) the computer
> - _<mark style="background: #FFB86CA6; color: black;">rescue.target (1)</mark>_: initiate a rescue shell process
> - _<mark style="background: #FFB86CA6; color: black;">multi-user.target (3)</mark>_: configure the system as a non-graphical (console) multi-user environment
> - _<mark style="background: #FFB86CA6; color: black;">graphical.target (5)</mark>_: establish a graphical multi-user interface with network services
> - _<mark style="background: #FFB86CA6; color: black;">reboot.target (6)</mark>_: restart the machine
> - _<mark style="background: #FFB86CA6; color: black;">emergency.target</mark>_: emergency run level

> [!note] 
> The run level for a server without a GUI is _3_ because the default target is _<mark style="background: #D2B3FFA6;">multi-user.target</mark>_.

##### Switch targets using the following commands:

- To switch to _==run level 3==_ from ==_run level 5_==, we can run the following command:

```bash
$ sudo systemctl isolate multi-user.target
```

- To take the system to ==_run level 5_==, let’s run the command:

```bash
$ sudo systemctl isolate graphical.target
```