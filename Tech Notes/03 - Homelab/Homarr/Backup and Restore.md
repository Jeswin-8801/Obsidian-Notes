---
tags: [homarr, kubernetes]
---

#### Backup DB

```bash ln:False
kubectl cp \
	homarr/$(kubectl -n homarr get pods | grep homarr | awk -F' ' '{print $1}'):/appdata/db/db.sqlite \
	./db.sqlite_backup
```

> if you see the message
> ```bash ln:False
> tar: removing leading '/' from member names
> ```
> It does not mean that the backed up file is a tar file.
> 
> When you use `kubectl cp`, it uses `tar` **under the hood** to transfer files between your machine and the pod.
> - On the **source side**, it runs `tar cf -` (archive to stdout)  
> - On the **destination side**, it runs `tar xf -` (extract from stdin)


</br>

#### Restore

```bash ln:False
kubectl cp \
	./db.sqlite_backup \
	homarr/$(kubectl -n homarr get pods | grep homarr | awk -F' ' '{print $1}'):/appdata/db/db.sqlite
```
