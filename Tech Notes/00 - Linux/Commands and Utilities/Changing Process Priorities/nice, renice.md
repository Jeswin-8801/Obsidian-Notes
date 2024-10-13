
# `nice`

Run a program with modified scheduling priority.

> Standard nice value of a process is `0`
> Ranges from `-20` to `19`, where `-20` is the best value and `19` the worst.

Better the nice value, the higher is the scheduling priority as well as the allotted computing resources.

> [!Attention]
> Processes with `-ve` nice values can only be changed by `root`

Setting the command with the nice value 5:
```bash
~$ nice -n 5 sleep 100 &
[1] 22417
```

```bash
~$ top -p 22417

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
  22417 jeswins   25   5    5684   1920   1920 S   0.0   0.0   0:00.02 sleep
```

> [!Note]
> When `-n` is not specified, a default nice value of `10` will be allotted


---

# `renice`

Alter the priority of a running process.

```bash
~$ sleep 100 &
[1] 22463
```

```bash
~$ top -p 22463

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
  22463 jeswins   20   0    5684   1920   1920 S   0.0   0.0   0:00.00 sleep
```

```bash
~$ renice 2 -p 22463
22463 (process ID) old priority 0, new priority 2
```

Change the priority of all processes run by a user:
```bash
~$ sudo renice 1 -u jeswins
1000 (user ID) old priority 0, new priority 1
```

### Checking the nice value of a process using `ps`
```bash
~$ ps -efo pid,ni,cmd
    PID  NI CMD
  22222  -1 -bash USER=jeswins LOGNAME=jeswins HOME=/home/jeswins PATH=/usr/loc...
  22505  -1  \_ sleep 1000 SHELL=/bin/bash PYENV_SHELL=bash PWD=/home/jeswins L...
  22506  -1  \_ ps -efo pid,ni,cmd SHELL=/bin/bash PYENV_SHELL=bash PWD=/home/j...
   2211  -1 -bash DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus HOME=/h...
   2029  -1 -bash DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus HOME=/h...
   1932  -1 /bin/bash STY=1931.pts-0.ubuntu-server TERM=screen.xterm-256color T...
   1782  -1 /bin/bash STY=1687.pts-0.ubuntu-server TERM=screen.xterm-256color T...
   1688  -1 /bin/bash STY=1687.pts-0.ubuntu-server TERM=screen.xterm-256color T...
```

***OR***

```bash
~$ ps -o pid,ni,comm
    PID  NI COMMAND
  22222   1 bash
  22505   1 sleep
  22550   1 ps
```