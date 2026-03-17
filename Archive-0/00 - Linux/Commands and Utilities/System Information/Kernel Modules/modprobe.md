
Add or remove modules from the Linux Kernel


### Example

```shell ln:False
$ lsmod | grep -E "^ip_tables\b"
ip_tables              32768  0
```

- use `-r` to remove
```shell ln:False
$ sudo modprobe -r ip_tables
```

- not found
```shell ln:False
$ lsmod | grep -E "^ip_tables\b"
```

- Adds module (no flag needed)
```shell ln:False
$ sudo modprobe ip_tables
```

```shell ln:False
$ lsmod | grep -E "^ip_tables\b"
ip_tables              32768  0
```

---

</br>

>[!note] 
> `insmod` is an older command used for the same purpose.
> However, we must specify the full path to the module.