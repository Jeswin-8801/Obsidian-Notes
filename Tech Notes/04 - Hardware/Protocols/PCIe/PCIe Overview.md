---
tags: [pci,protocol]
---

</br>


<mark style="background: #CACFD9A6;">PCIe</mark> a **high-speed serial expansion bus standard** used to connect hardware devices (like GPUs, SSDs, NICs) to a computer's motherboard.

> [!note] 
> Checkout Lane Architechture at [[PCIe Lane Configurations and Slots]]

---

## 📈 PCIe Generations & Bandwidth

|PCIe Gen|Per Lane (x1)|x4 Bandwidth|x16 Bandwidth|Encoding|Notes|
|---|---|---|---|---|---|
|Gen 1|250 MB/s|1 GB/s|4 GB/s|8b/10b|Legacy|
|Gen 2|500 MB/s|2 GB/s|8 GB/s|8b/10b||
|Gen 3|~1 GB/s|~4 GB/s|~16 GB/s|128b/130b|Widely adopted|
|Gen 4|~2 GB/s|~8 GB/s|~32 GB/s|128b/130b|NVMe Gen 4 SSDs|
|Gen 5|~4 GB/s|~16 GB/s|~64 GB/s|128b/130b|AI, HPC, servers|
|Gen 6|~8 GB/s|~32 GB/s|~128 GB/s|**PAM4 (Pulse-Amplitude Modulation)**|2024+, not backward compatible electrically|

> [!note] 
> Gen 6 drops traditional NRZ encoding in favor of **PAM4** for double data rates.

</br>

---

## 🔌 PCIe Form Factors

|Form Factor|Used In|Notes|
|---|---|---|
|**Add-in Card**|Desktops, servers|Full/half height/length|
|**M.2 (NGFF)**|Laptops, desktops|Up to x4 lanes, compact|
|**U.2 (SFF-8639)**|Enterprise SSDs|Hot-swappable, often x4|
|**EDSFF (E1/E3)**|Data centers|Next-gen hot-swappable form factors|
|**Mini PCIe / mPCIe**|Embedded/legacy laptops|Based on Gen 1/2|

</br>

---

## 🛠 Key PCIe Features

- **Hot-Plug Support**
- **Link Negotiation**: Devices can train for fewer lanes than available (e.g., x1 on x16 slot).
- **Power Management**:
    - **L0s, L1, L1.1, L1.2**: Low power link states
    - **ASPM** (Active State Power Management)
- **Peer-to-peer support**: Devices can talk without CPU involvement (useful for AI/GPUs). 

</br>

---

## 🧬 PCIe Layers

PCIe uses a layered architecture similar to the OSI model:

```yaml ln:False
+---------------------------+
|   Transaction Layer       | ◄─ High-level communication (packets)
+---------------------------+
|     Data Link Layer       | ◄─ Reliable data delivery (ACK/NAK, CRC)
+---------------------------+
|     Physical Layer        | ◄─ Electrical signaling (bit transmission)
+---------------------------+
```

1. **Transaction Layer**: Handles read/write requests and completions.
2. **Data Link Layer**: Adds CRC and ensures reliable delivery.
3. **Physical Layer**: Converts bits to signals over wires (includes electrical signaling, encoding, equalization).

</br>
Example Packet flow:

- **Transaction Layer:** NVMe creates a write request (TLP).
> ⠀
- **Data Link Layer:** Adds CRC and control header.
> ⠀
- **Physical Layer:** Encodes and transmits bits over PCIe lanes.
> ⠀ 
- **CPU Physical Layer:** Receives and decodes bits.
> ⠀
- **Data Link Layer:** Validates CRC, sends ACK.
> ⠀
- **Transaction Layer:** Passes payload to the CPU/memory.

</br>


> [!info] 
> Also checkout [[PCI devices]]

---

#### Youtube

1. [PCI Express Physical Layer](https://youtu.be/EHkuzkNWXFk?si=4P05aOtlXT74CfKC)
2. [Linux and PCIe (Playlist)](https://www.youtube.com/watch?v=E3p0DXmRSV4&list=PLCGpd0Do5-I1hZpk8zi9Zh7SCnHrIQlgT)
3. [PCIe Architecture](https://youtube.com/@pcie3823?si=t6EcHhgMjVJGGAEi)


