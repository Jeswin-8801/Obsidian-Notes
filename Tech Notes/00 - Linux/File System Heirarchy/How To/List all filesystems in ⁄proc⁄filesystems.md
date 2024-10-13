
### **Step 1**

```bash
~$ cat /proc/filesystems
nodev   sysfs
nodev   tmpfs
nodev   bdev
nodev   proc
.
.
.
```

### **Step 2**

```bash
~$ cat /proc/filesystems | tr '\t' ','
nodev,sysfs
nodev,tmpfs
nodev,bdev
nodev,proc
.
.
.
```

### **Step 3**

```bash
~$ cat /proc/filesystems | tr '\t' ',' | cut -d ',' -f 2
sysfs
tmpfs
bdev
proc
.
.
.
```

### **Step 4**

```bash
~$ cat /proc/filesystems | tr '\t' ',' | cut -d ',' -f 2 | xargs
sysfs tmpfs bdev proc cgroup cgroup2 cpuset devtmpfs configfs debugfs tracefs securityfs sockfs bpf pipefs ramfs hugetlbfs devpts ext3 ext2 ext4 squashfs vfat ecryptfs fuseblk fuse fusectl efivarfs mqueue pstore btrfs autofs binfmt_misc
```
