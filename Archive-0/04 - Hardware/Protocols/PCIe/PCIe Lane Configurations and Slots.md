---
tags: [pci]
---

</br>

A **PCIe lane** is a **bi-directional data path** made of **two pairs of wires**:

- 1 pair for <mark style="background: #CACFD9A6;">**transmit (Tx)**</mark>
    
- 1 pair for <mark style="background: #CACFD9A6;">**receive (Rx)**</mark>

> Each lane carries data independently and in parallel.


---

## 🔢 Common PCIe Lane Configurations

|Lane Count|Written As|Typical Use|
|---|---|---|
|1 lane|**x1**|NICs, USB expansion cards|
|4 lanes|**x4**|NVMe SSDs, RAID cards|
|8 lanes|**x8**|High-end RAID/NICs, GPUs (occasionally)|
|16 lanes|**x16**|Graphics cards (standard)|

> PCIe **slots and devices must negotiate lanes** — a device can operate with fewer lanes if the system supports it.

---

## 🛠 PCIe Slot Sizes

|Slot Size|Physical Length|Maximum Lanes Supported|Typical Use|
|---|---|---|---|
|**x1**|Short|1 lane|Low-bandwidth devices|
|**x4**|Medium|Up to 4 lanes|SSDs, small GPUs|
|**x8**|Long|Up to 8 lanes|Network/storage cards|
|**x16**|Longest|Up to 16 lanes|GPUs, AI accelerators|

> [!attention] **Slot size ≠ lane count always!**  
> A **x16 slot** may only be wired for **x4** or **x8** electrically — depends on motherboard & chipset.

---

## 🧪 Examples

|Device|Typical Slot|Lane Usage|
|---|---|---|
|GPU (RTX 4090)|x16 slot|x16 lanes|
|NVMe SSD (M.2)|M.2 (x4 PCIe)|x4 lanes|
|10Gb NIC|x4 or x8 slot|x4 lanes|
|Sound card|x1 slot|x1 lane|