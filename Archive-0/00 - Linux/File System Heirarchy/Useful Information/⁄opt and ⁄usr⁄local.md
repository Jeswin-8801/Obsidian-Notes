---
tags:
  - INFO
  - Linux-Directories
---


> [!Note] Note
> While both are designed to contain files not belonging to the operating system, `/opt` and `/usr/local` are not intended to contain the same set of files.

</br>

## `/usr/local`

The `/usr/local` directory in Linux is ==used by system administrators to install software locally==.

Contains user programs installed from source or outside the distribution's provided software.

> `/usr/local` is a place to install files built by the administrator, typically by using the `make` command (e.g., `./configure; make; make install`). 

</br>

#### **Why use `/usr/local` over `/usr/bin` in certain cases?**

The idea is to avoid clashes with files that are part of the operating system, which would either be overwritten or overwrite the local ones otherwise (e.g., `/usr/bin/foo` is part of the OS while `/usr/local/bin/foo` is a local alternative).

All files under `/usr` are shareable between OS instances, although this is rarely done with Linux. This is a part where the FHS is slightly self-contradictory, as `/usr` is defined to be read-only, but `/usr/local/bin` needs to be read-write for local installation of software to succeed. The SVR4 file system standard, which was the FHS' main source of inspiration, is recommending to avoid `/usr/local` and use `/opt/local` instead to overcome this issue.

`/usr/local` is a legacy from the original BSD. At that time, the source code of `/usr/bin` OS commands were in `/usr/src/bin` and `/usr/src/usr.bin`, while the source of locally developed commands was in `/usr/local/src`, and their binaries in `/usr/local/bin`. There was no notion of packaging (outside tarballs).

---

</br>

## `/opt`

> `/opt` is a directory for installing unbundled packages (i.e. packages not part of the Operating System distribution, but provided by an independent source), each one in its own subdirectory. 

They are already built whole packages provided by an independent third party software distributor. Unlike `/usr/local` stuff, these packages follow the directory conventions (or at least they should). For example, `someapp` would be installed in `/opt/someapp`, with one of its command being `/opt/someapp/bin/foo`, its configuration file would be in `/etc/opt/someapp/foo.conf`, and its log files in `/var/opt/someapp/logs/foo.access`.