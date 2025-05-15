---
tags: [protocols]
---

</br>

## 📦 **Storage Protocols (like NVMe)**

|Protocol|Transport Layer|Usage|Notes|
|---|---|---|---|
|<mark style="background: #D2B3FFA6;">[[NVMe]]</mark>|PCIe|SSDs|High-speed, low-latency storage protocol designed for flash and future memory|
|<mark style="background: #CACFD9A6;">**AHCI**</mark>|SATA|HDD/SSDs|Legacy interface for spinning disks and early SSDs|
|<mark style="background: #CACFD9A6;">**SCSI**</mark>|Parallel or SAS|HDDs, enterprise|Command set for managing block storage devices|
|<mark style="background: #CACFD9A6;">**SAS**</mark>|Serial (SCSI)|Enterprise HDD/SSD|Faster, full-duplex version of SCSI, hot-swappable|
|<mark style="background: #CACFD9A6;">**UFS**</mark>|M-PHY/UniPro|Phones, embedded|Universal Flash Storage, used in mobile devices|
|<mark style="background: #CACFD9A6;">**eMMC**</mark>|Parallel/MMC|Embedded|Slower, cheaper storage for embedded/mobile|
|<mark style="background: #CACFD9A6;">**ZNS (Zoned Namespace)**</mark>|NVMe over PCIe|Advanced SSDs|NVMe variant optimized for large-scale, zoned storage|
|<mark style="background: #CACFD9A6;">**SMR (Shingled Magnetic Recording)**</mark>|SATA/SAS|HDDs|Sequential writing zones to increase HDD density|

</br>

---

## 🔌 **Interface Buses (like PCIe and PCI)**

|Protocol|Type|Notes|
|---|---|---|
|<mark style="background: #D2B3FFA6;">[[PCI Configuration Space\|PCI]]</mark>|Parallel bus|Legacy interface, replaced by PCIe|
|<mark style="background: #D2B3FFA6;">[[PCIe]]</mark>|Serial point-to-point|High-speed, scalable, used in GPUs, SSDs, NICs|
|<mark style="background: #CACFD9A6;">**USB**</mark>|Serial bus|General-purpose peripheral interconnect|
|<mark style="background: #CACFD9A6;">**Thunderbolt**</mark>|Serial bus (based on PCIe + DisplayPort)|High-speed external I/O for storage, graphics, docks|
|<mark style="background: #CACFD9A6;">**SATA**</mark>|Serial|Storage interface for HDDs/SSDs|
|<mark style="background: #CACFD9A6;">**SAS**</mark>|Serial|Enterprise-grade storage with higher speed and reliability|
|<mark style="background: #CACFD9A6;">**CXL (Compute Express Link)**</mark>|Built on PCIe|Next-gen memory and device interconnect for CPUs, GPUs, accelerators|
|<mark style="background: #CACFD9A6;">**M.2**</mark>|Form factor, uses PCIe/SATA|Connector for SSDs, WiFi, etc.|
|<mark style="background: #CACFD9A6;">**U.2**</mark>|Connector for PCIe-based SSDs|Often used in servers with NVMe drives|

</br>

---

## 🌐 **Networking & Interconnect Protocols**

|Protocol|Type|Notes|
|---|---|---|
|<mark style="background: #CACFD9A6;">**Ethernet**</mark>|Packet-switched|Standard for LAN/WAN, also used in storage (iSCSI, NFS)|
|<mark style="background: #CACFD9A6;">**InfiniBand**</mark>|High-performance interconnect|Used in HPC, low-latency networking|
|<mark style="background: #CACFD9A6;">**Fibre Channel (FC)**</mark>|Storage networking|Enterprise SANs, high-speed, reliable|
|<mark style="background: #CACFD9A6;">**iSCSI**</mark>|Storage over TCP/IP|SCSI commands sent over IP networks|
|<mark style="background: #CACFD9A6;">**RDMA (RoCE/iWARP)**</mark>|Direct memory access over network|Used in high-speed data centers|