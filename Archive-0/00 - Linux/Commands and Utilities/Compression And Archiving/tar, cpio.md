
# `tar`

Used to create archives.

```bash
~$ tar -cf file.tar file1.txt file2.txt
~$ ls
file1.txt  file2.txt  file.tar
```
- `-c` stands for create
- `-f` used to specify the name of archive

> [!Note]
> Once `-f` is specified, the archive name must be specified right after
> Therefore, for the above example, `-fc` would not work

- list the contents of an archive (`-t`)
```bash
~$ tar -tf file.tar
file1.txt
file2.txt
```

- add files to an existing archive (`-r`)
```bash
~$ tar -rf file.tar file3.txt
~$ tar -tf file.tar
file1.txt
file2.txt
file3.txt
```

> [!Note]
> We can also create nested archives

- To extract an archive (`-x`)
```bash
~$ tar -xf file.tar
```

- extract and show the contents being extracted using `-v` (verbose)
```bash
~$ tar -xvf file.tar
file1.txt
file2.txt
file3.txt
```

### Compress archives

- `gzip` compression
```bash
~$ tar -czf file.tar.gz file1.txt file2.txt
~$ ls
file1.txt  file2.txt  file.tar.gz
```

- view contents of `gzip` compressed archive
```bash
~$ tar -tzf file.tar.gz
file1.txt
file2.txt
```

- extract
```bash
~$ tar -xzvf file.tar.gz
file1.txt
file2.txt
```

- `bzip2` compression
- `-v` option can be used in both compression and extraction
```bash
~$ tar -cjvf file.tar.bz2 file1.txt file2.txt
file1.txt
file2.txt
```

```bash
~$ tar -tjf file.tar.bz2
file1.txt
file2.txt
```

```bash
~$ tar -xjvf file.tar.bz2
file1.txt
file2.txt
```

- `xz` compression
```bash
~$ tar -cJvf file.tar.xz file1.txt file2.txt
file1.txt
file2.txt
```

```bash
~$ tar -tJf file.tar.xz
file1.txt
file2.txt
```

```bash
~$ tar -xJvf file.tar.xz
file1.txt
file2.txt
```

---
- [[sed, split, awk#`awk`|Learn about awk]]
```bash
~$ ls -lh file* | awk '{printf("%-10s %s\n", $5, $9)}'
7          file1.txt
7          file2.txt
7          file3.txt
10K        file.tar
162        file.tar.bz2
151        file.tar.gz
196        file.tar.xz
```

```bash
~$ file file*
file1.txt:    ASCII text
file2.txt:    ASCII text
file3.txt:    ASCII text
file.tar:     POSIX tar archive (GNU)
file.tar.bz2: bzip2 compressed data, block size = 900k
file.tar.gz:  gzip compressed data, from Unix, original size modulo 2^32 10240
file.tar.xz:  XZ compressed data, checksum CRC64
```

---
# `cpio`

copy files to and from archives

- create archive
- `-o` copy out mode
```bash
~$ ls file[1,2]*
file1.txt  file2.txt
```
⬇️
```bash
~$ ls file[1,2]* | cpio -o > file.cpio
1 block
```

- list contents of archive (`-t`)
```bash
~$ cpio -t < file.cpio
file1.txt
file2.txt
1 block
```

- `-i` copy in mode
```bash
~$ cpio -i < file.cpio
1 block
```

- `-p` copy pass mode
- `-d` create directory if it does not exist
```bash
$ find . | cpio -pd ./test
24 blocks
```
- copies all files in current directory to `/test`

> [!Note]
> `-p` is the same as the copy command `cp`

