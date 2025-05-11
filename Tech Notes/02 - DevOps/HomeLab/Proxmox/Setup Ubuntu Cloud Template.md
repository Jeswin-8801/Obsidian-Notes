
</br>

1. Download the ubuntu cloud server image file from: [Ubuntu Cloud Images](https://cloud-images.ubuntu.com/) at 👇

![[20250511170645_proxmox_download_iso.png]]

Alternatively, download Ubuntu server iso from URL => `https://releases.ubuntu.com/24.04.2/ubuntu-24.04.2-live-server-amd64.iso`

> I had decided to go with <mark style="background: #ABF7F7A6;">noble/ > current/ > noble-server-cloudimg-amd64.img</mark> at the time of setting up this server.
>
> To know more about ==cloud images==, refer: https://serverfault.com/a/940662. In Ubuntu cloud image, ==cloud-init== takes care of this initial setup and in short it performs the following operations: [CloudInit - Community Help Wiki](https://help.ubuntu.com/community/CloudInit)

</br>

2. ==ssh== into the Proxmox instance and run the following commands

```bash ln:False
qm create 5000 --memory 4096 --core 2 --name ubuntu-cloud --net0 virtio,bridge=vmbr0
```

> This creates a VM entry that will show up as <mark style="background: #ABF7F7A6;">5000 (ubuntu-cloud)</mark> on the web interface

```bash ln:False
$ cd /var/lib/vz/template/iso
$ ls
ubuntu-server-24.04.2.iso  ubuntu-server-cloudimg-2404.img
```

> [!note] 
> This is where Proxmox stores all the downloaded iso files.

```bash ln:False
qm importdisk 5000 ubuntu-server-cloudimg-2404.img local-lvm
```

> This command imports the disk image to the VM ==5000==
> 
> ==local-lvm== is the logical volume we had selected on startup when installing Proxmox. It will be displayed on the web interface as given in the image above.

Below command attaches a drive to the VM (similar to plugging in hardware to motherboard but in a VM context)
```bash ln:False
qm set 5000 --scsihw virtio-scsi-pci --scsi0 local-lvm:vm-5000-disk-0
```
Attached to ==scsi port 0==

Equivalent to attaching a DVD drive with a disk insertedmounted to `ide2`
```bash ln:False
qm set 5000 --ide2 local-lvm:cloudinit
```

```bash ln:False
qm set 5000 --boot c --bootdisk scsi0
```

> Above command sets the boot drive to the drive at ==scsi0== created above.

Physical equivalent of plugging in a VGA monitor.
```bash ln:False
qm set 5000 --serial0 socket --vga serial0
```

> Creates a serial port to enable access to a serial terminal (Refer [Serial Terminal - Proxmox VE](https://pve.proxmox.com/wiki/Serial_Terminal) for the advantages of using it)
> 
> This command is optional

</br>

1. Select the VM (5000) in the web interface and edit the following options in the <mark style="background: #ABF7F7A6;">Hardware</mark> section.

- **Memory**
 Uncheck ballooning
![[proxmox_ubuntu_template_memory.png]]

> When using Hardware Passthrough (refer [PCI Passthrough - Proxmox VE](https://pve.proxmox.com/wiki/PCI_Passthrough)), a static memory is preferred over ballooned or dynamically allotted memory. as hardware like GPUs and PCIe cards often expect dedicated, fixed memory.

- **Processor**

![[proxmox_ubuntu_template_processor.png]]

- **Hard Disk**

![[proxmox_ubuntu_template_hard_disk.png]]

> This feature helps reclaim unused space in SSDs and NVME drives.

</br>

2. <mark style="background: #D2B3FFA6;">Clout-Init</mark> section

The following options need to be modified
![[proxmox_ubuntu_cloud_init.png]]

- The ==Username== and ==Password== field will be used to create an account in every VM created using this template therefore we can login using the same credentials on every VM.
- The SSH key set in the ==SSH public key== field will be copied to every VM created using this template therefore we can SSH into the VMs without any additional key management.
> To setup a SSH key in Proxmox, enter the following commands in the Proxmox instance.
> ```bash ln:False
> cd ~/.ssh
> ssh-keygen -t ed25519 -C "jeswin.santosh@outlook.com"
> # I have set the name of the key to 'ubuntu_cloud_ssh_key'
> ```
> 
> Copy the key below to the web interface
> ```bash ln:False
> cat ~/.ssh/ubuntu_cloud_ssh_key.pub
> ```

- remember to set the IP to dynamic (DHCP) as we do not want every clone of the template to have the same IP.

</br>

3. Convert to Template

![[20250511173115_proxmox_convert_to_template.png]]