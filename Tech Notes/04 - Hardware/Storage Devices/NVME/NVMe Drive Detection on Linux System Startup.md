---
tags: [nvme,linux]
---

</br>

> [!info] 
> Checkout [[NVMe]]

</br>

## Entities Involved

|Entity|Role|
|---|---|
|BIOS/UEFI|Boot-time PCI enumeration, config space and BAR allocation|
|PCI Bus|Transport layer for config and MMIO communication|
|PCI Config Space|Holds device IDs, BARs, capabilities, interrupt lines|
|BARs|Mapped memory regions for MMIO access (registers, queues)|
|Kernel|Re-probes PCI, binds drivers, maps BARs|
|Driver|Sends admin commands, interprets responses, sets up I/O subsystem|
|NVMe ASIC|Executes NVMe command set, allocates queues, processes MMIO commands|
|NVMe Drive (device)|Contains NVMe ASIC, DRAM/cache, NAND, firmware|

</br>

## System Power On Sequence

<mark style="background: #FFB86CA6;">[Power On]</mark>
```text ln:False
|
v
```
<mark style="background: #FFB86CA6;">[Bios / UEFI]</mark>
> Refer: [[Boot Process]]
>   - <mark style="background: #CACFD9A6;">Initiates POST</mark>
>	- Verifies basic CPU, RAM, and chipset functionality.
>	- Ensures system integrity before hardware initialization.
>   - <mark style="background: #CACFD9A6;">Enumerates PCI bus</mark>
>	- Scans PCI buses starting from Bus 0.
>	- Walks through each possible Device (0–31) and Function (0–7).
>	> Refer => [[PCI Addressing]]
>   - <mark style="background: #CACFD9A6;">Reads Vendor ID / Device ID from each PCI device (via PCI config space)</mark>
>	- Issues configuration read cycles to check for devices.
>	- *Also Reads:*
>		- *Class Code* (e.g., 0x0108 for NVMe mass storage)
>		- *Header Type*, *Capabilities*
>   - <mark style="background: #CACFD9A6;">Allocates Bus Numbers and Device/Function Numbers</mark>
>	- Assigns **Bus Number** for PCI bridges and downstream buses.
>	- Assigns **Device/Function Number** uniquely per bus.
>	- Ensures a globally unique path for each PCI function.
>   - <mark style="background: #CACFD9A6;">Initializes PCI Config Space</mark>
>   - <mark style="background: #CACFD9A6;">Assigns BARs for MMIO space</mark>
> 	- **BARs** are registers in PCI/PCIe devices that define where the device’s **memory or I/O regions** are mapped in the system address space.   
> 	- **MMIO (Memory-Mapped I/O)** address ranges — device registers mapped into CPU memory space.
>   - <mark style="background: #CACFD9A6;">Sets up basic interrupt routing</mark>
```text ln:False
|
v
```
<mark style="background: #FFB86CA6;">[PCI Bus]</mark>
 >  - Acts as a transport layer to access PCI devices
```text ln:False
|
v
```
<mark style="background: #FFB86CA6;">[PCI NVMe Drive]</mark>
>   - Responds with its IDs and capabilities through Config Space
>   - Exposes Base Address Registers (BARs) for MMIO
>   - Registers class code: 0x01 (Mass Storage) / 0x08 (Non-Volatile Memory)
```text ln:False
|
v
```
<mark style="background: #FFB86CA6;">[PCI Config Space]</mark>
>   - Contains device identity and control fields
>   - Firmware partially initializes it (addressing, BARs)

</br>

---

### Kernel Initialization

```markdown ln:False
[Kernel PCI Subsystem]
   - Probes all PCI devices
   - Reads PCI Config Space via MMIO or I/O ports
   - Maps BARs into kernel virtual memory space
   - Matches device class/vendor ID to a driver (e.g., nvme.ko)
   - Passes control to the appropriate driver
   |
   v
[NVMe Driver]
   - Initializes admin queue using MMIO BARs
   - Issues admin commands to controller (identify, get features, etc.)
   |
   v
[NVMe ASIC (inside the drive)]
   - Executes commands sent via MMIO (e.g., doorbell registers, queue heads)
   - Returns controller metadata (model, firmware, namespace info)
   - Allocates internal resources (queues, DMA mappings, tag pools)
   - Maps NVMe queues to physical DRAM/cache on the drive
   - Responds via Completion Queue entries and Interrupts
   |
   v
[Driver -> Kernel]
   - Registers block device (/dev/nvme0n1)
   - Exposes device info via sysfs (/sys/class/nvme/)

```

### NVMe ASIC Behavior

```markdown ln:False
[Driver sends Identify Controller cmd] --> [MMIO Write via BAR]
   |
   v
[NVMe ASIC]
   - Parses command from Submission Queue
   - Looks up command type in firmware
   - Reads from internal Flash (e.g., namespace info)
   - Writes result to Completion Queue
   - Triggers MSI-X interrupt to CPU

[Driver receives interrupt]
   |
   v
[Driver reads Completion Queue] --> [Parses result] --> [Continues init process]

```
