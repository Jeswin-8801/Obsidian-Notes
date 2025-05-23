---
tags: [nvme,linux]
---

</br>

> [!info] 
> Checkout [[NVMe]]

## 1. `nvme id-ctrl` — **NVMe Identify Controller**

Used to **query and display detailed information about an NVMe controller**.

```bash ln:False
$ nvme id-ctrl /dev/nvme0
NVME Identify Controller:
vid       : 0x15b7
ssvid     : 0x15b7
sn        :

... (Truncated)
```

#### Availability of Device Node

```bash ln:False
nvme id-ctrl /dev/nvme1 &>/dev/null; echo $?
```

> Output `0` denotes that the controller exists else false.

#### 🔍 **Key Fields**

|Field|Meaning|
|---|---|
|`vid`|Vendor ID (PCIe Vendor ID)|
|`ssvid`|Subsystem Vendor ID|
|`sn`|Serial number|
|`mn`|Model number|
|`fr`|Firmware revision|
|`rab`|Recommended Arbitration Burst|
|`ieee`|IEEE OUI for the manufacturer|
|`cmic`|Controller Multi-path and Namespace Sharing capabilities|
|`mdts`|Maximum Data Transfer Size (in 2^n blocks)|
|`cntlid`|Controller ID|
|`nn`|Number of namespaces supported|
|`vwc`|Volatile Write Cache (enabled/disabled)|


#### 💡 **Use Cases**

|Scenario|Why use `nvme id-ctrl`?|
|---|---|
|<mark style="background: #CACFD9A6;">Debugging NVMe issues</mark>|Check capabilities, FW version, etc.|
|<mark style="background: #CACFD9A6;">Firmware validation</mark>|Confirm correct version is running|
|<mark style="background: #CACFD9A6;">Inventory or auditing</mark>|Get SN/MN/vendor from hardware|
|<mark style="background: #CACFD9A6;">Automation scripts</mark>|Programmatically extract model/vendor info|

- Specifically extract <mark style="background: #D2B3FFA6;">max data transfer size</mark>:
	Dependencies:
	- [[jq]]
```bash ln:False
nvme id-ctrl /dev/nvme0 --output-format=json | jq -r '.mdts'
```

> Refer [[#🔍 **Key Fields**]] on more details

</br>

---

## 2. `nvme list`

List all nvme devices

```bash ln:False
$ nvme list
Node                  SN                   Model                                    Namespace Usage                      Format           FW Rev
--------------------- -------------------- ---------------------------------------- --------- -------------------------- ---------------- --------
/dev/nvme0n1                               SANDISK_*****************                1           2.10  MB /   2.10  MB      4 KiB +  0 B   1V
```

</br>

---

## 3. `nvme id-ns` - **NVME Identify Namespace**

```bash ln:False
$ nvme id-ns /dev/nvme0n1
NVME Identify Namespace 1:
nsze    : 0x200
ncap    : 0x200
nuse    : 0x200

... (Truncated)
```

</br>

---

## 4. `nvme smart-log`

```bash ln:False
$ nvme smart-log /dev/nvme0n1
Smart Log for NVME device:nvme0n1 namespace-id:ffffffff
critical_warning                        : 0
temperature                             : -18 C (255 Kelvin)
available_spare                         : 0%
available_spare_threshold               : 0%

... (Truncated)
```

