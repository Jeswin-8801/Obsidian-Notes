---
tags: [storage,protocol]
---

</br>

The **NVMe protocol** (<mark style="background: #D2B3FFA6;">Non-Volatile Memory express</mark>) is a **high-performance, scalable, and efficient storage interface protocol** designed to access modern **non-volatile memory (NVM)**, like **NAND flash** and **emerging storage-class memory**, over <mark style="background: #D2B3FFA6;">**PCI Express (PCIe)**</mark>.

</br>

## 🚀 NVMe at a Glance

|Feature|Value|
|---|---|
|**Full Name**|Non-Volatile Memory Express|
|**First Released**|2011|
|**Transport**|PCIe (also over Fabrics: NVMe-oF)|
|**Optimized For**|SSDs and storage-class memory (SCM)|
|**Replaces**|AHCI (used with SATA SSDs/HDDs)|
|**Latency**|Low (microseconds)|
|**Queue Depth**|64K queues × 64K commands/queue|
|**Target Systems**|PCs, servers, enterprise storage, mobile devices (via UFS/NVMe over M.2)|

## 🔁 NVMe Generational Improvements (PCIe Tie-in)

|NVMe Version|PCIe Gen|Bandwidth (x4)|Key Features|
|---|---|---|---|
|1.0 (2011)|Gen 3|~4 GB/s|Base NVMe protocol|
|1.2 (2014)|Gen 3|~4 GB/s|Power states, autonomous power|
|1.3 (2017)|Gen 3|~4 GB/s|Boot support, telemetry, streams|
|1.4 (2019)|Gen 4|~8 GB/s|Zoned Namespaces (ZNS), endurance grouping|
|2.0 (2021)|Gen 4/5|~8–16 GB/s|Modular command sets, improved SCM support|