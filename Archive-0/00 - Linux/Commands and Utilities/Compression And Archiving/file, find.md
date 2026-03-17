</br>

# <mark style="background: #ABF7F7A6;">find</mark>

Shows the file type

```bash ln:False
~$ file /etc/passwd
/etc/passwd: ASCII text
```

---

</br>

# <mark style="background: #ABF7F7A6;">find</mark>

```bash ln:False
~$ find -name *keys
./.ssh/authorized_keys
```

```bash ln:False
~$ sudo find /var -name journal
/var/log/journal
```
 
 - ignore case
```bash ln:False
~$ find -iname 'xa*log'
./split/xarhrt.log
./split/XAR.log
./xa_hart.log
./Xamd.log
```

- find by file type
- `f` stands for file
```bash ln:False
~$ sudo find / -type f -name '*\.ini'
/usr/src/linux-headers-6.8.0-45/scripts/kconfig/tests/pytest.ini
/usr/lib/python3.12/test/libregrtest/mypy.ini
/home/jeswins/.local/share/nsnake/settings.ini
```

- `d` stands for directory
```bash ln:False
~$ sudo find / -type d -name sbin
/usr/sbin
/usr/local/sbin
```

- `l` symlink
```bash ln:False
~$ sudo find / -type l -name python3
/usr/share/bash-completion/completions/python3
/usr/bin/python3
```

- find only in current directory
```bash ln:False
~$ find / -maxdepth 1 -type l
/lib
/sbin
/lib64
/bin
```