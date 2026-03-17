
# `pgrep`

Lists the PIDs of the processes that match the pattern.

```bash
~$ pgrep nginx
945
946
947
```

- Display the name of the process along with PID
```bash
~$ pgrep -l nginx
945 nginx
946 nginx
947 nginx
```

- List all processes run by a user
```bash
~$ pgrep -u jeswins bash
1392
```

---

# `kill`

Sends a signal to a process.

- Send the default signal `SIGTERM` to the process
```bash
~$ kill 928
```

- Send a signal to processes
```bash
~$ sudo kill -SIGTERM 685 686
```

- Another way to send a signal
```bash
~$ sudo kill -15 685
```

- List all signals
```bash
~$ kill -l
 1) SIGHUP       2) SIGINT       3) SIGQUIT      4) SIGILL       5) SIGTRAP
 6) SIGABRT      7) SIGBUS       8) SIGFPE       9) SIGKILL     10) SIGUSR1
11) SIGSEGV     12) SIGUSR2     13) SIGPIPE     14) SIGALRM     15) SIGTERM
16) SIGSTKFLT   17) SIGCHLD     18) SIGCONT     19) SIGSTOP     20) SIGTSTP
21) SIGTTIN     22) SIGTTOU     23) SIGURG      24) SIGXCPU     25) SIGXFSZ
26) SIGVTALRM   27) SIGPROF     28) SIGWINCH    29) SIGIO       30) SIGPWR
31) SIGSYS      34) SIGRTMIN    35) SIGRTMIN+1  36) SIGRTMIN+2  37) SIGRTMIN+3
38) SIGRTMIN+4  39) SIGRTMIN+5  40) SIGRTMIN+6  41) SIGRTMIN+7  42) SIGRTMIN+8
43) SIGRTMIN+9  44) SIGRTMIN+10 45) SIGRTMIN+11 46) SIGRTMIN+12 47) SIGRTMIN+13
48) SIGRTMIN+14 49) SIGRTMIN+15 50) SIGRTMAX-14 51) SIGRTMAX-13 52) SIGRTMAX-12
53) SIGRTMAX-11 54) SIGRTMAX-10 55) SIGRTMAX-9  56) SIGRTMAX-8  57) SIGRTMAX-7
58) SIGRTMAX-6  59) SIGRTMAX-5  60) SIGRTMAX-4  61) SIGRTMAX-3  62) SIGRTMAX-2
63) SIGRTMAX-1  64) SIGRTMAX
```

- To search for info on a signal
```bash
~$ man 7 kill

# search for the required signal
```
### Important Signals

- `SIGTERM` 15
Gives the process the time to end the process in an orderly manner.

- `SIGKILL` 9
Ensure that the process is terminated immediately. Used if `SIGTERM` does not work as the process might have crashed.

- `SIGSTOP` 19
Stops a process and not terminated.
Can be verified by using [[top]] where the process Status will be `T` (stopped by job control signal)

- `SIGCONT` 18
To continue a stopped process.
Process status will turn from `T` to `S` when using [[top]]

- `SIGHUP` 1
- `SIGINT` 2


---

# `pkill`

Send a signal to all processes that match a pattern.
`SIGTERM` is the default signal.

```bash
~$ sudo pkill nginx
```

- By exact matching of pattern `-x`
```bash
~$ sudo pkill -x nginx
```

> [!Note]
> Avoid using `pkill` without `-x` as unintended processes that match the pattern might get stopped


---

# `killall`

Sends a signal to all processes with a specific property such as name or user.
`SIGTERM` is the default signal.

- Terminate all processes run by a user
```bash
~$ sudo killall -u jeswins
```

- list all signals
```bash
~$ killall -l
HUP INT QUIT ILL TRAP ABRT BUS FPE KILL USR1 SEGV USR2 PIPE ALRM TERM STKFLT
CHLD CONT STOP TSTP TTIN TTOU URG XCPU XFSZ VTALRM PROF WINCH POLL PWR SYS
```