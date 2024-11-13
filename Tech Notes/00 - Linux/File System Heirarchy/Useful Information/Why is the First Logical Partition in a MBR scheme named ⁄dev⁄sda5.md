---
tags:
  - INFO
  - Disk-Partition
  - MBR
---


**The first 4 are reserved for primary partitions**. 

Even if there are only 3 primary partitions, the first logical partition will still get the name sda5.

- Logical partitions are created within extended partitions, which are a type of primary partition that can contain multiple logical partitions. 

- Logical partitions can be formatted and assigned a drive letter. 

- The number of logical partitions that can exist on a disk is unlimited, unlike primary partitions, which are limited to four per disk.

> [!NOTE] Note
> **In the MBR scheme with 32-bit entries, we can only have a maximum disk size of 2 TB.**
> Only four primary partitions are allowed.