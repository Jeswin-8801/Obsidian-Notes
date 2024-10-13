
```bash
~$ top

top - 16:35:47 up 13:37,  2 users,  load average: 0.01, 0.02, 0.00
Tasks: 225 total,   1 running, 224 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.2 us,  0.7 sy,  0.0 ni, 99.2 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :   3868.2 total,   2962.8 free,    530.9 used,    610.6 buff/cache
MiB Swap:   1964.0 total,   1964.0 free,      0.0 used.   3337.2 avail Mem

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
  23445 root      20   0       0      0      0 I   1.3   0.0   0:06.51 kworker
  23861 jeswins   20   0   11908   5760   3712 R   0.7   0.1   0:00.46 top
    850 root      20   0  315860   9472   7936 S   0.3   0.2   4:27.14 vmtoolsd
    .
    .
    .
```

- `PR` ==priority==
- `NI` ==Nice== value [[nice, renice#`nice`|Checkout more about nice]]
- `VIRT` amount of memory used including shared libraries and SWAP
- `RES` ==Reserved==; stands for physical main memory that is not swapped
- `SHR` ==Shared==; memory shared with other processes
- `S` ==Status==; There are different states such as S, R, I, Z
	- `S` Sleep
	- `D` Uninterruptible sleep
	- `R` Running
	- `I` Idle
	- `Z` Zombie; A process that is no longer running but uses memory
	- `T` Stopped by job control signal
	- `t` stopped by debugger during trace
- `TIME+` Time that the process used (in seconds)

### In the top half
Each line shows
1. shows uptime
	- `load average: 0.01, 0.02, 0.00`
		- `0.01` system utilization in the last minute
		- `0.02` system utilization in the last 5 minutes
		- `0.00` system utilization in the last 15 minutes
2. shows overview of all the tasks/processes.
3. `%Cpu(s):  0.2 us,  0.7 sy,  0.0 ni, 99.2 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st`
	- `us` - Time spent in user space
	- `sy` - Time spent in kernel space
	- `ni` - Time spent running niced user processes (User defined priority/CPU time spent on low priority processes) [[nice, renice#`nice`|Checkout nice]]
	- `id` - Time spent in idle operations
	- `wa` - Time spent on waiting on IO peripherals (e.g.. disk)
	- `hi` - Time spent handling hardware interrupt routines. (Whenever a peripheral unit want attention form the CPU, it literally pulls a line, to signal the CPU to service it)
	- `si` - Time spent handling software interrupt routines.
	- `st` - Time spent on involuntary waits by virtual CPU while hypervisor is servicing another processor (stolen from a virtual machine)
4. Shows the RAM or physical memory info (checkout `free` command | [[Important Virtual Files in ⁄proc#`/proc/meminfo`|/proc/meminfo]])
	- `MiB` stands for Megabytes and the same holds true if shown as `KiB` or `GiB`
5. Shows the swap memory

## Hotkeys

- `h` for help, shows all available hotkeys
- `t` for sort by time