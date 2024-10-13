# `file`

Shows the file type

```bash
~$ file /etc/passwd
/etc/passwd: ASCII text
```

---

# `find`

```bash
~$ find -name *keys
./.ssh/authorized_keys
```

```bash
~$ sudo find /var -name journal
/var/log/journal
```
 
 - ignore case
```bash
~$ find -iname 'xa*log'
./split/xarhrt.log
./split/XAR.log
./xa_hart.log
./Xamd.log
```

- find by file type
- `f` stands for file
```bash
~$ sudo find / -type f -name '*\.ini'
/usr/src/linux-headers-6.8.0-45/scripts/kconfig/tests/pytest.ini
/usr/lib/python3.12/test/libregrtest/mypy.ini
/home/jeswins/.local/share/nsnake/settings.ini
```

- `d` stands for directory
```bash
~$ sudo find / -type d -name sbin
/usr/sbin
/usr/local/sbin
```

- `l` symlink
```bash
~$ sudo find / -type l -name python3
/usr/share/bash-completion/completions/python3
/usr/bin/python3
```

- find only in current directory
```bash
~$ find / -maxdepth 1 -type l
/lib
/sbin
/lib64
/bin
```