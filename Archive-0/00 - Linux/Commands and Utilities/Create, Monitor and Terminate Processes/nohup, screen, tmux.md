
# `nohup`

short for `no hang up` is a command in Linux systems that keep processes running even after exiting the shell or terminal

```bash
~$ nohup sleep 30 &
[1] 61318
~$ nohup: ignoring input and appending output to 'nohup.out'

```

```bash
~$ ls | grep nohup.out
nohup.out
```

---

# `screen`

same function as `nohup`. Provides a virtual terminal.
Similar to `tmux`.

To start a new window
```bash
~$ screen
.
.

[Press Space or Return to end.]
```

To start a new window
```
[Ctrl-A] + C
```

In the new window start a process and switch windows using:
```bash
~$ sleep 100

[Ctrl-A] + [space]
```

To stop the screen session, use `D` for detach
```
~$

[Ctrl-A] + D
```

> [!Note]
> Here, `Ctrl-A` is the initiator for hotkeys.
> `[Ctrl-A] + C` is used to start a new window
> `[Ctrl-A] + [space]` is used to switch between windows, but not exit the screen session
> `[Ctrl-A] + D` for detach


---

# `tmux`

Also has the same function as `nohup`. Starts a new shell.

```
~$ tmux
```

To open a new window:
```
~$

[Ctrl-B] + C
```

Start a process, then use the hotkey `S` for switch
```
~$ sleep 100

[Ctrl-B] + S
```

We get the following box:
```bash
(0) - 0: 2 windows (attached)
(1) ├─> 0: bash-
(2) └─> 1: [tmux]*


┌ 0 (sort: index) ──────────────────────────────────────────────┐
│ ~$                           │~$ sleep 100                    │
│                              │                                │
│                              │                                │
│           ┌────────┐         │          ┌──────────┐          │
│           │ 0:bash │         │          │ 1:[tmux] │          │
│           └────────┘         │          └──────────┘          │
│                              │                                │
└───────────────────────────────────────────────────────────────┘
[0] 0:bash- 1:[tmux]*             "ubuntu-server" 14:11 29-Sep-24
```
> use arrow keys to navigate and enter to select

To detach use `[Ctrl-B] + D`