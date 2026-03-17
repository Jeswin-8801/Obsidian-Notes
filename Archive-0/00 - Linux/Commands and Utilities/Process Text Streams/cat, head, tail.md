
# `cat`

```bash
~$ cat file1
Hello
```

- List multiple file contents at once
```bash
~$ cat file1 file2
Hello
World!
```

---

# `head`

```bash
~$ head /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
```

> By default prints first 10 lines

- print file name `-v` (verbose) and only the first `n` lines (`-n`)
```bash
~$ head -vn 3 /etc/passwd
==> /etc/passwd <==
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
```

---

# `tail`

- print file name `-v` (verbose) and only the last `n` lines (`-n`)
```bash
~$ tail -vn 3 /etc/passwd
==> /etc/passwd <==
usbmux:x:108:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
sshd:x:109:65534::/run/sshd:/usr/sbin/nologin
jeswins:x:1000:1000:Jeswin:/home/jeswins:/bin/bash
```

- Continuous update of last line from file (`-f)
```bash
~$ tail -f /var/log/dpkg.log
2024-10-01 06:07:59 status unpacked vim:amd64 2:9.1.0016-1ubuntu7.3
2024-10-01 06:07:59 status half-configured vim:amd64 2:9.1.0016-1ubuntu7.3
2024-10-01 06:07:59 status installed vim:amd64 2:9.1.0016-1ubuntu7.3
2024-10-01 06:07:59 configure vim-tiny:amd64 2:9.1.0016-1ubuntu7.3 <none>
2024-10-01 06:07:59 status unpacked vim-tiny:amd64 2:9.1.0016-1ubuntu7.3
2024-10-01 06:07:59 status half-configured vim-tiny:amd64 2:9.1.0016-1ubuntu7.3
2024-10-01 06:07:59 status installed vim-tiny:amd64 2:9.1.0016-1ubuntu7.3
2024-10-01 06:07:59 trigproc man-db:amd64 2.12.0-4build2 <none>
2024-10-01 06:07:59 status half-configured man-db:amd64 2.12.0-4build2
2024-10-01 06:08:04 status installed man-db:amd64 2.12.0-4build2
.
.
.
```