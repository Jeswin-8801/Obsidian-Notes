---
tags: How-To
---

```shell ln:False
$ sudo systemctl status /boot
● boot.mount - /boot
     Loaded: loaded (/etc/fstab; generated)
     Active: active (mounted) since Fri 2024-11-15 10:46:57 UTC; 1 day 2h ago
      Where: /boot
       What: /dev/sda2
       Docs: man:fstab(5)
             man:systemd-fstab-generator(8)
      Tasks: 0 (limit: 4556)
     Memory: 104.0K (peak: 576.0K)
        CPU: 4ms
     CGroup: /system.slice/boot.mount

Nov 15 10:46:57 ubuntu systemd[1]: Mounting boot.mount - /boot...
Nov 15 10:46:57 ubuntu systemd[1]: Mounted boot.mount - /boot.
```

- <mark style="background: #D2B3FFA6;">systemctl stop</mark> unmounts the partition
```bash ln:False
$ sudo systemctl stop /boot
● boot.mount - /boot
     Loaded: loaded (/etc/fstab; generated)
     Active: inactive (dead) since Fri 2024-11-16 21:46:57 UTC; 10s ago
      Where: /boot
       What: /dev/sda2
       Docs: man:fstab(5)
             man:systemd-fstab-generator(8)
      Tasks: 0 (limit: 4556)
     Memory: 104.0K (peak: 576.0K)
        CPU: 4ms
     CGroup: /system.slice/boot.mount

Nov 15 10:46:57 ubuntu systemd[1]: Unmounting /boot...
Nov 15 10:46:57 ubuntu systemd[1]: Unmounted boot.mount - /boot.
```

> [!note] 
> The file `boot.mount` can be found in <mark style="background: #D2B3FFA6;">/run/systemd/generator</mark>