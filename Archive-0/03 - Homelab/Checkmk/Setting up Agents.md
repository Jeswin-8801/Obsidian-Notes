---
tags: [monitoring, ]
---


#### 1. Get `checkmk-agent`

- copy the download link for the `.deb` package and use it to download and install onto different hosts.

![[20250628120100_checkmk_agent_package.png]]

#### 2. Install onto Hosts (VMs)

- `ssh` into each VM and run the following scripts
```bash ln:False
mkdir ./Checkmk && cd ./Checkmk
wget --no-check-certificate https://checkmk.home.local/cmk/check_mk/agents/check-mk-agent_2.3.0-2025.06.27-1_all.deb
sudo dpkg -i check-mk-agent_2.3.0-2025.06.27-1_all.deb
```

#### 3. Add Host to CheckMk

![[20250628145549_checkmk_add_host.png]]

#### 4. Select Services and apply changes

- Select the services needed from <mark style="background: #D2B3FFA6;">Undecided Services</mark>
- Click the <mark style="background: #D2B3FFA6;">changes</mark> icon, the top right to apply only the selected changes.
	- Click <mark style="background: #D2B3FFA6;">activate on selected sites</mark>

![[20250628145104_checkmk_select_services.png]]


