---
tags: Formatting
---

The <mark style="background: #D2B3FFA6;">mkswap</mark> and <mark style="background: #D2B3FFA6;">swapon</mark> commands are used in Linux to set up and enable swap space, which is used to extend the system’s physical memory by using disk space when the memory is full.

</br>

# `mkswap`

The `mkswap` command is used to set up a Linux swap area on a device or in a file. This command prepares the specified partition or file to be used as swap space.

```bash ln:False
sudo mkswap /dev/sdX1
```

This command sets up the partition `/dev/sdX1` as swap space.

> [!note] 
> This will also erase any data on the specified partition.

---

</br>

# `swapon`

The `swapon` command is used to enable the swap area created by `mkswap`. This command activates the swap space so that the system can start using it.

```bash ln:False
sudo swapon /dev/sdX1
```

This command enables the swap space on the partition `/dev/sdX1`.

---

</br>

# Steps to Add Swap Space

1. **Create a Swap File** (if not using a partition):
    
    ```bash ln:False
    sudo dd if=/dev/zero of=/swapfile bs=1M count=1024
    sudo chmod 600 /swapfile
    ```

	- <mark style="background: #ABF7F7A6; color: black;">if</mark> stands for “input file”. <mark style="background: #ABF7F7A6; color: black;">/dev/zero</mark> generates a continuous stream of zero bytes. Each byte is an ASCII NUL character (0x00).
	</br>
	- <mark style="background: #ABF7F7A6; color: black;">of</mark> stands for “output file”. This specifies the file to which the data will be written. In this case, it is <mark style="background: #ABF7F7A6; color: black;">/swapfile</mark>.
    
2. **Set Up the Swap Area**:
    
    ```bash ln:False
    sudo mkswap /swapfile
    ```
    
3. **Enable the Swap Space**:
    
    ```bash ln:False
    sudo swapon /swapfile
    ```
    
4. **Make the Swap Space Permanent**: Add the following line to `/etc/fstab` to ensure the swap space is enabled at boot:
    
    ```bash ln:False
    /swapfile none swap sw 0 0
    ```
    
5. **Verify the Swap Space**:
    
    ```bash ln:False
    sudo swapon --show
    free -h
    ```


</br>

> [!important] 
> A <mark style="background: #ABF7F7A6;">swap file</mark> is a file on your computer’s hard drive or SSD that acts as an ==extension of the system’s physical RAM==. When the system’s RAM is fully utilized, the operating system moves inactive data from RAM to the swap file, freeing up RAM for other tasks.