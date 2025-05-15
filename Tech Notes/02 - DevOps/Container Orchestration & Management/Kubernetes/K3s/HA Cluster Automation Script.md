---
tags: [k3s,ha,bash,homelab,kubernetes]
---

</br>

> [!note] 
> This is equivalent to following through [[K3s Setup]] using the web interface.
> 
> It creates 5 VMs each with different resources as per the type of node (server/agent) and assigns them static IP addresses.

- `cd` into the script directory:
```bash ln:False
cd ~/Downloads/HomeLab/Kubernetes/K3s
```

> [!important] 
> Checkout what each CLI argument does and assign values according to your specifications before running the script below.
> 
> For help:
> ```bash ln:False
> sudo ./create_vms_for_k3s.sh -h
> ```

- execute script with required params:
```bash ln:False
sudo ./create_vms_for_k3s.sh -s 192.168.0.51 -g 192.168.0.1 -m 3 -w 2 -i 101
```


**After this step, follow through the instructions in the section [[K3s Setup#Configuring VMs as a HA Kubernetes cluster]] to complete the setup.**