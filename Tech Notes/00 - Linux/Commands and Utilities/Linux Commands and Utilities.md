---
tags:
  - MAIN
  - Linux-Commands
---
## System Information

| CPU and Kernel                 | Hardware                       | Kernel Modules                                      |
| ------------------------------ | ------------------------------ | --------------------------------------------------- |
| [[lscpu]]    <br><br>[[uname]] | [[lspci]]    <br><br>[[lsusb]] | [[lsmod]]   <br><br>[[modinfo]]<br><br>[[modprobe]] |

---
## Compression And Archiving

| [[file, find#`file`\|file]]      <br><br>[[file, find#`find`\|find]] | [[dd]]         | [[tar, cpio#`tar`\|tar]]       <br><br>[[tar, cpio#`cpio`\|cpio]] | [[gzip, gunzip, bzip2, bunzip, xz, unxz#`gzip`\|gzip]]<br><br>[[gzip, gunzip, bzip2, bunzip, xz, unxz#`gunzip`\|gunzip]]<br><br>[[gzip, gunzip, bzip2, bunzip, xz, unxz#`bzip2`\|bzip2]]<br><br>[[gzip, gunzip, bzip2, bunzip, xz, unxz#`bunzip2`\|bunzip2]]<br><br>[[gzip, gunzip, bzip2, bunzip, xz, unxz#`xz`\|xz]]<br><br>[[gzip, gunzip, bzip2, bunzip, xz, unxz#`unxz`\|unxz]] |
| -------------------------------------------------------------------- | -------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

---
## Process Text Streams with Filters

| [[cat, head, tail#`cat`\|cat]]      <br><br>[[cat, head, tail#`head`\|head]]<br><br>[[cat, head, tail#`tail`\|tail]] | [[zcat, bzcat, xzcat#`zcat`\|zcat]]     <br><br>[[zcat, bzcat, xzcat#`bzcat`\|bzcat]]<br><br>[[zcat, bzcat, xzcat#`xzcat`\|xzcat]] | [[nl, wc, od#`nl`\|nl]]        <br><br>[[nl, wc, od#`wc`\|wc]]<br><br>[[nl, wc, od#`od`\|od]] | [[md5sum, sha256sum, sha512sum#`md5sum`\|md5sum]]<br><br>[[md5sum, sha256sum, sha512sum#`sha256sum`\|sha256sum]]<br><br>[[md5sum, sha256sum, sha512sum#`sha512sum`\|sha512sum]] | [[sort, uniq, tr, cut, paste#`sort`\|sort]]        <br><br>[[sort, uniq, tr, cut, paste#`uniq`\|uniq]]<br><br>[[sort, uniq, tr, cut, paste#`tr`\|tr]]<br><br>[[sort, uniq, tr, cut, paste#`cut`\|cut]]<br><br>[[sort, uniq, tr, cut, paste#`paste`\|paste]] | [[sed, split, awk#`sed`\|sed]]<br><br>[[sed, split, awk#`split`\|split]]<br><br>[[sed, split, awk#`awk`\|awk]] |
| -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |

---
## Create, Monitor and Terminate Processes

| [[ps, pstree, uptime, free#`ps`\|ps]]           <br><br>[[ps, pstree, uptime, free#`pstree`\|pstree]]<br><br>[[top]]<br><br>[[ps, pstree, uptime, free#`uptime`\|uptime]]<br><br>[[ps, pstree, uptime, free#`free`\|free]] | [[pgrep, kill, pkill, killall#`pgrep`\|pgrep]]     <br><br>[[pgrep, kill, pkill, killall#`kill`\|kill]]<br><br>[[pgrep, kill, pkill, killall#`pkill`\|pkill]]<br><br>[[pgrep, kill, pkill, killall#`killall`\|killall]] | [[jobs, fg, bg#`jobs`\|jobs]]      <br><br>[[jobs, fg, bg#`fg`\|fg]]<br><br>[[jobs, fg, bg#`bg`\|bg]] | [[nohup, screen, tmux#`nohup`\|nohup]]   <br><br>[[nohup, screen, tmux#`screen`\|screen]]<br><br>[[nohup, screen, tmux#`tmux`\|tmux]] | [[watch]] |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | --------- |

---
## Changing Process Execution Priorities

| [[nice, renice#`nice`\|nice]]<br><br>[[nice, renice#`renice`\|renice]] |
| ---------------------------------------------------------------------- |

---
## Searching text files with Regex

| [[grep, egrep, fgrep#`grep`\|grep]]<br><br>[[grep, egrep, fgrep#`egrep`\|egrep]]<br><br>[[grep, egrep, fgrep#`fgrep`\|fgrep]] |
| ----------------------------------------------------------------------------------------------------------------------------- |

---

## Using Streams and Diversions

| [[Diversions\|>]]<br><br>[[Diversions\|>>]]<br><br>[[Diversions#`<<`\|<<]]<br><br>[[Diversions\|<<<]] | [[STDIN, STDOUT, STDERR, tee#`STDIN`\|stdin]]<br><br>[[STDIN, STDOUT, STDERR, tee#`STDOUT`\|stdout]]<br><br>[[STDIN, STDOUT, STDERR, tee#`STDERR`\|stderr]]<br><br>[[STDIN, STDOUT, STDERR, tee#`tee`\|tee]] |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

---

## Create Partitions and File Systems

| Partitioning | Filesystem                                           |
| ------------ | ---------------------------------------------------- |
| [[fdisk]]    | [[mkfs]]<br><br>[[mke2fs]]<br><br>[[mkswap, swapon]] |

---

## Ensuring the Integrity of Filesystems

| [[du]]    <br><br>[[df]] | [[fsck]] | [[tune2fs]] | [[xfs_repair, xfs_db, xfs_fsr#<mark style="background ABF7F7A6;">xfs_repair</mark>\|xfs_repair]]<br><br>[[xfs_repair, xfs_db, xfs_fsr#<mark style="background ABF7F7A6;">xfs_db</mark>\|xfs_db]]<br><br>[[xfs_repair, xfs_db, xfs_fsr#<mark style="background ABF7F7A6;">xfs_fsr</mark>\|xfs_fsr]] |
| ------------------------ | -------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

---

## Mounting and Unmounting of Filesystems

| [[findmnt]]<br><br>[[fstab\|/etc/fstab]] | [[mount, umount#<mark style="background ABF7F7A6;">mount</mark>\|mount]]<br><br>[[mount, umount#<mark style="background ABF7F7A6;">umount</mark>\|umount]] |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
> - How to [[retrieve UUID of a partition]]
> - How to [[get systemctl status of a mount point]]

---

## [[Permissions]]

| [[chmod]] | [[chown]]<br><br>[[chgrp]] | [[umask]] |
| --------- | -------------------------- | --------- |

---

## [[Hardlinks and Softlinks|Symbolic Links in Linux]]

---

## Others

|                                          | Logging                         |
| ---------------------------------------- | ------------------------------- |
| [[ip]]<br><br>[[passwd]]<br><br>[[udev]] | [[dmesg]]<br><br>[[journalctl]] |

