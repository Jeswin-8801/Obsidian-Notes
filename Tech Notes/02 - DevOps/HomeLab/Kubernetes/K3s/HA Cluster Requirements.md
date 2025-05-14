---
tags: [kubernetes,homelab,proxmox]
---

</br>

### **Spec Sheet (Proxmox Node)**


| Resource | Quantity                            |
| -------- | ----------------------------------- |
| <mark style="background: #FFB86CA6;">CPU</mark>      | **i7 10700 => 8-cores, 16-threads** |
| <mark style="background: #FFB86CA6;">Memory</mark>   | **64 GB DDR4**                      |
| <mark style="background: #FFB86CA6;">Storage</mark>  | **512 GB NVME drive**               |

### **Recommended VM Resource Allocation**

Designing an **optimal resource allocation** for your **K3s HA cluster** with **3 master nodes and 2 agents** on **Proxmox**.

| **VM Role**          | **CPU Cores**  | **RAM**      | **Storage**                          |
| -------------------- | -------------- | ------------ | ------------------------------------ |
| **Master Node (x3)** | 2-3 cores each | 8-12GB each  | **40GB minimum** (Recommended: 60GB) |
| **Worker Node (x2)** | 3-4 cores each | 12-16GB each | **50GB minimum** (Recommended: 80GB) |

### **Breakdown of Resources**

1. **Master Nodes (3x)**
    
    - **CPU**: 2-3 cores each → Since K3s is lightweight, this is enough for control plane tasks.
        
    - **RAM**: 8-12GB each → Ensures stable performance with ETCD and control services.
        
    - **Storage**: Minimum **40GB** per VM, **60GB recommended** → For logs, Kubernetes objects, and system files.
        
2. **Worker Nodes (2x)**
    
    - **CPU**: 3-4 cores each → Handles workloads efficiently.
        
    - **RAM**: 12-16GB each → Depends on the number of pods running.
        
    - **Storage**: Minimum **50GB**, **80GB recommended** → Pods, container images, and logs.


> [!important] 
> Refer: [Requirements | K3s](https://docs.k3s.io/installation/requirements)