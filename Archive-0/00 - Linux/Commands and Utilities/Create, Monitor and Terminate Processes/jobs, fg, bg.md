
# `jobs`

Lists active processes running in the background.

```bash
~$ sleep 10 &
[1] 61257
```

```bash
~$ jobs
[1]+  Running                 sleep 10 &
```

Show only the PID

```bash
~$ jobs -p
61257
```

---

# `fg`

brings the process from background to the foreground, making it the current job.

> [!NOTE]
> Does not exit unless the process finishes or when exited manully

```bash
~$ fg
sleep 10
```


---

# `bg`

Move jobs to background.

> A stopped process running in the foreground can be started in the background using this command

```bash
~$ sleep 20 &
[1] 61283
```

```bash
~$ fg
sleep 20
^Z
[1]+  Stopped                 sleep 20
```

> [!Note]
> `Ctrl-Z` is used to stop the process whereas `Ctrl-C` kills the process.

```bash
~$ bg
[1]+ sleep 20 &
```