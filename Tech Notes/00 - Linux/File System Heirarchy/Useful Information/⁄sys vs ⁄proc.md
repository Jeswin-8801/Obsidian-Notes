---
tags:
  - INFO
  - Linux-Directories
---

In Linux, both `/sys` and `/proc` are special filesystems that provide interfaces to kernel data structures, but they serve different purposes and contain different types of information.

## [[⁄proc]]

- <mark style="background: #FFB86CA6; color: black;">Purpose</mark>: Checkout [[⁄proc]]
- <mark style="background: #FFB86CA6; color: black;">Content</mark>: Contains files and directories that represent the current state of the system, including process information, kernel parameters, and system statistics.
- <mark style="background: #FFB86CA6; color: black;">Examples</mark>:
    - `/proc/cpuinfo`: Information about the CPU.
    - `/proc/meminfo`: Information about memory usage.
    - `/proc/[pid]`: Directories for each running process, containing information about the process.
    
	> [!info]
	> Checkout [[Important Virtual Files in ⁄proc]]
	
- <mark style="background: #FFB86CA6; color: black;">Usage</mark>: Often used for monitoring and debugging purposes. It allows users to read kernel data structures and change certain kernel parameters at runtime using `sysctl`.

## `/sys`

- <mark style="background: #FFB86CA6; color: black;">Purpose</mark>: Provides a structured view of the kernel’s device model and is used to export information about devices and drivers.
- <mark style="background: #FFB86CA6; color: black;">Content</mark>: Contains files and directories that represent devices, drivers, and other kernel objects.
- <mark style="background: #FFB86CA6; color: black;">Examples</mark>:
    - `/sys/class`: Contains directories for different classes of devices (e.g., block, net).
    - `/sys/devices`: Contains directories for physical devices.
    - `/sys/module`: Contains information about loaded kernel modules.
- <mark style="background: #FFB86CA6; color: black;">Usage</mark>: Used for device management and configuration. It allows users to interact with kernel objects and change their attributes.

---

</br>

## Key Differences

- <mark style="background: #FFB86CA6; color: black;">Focus</mark>: `/proc` is more focused on <mark style="background: #D2B3FFA6;">process and system information</mark>, while `/sys` is focused on <mark style="background: #D2B3FFA6;">device and driver information</mark>.
  </br>
- <mark style="background: #FFB86CA6; color: black;">Structure</mark>: `/proc` is less structured and more ad-hoc, whereas `/sys` follows a more organized and hierarchical structure reflecting the kernel’s device model.
  </br>
- <mark style="background: #FFB86CA6; color: black;">Interaction</mark>: Both filesystems allow reading and writing to kernel data structures, but `/sys` is more commonly used for device configuration and management.