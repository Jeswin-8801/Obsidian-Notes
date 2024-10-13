> **`/var` contains variable data files**. 

This includes spool directories and files, administrative and logging data, and transient and temporary files.

> [!NOTE] Note
> Some portions of `/var` are not shareable between different systems. For instance, `/var/log` , `/var/lock` , and `/var/run` .

---

```
/var/
  ├── log/
  ├── temp/
  ├── run/
  .
  .
  .
```

| `/var/log`  | Contains log files                           |
| ----------- | -------------------------------------------- |
| `/var/temp` | Contains cached data needed at boot time     |
| `/var/run`  | Contains the current state of a Linux system |
