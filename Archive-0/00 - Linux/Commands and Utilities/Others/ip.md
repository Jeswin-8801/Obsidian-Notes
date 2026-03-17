Tool used for displaying and modifying the network interface configurations

---

# `ip link`

**<mark style="background: #D2B3FFA6;">Network Interfaces</mark>**

command in Linux is used to manage and display information about network interfaces.

```shell ln:False
$ ip link
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether 00:0c:29:21:8f:1d brd ff:ff:ff:ff:ff:ff
    altname enp2s1
```

- **Interface Name**: The name of the network interface (e.g., `eth0`, `lo`).
> [!info] 
> 
> ==eth0 and lo are both network interfaces in Linux, but they serve different purposes:==
> 
> **<mark style="background: #BBFABBA6;">eth0:</mark>**
> - **Purpose:** Represents a physical Ethernet interface.
> - **Usage:** Used for actual network communication over an Ethernet cable.
> - **Commonly Found:** On physical network cards or virtual machines.
> - **IP Address:** Usually assigned an IP address to connect to other devices on the network.
> 
> **<mark style="background: #BBFABBA6;">lo:</mark>**
> - **Purpose:** Represents the loopback interface.
> - **Usage:** Used for network communication within the same machine. It’s like talking to yourself.
> - **Commonly Found:** On every Linux system.
> - **IP Address:** Typically uses the IP address 127.0.0.1


- **State**: The current state of the interface (e.g., `UP`, `DOWN`).
    
- **MAC Address**: The Media Access Control (MAC) address of the interface.
    
- **MTU (Maximum Transmission Unit)**: The size of the largest packet that can be transmitted.
    
- **Queueing Discipline**: The type of packet scheduler used (e.g., `mq`, `pfifo_fast`).
    
- **Link Type**: The type of network link (e.g., `Ethernet`, `Loopback`).
    
- **Hardware Address**: The physical hardware address of the network interface.
    
- **Broadcast Address**: The broadcast address for the network interface.

---

# `ip addr`

**<mark style="background: #D2B3FFA6;">IP Addresses</mark>**

Lists IP addresses assigned to network interfaces.

```shell ln:False
$ ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute
       valid_lft forever preferred_lft forever
2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 00:0c:29:21:8f:1d brd ff:ff:ff:ff:ff:ff
    altname enp2s1
    inet 192.168.182.130/24 metric 100 brd 192.168.182.255 scope global dynamic ens33
       valid_lft 1470sec preferred_lft 1470sec
    inet6 fe80::20c:29ff:fe21:8f1d/64 scope link proto kernel_ll
       valid_lft forever preferred_lft forever
```

> [!info] 
> ```bash ln:False
> inet 127.0.0.1/8 scope host lo
> 	valid_lft forever preferred_lft forever
> ```
> 
> - **<mark style="background: #ABF7F7A6;">inet `127.0.0.1/8`:</mark>**
> 	This indicates that the loopback interface lo has an IP address of 127.0.0.1 with a subnet mask of 8 bits (255.0.0.0). The loopback address is used for local communications within the host.
> 
> - **<mark style="background: #ABF7F7A6;">scope host:</mark>**
> 	The scope of this IP address is limited to the local host. It cannot be used for external communications.
> 
> - **<mark style="background: #ABF7F7A6;">lo:</mark>**
> 	This is the name of the loopback interface.
> 
> - **<mark style="background: #ABF7F7A6;">valid_lft forever:</mark>**
> 	The valid lifetime of this address is infinite, meaning it will never expire.
> 
> - **<mark style="background: #ABF7F7A6;">preferred_lft forever:</mark>**
> 	The preferred lifetime is also infinite, meaning the address is always preferred and won't be deprecated.

---

# `ip route`

**<mark style="background: #D2B3FFA6;">Routing Tables</mark>**

Shows the routing table.

```shell ln:False
$ ip route
default via 192.168.182.2 dev ens33 proto dhcp src 192.168.182.130 metric 100
192.168.182.0/24 dev ens33 proto kernel scope link src 192.168.182.130 metric 100
192.168.182.2 dev ens33 proto dhcp scope link src 192.168.182.130 metric 100
```

> [!info] 
> 
> - **<mark style="background: #FFB86CA6;color: black">default</mark>**
> 	This is the default route, used when no other routes match the destination IP.
>     
> - **<mark style="background: #FFB86CA6;color: black">via 192.168.182.2</mark>**
> 	Traffic is routed through the gateway at IP address `192.168.182.2`.
>     
> - **<mark style="background: #FFB86CA6;color: black">dev ens33</mark>**
> 	The network interface used is `ens33`.
>     
> - **<mark style="background: #FFB86CA6;color: black">proto dhcp</mark>**
> 	This route was configured by DHCP (Dynamic Host Configuration Protocol).
>     
> - **<mark style="background: #FFB86CA6;color: black">src 192.168.182.130</mark>**
> 	The source IP address is `192.168.182.130`.
>     
> - **<mark style="background: #FFB86CA6;color: black">metric 100</mark>**
> 	The metric value for this route is `100`, which influences route preference (lower is preferred).
> ---
> - **<mark style="background: #FFB86CA6;color: black">192.168.182.0/24</mark>**
> 	This is a subnet route for the network `192.168.182.0` with a subnet mask of `255.255.255.0` (24 bits).
> 	
> - **<mark style="background: #FFB86CA6;color: black">scope link</mark>**
> 	This route is valid only for directly connected networks.

---

# `ip neigh`

**<mark style="background: #D2B3FFA6;">Neighbor Tables</mark>**

Displays neighbor table entries (similar to ARP)

```shell ln:False
$ ip neigh
192.168.182.2 dev ens33 lladdr 00:50:56:e9:4c:96 STALE
192.168.182.1 dev ens33 lladdr 00:50:56:c0:00:08 REACHABLE
192.168.182.254 dev ens33 lladdr 00:50:56:ef:a8:70 STALE
```

> [!info] 
> 
> - **<mark style="background: #FFB86CA6;color: black">lladdr 00:50:56:e9:4c:96</mark>**
> 	The link-layer address (MAC address) of the neighbor.
> 
> - **<mark style="background: #FFB86CA6;color: black">STALE</mark>**
> 	The state of the neighbor entry. "STALE" indicates that the entry is valid but hasn't been used recently.
> 
> - **<mark style="background: #FFB86CA6;color: black">REACHABLE</mark>**
> 	The state of the neighbor entry. "REACHABLE" means the neighbor is actively reachable and communication is successful.

---

# `ip -s link`

**<mark style="background: #D2B3FFA6;">Network Statistics</mark>**

View network-related statistics.

```shell ln:False
$ ip -s link
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    RX:  bytes packets errors dropped  missed   mcast
          6320      80      0       0       0       0
    TX:  bytes packets errors dropped carrier collsns
          6320      80      0       0       0       0
2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether 00:0c:29:21:8f:1d brd ff:ff:ff:ff:ff:ff
    RX:  bytes packets errors dropped  missed   mcast
     157534913  128873      0       0       0       0
    TX:  bytes packets errors dropped carrier collsns
       4468830   49804      0       0       0       0
    altname enp2s1
```