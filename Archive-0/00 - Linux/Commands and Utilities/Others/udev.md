
`udev` (userspace /dev) is **a device manager for the Linux kernel**.

`udev` is the Linux subsystem that supplies your computer with device events. It's the code that detects when you have things plugged into your computer, like a network card, external hard drives (including USB thumb drives), mouses, keyboards, etc.

 It's responsible for: 

- **Creating and removing device nodes**
	`udev` dynamically creates or removes device node files. 
    
- **Handling hotplug events**
	`udev` handles events that occur when hardware devices are added or removed from the system. 
    
- **Loading drivers**
	`udev` loads drivers as needed. 
    
- **Identifying devices**
	`udev` uses rules files to identify devices and create device names. 
    
- **Running userspace commands**
	`udev` can run arbitrary userspace commands in response to events.


### **`udev` rules and configuration files are located in various directories on a Linux system:** 

| `etc/udev/rules.d`     | Administrator-written rules                                      |
| ---------------------- | ---------------------------------------------------------------- |
| `usr/lib/udev/rules.d` | Rules that are shipped with packages                             |
| `run/udev/rules.d`     | A location for administrators to override package-provided rules |

>[!NOTE] Note
>`udev rules` are files with a `.rules` extension that configure how the kernel handles devices. When a new device is attached to the system, `udev` processes the event and configures the device based on the rules.