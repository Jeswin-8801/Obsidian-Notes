`mkfs` stands for "<mark style="background: #ABF7F7A6;">make filesystem</mark>". It's used to format a storage device with a specific filesystem type.

For example, if you wanted to format a partition with the ==ext4== filesystem, you'd use:

```bash ln:False
sudo mkfs.ext4 /dev/sdXn
```

Where `/dev/sdXn` is your target partition. There are different options for other filesystems like `mkfs.fat` for FAT, `mkfs.xfs` for XFS, etc.

---
## `mkfs.fat`

`mkfs` can be used to create FAT12, FAT16, and FAT32 filesystems on `/dev/sda1` (example) based on the size of the partition:

- **FAT12**

```bash ln:False
sudo mkfs.fat -F 12 /dev/sda1
```

- **FAT16**

```bash ln:False
sudo mkfs.fat -F 16 /dev/sda1
```

- **FAT32**

```bash ln:False
sudo mkfs.fat -F 32 /dev/sda1
```