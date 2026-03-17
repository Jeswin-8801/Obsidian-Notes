---
tags: Formatting
---


</br>

The <mark style="background: #D2B3FFA6;">mke2fs</mark> command in Linux is used to create a new file system with support only for ==ext2==, ==ext3==, and ==ext4== file systems.

- creates a default ext2 file system on the partition `/dev/sdX1`
```bash ln:False
sudo mke2fs /dev/sdX1
```

> It is the same as <mark style="background: #D2B3FFA6;">[[mkfs]]</mark> that specifies the ext file system.

