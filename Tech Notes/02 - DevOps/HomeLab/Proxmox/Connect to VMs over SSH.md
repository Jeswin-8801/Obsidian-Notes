---
tags: [vm,proxmox,ssh]
---

</br>

Add the key created during the setup of cloud-init in [[Setup Ubuntu Cloud Template]] to your local system so that the VMs created from this template can be accessed through SSH.

- Copy the private key from <mark style="background: #D2B3FFA6;">/root/.ssh/ubuntu_cloud_ssh_key</mark> to a file in <mark style="background: #D2B3FFA6;">$HOME/.ssh/ubuntu_cloud_ssh_key</mark> on your PC (assuming it to be Linux based).
  
- Add appropriate permissions to the file

```bash ln:False
chmod 600 ~/.ssh/ubuntu_cloud_ssh_key
```

- permanently add SSH key to config
  
```bash ln:False
cat >> ~/.ssh/config << EOF
Host *
    IdentityFile ~/.ssh/ubuntu_cloud_ssh_key
EOF
```

> We can now access the VMs by
> ```bash ln:False
> ssh ubuntu@<IP-of-VM>
> ```

> [!note] 
> IP will be allotted after the VM has started up and can be optained using the command <mark style="background: #ABF7F7A6;">hostname -I</mark>