---
tags: How-To
---


# using <mark style="background: #CACFD9A6;">blkid</mark>

```bash ln:False
$ blkid /dev/sda2
/dev/sda2: UUID="e28f5bc5-7f07-4255-9449-eb8c4b5ffc3e" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="8b21a4e4-1d4f-4ddb-aa72-764fe269e0ef"
```

</br>

# using <mark style="background: #CACFD9A6;">lsblk</mark>

- the <mark style="background: #D2B3FFA6;">-f</mark> flag outputs info about filesystems
```bash ln:False
$ lsblk -f
NAME FSTYPE FSVER LABEL                           UUID                                   FSAVAIL FSUSE% MOUNTPOINTS
sda
├─sda1
│
├─sda2
│    ext4   1.0                                   e28f5bc5-7f07-4255-9449-eb8c4b5ffc3e      1.5G     5% /boot
└─sda3
```

</br>

# using <mark style="background: #CACFD9A6;">[[tune2fs]]</mark>

```bash ln:False
$ sudo tune2fs -l /dev/sda2 | grep -i uuid
Filesystem UUID:          e28f5bc5-7f07-4255-9449-eb8c4b5ffc3e
```
