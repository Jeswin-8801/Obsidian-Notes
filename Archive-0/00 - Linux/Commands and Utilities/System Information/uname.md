
Provides system information.

- `uname` by itself prints the Kernel Name
```shell ln:False
$ uname
Linux
```

#### Important Flags

- `-a` prints all information
```shell ln:False
$ uname -a
Linux ubuntu 6.8.0-48-generic 48-Ubuntu SMP PREEMPT_DYNAMIC Fri Sep 27 14:04:52 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux
```

- `-r` prints the Kernel Release
```shell ln:False
$ uname -r
6.8.0-48-generic
```

- `-v` provides detailed information about the Kernel Version, as well as build information.
```shell ln:False
$ uname -v
48-Ubuntu SMP PREEMPT_DYNAMIC Fri Sep 27 14:04:52 UTC 2024
```
> The output includes the following info:
> - <mark style="background: #FFB86CA6; color: black;">Kernel build number</mark>: This indicates the specific build of the kernel.
> - <mark style="background: #FFB86CA6; color: black;">SMP (Symmetric Multiprocessing)</mark>: If the kernel supports SMP, this will be indicated.
> - <mark style="background: #FFB86CA6; color: black;">PREEMPT_DYNAMIC</mark>: Indicates that the kernel is built with dynamic preemption, allowing it to switch between different preemption models (like low-latency or real-time) based on the workload
> - <mark style="background: #FFB86CA6; color: black;">Build date and time</mark>: The exact date and time when the kernel was built.

---

```shell ln:False
$ printf "%-15s %-15s %-20s %-20s %-10s %-10s %-20s %-10s\n" "Kernel Name" "Node Name" "Kernel Release" "Kernel Version" "Machine" "Processor" "Hardware Platform" "OS"; printf "%-15s %-15s %-20s %-20s %-10s %-10s %-20s %-10s\n" "$(uname -s)" "$(uname -n)" "$(uname -r)" "$(uname -v | grep -io '.*ubuntu')" "$(uname -m)" "$(uname -p)" "$(uname -i)" "$(uname -o)"
Kernel Name     Node Name       Kernel Release       Kernel Version       Machine    Processor  Hardware Platform    OS
Linux           ubuntu          6.8.0-48-generic     48-Ubuntu           x86_64     x86_64     x86_64               GNU/Linux
```
