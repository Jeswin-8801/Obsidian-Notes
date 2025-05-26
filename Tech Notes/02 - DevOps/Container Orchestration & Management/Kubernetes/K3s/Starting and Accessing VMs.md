---
tags: [bash]
---

</br>

### Start all VMs from the Proxmox Instance

```bash ln:False
bash -c "for vmid in 101 102 103 104 105; do
     sudo qm start \$vmid
	done
   "
```

</br>

### Add SSH access to all VMs

- add the following config to the SSH config file

```bash title:~/.ssh/config
Host 192.168.0.*
    User ubuntu
    IdentityFile ~/.ssh/ubuntu_cloud_ssh_key
    Port 22
    StrictHostKeyChecking no
```
