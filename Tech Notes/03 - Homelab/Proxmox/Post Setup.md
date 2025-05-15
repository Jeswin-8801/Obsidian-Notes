---
tags: [homelab,proxmox,setup]
---


</br>

#### Create a new User

> [!note] 
> The objective of doing this is to make it so that the root user is intended to access serial console while having no tools or bloated UI, while the new user account will have multiple tools installed with customizations as per our need.

- ==ssh== into the instance
- install necessary packages

```bash ln:False
apt update && apt upgrade
```

```bash ln:False
apt install -y git vim sudo
```

```bash ln:False
echo "alias ll=\"ls -alhtr\"" >> ~/.bashrc
```

- create new user

```bash ln:False
adduser jeswins
```
> Follow the prompts and enter the required information for creating a new user account.

- add user to group

```bash ln:False
gpasswd -a jeswins sudo
```

- add user to Proxmox auth space

```bash ln:False
pveum user add jeswins@pam
pveum acl modify / --roles Administrator --users jeswins@pam
```

> [!info] 
> Git though SSH must be set up, if we need to work on repos and also since we are cloning through SSH below.
> 
> Refer: [[Git SSH setup]]

</br>

# Customize Shell Environment 

- SSH into the server with the new user
```bash ln:False
ssh jeswins@<IP-of-PROXMOX-node>
```

- Install `fish` and apply change shell operation
```bash ln:False
sudo apt install -y fish
chsh -s "$(which fish)" # set as default shell
```

> Exit session and SSH again.

Run the following script to install all the necessary tools:

```bash ln:False
mkdir -p ~/Downloads
git clone git@github.com:Jeswin-8801/HomeLab.git ~/Downloads/HomeLab
cd ~/Downloads/HomeLab/proxmox
sudo ./install.sh
```

> [!note] 
> This script also includes adding a theme to the ==grub== boot menu.
> 
> To, enable the boot menu for an extended duration:
> ```bash ln:False
> sudo nvim /etc/default/grub
> # Update GRUB_TIMEOUT to a longer duration
> sudo update-grub
> ```

- finally, source the file to apply the changes
```bash ln:False
source ~/.config/fish/config.fish
```

</br>

# Setup Nginx Reverse Proxy

> Refer: [[Reverse Proxy]]