
# `ps`

```bash
~$ ps -ef
UID          PID    PPID  C STIME TTY          TIME CMD
root           1       0  0 02:58 ?        00:00:11 /sbin/init
root           2       0  0 02:58 ?        00:00:00 [kthreadd]
root           3       2  0 02:58 ?        00:00:00 [pool_workqueue_release]
root           4       2  0 02:58 ?        00:00:00 [kworker/R-rcu_g]
.
.
.
```
- `-e` displays all running processes
- `-f` stands for full format printing (displays more information)

> [!Note]
> `/sbin/init` is always the first process with the PID 1

- search processes using [[grep, egrep, fgrep|grep]] or `pgrep`

To display all processes run by a certain user:
```bash
~$ ps -u jeswins
    PID TTY          TIME CMD
   1310 ?        00:00:00 systemd
   1311 ?        00:00:00 (sd-pam)
   1687 ?        00:00:00 screen
   1688 pts/1    00:00:00 bash
   1782 pts/2    00:00:00 bash
   .
   .
   .
```

---
# `pstree`

lists processes as a tree

```bash
~$ pstree
systemd-+-ModemManager---3*[{ModemManager}]
        |-VGAuthService
        |-agetty
        |-cron
        |-dbus-daemon
        |-fwupd---5*[{fwupd}]
.
.
.
```

- show processes with PIDs using `-p`
```bash
~$ pstree -p
systemd(1)-+-ModemManager(1040)-+-{ModemManager}(1191)
           |                    |-{ModemManager}(1209)
           |                    `-{ModemManager}(1211)
           |-VGAuthService(849)
           |-agetty(1015)
           |-cron(911)
           .
           .
           .
```

---

# `uptime`

```bash
~$ uptime
 06:22:17 up 14:21,  2 users,  load average: 0.03, 0.03, 0.04
```

---

# `free`

Shows memory information.

> uses the [[Important Virtual Files in ⁄proc#`/proc/meminfo`|/proc/meminfo]] file

```bash
~$ free
               total        used        free      shared  buff/cache   available
Mem:         3960992      545360     2936332        1564      727096     3415632
Swap:        2011132           0     2011132
```

- for human readable format use `-h`
```bash
~$ free -h
               total        used        free      shared  buff/cache   available
Mem:           3.8Gi       532Mi       2.8Gi       1.5Mi       710Mi       3.3Gi
Swap:          1.9Gi          0B       1.9Gi
```
