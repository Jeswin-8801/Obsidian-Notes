---
tags: [vm,containers,linux]
---

</br>

> [!tldr] 
> In short, LXC is a container technology like Docker which **share the host systems kernel** making them much faster to start and they use fewer resources than virtual machines.

|Feature|**LXC Container**|**Virtual Machine (KVM)**|
|---|---|---|
|<mark style="background: #FFB86CA6;">**Isolation**</mark>|Shared kernel (host + container)|Full isolation (separate kernel & OS)|
|<mark style="background: #FFB86CA6;">**Performance**</mark>|Near-native (lightweight, minimal overhead)|Slightly lower due to hardware emulation|
|<mark style="background: #FFB86CA6;">**Boot Time**</mark>|Fast (seconds)|Slower (OS boots fully)|
|<mark style="background: #FFB86CA6;">**Resource Usage**</mark>|Lower (shares host resources more efficiently)|Higher (includes full OS, kernel)|
|<mark style="background: #FFB86CA6;">**OS Support**</mark>|Linux only (same kernel family)|Any OS (Linux, Windows, BSD, etc.)|
|<mark style="background: #FFB86CA6;">**Security Isolation**</mark>|Weaker (shared kernel)|Strong (full kernel separation)|
|<mark style="background: #FFB86CA6;">**Storage Flexibility**</mark>|Easier ZFS dataset integration|More manual ZFS configuration needed|

> [!info] 
> For info on differences between LXCs and Docker Containers refer [[LXCs vs Docker]]

---

## 🔧 When to Use Each

### ✅ **Use LXC if:**

- You're running **Linux services** (e.g., NGINX, MariaDB, Docker host, Git server).
    
- You want **lightweight, fast-starting containers**.
    
- You need efficient **ZFS integration** (e.g., datasets as container storage).
    
- You want **high density** (many services on limited resources).


### ✅ **Use a VM if:**

- You need to run **non-Linux OSes** (e.g., Windows, BSD).
    
- You want **full system-level isolation** (e.g., for untrusted services).
    
- You require **custom kernels**, kernel modules, or specific distros.

---

## 🛠️ Use Case

- <mark style="background: #FFB86CA6;">**LXC Container**</mark> for
	- Nextcloud
	- Jellyfin
	- MySQL
	- NGINX
	- Pi-hole
    
- <mark style="background: #FFB86CA6;">**VM**</mark> for
	- TrueNAS SCALE
	- Windows Server (or other distributions)
	- pfSense
	- Home Assistant (with USB passthrough)