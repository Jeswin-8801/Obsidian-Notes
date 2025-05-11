
</br>


> [!important] 
> During the installation of the OS make sure that the PC is connected to the internet over ethernet as `Proxmox` automatically fetches and assigns IP, gateway and other network configs.

Post installation of the OS, verify the availability of the following services:

- Network
```bash ln:False
ping google.com
```

> If Wi-Fi is opted instead, connect to the Wi-Fi network using <mark style="background: #ABF7F7A6;">iwctl</mark>.
> If, the application is not found, install it using:
> ```bash ln:False
> apt install -y iwd
> ```
> Refer [[Arch Installation#Check network connection#Connect to Wi-Fi]]

- SSH services
```bash ln:False
systemctl status sshd
```

- verify that the hostname is the one set during installation:
```bash ln:False
hostname
```

- get IP
```bash ln:False
hostname -I
```

We can now SSH into the PROXMOX instance and continue to install any additional applications from any system using:

```bash ln:False
ssh root@<ip-address-of-the-proxmox-instance>
```

> [!tip] 
> If there is no method at hand to obtain the IP of the instance, use the method described above to get IP.

