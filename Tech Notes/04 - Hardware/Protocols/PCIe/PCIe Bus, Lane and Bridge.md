---
tags: [pci]
---

</br>


> [!tldr] 
> - The **PCIe lane** is **how data moves**.  
> - The **PCIe bus** is **how the system knows where to send data**.

> The **PCIe "bus"** is a **logical routing structure**, while **PCIe "lanes"** are the **physical high-speed data paths**.

</br>

## PCIe Bus

- <mark style="background: #CACFD9A6;">**Serial Bus:**</mark>
	
	PCIe uses a serial bus, sending data across a single wire (or a series of wires called lanes). 
</br>
- <mark style="background: #CACFD9A6;">**Point-to-Point:**</mark>

	Unlike traditional PCI which uses a shared bus, PCIe uses a **switched point-to-point architecture**. Each device connects directly to a switch (like a root complex) or to the CPU chipset.
	
	#### Example:
	- A GPU connects to the CPU via a PCIe x16 slot.
	- An SSD connects to the chipset via a PCIe x4 slot.
	- Both devices have their own dedicated bandwidth and don’t interfere with each other.
	```mathematica ln:False
	         CPU/Root Complex
				    |
		+----+--------------------+
		|                         |
	PCIe Switch             Integrated Links
	 |      |                     |
	GPU   NVMe SSD           Ethernet Card
	(x16)   (x4)                 (x1)
	```

#### **Switches and Bridges**

PCIe supports switches that allow multiple devices to share one root complex connection.

##### Example:

If your CPU only has 16 PCIe lanes, you can connect:
- A PCIe switch that fans out to multiple devices like SSDs or NICs.
- Each device gets some share of the 16 lanes based on priority or need.

</br>

---

## PCIe Lanes

PCIe uses [[PCIe Lanes and Slots|Lanes]] (or links) to transmit data. The number of lanes can range from 1 to 16, with more lanes providing higher bandwidth.


## Example PCIe tree

```java ln:False
CPU
├── Root Complex
│   ├── x16 Link → PCIe Switch (Upstream Port)
│   │   ├── Downstream Port 1 (x4) → NVMe SSD 1
│   │   ├── Downstream Port 2 (x4) → NVMe SSD 2
│   │   ├── Downstream Port 3 (x4) → NVMe SSD 3
│   │   └── Downstream Port 4 (x4) → NVMe SSD 4
│   │        [Total: 4 x4 links = 16 lanes]
│   │
│   └── x16 Link → GPU (x16) [Dedicated]
│
└── Chipset (PCH)
    └── x1 Link → NIC
```

`lspci -t`:
```bash ln:False
-[0000:00]--+-[01]----00.0  PCIe Switch (x16)
            |  |
            |  +-03:00.0  Non-Volatile memory controller NVMe SSD 1 (x4)
            |  +-04:00.0  Non-Volatile memory controller NVMe SSD 2 (x4)
            |  +-05:00.0  Non-Volatile memory controller NVMe SSD 3 (x4)
            |  \-06:00.0  Non-Volatile memory controller NVMe SSD 4 (x4)
            |
			+-[02]----00.0  NVIDIA Corporation GPU (x16)
            |
            \-1f:00.0  Ethernet controller NIC (x1)
```

- `[0000:00]` — Root Complex / main bus
- `[01]` — PCIe switch connected via Root Port (bus 02)
    - Under it, 4 NVMe SSD endpoints on buses 03, 04, 05, and 06 respectively
- `[02]` — GPU connected via Root Port (bus 01)   
- `1f:00.0` — NIC connected directly via chipset on main bus (bus 00)

| Component          | Connection Type                 | Lane Count   | Notes                |
| ------------------ | ------------------------------- | ------------ | -------------------- |
| **NVMe SSDs** (x4) | Through PCIe Switch             | 4 lanes each | High-speed endpoints |
| **PCIe Switch**    | x16 upstream, 4 x x4 downstream | 16 lanes     | Splits one x16 slot  |
| **GPU**            | Direct to Root Complex          | x16          | Full bandwidth       |
| **NIC**            | Connected via chipset           | x1           | Lower speed device   |

</br>

---

## **PCI Bridge**

- A **PCI bridge** (also called a PCI-to-PCI bridge) is a hardware component that connects **two PCI buses**.
    
- It **extends the PCI bus** by creating a **new secondary bus** behind it.
    
- Acts like a **traffic controller** forwarding transactions between upstream (primary) and downstream (secondary) buses.