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

With **3 master nodes and 2 agent nodes**, given below is a balanced recommendation for **VM specs** per node, assuming large workloads, the agent takes most of the heavy working.

Therefore, the **VM specs** to support multiple services is given as follows:

---

## 🧮 Recommended Node Specs (Revised for 20 Services)

| Node Role   | vCPUs per Node | RAM per Node | Storage per Node |
| ----------- | -------------- | ------------ | ---------------- |
| <mark style="background: #FFB86CA6;">**Masters**</mark> | 2–3 vCPUs      | 6–8 GB       | 30–40 GB SSD     |
| <mark style="background: #FFB86CA6;">**Agents**</mark>  | 3–4 vCPUs      | 10–12 GB     | 40–60 GB SSD     |

---

## ⚙️ Suggested Allocation (Balanced across 5 VMs)

| Node                                                 | vCPUs | RAM   | Notes                       |
| ---------------------------------------------------- | ----- | ----- | --------------------------- |
| <mark style="background: #FFB86CA6;">Master 1</mark> | 2     | 6 GB  | Etcd + Control Plane        |
| <mark style="background: #FFB86CA6;">Master 2</mark> | 2     | 6 GB  |                             |
| <mark style="background: #FFB86CA6;">Master 3</mark> | 2     | 6 GB  |                             |
| <mark style="background: #FFB86CA6;">Agent 1</mark>  | 4     | 12 GB | Runs workloads              |
| <mark style="background: #FFB86CA6;">Agent 2</mark>  | 4     | 12 GB | Runs workloads              |
| **Total**                                            | 14    | 42 GB | Leaves headroom on the host |

### This leaves:

- **2 vCPUs + 22 GB RAM free** on the host for:
    
    - VM overhead
        
    - Management tools (e.g., your hypervisor or SSH)
        
    - Buffer for Kubernetes and OS operations

> [!important] 
> Refer: [Requirements | K3s](https://docs.k3s.io/installation/requirements)
> Contrary to what is specified here, since we will have an increased number of services deployed, we will need to either increase the resources if the agent nodes or the number of agent nodes.