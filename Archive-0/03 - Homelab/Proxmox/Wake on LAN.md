---
tags: [proxmox]
---

</br>

- get link name
```bash ln:False
ip link
```

```bash ln:False
sudo apt install ethtool
```

```bash ln:False
sudo ethtool eno1 | grep Wake
```

> If we get the following output for the above command:
> ```text ln:False
> Wake-on: g
> ```
> The NIC supports magic packets
> if displayed as `d`, it is currently disabled; Enable it using:
> ```bash ln:False
> sudo ethtool -s eno1 wol g
> ```
> Note: This effect is temporary

### Permanently enable WoL

- create a new systemd service
```bash ln:False title:etc/systemd/system/wol.service
[Unit]
Description=Enable Wake-on-LAN
After=network.target

[Service]
ExecStart=/sbin/ethtool -s eno1 wol g

[Install]
WantedBy=multi-user.target
```

- enable service
```bash ln:False
sudo systemctl daemon-reexec
sudo systemctl enable wol.service
```

### Get MAC address

```bash ln:False
ip link show eno1 | grep link/ether | awk -F' ' '{print$2}'
```

> Store it in a secure location

### Wake-on-LAN

- install `wakeonlan`
```bash ln:False
sudo apt install wakeonlan
```

```bash ln:False
wakeonlan <MAC-ADDRESS>
```

</br>

---

## On Windows
  
```powershell ln:False title:ㅤPowershell
winget install "WakeOnLan(Magic Packet)" -s msstore
```

![[20250525090658_Proxmox_WoL.png]]




