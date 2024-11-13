---
tags:
  - INFO
---


<mark style="background: #D2B3FFA6;">Character Special Files</mark> are simple interfaces to character devices. 
Likewise, <mark style="background: #D2B3FFA6;">Block Special Files</mark> are to block devices.

> The difference between these devices depends on how the operating system reads data off of them. 

</br> 

#### Character Devices

- These devices transfer data, but one a character at a time.
- A driver communicates with a character device by sending ==single characters== as data such as bytes. 
- In addition, character devices don’t require buffering when communicating with a driver. 

#### Block Devices

- These devices transfer data, but in large ==fixed-sized blocks==.
- A driver accesses data from block devices through a cache and communicates by sending an entire ==block of data==.

---

</br>

### Identifying Character Special Files and Block Special Files 

- Character devices can be sound cards or serial ports
- Block devices can be hard disks or USBs

> [!NOTE] Note
> We identify block and character devices by the letter that appears in front of the permissions.
> 
> The letter `b` that is displayed in the first column denotes a block device. 
> On the other hand, the letter `c` shown in the first column symbolizes a character device:

```
brw-rw---- 1 root disk      8,   0 Sep 25 15:49 sda
brw-rw---- 1 root disk      8,   1 Sep 25 15:08 sda1
brw-rw---- 1 root disk      8,   2 Sep 25 15:08 sda2

crw-rw---- 1 root tty       7,   0 Sep 25 15:08 vcs
crw-rw---- 1 root tty       7,   1 Sep 25 15:08 vcs1
crw-rw---- 1 root tty       7,   2 Sep 25 15:08 vcs2

vcs corresponds to /dev/tty for the same number
The /dev/tty file is a special file that represents the terminal for the current process, which displays the terminal associated with the current SSH session
```