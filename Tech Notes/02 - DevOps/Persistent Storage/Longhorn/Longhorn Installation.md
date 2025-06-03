---
tags: [storage,kubernetes]
---

</br>


> [!important] 
> Must have K3s nodes already setup. Refer: [[K3s Setup]]

</br>

> Setup 3 VMs from the existing cloud-init template using the script in the ==Homelab== repo at location `Kubernetes/Longhorn`:

```bash ln:False
sudo ./create_vms_for_longhorn.sh -s 192.168.0.56 -g 192.168.0.1 -n 3 -i 111
```

- once created, start all VMs
```bash ln:False
bash -c "for vmid in 111 112 113; do
     sudo qm start \$vmid
	done
   "
```

</br>

> [!note] This script is intended to be run on the Proxmox instance as a non root user (refer: [[Post Setup#Create a new User]])

</br>

### Setup Longhorn Nodes for HA

> [!info] Run it on the VM which was used to setup K3s as it will already have the required applications to manage kubernetes.

- download and make the script executable
```bash ln:False
wget -O /home/ubuntu/longhorn-K3S.sh "https://raw.githubusercontent.com/Jeswin-8801/HomeLab/refs/heads/main/Kubernetes/Longhorn/longhorn-K3S.sh"
chmod +x /home/ubuntu/longhorn-K3S.sh
```

- run
```bash ln:False
./longhorn-K3S.sh
```

> This can take a few minutes.

- check for labels in correct nodes
```bash ln:False
kubectl get nodes --show-labels | grep longhorn
```

> if the worker nodes have also been added, remove label
> ```bash ln:False
> kubectl label node k3s-w-01 longhorn-
> kubectl label node k3s-w-02 longhorn-
> ```

> [Tip: Set Longhorn To Only Use Storage On A Specific Set Of Nodes | The Longhorn Knowledge Base](https://longhorn.io/kb/tip-only-use-storage-on-a-set-of-nodes/#deploy-longhorn-components-only-on-a-specific-set-of-nodes)
> ```bash ln:False
> kubectl label nodes longhorn-01 storage=longhorn
> kubectl label nodes longhorn-02 storage=longhorn
> kubectl label nodes longhorn-03 storage=longhorn
> ```

- delete the disabled nodes in the Longhorn Dashboard if any.

</br>

> [!note] 
> Access the Longhorn UI from the Rancher Dashboard.
