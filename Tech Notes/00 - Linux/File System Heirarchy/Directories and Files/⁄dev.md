> The `/dev/` directory consists of files that represent devices that are attached to the local system.

However, these are not regular files that a user can read and write to; these files are called devices files or special files

**Device files are abstractions of standard devices that applications interact with via I/O system calls.** 

The device files that correspond to hardware devices fall into two main categories. Mainly character special files and block special files.

### Device files are denoted as the following:

- `c`  character
> [[Difference Between Character Special Files and Block Special Files#Character Devices|Character Devices]]

- `b`  block
> [[Difference Between Character Special Files and Block Special Files#Block Devices|Block Devices]]

- `p`  pipe
> Named pipes allow two or more processes to communicate with each other, these are similar to character devices, but instead of having output sent to a device, it's sent to another process.

- `s`  socket
> Socket devices facilitate communication between processes, similar to pipe devices but they can communicate with many processes at once.

[[Difference Between Character Special Files and Block Special Files|Learn about the differences between the Character Devices and Block Devices]]

---

## **Device Names**

The most common device names:
### **SCSI**

> It is a protocol used for allow communication between disks, printers, scanners and other peripherals to your system.

They are represented by a prefix of `sd` (SCSI disk).

Common SCSI device files:

- `/dev/sda` - First hard disk
- `/dev/sdb` - Second hard disk
- `/dev/sda3` - Third partition on the first hard disk

>[!IMPORTANT] Important
>[[Why is the First Logical Partition in a MBR scheme named ⁄dev⁄sda5]]

### **Pseudo Devices**

Pseudo devices are ==devices in Linux that are implemented entirely in software, rather than hardware==. They can be used to add enhanced features to real devices, or to provide device-like interfaces to other subsystems.

>A lot of pseudo devices are denoted as `character devices` such as `/dev/null`

[[Types of Pseudo Devices]]


### **PATA Devices**

Sometimes in older systems you may see hard drives being referred to with an hd prefix:

- `/dev/hda` - First hard disk
- `/dev/hdd2` - Second partition on 4th hard disk

---

## Commands and Utilities associated with `/dev`
### **[[udev]]**


