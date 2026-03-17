
> **[[#`/proc/meminfo`|/proc/meminfo]]**
> **[[#`/proc/cpuinfo`|/proc/cpuinfo]]**
> **[[#`/proc/filesystems`|/proc/filesystems]]**
> **[[#`/proc/sys`|/proc/sys]]**
> **[[#`/proc/modules`|/proc/modules]]**
> **[[#`/proc/mounts`|/proc/mounts]]**
> **[[#`/proc/pci`|/proc/pci]]**
> **[[#`/proc/uptime`|/proc/uptime]]**
> **[[#`/proc/version`|/proc/version]]**

> [!NOTE]
> Checkout [[List all ls commands|How to list all ls commands]]

---
### `/proc/meminfo`

List details about ==memory usage and statistics== that contain the total amount of memory, free memory, and the memory used by each process. 

> `lsmem`

```
~$ cat /proc/meminfo
MemTotal:        3961028 kB
MemFree:         1249148 kB
MemAvailable:    3360108 kB
Buffers:           83068 kB
Cached:          2161636 kB
SwapCached:            0 kB
Active:           282580 kB
Inactive:        2009160 kB
.
.
.
```

---
### `/proc/cpuinfo`

List information about the CPU(s) on the system, such as the model, speed, and number of cores.

> `lscpu`

```
~$ cat /proc/cpuinfo
processor       : 0
vendor_id       : GenuineIntel
cpu family      : 6
model           : 142
model name      : Intel(R) Core(TM) i5-10210U CPU @ 1.60GHz
stepping        : 12
.
.
.
```

---
### `/proc/filesystems`

Contains a list of all the filesystems that are supported by the kernel.

```
~$ cat /proc/filesystems
nodev   sysfs
nodev   tmpfs
nodev   bdev
nodev   proc
nodev   cgroup
nodev   cgroup2
nodev   cpuset
.
.
.
```

> [!NOTE]
> [[List all filesystems in ⁄proc⁄filesystems|See how to list all supported filesystems using tr, cut and xargs]]

---
### `/proc/sys`

List configuration and runtime parameters for the kernel.

---
### `/proc/modules`

Currently loaded kernel modules. 

> `lsmod`

```
~$ cat /proc/modules
tls 155648 0 - Live 0x0000000000000000
qrtr 53248 2 - Live 0x0000000000000000
vsock_loopback 12288 0 - Live 0x0000000000000000
.
.
.
```

---
### `/proc/mounts`

List of all mounts in use by the system.

> `mount -l`

```
~$ cat /proc/mounts
sysfs /sys sysfs rw,nosuid,nodev,noexec,relatime 0 0
proc /proc proc rw,nosuid,nodev,noexec,relatime 0 0
udev /dev devtmpfs rw,nosuid,relatime,size=1944236k,nr_inodes=486059,mode=755,inode64 0 0
.
.
.
```

---
### `/proc/pci`

Information about every PCI device.

> `lspci`

---

### `/proc/uptime`

Uptime information (in seconds).

> `uptime`

```
~$ cat /proc/uptime
132172.02 257845.76
```

---

### `/proc/version`

Kernel version, `gcc` version, and Linux distribution installed.

> `uname -a`

```
~$ cat /proc/version
Linux version 6.8.0-45-generic (buildd@lcy02-amd64-115) (x86_64-linux-gnu-gcc-13 (Ubuntu 13.2.0-23ubuntu4) 13.2.0, GNU ld (GNU Binutils for Ubuntu) 2.42) #45-Ubuntu SMP PREEMPT_DYNAMIC Fri Aug 30 12:02:04 UTC 2024
```