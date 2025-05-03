
</br>

**PCI configuration space** is a special <mark style="background: #ABF7F7A6;">memory region</mark> used by <mark style="background: #ABF7F7A6;">PCI devices</mark> *(like network cards, graphics cards, etc.)* to store important information about themselves.

It consists of a standardized set of <mark style="background: #ABF7F7A6;">registers</mark>, **accessible via the host bridge**, that provide a way for the system to identify and control the PCI devices.

There are two types of configuration space:
- <mark style="background: #FFB86CA6;">type 0</mark> for endpoints
- <mark style="background: #FFB86CA6;">type 1</mark> for switches.

Both types share some common registers even though the contents of the configuration space are different.

The key registers to note are:

- <mark style="background: #FFB86CA6;">**Vendor ID**</mark>
	A 16 bit value assigned by PCI-SIG to identify a company. *Eg: Microchip’s Vendor ID is 0x1055*
	
- <mark style="background: #FFB86CA6;">**Device ID**</mark>
	A 16 bit value assigned by the vendor to identify their product. Microchip has unique Device IDs for all of their PCIe products. Consult the appropriate datasheet for the Device ID
	> [!info] 
	> Refer: [[lspci#List all PCI devices along with their <mark style="background ABF7F7A6;">Vendor and Device IDs</mark>|lspci: list PCI device Vendor and Device ID]]

- <mark style="background: #FFB86CA6;">**Header Type**</mark>
	Identifies whether it is a type 0 or type 1 config space
	
- <mark style="background: #FFB86CA6;">**Base Address Registers (BARs)**</mark>
	Indicates the position in memory the host has mapped to the PCIe device
	
- <mark style="background: #FFB86CA6;">**Capabilities pointer**</mark>
	Provides a 16 bit offset in memory to the start of the extended capabilities space. This space provides PCIe specific information about the device

#### Type 0
A type 0 configuration space is specifically used for <mark style="background: #ABF7F7A6;">PCIe endpoints</mark>, which are the terminal points of communication in the PCIe architecture.

The structure of the type 0 config space is given below:
![[Pasted image 20250503192908.png]]

#### Type 1
A type 1 config space is used for <mark style="background: #ABF7F7A6;">PCIe switches</mark>, which facilitate the transmission of messages from their upstream ports to their downstream ports.

</br>

## Configuration Space Components

The **PCI configuration space** consists of the following primary parts:

- <mark style="background: #FFB86CA6;">Legacy PCI v3.0 Type 0/1 Configuration Space Header</mark>
	- Type 0 Configuration Space Header used by <mark style="background: #ABF7F7A6;">Endpoint</mark> applications
	- Type 1 Configuration Space Header used by <mark style="background: #ABF7F7A6;">Root Port</mark> applications
	
	> [!info] 
	> <mark style="background: #D2B3FFA6;">PCI standard configuration headers</mark> are part of the PCI configuration space, which is used for initializing and configuring PCI devices.
	> The configuration space is divided into several parts, with the <mark style="background: #ABF7F7A6;">first 64 bytes</mark> being <mark style="background: #ABF7F7A6;">standardized</mark> and the remaining bytes available for vendor-specific purposes.

- <mark style="background: #FFB86CA6;">Legacy Extended Capability Items</mark>
	- PCIe Capability Item
	- Power Management Capability Item
	- Message Signaled Interrupt (MSI) Capability Item

- <mark style="background: #FFB86CA6;">PCIe Capabilities</mark>
	- Advanced Error Reporting Extended Capability Structure (AER)
	- Alternate Requester ID (ARI) (optional)
	- Device Serial Number Extended Capability Structure (DSN) (optional)
	- Single Root I/O Virtualization (SR-IOV) (optional)
	- Virtual Channel Extended Capability Structure (VC) (optional)

- <mark style="background: #FFB86CA6;">PCIe Extended Capabilities</mark>
	- Device Serial Number Extended Capability Structure (optional)
	- Virtual Channel Extended Capability Structure (optional)
	- Media Configuration Access Port (MCAP) Extended Capability Structure (optional)
