
- **Shared libraries**
	The `/lib` directory contains shared library images that are required to boot the system and run commands in the root filesystem, i.e. by binaries in `/bin` and `/sbin`. 

>[!Important] Important
>[[⁄bin ⁄lib and ⁄sbin are now symlinks]]

- **Kernel modules**
	The `/lib` directory contains loadable kernel modules. 
    
- **Binaries**
	The `/lib` directory contains binaries in `/bin` and `/sbin`. 
    
- **Other files**
	The `/lib` directory contains other helpful files that are used by applications, commands, and processes to execute properly.

> [!NOTE] Note
> The `/lib` directory is present on 32-bit systems, while the `/lib64` directory is used on 64-bit systems.