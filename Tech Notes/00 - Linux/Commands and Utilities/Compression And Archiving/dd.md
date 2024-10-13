Disk Dump
Used to copy directly from disk partitions.

```bash
~$ dd if=/dev/sda1 of=/dev/sdb1
```
- `if` input file
- `of` output file

copies `file1` to `file2`
```bash
$ dd if=file1.txt of=file2.txt
0+1 records in
0+1 records out
60 bytes copied, 0.000217713 s, 276 kB/s
```

- Read blocks of `512 bytes` each from /dev/sda1; here only 1 block is copied as `count` is 1
-  `bs` stands for bytes
-  Here the first 512 bytes is the partition table and is being copied
```bash
~$ sudo dd if=/dev/sda1 of=backup_bootloader bs=512 count=1
1+0 records in
1+0 records out
512 bytes copied, 0.000849879 s, 602 kB/s
```
⬇️
```bash
~$ cat backup_bootloader
R�(V�3��L^��f�-����|�tFf�f�Mf1��9�)ff�U��Df�f�L
                                               �DpP�D�B����p�hf�Ef      ���f�f1�f�4�T
f1�f�t�T
        �D
          ;���*D
���Lf�U�T
.
.
.
```
