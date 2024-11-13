</br>

Lists all PCI devices.

```shell ln:False
$ lspci
00:00.0 Host bridge: Intel Corporation 440BX/ZX/DX - 82443BX/ZX/DX Host bridge (rev 01)
00:01.0 PCI bridge: Intel Corporation 440BX/ZX/DX - 82443BX/ZX/DX AGP bridge (rev 01)
00:07.0 ISA bridge: Intel Corporation 82371AB/EB/MB PIIX4 ISA (rev 08)
... (Truncated)
```

- Verbose
```shell ln:False
$ lspci -v | head
00:00.0 Host bridge: Intel Corporation 440BX/ZX/DX - 82443BX/ZX/DX Host bridge (rev 01)
        Subsystem: VMware Virtual Machine Chipset
        Flags: bus master, medium devsel, latency 0
        Kernel driver in use: agpgart-intel

00:01.0 PCI bridge: Intel Corporation 440BX/ZX/DX - 82443BX/ZX/DX AGP bridge (rev 01) (prog-if 00 [Normal decode])
... (Truncated)
```

> `-vv` and `-vvv` flags commands can be used to even more verbose information.

</br>

#### Show <mark style="background: #ABF7F7A6;">Kernel Modules</mark> as well

```shell ln:False
$ lspci -k
00:00.0 Host bridge: Intel Corporation 440BX/ZX/DX - 82443BX/ZX/DX Host bridge (rev 01)
        Subsystem: VMware Virtual Machine Chipset
        Kernel driver in use: agpgart-intel
00:07.1 IDE interface: Intel Corporation 82371AB/EB/MB PIIX4 IDE (rev 01)
        Subsystem: VMware Virtual Machine Chipset
        Kernel driver in use: ata_piix
        Kernel modules: pata_acpi
... (Truncated)
```

---

</br>

#### List all PCI devices along with their <mark style="background: #ABF7F7A6;">Vendor and Device IDs</mark>

```shell ln:False
$ lspci -nn | head
00:00.0 Host bridge [0600]: Intel Corporation 440BX/ZX/DX - 82443BX/ZX/DX Host bridge [8086:7190] (rev 01)
00:01.0 PCI bridge [0604]: Intel Corporation 440BX/ZX/DX - 82443BX/ZX/DX AGP bridge [8086:7191] (rev 01)
00:07.0 ISA bridge [0601]: Intel Corporation 82371AB/EB/MB PIIX4 ISA [8086:7110] (rev 08)
... (Truncated)
```

> Breakdown of Each Value in
> 
> ```shell ln:False
> 00:01.0 PCI bridge [0604]: Intel Corporation 440BX/ZX/DX - 82443BX/ZX/DX AGP bridge [8086:7191] (rev 01)
> ```
> 
> - <mark style="background: #FFB86CA6; color: black;">00:01.0</mark>:
>     - **==00==**: Bus number.
>     - **==01==**: Device number.
>     - **==0==**: Function number. This combination uniquely identifies the PCI device on the system.
> -  <mark style="background: #FFB86CA6; color: black;">PCI bridge [0604]</mark>:
>     - **==PCI bridge==**: The type of device (in this case, a PCI bridge).
>     - **==[0604]==**: The class code for the device type. `0604` indicates a PCI bridge.
> -  <mark style="background: #FFB86CA6; color: black;">Intel Corporation 440BX/ZX/DX - 82443BX/ZX/DX AGP bridge</mark>:
>     - **==Intel Corporation==**: The vendor name.
>     - **==440BX/ZX/DX - 82443BX/ZX/DX AGP bridge==**: The specific model and description of the device, indicating it is an AGP bridge from Intel’s 440BX/ZX/DX chipset series.
> - <mark style="background: #FFB86CA6; color: black;">[8086:7191]</mark>:
>     - ==[8086]==: The vendor ID for Intel Corporation.
>     - ==[7191]==: The device ID for this specific AGP bridge.
> - <mark style="background: #FFB86CA6; color: black;">(rev 01)</mark>:
>     - **==rev 01==**: The revision number of the device, indicating the version of the hardware.

---

</br>

#### Get Information about a Specific PCI Device
- Getting info on the GPU
```shell ln:False
$ lspci -v -s $(lspci | grep -i vga | grep -oE "^[0-9]+:[0-9a-z]+.[0-9a-z]+\b")
00:0f.0 VGA compatible controller: VMware SVGA II Adapter (prog-if 00 [VGA controller])
        Subsystem: VMware SVGA II Adapter
        Flags: bus master, medium devsel, latency 64, IRQ 16
        I/O ports at 1070 [size=16]
        Memory at e8000000 (32-bit, prefetchable) [size=128M]
        Memory at fe000000 (32-bit, non-prefetchable) [size=8M]
        Expansion ROM at 000c0000 [virtual] [disabled] [size=128K]
        Capabilities: <access denied>
        Kernel driver in use: vmwgfx
        Kernel modules: vmwgfx
```

</br>

> [[List all ls commands|Checkout other ls commands]]