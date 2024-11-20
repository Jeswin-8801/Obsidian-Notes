</br>

Used to set default permissions for newly created files and directories.

> It stands for <mark style="background: #D2B3FFA6;">“user file creation mode mask”</mark> and determines the permissions that are <mark style="background: #FF5582A6;">not</mark> set for new files and directories.

</br>

### How `umask` Works

When a new file or directory is created, it is assigned [[#Default Permissions]] and the <mark style="background: #D2B3FFA6;">umask</mark> value modifies these default permissions by masking out certain permission bits.

### Default Permissions

- **<mark style="background: #FFB86CA6; color: black;">Files</mark>**: Default permissions are `666` (read and write for everyone).
- **<mark style="background: #FFB86CA6; color: black;">Directories</mark>**: Default permissions are `777` (read, write, and execute for everyone).

The `umask` value is subtracted from the default permissions to determine the final permissions for new files and directories.

- viewing the current `umask` value:

```shell ln:False
$ umask
0002
```

### <mark style="background: #BBFABBA6;">Example</mark>

- setting the <mark style="background: #D2B3FFA6;">umask</mark> value
```shell ln:False
umask 022
```

If the `umask` value is `022`, the permissions for new files and directories will be:

- **<mark style="background: #FFB86CA6; color: black;">Files</mark>**: `666 - 022 = 644` (read and write for the owner, read-only for group and others).
- **<mark style="background: #FFB86CA6; color: black;">Directories</mark>**: `777 - 022 = 755` (read, write, and execute for the owner, read and execute for group and others).

### Persisting `umask` Settings

To make the `umask` setting persistent across sessions, add the `umask` command to:

- <mark style="background: #FFB86CA6; color: black;">/etc/login.defs</mark>
	- search for ==UMASK==, and modify the value
> *OR*
- your shell’s configuration file (e.g., `.bashrc`, `.profile`).