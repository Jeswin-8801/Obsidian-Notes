---
tags:
  - INFO
  - Linux-Directories
---

All files from the directories in / will be merged into their respective counterparts in `/usr`, and `symlinks` for the old directories will be created instead.

```
/bin → /usr/bin
/sbin → /usr/sbin
/lib → /usr/lib
/lib64 → /usr/lib64
```

 [For more info checkout](https://www.freedesktop.org/wiki/Software/systemd/TheCaseForTheUsrMerge/)