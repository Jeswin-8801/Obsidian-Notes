
</br>

Stands for <mark style="background: #D2B3FFA6;">disk usage</mark> and estimates file space usage.

</br>

- Estimates the size of every single file in the given directory (==in bytes==)
```bash ln:False
$ sudo du / | head
4       /lib.usr-is-merged
8       /run/initramfs
0       /run/udev/tags/seat
0       /run/udev/tags/systemd
0       /run/udev/tags/power-switch
0       /run/udev/tags/uaccess
... (Truncated)
```

- `-s` for summarize
- `-h` for human readable
```bash ln:False
$ sudo du -sh /boot
95M     /boot
```

- use `--max-depth` to limit child directory traversal
```bash ln:False
$ sudo du -h --max-depth 2 /etc
32K     /etc/cron.daily
4.0K    /etc/rc0.d
4.0K    /etc/initramfs-tools/hooks
44K     /etc/initramfs-tools/scripts
4.0K    /etc/initramfs-tools/conf.d
68K     /etc/initramfs-tools
12K     /etc/supercat
12K     /etc/vim
... (Truncated)
```