
</br>

Displays file system space usage.

```bash ln:False
$ df -h
Filesystem                         Size  Used Avail Use% Mounted on
tmpfs                              387M  1.6M  386M   1% /run
/dev/mapper/ubuntu--vg-ubuntu--lv  9.8G  4.2G  5.1G  46% /
tmpfs                              1.9G     0  1.9G   0% /dev/shm
tmpfs                              5.0M     0  5.0M   0% /run/lock
/dev/sda2                          1.8G   95M  1.6G   6% /boot
tmpfs                              387M   12K  387M   1% /run/user/1000                           396100      12    396088   1% /run/user/1000
```

> `-h` for human readable

</br>

- `-i` shows the corresponding <mark style="background: #D2B3FFA6;">Inodes</mark>
```bash ln:False
$ df -ih
Filesystem                        Inodes IUsed IFree IUse% Mounted on
tmpfs                               484K   891  483K    1% /run
/dev/mapper/ubuntu--vg-ubuntu--lv   640K   92K  549K   15% /
tmpfs                               484K     1  484K    1% /dev/shm
tmpfs                               484K     3  484K    1% /run/lock
/dev/sda2                           114K   317  114K    1% /boot
tmpfs                                97K    32   97K    1% /run/user/1000
```

> [!note] 
> - **inodes** are data structures used by the filesystem to store information about files and directories. It is a unique identifier for a file or directory in a filesystem.
> 
> <mark style="background: #D2B3FFA6;">Inodes</mark> contain metadata like:
> > - File type (regular file, directory, etc.)
> > - Permissions (read, write, execute)
> > - Owner and group
> > - Size of the file
> > - Timestamps (creation, modification, access)
> > - Pointers to the data blocks where the file’s content is stored