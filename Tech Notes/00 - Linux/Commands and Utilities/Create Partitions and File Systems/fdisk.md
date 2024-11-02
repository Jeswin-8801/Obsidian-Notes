Used to create partitions.

- A drive needs to have at least one partition before you can format it and store files on it.

> Create (<mark style="background: #FFF3A3A6;">EFI</mark>), (<mark style="background: #FFF3A3A6;">root</mark>) and (<mark style="background: #FFF3A3A6;">home</mark>) partitions
> same as for [[Arch Installation#Using `cfdisk`]]

```shell ln:False
$ fdisk /dev/sda

Welcome to fdisk (util-linux 2.40.2).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.


Command (m for help): n
Partition number (1-128, default 1):
First sector (2048-25165790, default 2048):
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-25165790, default 25163775): +512M

Created a new partition 1 of type 'Linux filesystem' and of size 512 MiB.

Command (m for help): t
Selected partition 1
Partition type or alias (type L to list all): uefi
Changed type of partition 'Linux filesystem' to 'EFI System'.

Command (m for help): n
Partition number (2-128, default 2):
First sector (1050624-25165790, default 1050624):
Last sector, +/-sectors or +/-size{K,M,G,T,P} (1050624-25165790, default 25163775): +10G

Created a new partition 2 of type 'Linux filesystem' and of size 10 GiB.

Command (m for help): n
Partition number (3-128, default 3):
First sector (22022144-25165790, default 22022144):
Last sector, +/-sectors or +/-size{K,M,G,T,P} (22022144-25165790, default 25163775):

Created a new partition 3 of type 'Linux filesystem' and of size 1.5 GiB.

Command (m for help): w
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.
```

- list partitions
```shell ln:False
$ lsblk
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
loop0    7:0    0 794.4M  1 loop /run/archiso/airootfs
sda      8:0    0    12G  0 disk
├─sda1   8:1    0   512M  0 part
├─sda2   8:2    0    10G  0 part
└─sda3   8:3    0   1.5G  0 part
sr0     11:0    1   1.1G  0 rom  /run/archiso/bootmnt
```
