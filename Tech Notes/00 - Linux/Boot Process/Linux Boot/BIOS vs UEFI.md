---
tags:
  - boot
---

</br>

**<mark style="background: #D2B3FFA6;">BIOS (Basic Input/Output System)</mark>** and **<mark style="background: #D2B3FFA6;">UEFI (Unified Extensible Firmware Interface)</mark>** are both firmware interfaces that control the boot process of a computer.

> It is the first step in a boot process.

</br>

### **<mark style="background: #ABF7F7A6;">BIOS</mark>**

BIOS is the older of the two, dating back to the 1980s.

- **<mark style="background: #FFB86CA6;color:black">Interface</mark>**: 
	Text-based interface, navigated using keyboard only.
- **<mark style="background: #FFB86CA6;color:black">Boot Process</mark>**:
	Uses the ==Master Boot Record (MBR)== to store information about the disk partitions.
- **<mark style="background: #FFB86CA6;color:black">Limitations</mark>**:
    - Supports up to 2 TB disks.
    - Can only handle up to 4 primary partitions.
    - Operates in 16-bit mode, which limits the speed and capabilities.

### **<mark style="background: #ABF7F7A6;">UEFI (Unified Extensible Firmware Interface)</mark>**

A modern replacement for BIOS, developed in the early 2000s.

- **<mark style="background: #FFB86CA6;color:black">Interface</mark>**:
	Graphical interface with mouse support, making it more user-friendly.
- **<mark style="background: #FFB86CA6;color:black">Boot Process</mark>**: 
	Uses the ==GUID Partition Table (GPT)==, which supports larger disks and more partitions.
- **<mark style="background: #FFB86CA6;color:black">Advantages</mark>**:
    - Supports disks larger than 2 TB.
    - Can handle up to 128 partitions.
    - Operates in 32-bit or 64-bit mode, allowing for faster boot times and more advanced features.
    - Includes Secure Boot, which helps prevent unauthorized software from loading during the boot process.
    - Supports networking capabilities and remote diagnostics.

---

</br>

## Key Differences

- **<mark style="background: #FFB86CA6;color:black">Boot Speed</mark>**: 
	UEFI generally offers faster boot times compared to BIOS.
- **<mark style="background: #FFB86CA6;color:black">Security</mark>**: 
	UEFI provides more robust security features, including Secure Boot.
- **<mark style="background: #FFB86CA6;color:black">Disk Support</mark>**: 
	UEFI supports larger disks and more partitions due to its use of GPT.
- **<mark style="background: #FFB86CA6;color:black">User Interface</mark>**: 
	UEFI’s graphical interface is more modern and easier to navigate compared to the text-based BIOS interface.