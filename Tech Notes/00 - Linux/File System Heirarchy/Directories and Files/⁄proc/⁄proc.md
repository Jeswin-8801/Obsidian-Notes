
> Virtual directory that represents running processes
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

## **In the `/proc` directory:**

### Process subdirectories
> Each process running on the system has a subdirectory named after its process ID (PID).

#### Information about processes
> The `/proc` directory contains information about running processes, including their PID, user, current working directory, and memory.

#### Information about hardware
> The `/proc` directory contains information about the system's hardware, including CPU and RAM information. (`/proc/cpuinfo`)

#### Information about the network
> The `/proc` directory contains information about the system's network, including active TCP connections and network interface statistics. 

#### Security-related information
> The `/proc` directory contains security-related information, such as memory mappings of a process and file descriptors opened by a process.

---

> [!IMPORTANT]
> [[Important Virtual Files in ⁄proc]]

