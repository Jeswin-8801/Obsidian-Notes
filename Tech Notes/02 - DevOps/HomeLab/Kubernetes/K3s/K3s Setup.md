---
tags: [homelab,kubernetes]
---

</br>

> [!note] 
> Both ==K3s== and ==K8s== are container orchestration platforms, but K3s is a lightweight version for edge compute and smaller clusters whereas K8s is more feature rich intended as an enterprise solution.
> 
> ==HA== is short for High Availability

</br>

## Setting up VMs for Cluster

### Setup master and worker VMs

1. Set up 5 VMs from the template we created from [[Setup Ubuntu Cloud Template]]. Refer [[Starting a VM from Template]].

![[20250512164314_k3s_vms.png]]

> Here, the first 3: <mark style="background: #D2B3FFA6;">k3s-01</mark>, <mark style="background: #D2B3FFA6;">k3s-02</mark>, <mark style="background: #D2B3FFA6;">k3s-03</mark> are master nodes whereas <mark style="background: #D2B3FFA6;">k3s-w-01</mark>, <mark style="background: #D2B3FFA6;">k3s-w-02</mark> are worker nodes.

2. Before starting the VMs, modify the VM configs in the web interface as per your needs (refer [[HA Cluster Requirements]]). It is recommended to set the IP of the VMs as static.

> [!info] 
> I have made it so that all VMs are allotted static IPs in the range: <mark style="background: #D2B3FFA6;">192.168.0.51 <-> 192.168.0.55</mark>
> 
> This was taking into consideration the fact that my local DHCP is set to allot IPs in the range `2-30`, therefore the IPs that will be set now is outside this range.
> 
> This can be done by using the Web interface:
>   ![[20250513132821_proxmox_vm_static_ip_setup.png]]
> 
> *Alternatively, you can change it inside the VM => [[Cloud-Init VM Network Settings]]*
> 
> Remember to change the IP of each VM. (here, it is configured as per the table below) 
> 
> | VM                                                   | IP           |
> | ---------------------------------------------------- | ------------ |
> | <mark style="background: #FFB86CA6;">k3s-01</mark>   | 192.168.0.51 |
> | <mark style="background: #FFB86CA6;">k3s-02</mark>   | 192.168.0.52 |
> | <mark style="background: #FFB86CA6;">k3s-03</mark>   | 192.168.0.53 |
> | <mark style="background: #FFB86CA6;">k3s-w-01</mark> | 192.168.0.54 |
> | <mark style="background: #FFB86CA6;">k3s-w-02</mark> | 192.168.0.55 |

3. Start all 5 VMs one by one and verify login using the username and password we setup in ==cloud-init== in the Username and Password setup section in [[Setup Ubuntu Cloud Template]].

</br>

---

### Configuring VMs as a HA Kubernetes cluster

- Spin up a new VM from template.

> [!note] 
> This VM is intended only to run the script below to setup the Kubernetes cluster in the VMs configured above.

- The following files are required to set up the cluster:
    - SSH key used to create the template.
    - The script that sets up the cluster.

- download the script and make it executable

```bash ln:False
wget -O /home/ubuntu/k3s.sh "https://raw.githubusercontent.com/Jeswin-8801/HomeLab/refs/heads/main/Kubernetes/K3s/k3s.sh"
chmod +x /home/ubuntu/k3s.sh
```

> Update the script if necessary with the configurations you require in the first section.

- ==SCP== the private key onto the VM from your local machine (This key has already been placed at `$HOME/.ssh` in step [[Starting a VM from Template#Connect to VM over SSH]])

```bash ln:False
scp ~/.ssh/ubuntu_cloud_ssh_key* ubuntu@<IP-of-new-VM>:/home/ubuntu
```

> [!note] 
> This script has been referenced from YT => [The Simplest Kubernetes Deployment? K3S, HA, Loadbalancer! Kubernetes At Home: Part 3 - YouTube](https://www.youtube.com/watch?v=6k8BABDXeZI&list=PLXHMZDvOn5sVXjb88kYXSI7UMx4rhQwOj&index=3)

- simply run the script
** Before running, make sure to update variables in the script like the IP ranges of nodes **
```bash ln:False
./k3s.sh
```

You should be able to see the output:

```bash ln:False
$ kubectl get svc
NAME         TYPE           CLUSTER-IP      EXTERNAL-IP    PORT(S)        AGE
kubernetes   ClusterIP      10.43.0.1       <none>         443/TCP        12m
nginx-1      LoadBalancer   10.43.123.115   192.168.0.60   80:31601/TCP   10m
```

And the nginx home page will now be deployed on the load balancer IP.