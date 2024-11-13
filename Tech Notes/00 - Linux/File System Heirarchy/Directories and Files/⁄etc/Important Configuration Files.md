
</br>

| `/etc/grub.conf`    | It is the grub bootloader configuration file.                                                                                  |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `/etc/default/grub` | GRUB 2 configuration file which can be modified <br><br>(changes are made with the command `grub-mkconfig` or `grub2-mkconfig) |
| `/etc/inittab`      | File that is consulted by `/sbin/init`. Contains the standard run level                                                        |
| `/etc/init.d`       | Start / stop scripts for `init` (Debian systems)                                                                               |
| `/etc/rc.d`         | Start / stop scripts for `init` (Red Hat systems)                                                                              |
| `/etc/rc.d/init.d`  | Run Level `initialization script`. (Red Hat systems)                                                                           |

---

| `/etc/init`                | Contains configuration files that are started at system start (`upstart`)                                                      |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `/etc/systemd/system`      | Contains the so-called systemd units that are started by systemd (`systemd`)<br><br>Can also be found in `/lib/systemd/system` |
| `/etc/systemd/system.conf` | Main configuration file of `systemd`                                                                                           |

---

| `/etc/bashrc`    | It is used by bash shell that contains system defaults and aliases.       |
| ---------------- | ------------------------------------------------------------------------- |
| `/etc/profile`   | Bash shell defaults.                                                      |
| `/etc/profile.d` | It contains other scripts like application scripts, executed after login. |

---

| `/etc/apt/sources.list` | File in which the package sources are stored (`Debian` systems)  |
| ----------------------- | ---------------------------------------------------------------- |
| `/etc/yum.repos.d`      | File in which the package sources are stored (`Red Hat` systems) |

---

| 🚀`/etc/fstab`        | Information of the Disk Drive and their mount point.                         |
| --------------------- | ---------------------------------------------------------------------------- |
| `/etc/exports`        | It contains information on the file system available on the network.         |
| `/etc/crontab`        | A shell script to run specified commands on a predefined time interval.      |
| `/etc/lilo.conf`      | It contains lilo bootloader configuration file.                              |
| 🚀`/etc/hosts`        | Information of IP and corresponding hostnames                                |
| 🚀`/etc/hosts.allow`  | It contains a list of hosts allowed accessing services on the local machine. |
| `/etc/host.deny`      | List of hosts denied accessing services on the local machine.                |
| `/etc/issue`          | Allows editing the pre-login message.                                        |
| 🚀`/etc/modules.conf` | It contains the configuration files for the system modules.                  |
| 🚀`/etc/motd`         | It contains the message of the day.                                          |
| `/etc/mtab`           | Currently mounted blocks information.                                        |
| 🚀`/etc/passwd`       | It contains username, password of the system, users in a shadow file.        |
| 🚀`/etc/group`        | It is a text file to define Information of Security Group.                   |
| `/etc/printcap`       | It contains printer Information.                                             |
| `/etc/resolv.conf`    | DNS being used by System.                                                    |
| `/etc/security`       | It contains the name of terminals where root login is possible.              |
| `/etc/skel`           | Script that initiates new user home directory.                               |
| `/etc/termcap`        | An ASCII file that defines the behavior of different types of the terminal.  |
| `/etc/X11`            | Directory tree contains all the conf files for the X-window System.          |
