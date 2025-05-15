
</br>

CLI utilities used in Linux for interacting with PCI devices

</br>

# lspci

> Checkout <mark style="background: #D2B3FFA6;">lspci</mark> at [[lspci|Linux notes on lspci]]

- get <mark style="background: #ABF7F7A6;">root port</mark>

```bash ln:False
$ lspci -D | grep "Host bridge" | cut -d ' ' -f 1
0000:00:00.0
```

- to get a more verbose PCI information on a device

```bash ln:False
$ lsudo lspci -vvvs $(lspci | grep "Non-Volatile memory controller" | awk -F' ' '{print$1}')
01:00.0 Non-Volatile memory controller: Sandisk Corp Device 7e9a (rev 01) (prog-if 02 [NVM Express])
        Subsystem: Sandisk Corp Device 0000
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0
        Interrupt: pin A routed to IRQ 16
        IOMMU group: 8
        Region 0: Memory at e1100000 (64-bit, non-prefetchable) [size=32K]
# ...truncated
```

- display PCI device <mark style="background: #ABF7F7A6;">Vendor ID</mark> and <mark style="background: #ABF7F7A6;">Device ID</mark> as numbers

```bash ln:False
$ lspci -nvmms $(lspci | grep "Non-Volatile memory controller" | awk -F' ' '{print$1}')
Slot:   01:00.0
Class:  0108
Vendor: 15b7
Device: 7e9a
SVendor:        15b7
SDevice:        0000
Rev:    01
ProgIf: 02
IOMMUGroup:     8
```

- command to get <mark style="background: #ABF7F7A6;">Vendor ID:Device ID</mark> of a device

```bash ln:False
$ lspci -nn | grep "Non-Volatile memory controller" | awk -F' ' '{print $(NF-2)}' | sed 's/[][]//g'
15b7:7e9a
```

- display a hexadecimal dump of the whole <mark style="background: #ABF7F7A6;">PCI configuration space</mark>.

```bash ln:False
$ sudo lspci -d $(lspci -nn | grep "Non-Volatile memory controller" | awk -F' ' '{print $(NF-2)}' | sed 's/[][]//g') -xxx
01:00.0 Non-Volatile memory controller: Sandisk Corp Device 7e9a (rev 01)
00: b7 15 9a 7e 06 04 10 00 01 02 08 01 00 00 00 00
10: 04 00 10 e1 00 00 00 00 00 00 00 00 00 00 00 00
20: 00 00 00 00 00 00 00 00 00 00 00 00 b7 15 00 00
30: 00 00 00 00 40 00 00 00 00 00 00 00 0b 01 00 00
40: 01 50 c3 df 08 00 00 00 00 00 00 00 00 00 00 00
50: 05 70 8a 01 00 00 00 00 00 00 00 00 00 00 00 00
60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
70: 10 b0 02 00 e3 8f e8 17 3f 21 09 00 45 68 47 00
80: 42 01 23 10 00 00 00 00 00 00 00 00 00 00 00 00
90: 00 00 00 00 1f 08 05 00 00 04 00 00 3e 00 80 01
a0: 05 00 1e 01 00 00 00 00 00 00 00 00 00 00 00 00
b0: 11 00 ff 81 00 20 00 00 00 40 00 00 00 00 00 00
c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
```


</br>

# setpci

Used for reading from and writing to configuration registers.

- display a list of all PCI registers and capabilities. (`setpci` knows the names of all registers in the standard configuration headers; Refer: [[PCI Configuration Space#Configuration Space Components|PCI Configuration Space#Configuration Space Components]])

```bash ln:False
$ setpci --dumpregs
cap pos w name
     00 W VENDOR_ID
     02 W DEVICE_ID
     04 W COMMAND
     06 W STATUS
     08 B REVISION
     09 B CLASS_PROG
     0a W CLASS_DEVICE

# ...truncated
```

#### Reading Registers with `setpci`

When using `setpci`, you can specify the width of the data you want to read:

- <mark style="background: #FFB86CA6;">**Byte (b)**</mark>: Reads 8 bits (1 byte).
- <mark style="background: #FFB86CA6;">**Word (w)**</mark>: Reads 16 bits (2 bytes).
- <mark style="background: #FFB86CA6;">**Long Word (l)**</mark>: Reads 32 bits (4 bytes).

```text ln:False
setpci -s <bus>:<slot>.<func> <offset>.<width>
```

#### Examples

- reads the `16-bit` register at offset `0x04`
```bash ln:False
$ setpci -s 01:00.0 0x04.w
0406
```

- read <mark style="background: #ABF7F7A6;">Vendor ID</mark> and <mark style="background: #ABF7F7A6;">Device ID</mark>
```bash ln:False
$ lspci -nn | grep "Non-Volatile memory controller" | awk -F' ' '{print $(NF-2)}' | sed 's/[][]//g'
15b7:7e9a

# Vendor ID
$ setpci -s 01:00.0 0x00.w
15b7
# OR
$ setpci -s 01:00.0 VENDOR_ID
15b7

# Device ID
$ setpci -s 01:00.0 0x02.w
7e9a
# OR
$ setpci -s 01:00.0 DEVICE_ID
7e9a
```

- point to both `COMMAND` and `STATUS` register
```bash ln:False
$ setpci -s 01:00.0 COMMAND.l
00100406
$ setpci -s 01:00.0 COMMAND
0406
$ setpci -s 01:00.0 STATUS
0010
```

> [!note] 
> The values above are read in **little-endian format**, which is common in many computer systems, including those using PCI.

##### Little-endian
> Least significant byte first (e.g., `0406` is stored as `06 04`)

##### Big-endian
> Most significant byte first (e.g., `0406` would be stored as `04 06`)