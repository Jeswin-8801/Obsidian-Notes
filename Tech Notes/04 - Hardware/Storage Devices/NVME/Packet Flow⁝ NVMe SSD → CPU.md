---
tags: [nvme,pci]
---

</br>


```yaml ln:False
+---------------------------+
|  NVMe SSD (Endpoint)      |
|  - Generates data packet  |
+------------+--------------+
             |
             v
+---------------------------------------------+
|  Transaction Layer                          |
|  - Formats a TLP (Transaction Layer Packet) |
+------------+--------------------------------+
             |
             v
+-----------------------------+
|  Data Link Layer            |
|  - Adds Sequence Number     |
|  - Adds CRC for error check |
+------------+----------------+
             |
             v
+-----------------------------------------------+
|  Physical Layer                               |
|  - Encodes signal (e.g., 128b/130b for Gen3+) |
|  - Converts to serial bits                    |
+------------+----------------------------------+
             |
             v
============PCIe Lane(s)===========
| x4 lanes (full-duplex, serial)  |
===================================
             |
             v
+--------------------------------+
|  Root Complex (CPU or Chipset) |
+------------+-------------------+
             |
             v
+---------------------------+
|  Physical Layer           |
|  - Decodes signal         |
+------------+--------------+
             |
             v
+---------------------------+
|  Data Link Layer          |
|  - Verifies CRC           |
|  - Sends ACK/NAK          |
+------------+--------------+
             |
             v
+---------------------------+
|  Transaction Layer        |
|  - Delivers payload to    |
|    memory or processor    |
+---------------------------+
```

> [!info] 
> Checkout => [[PCIe Overview#**Layered Architecture (Protocol Stack)**]]


|Stage|Function|
|---|---|
|**Endpoint (NVMe SSD)**|Prepares data to send using PCIe protocol.|
|**Transaction Layer**|Encapsulates payload (e.g., read response) in a TLP.|
|**Data Link Layer**|Adds error checking and sequence control.|
|**Physical Layer**|Converts data into electrical signals over PCIe lanes.|
|**Root Complex**|Receives, verifies, and decodes the data.|
|**CPU/Memory**|Uses the data for application or OS needs.|
