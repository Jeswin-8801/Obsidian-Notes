
The `lost+found` directory in Linux is ==a special directory that stores files that have been lost or deleted, or have become obsolete==. It's created by the [[fsck]] file system check tool when a file system is created, or when a system crash or other issue causes file corruption.

---

The `lost+found` directory contains files that have been deleted or lost in a disk operation. **The files inside this directory have an [_inode_](https://man7.org/linux/man-pages/man7/inode.7.html), but they’re missing the corresponding filename that normally enables us to access files on the system.**

In rare cases, when a process opens a file for an operation, and somehow another process deletes the file when it’s still being used by the old process, it becomes just a data fragment. So, when there’s an improper shutdown or a kernel panic while the data is being used by the process, the data becomes obsolete.

> **Since the references to the file no longer exist and the file is no longer accessible normally, `fsck` turns the data back into a new file and deposits it in the `lost+found` directory.**