
# `zcat`

For `.gz` files.
> [[gzip, gunzip, bzip2, bunzip, xz, unxz#`gzip`|Checkout gzip]]

[[#Example]]
```bash
~$ zcat file.txt.gz
Hello World!
```

---
# `bzcat`

For `.bz2` files.

[[#Example]]
```bash
bzcat file.txt.bz2
Hello World!
```

---
# `xzcat`

For `.xz` files.

[[#Example]]
```bash
xzcat file.txt.xz
Hello World!
```

---

# Example
```bash
~$ ls
file.txt  file.txt.bz2  file.txt.gz  file.txt.xz
~$ cat file.txt
Hello World!
```