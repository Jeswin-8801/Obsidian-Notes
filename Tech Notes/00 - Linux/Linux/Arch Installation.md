</br>

## SHELL

```shell ln:False
$ echo $SHELL
/usr/bin/zsh
```

---
## Check network connection

```bash ln:False
$ ping -c 3 archlinux.org
```

#### Enable network time Protocols
- enable NTP and allow the system to update the time via the Internet
```bash ln:False
timedatectl set-ntp true
```

- check NTP service status
```bash ln:False
$ timedatectl status
               Local time: Sat 2024-11-02 18:58:47 UTC
           Universal time: Sat 2024-11-02 18:58:47 UTC
                 RTC time: Sat 2024-11-02 18:58:47
                Time zone: UTC (UTC, +0000)
System clock synchronized: yes
              NTP service: active
          RTC in local TZ: no
```

> list available interfaces using [[ip#`ip link`|ip link]]

If not connected:
- setup wi-fi using `iwctl`
```bash ln:False
$ iwctl
NetworkConfigurationEnabled: disabled
StateDirectory: /var/lib/iwd
Version: 2.22
[iwd]# device list
                                    Devices                                   *
--------------------------------------------------------------------------------
  Name                  Address               Powered     Adapter     Mode
--------------------------------------------------------------------------------
  wlan0                 14:f6:d8:9b:f2:f3     on          phy0        station


[iwd]# station wlan0 scan
[iwd]# station wlan0 get-networks
                               Available Networks                               
--------------------------------------------------------------------------------
      Network Name                      Security            Signal              
--------------------------------------------------------------------------------
  >   conhem_87C                        psk                 ****
      conhem_87C-5G                     psk                 ****

[iwd]# station wlan0 connect conhem_87C
Type the network passphrase for conhem_87C psk
Passphrase: ***********
[iwd]# exit

[iwd]# 
```

---

## Partition

- List the available partitions and disks:
```shell ln:False
$ lsblk
NAME  MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
loop0   7:0    0 794.4M  1 loop /run/archiso/airootfs
sda     8:0    0    12G  0 disk
sr0    11:0    1   1.1G  0 rom  /run/archiso/bootmnt
```

- if several hard drives are present use `fdisk` to list them
```shell ln:False
$ fdisk -l
Disk /dev/sda: 12 GiB, 12884901888 bytes, 25165824 sectors
Disk model: VMware Virtual S
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/loop0: 794.42 MiB, 833007616 bytes, 1626968 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
```
> [!info] 
> <mark style="background: #ABF7F7A6;">/dev/sda</mark>
> 
> - **<mark style="background: #FFB86CA6;color: black">Type</mark>**
> 	Physical storage device
> 
> - **<mark style="background: #FFB86CA6;color: black">Example</mark>**
> 	Hard drives, SSDs
> 
> - **<mark style="background: #FFB86CA6;color: black">Usage</mark>**
> 	Represents an entire disk or partitioned drives (e.g., /dev/sda1, /dev/sda2)
> 
> - **<mark style="background: #FFB86CA6;color: black">Common Operations</mark>**
> 	Formatting, partitioning, mounting
> 
> <mark style="background: #ABF7F7A6;">/dev/loop0</mark>
> 
> - **<mark style="background: #FFB86CA6;color: black">Type</mark>**
> 	Loopback device
> 
> - **<mark style="background: #FFB86CA6;color: black">Example</mark>**
> 	Disk images (ISO files)
> 
> - **<mark style="background: #FFB86CA6;color: black">Usage</mark>**
> 	Used to mount files as if they were disks
> 
> - **<mark style="background: #FFB86CA6;color: black">Common Operations</mark>**
> 	Mounting disk images, creating virtual file systems

> Checkout Partition disks using [[fdisk]]
#### Using `cfdisk`

```shell ln:False
$ cfdisk /dev/sda
```

- select **<mark style="background: #ABF7F7A6;">gpt</mark>**
```shell ln:False title:next
┌ Select label type ───┐
│ gpt                  │
│ dos                  │
│ sgi                  │
│ sun                  │
└──────────────────────┘
Select a type to create a new label, press 'L' to load script file, 'Q' quit
```

```shell ln:False title:next
                               Disk: /dev/sda
             Size: 12 GiB, 12884901888 bytes, 25165824 sectors
        Label: gpt, identifier: 443A2601-7BED-4E59-B00E-5383FB8C2F87

    Device             Start          End      Sectors     Size Type
>>  Free space          2048     25165790     25163743      12G


         [   New  ]  [  Quit  ]  [  Help  ]  [  Write ]  [  Dump  ]


                    Create new partition from free space
```
Use arrow keys to create partitions
- <mark style="background: #BBFABBA6;">/dev/sda1</mark>
	choose 512Mb of space (UEFI)
- <mark style="background: #BBFABBA6;">/dev/sda2</mark>
	choose at least 10 GB of space (root)
- <mark style="background: #BBFABBA6;">/dev/sda3</mark>
	choose all the left space (home)
```shell ln:False title:after_defining
                               Disk: /dev/sda
             Size: 12 GiB, 12884901888 bytes, 25165824 sectors
        Label: gpt, identifier: FB7C7827-CF50-465A-B25D-0D4341DDE608

    Device            Start        End    Sectors    Size Type
    /dev/sda1          2048    1050623    1048576    512M EFI System
    /dev/sda2       1050624   17827839   16777216      8G Linux filesystem
>>  /dev/sda3      17827840   25163775    7335936    3.5G Linux filesystem

 ┌────────────────────────────────────────────────────────────────────────┐
 │Partition UUID: A09CE8FF-5178-4C69-BE30-781BC804A94D                    │
 │Partition type: Linux filesystem (0FC63DAF-8483-4772-8E79-3D69D8477DE4) │
 └────────────────────────────────────────────────────────────────────────┘
   [ Delete ]  [ Resize ]  [  Quit  ]  [  Type  ]  [  Help  ]  [  Write ]
   [  Dump  ]
```
> [!note] 
> Use `[Type]` to select the Partition type for (==EFI==)

- List all partitions
```shell ln:False
$ fdisk -l | awk '/^Device|^\/dev/ { printf "%-12s %-12s %-12s %-12s %-12s\n", $1, $2, $3, $4, $5 }'
Device       Start        End          Sectors      Size
/dev/sda1    2048         1050623      1048576      512M
/dev/sda2    1050624      22022143     20971520     10G
/dev/sda3    22022144     25163775     3141632      1.5G
```
*OR*
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

---
## Formatting

> Checkout [[mkfs]]

```bash ln:False
$ mkfs.fat -F32 /dev/sda1
mkfs.fat 4.2 (2021-01-31)
```

> [!important] 
> The first partition -> <mark style="background: #ABF7F7A6;">UEFI</mark>
> needs to be formatted with a ==FAT== file system

The other two partitions can be formatted in any Linux file system

```bash ln:False
$ mkfs.ext4 /dev/sda2
mke2fs 1.47.1 (20-May-2024)
Creating filesystem with 2621440 4k blocks and 655360 inodes
Filesystem UUID: fb9439fb-0ef1-4740-aa24-4014237c95e2
Superblock backups stored on blocks:
        32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632

Allocating group tables: done
Writing inode tables: done
Creating journal (16384 blocks): done
Writing superblocks and filesystem accounting information: done
```

```bash ln:False
$ mkfs.ext4 /dev/sda3
mke2fs 1.47.1 (20-May-2024)
...(Truncated)
```

---

## Mounting

> Mount the root partition

```bash ln:False
$ mount /dev/sda2 /mnt
```

> Create a folder to mount the <mark style="background: #ABF7F7A6;">home</mark> partition and mount it

```bash ln:False
$ mkdir /mnt/home
$ mount /dev/sda3 /mnt/home
```

- Check mountpoints
```bash ln:False
$ lsblk
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
loop0    7:0    0 794.4M  1 loop /run/archiso/airootfs
sda      8:0    0    12G  0 disk
├─sda1   8:1    0   512M  0 part
├─sda2   8:2    0    10G  0 part /mnt
└─sda3   8:3    0   1.5G  0 part /mnt/home
sr0     11:0    1   1.1G  0 rom  /run/archiso/bootmnt
```

---
## Check Mirror List for an Appropriate Mirror

- Sync the <mark style="background: #ABF7F7A6;">pacman</mark> repository

```bash ln:False
$ pacman -Syy
:: Synchronizing package databases...
 core                            116.8 KiB   942 KiB/s 00:00 [################################] 100%
 extra                             7.5 MiB  36.2 MiB/s 00:00 [################################] 100%
```

- Install **reflector** to be able to update the mirrors and sort them by download speed.

```bash ln:False
$ pacman -S reflector
warning: reflector-2023-2 is up to date -- reinstalling
resolving dependencies...
looking for conflicting packages...

Packages (1) reflector-2023-2

Total Download Size:   0.04 MiB
Total Installed Size:  0.15 MiB
Net Upgrade Size:      0.00 MiB

:: Proceed with installation? [Y/n] Y
:: Retrieving packages...

(... Truncated)
```

> [!note]
> If necessary create a backup of the mirror list:
> ```bash ln:False
> cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak
> ``` 

- Use ==reflector== to update the mirror list
```bash ln:False
$ reflector -c "IN" -f 12 -l 10 -n 12 --save /etc/pacman.d/mirrorlist
```

---
## Install Arch Linux

```bash ln:False
$ pacstrap /mnt base linux linux-firmware nano
==> Creating install root at /mnt
==> Installing packages to /mnt
:: Synchronizing package databases...

(... Truncated)
```

---

## Configure Arch Linux

#### Generate `fstab` file

> Checkout [[fstab]]

```bash ln:False
$ genfstab -U -p /mnt >> /mnt/etc/fstab
```

```bash ln:False
$ cat /mnt/etc/fstab
# Static information about the filesystems.
# See fstab(5) for details.

# <file system> <dir> <type> <options> <dump> <pass>
# /dev/sda2
UUID=fb9439fb-0ef1-4740-aa24-4014237c95e2       /               ext4            rw,relatime     0 1

# /dev/sda3
UUID=99becabb-0fe2-4427-92f1-cf0c1913a768       /home           ext4            rw,relatime     0 2
```

#### Chroot into the installed system

```shell ln:False
arch-chroot /mnt
```

#### Set Locale

```bash ln:False
$ nano /etc/locale.gen
```
- uncomment `#en_US.UTF-8 UTF-8`
> Search using `Ctrl + W`
> Save using `Ctrl + O` + `Enter`
> Exit using `Ctrl + X`

- Generate locale using `locale-gen`
```bash ln:False
$ locale-gen
Generating locales...
  en_US.UTF-8... done
Generation complete.
```

- create the `locale.conf` with the corresponding language setting
```bash ln:False
echo "LANG=en_US.UTF-8" > /etc/locale.conf
```

```bash ln:False
export LANG=en_US.UTF-8
```

#### Set the Timezone

- Find timezones
```bash ln:False
$ find /usr/share/zoneinfo -name "Kolkata"
/usr/share/zoneinfo/posix/Asia/Kolkata
/usr/share/zoneinfo/Asia/Kolkata
/usr/share/zoneinfo/right/Asia/Kolkata
```

- create a symbolic link from your desired timezone to `/etc/localtime`
```bash ln:False
ln -sf /usr/share/zoneinfo/Asia/Kolkata /etc/localtime
```

#### Set hostname
- Setting hostname to arch
```bash ln:False
echo arch > /etc/hostname
```

```bash ln:False
nano /etc/hosts
```
> add the following lines
```text
127.0.0.1	localhost
::1		localhost
127.0.1.1	[your_hostname]
```
> remember to change the hostname set above in `/etc/hosts`

#### Enable Network

- install network manager
```bash ln:False
pacman -S networkmanager
```

- enable

```bash ln:False
$ systemctl enable NetworkManager
Created symlink '/etc/systemd/system/multi-user.target.wants/NetworkManager.service' → '/usr/lib/systemd/system/NetworkManager.service'.
Created symlink '/etc/systemd/system/dbus-org.freedesktop.nm-dispatcher.service' → '/usr/lib/systemd/system/NetworkManager-dispatcher.service'.
Created symlink '/etc/systemd/system/network-online.target.wants/NetworkManager-wait-online.service' → '/usr/lib/systemd/system/NetworkManager-wait-online.service'.
```

#### Set root password

> Checkout [[passwd]]


---

## Install GRUB Bootloader (<mark style="background: #BBFABBA6;">UEFI System</mark>)



- Install the GRUB bootloader and EFI boot manager packages
```bash ln:False
pacman -S grub efibootmgr
```

- mount
```bash ln:False
$ mkdir /boot/efi
$ mount /dev/sda1 /boot/efi
$ lsblk
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
loop0    7:0    0 794.4M  1 loop
sda      8:0    0    12G  0 disk
├─sda1   8:1    0   512M  0 part /boot/efi
├─sda2   8:2    0    10G  0 part /
└─sda3   8:3    0   1.5G  0 part /home
sr0     11:0    1   1.1G  0 rom
```

- install grub
```bash ln:False
grub-install --target=x86_64-efi --bootloader-id=GRUB --efi-directory=/boot/efi
```

- create a GRUB configuration file
```bash ln:False
grub-mkconfig -o /boot/grub/grub.cfg
```

---

## Create a new User

```bash ln:False
pacman -S sudo
```

- Creating a new user
```bash ln:False
useradd -m jeswins
```

- setting password for `jeswins`
```bash ln:False
passwd jeswins
```

- add to group
```bash ln:False
usermod -aG wheel,audio,video,storage jeswins
```

- edit `visudo` file
```bash ln:False
EDITOR=nano visudo
```

> uncomment `# %wheel ALL=(ALL) ALL`


---

## Exit Arch-Chroot Environment and Reboot

```bash ln:False
$ exit
$ umount -f /mnt
$ sudo reboot
```