---
tags: [cloud-init,ubuntu,vm]
---

</br>

## Create a template

> [!note] 
> This is equivalent to [[Setup Ubuntu Cloud Template]] using the web interface.

- `cd` into the right directory in the project and execute the following
```bash ln:False
cd ~/Downloads/HomeLab/Proxmox/vm-template
```

- execute script with ==username== and ==password== params:
```bash ln:False
sudo ./ubuntu_ci_template.sh -u <username> -p '<password>'
```

> This creates a Ubuntu Cloud-Init VM template with the following settings:
![[20250514174105_VM_template_hardware_settings.png]]
![[20250514174148_VM_template_ci_settings.png]]


</br>

---

## K3s HA Cluster setup script

> Refer: [[HA Cluster Automation Script]]