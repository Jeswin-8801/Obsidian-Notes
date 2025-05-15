---
tags: [homelab,proxmox,template,vm]
---

</br>

- right click template and click clone
![[20250512162222_proxmox_vm_from_template_pointer.png]]

- add name and change mode
![[20250512162825_proxmox_vm_from_template_menu.png]]

> <mark style="background: #ABF7F7A6;">Full Clone</mark> creates a full VM that is not linked back to the template.

> [!important] 
> After creating, modify the configs for optimal resource allocation according to your use case.
> 
> For example: [[HA Cluster Requirements]]
> 
> For changing disk size of VM, do:
> ![[20250513130143_proxmox_vm_disk_size_modify.png]]

