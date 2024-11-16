
Used to list mountpoints and filesystems on linux.

```bash ln:False
findmnt <device|mountpoint>
```

```bash ln:False
$ findmnt /dev/sda2
TARGET
      SOURCE    FSTYPE OPTIONS
/boot /dev/sda2 ext4   rw,relatime
```