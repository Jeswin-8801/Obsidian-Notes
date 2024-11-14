
</br>

<mark style="background: #D2B3FFA6;">init systems</mark> are responsible for managing the startup and shutdown processes of Linux systems

</br>

# SysVinit

==SysVinit (System V init)== is one of the oldest init systems, originating from UNIX System V.

It Uses a series of scripts located in `/etc/init.d/` and symbolic links in `/etc/rc*.d/` directories to manage services.

- **<mark style="background: #FFB86CA6; color: black;">Runlevels</mark>**:
	Defines different runlevels (0-6) to represent different states of the system.
	
	> The sysvinit runlevels are:
	> - **<mark style="background: #D2B3FFA6; color: black;">0</mark>** - halt (shutdown)
	> - **<mark style="background: #D2B3FFA6; color: black;">1</mark>** – single user mode (rescue)
	> - **<mark style="background: #D2B3FFA6; color: black;">2</mark>** – Multiuser (without NFS/remote filesystems or Network)
	> - **<mark style="background: #D2B3FFA6; color: black;">3</mark>** – Full multisuer mode (including remote filesystems and network)
	> - **<mark style="background: #D2B3FFA6; color: black;">4</mark>** – unused
	> - **<mark style="background: #D2B3FFA6; color: black;">5</mark>** – X11 (Full multi-user with GUI)
	> - **<mark style="background: #D2B3FFA6; color: black;">6</mark>** – reboot
- **<mark style="background: #FFB86CA6; color: black;">Sequential Start</mark>**:
	Services are started sequentially, which can slow down the boot process.

</br>

# Upstart

Developed by Canonical for ==Ubuntu==. Upstart was designed to replace [[#SysVinit]] and handle the dynamic nature of modern systems.

- **<mark style="background: #FFB86CA6; color: black;">Event-Driven</mark>**:
	Uses an event-driven model to start services. Services can start in response to events like hardware changes or other services starting.
- **<mark style="background: #FFB86CA6; color: black;">Parallel Start</mark>**:
	Allows for parallel starting of services, which can speed up the boot process.

</br>

### Systemd

A modern init system and service manager designed to overcome the limitations of [[#SysVinit]] and [[#Upstart]].

**Default init system for most major Linux distributions.**

- **<mark style="background: #FFB86CA6; color: black;">Unit Files</mark>**:
	Uses unit files (e.g., service, socket, device units) instead of scripts to manage services. These files are located in `/etc/systemd/system/` and `/usr/lib/systemd/system/`.
- **<mark style="background: #FFB86CA6; color: black;">Parallel and Dependency-Based</mark>**:
	Starts services in parallel and manages dependencies between them, significantly speeding up the boot process.
- **<mark style="background: #FFB86CA6; color: black;">Features</mark>**:
	Includes advanced features like ==socket-based activation==, on-demand starting of ==daemons==, and ==cgroups== for resource management.
- **<mark style="background: #FFB86CA6; color: black;">Unified Management</mark>**:
	Provides a unified interface for managing services, devices, mount points, and more through the `systemctl` command.

> [!important] 
> The systemd config file `system.conf` is placed in <mark style="background: #D2B3FFA6;">/etc/systemd</mark>

---

</br>

### Key Differences

- **<mark style="background: #FFB86CA6; color: black;">Initialization Method</mark>**:
	[[#SysVinit]] uses sequential scripts, [[#Upstart]] uses an event-driven model, and [[#Systemd|systemd]] uses unit files with parallel and dependency-based startup.
- **<mark style="background: #FFB86CA6; color: black;">Performance</mark>**:
	[[#Systemd|systemd]] generally offers faster boot times due to its parallel startup and efficient dependency management.
- **<mark style="background: #FFB86CA6; color: black;">Flexibility</mark>**:
	[[#Upstart]] and [[#Systemd|systemd]] are more flexible and better suited for modern, dynamic systems compared to the older [[#SysVinit]].