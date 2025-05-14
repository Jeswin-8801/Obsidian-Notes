---
tags: [k3s,ha,bash,homelab,kubernetes]
---

</br>

> [!note] 
> This is equivalent to following through [[K3s Setup]] using the web interface.

- `cd` into the right directory in the project and execute the following
```bash ln:False
cd ~/Downloads/HomeLab/Kubernetes/K3s
```

- execute script with required params:
```bash ln:False
sudo ./create_vms_for_k3s.sh -s 192.168.0.51 -g 192.168.0.1 -m 3 -w 2 -i 101
```

> Checkout the `README.md` in the same directory for more info on CLI args for this script.
> Or run:
> ```bash ln:False
> sudo ./create_vms_for_k3s.sh -h
> ```

**After this step, follow through the instructions in the section [[K3s Setup#Configuring VMs as a HA Kubernetes cluster]] to complete the setup.**