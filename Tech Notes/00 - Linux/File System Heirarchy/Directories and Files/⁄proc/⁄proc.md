---
tags:
  - Virtual-Filesystem
  - Linux-Directories
---

</br>

> <mark style="background: #ABF7F7A6;">Virtual directory that represents running processes</mark>
> 
> It's a pseudo-filesystem that acts as an interface to the kernel's data structures.

```
$ ls /proc
1      203  236  42     6      74   986            meminfo
100    204  237  43     60     75   acpi           misc
107    205  238  44     60011  750  asound         modules
.
.
.
```
 
 ---
 
</br>

## **The `/proc` directory contains:**

#### <mark style="background: #FFB86CA6;">Process subdirectories</mark>
> Each process running on the system has a subdirectory named after its process ID (PID).

#### <mark style="background: #FFB86CA6;">Information about processes</mark>
> The `/proc` directory contains information about running processes, including their PID, user, current working directory, and memory.

#### <mark style="background: #FFB86CA6;">Information about hardware</mark>
> The `/proc` directory contains information about the system's hardware, including CPU and RAM information. (`/proc/cpuinfo`)

#### <mark style="background: #FFB86CA6;">Information about the network</mark>
> The `/proc` directory contains information about the system's network, including active TCP connections and network interface statistics. 

#### <mark style="background: #FFB86CA6;">Security-related information</mark>
> The `/proc` directory contains security-related information, such as memory mappings of a process and file descriptors opened by a process.

---

</br>

> [!IMPORTANT]
> [[Important Virtual Files in ⁄proc]]

> [!note] 
> Also checkout [[⁄sys vs ⁄proc]]