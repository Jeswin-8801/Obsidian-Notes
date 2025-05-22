---
tags: [dns,homelab]
---

</br>

### 🔧 Create a LXC container with the following settings:

- Add the same SSH key with which all other VMs were configured with.
- Select an ubuntu template.
- Add minimal resources:
	- 1 core
	- 4 GB RAM
	- 8 GB storage
- Set a static IP.

> You can now start the container and SSH into it from your local machine (with the username **root**).


### Install PiHole onto the Container

Run the following commands:

```bash ln:False
apt update
apt upgrade -y
apt install -y vim
```

```bash ln:False
wget -O basic-install.sh https://install.pi-hole.net
sudo bash basic-install.sh
```

> Follow the instructions on the console UI and finish installation


### Post Install

- set a new password

```bash ln:False
pihole setpassword
```

- also set start at boot

![[20250517165620_pi_hole_start_at_boot.png]]