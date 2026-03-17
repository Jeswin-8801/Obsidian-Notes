
</br>

List USB devices

```shell ln:False
$ lsusb
Bus 001 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 001 Device 002: ID 0e0f:0003 VMware, Inc. Virtual Mouse
Bus 001 Device 003: ID 0e0f:0002 VMware, Inc. Virtual USB Hub
Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```

> Here, ID displays [Vendor Id:Product Id]

> The `-v` flag can be used to show verbose information

---

</br>

#### Show info for specific devices

> By specifying [Bus Id:Device Id]
- using the `-s` flag
```shell ln:False
$ lsusb -s 001:001
Bus 001 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
```

- Display all devices with specific Bus Id
```shell ln:False
$ lsusb -s 001
Bus 001 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```

- Display all devices with specific Vendor Id
```shell ln:False
$ lsusb -d 1d6b:
Bus 001 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```
> Remember to add `:` after

---

</br>

#### Show Output as a Tree

```shell ln:False
$ lsusb -t
/:  Bus 001.Port 001: Dev 001, Class=root_hub, Driver=uhci_hcd/2p, 12M
    |__ Port 001: Dev 002, If 0, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 002: Dev 003, If 0, Class=Hub, Driver=hub/7p, 12M
/:  Bus 002.Port 001: Dev 001, Class=root_hub, Driver=ehci-pci/6p, 480M
```

---

</br>

> [[List all ls commands|Checkout other ls commands]]