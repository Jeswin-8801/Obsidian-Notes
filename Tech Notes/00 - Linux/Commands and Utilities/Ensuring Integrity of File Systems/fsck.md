
**`fsck`** (<mark style="background: #ABF7F7A6;">File System Check</mark>) checks filesystems for errors or outstanding issues. The tool is used to fix potential errors and generate reports.

```bash ln:False
$ sudo fsck /dev/sdb2
fsck from util-linux 2.39.3
e2fsck 1.47.0 (5-Feb-2023)
/dev/sdb2 is mounted.
e2fsck: Cannot continue, aborting.
```

```bash ln:False
$ sudo umount /dev/sdb2
```

```bash ln:False
$ sudo fsck /dev/sdb2
fsck from util-linux 2.39.3
e2fsck 1.47.0 (5-Feb-2023)
/dev/sdb2: clean, 144,65136 files, 49982/261888 blocks
```

> [!note] 
> <mark style="background: #D2B3FFA6;">fsck</mark> cannot run on a mounted partition.
> It also cannot be run on <mark style="background: #D2B3FFA6;">xfs</mark> file systems.

[[⁄lost+found|See how fsck works when recovering files]]