---
tags: [How-To, ip, vm]
---

</br>


Assuming you have created a VM from a ==cloud-init== template and have started the VM:

- SSH into VM

- Run the below commands in VM

```bash ln:False
# Take backup
sudo cp /etc/netplan/50-cloud-init.yaml /etc/netplan/50-cloud-init.yaml.bak
# delete last 2 lines
sudo bash -c "head -n -2 /etc/netplan/50-cloud-init.yaml.bak > /etc/netplan/50-cloud-init.yaml"
# add new Static IP and disable DHCP
sudo bash -c "cat >> /etc/netplan/50-cloud-init.yaml << EOF
      dhcp4: no
      addresses:
        - 192.168.0.51/24
      nameservers:
        addresses: [8.8.8.8, 8.8.4.4]
      routes:
        - to: default
          via: 192.168.0.1
EOF"
# apply changes
sudo netplan apply
```

- Start a new SSH session and verify changes.
