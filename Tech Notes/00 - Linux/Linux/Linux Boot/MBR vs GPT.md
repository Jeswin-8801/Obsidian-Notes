---
tags:
  - MBR
  - GPT
  - Disk-Partition
---

They are both <mark style="background: #D2B3FFA6;">partitioning schemes</mark>.

</br>

### <mark style="background: #ABF7F7A6;">MBR (Master Boot Record)</mark>

The MBR is located at the first sector of the disk and contains the bootloader, partition table, and boot signature.

- **<mark style="background: #FFB86CA6; color: black;">Partition Limitations</mark>**: 
	Supports up to 4 primary partitions or 3 primary partitions and 1 extended partition (which can contain multiple logical partitions).
- **<mark style="background: #FFB86CA6; color: black;">Disk Size Limit</mark>**:
	Can handle disks up to 2 TB in size.
- **<mark style="background: #FFB86CA6; color: black;">Compatibility</mark>**:
	Widely supported by older systems and BIOS firmware.

</br>

### <mark style="background: #ABF7F7A6;">GPT (GUID Partition Table)</mark>

Part of the UEFI standard, designed to replace MBR.

- **<mark style="background: #FFB86CA6; color: black;">Structure</mark>**:
	Stores multiple copies of the partition table for redundancy and includes a protective MBR for backward compatibility.
- **<mark style="background: #FFB86CA6; color: black;">Partition Limitations</mark>**:
	Supports up to 128 partitions on Windows (more on other systems) without the need for extended partitions.
- **<mark style="background: #FFB86CA6; color: black;">Disk Size Limit</mark>**:
	Can handle disks larger than 2 TB, up to 9.4 ZB (zettabytes).
- **<mark style="background: #FFB86CA6; color: black;">Features</mark>**:
	Provides better data integrity with CRC32 checksums and supports larger and more partitions.

---

</br>

 > **<mark style="background: #FFB86CA6; color: black;">Data Integrity</mark>**: GPT includes CRC32 checksums for better data integrity and redundancy.

