
# `gzip`

> [[#`gunzip`|gunzip]]
> [[zcat, bzcat, xzcat#`zcat`|zcat]]

```bash
~$ gzip file1.txt
~$ ls
file1.txt.gz
```

> [!Note]
> The above command does not keep the original file

```bash
~$ gzip file1.txt file2.txt
~$ ls
file1.txt.gz file2.txt.gz
```

- `-k` for keep
```bash
~$ gzip -k file*.txt
```

- `-d` for decompress >> [[#`gunzip`|gunzip]]
- `-v` for verbose
```bash
~$ gzip -dkv file*.txt.gz
file1.txt.gz:   -28.6% -- created file1.txt
file2.txt.gz:   -28.6% -- created file2.txt
file3.txt.gz:   -28.6% -- created file3.txt
~$ ls
file1.txt.gz  file2.txt.gz  file3.txt.gz  file1.txt  file2.txt  file3.txt
```

---
# `gunzip`

Alias for `gzip -d`.

- `-k` for keep
- `-v` for verbose
```bash
~$ gunzip -kv file1.txt.gz
file1.txt.gz:   -28.6% -- created file1.txt
```

---
# `bzip2`

> [[#`bunzip2`|bunzip2]]
> [[zcat, bzcat, xzcat#`bzcat`|bzcat]]

- `-k` for keep
- `-v` for verbose
```bash
~$ bzip2 -kv file*.txt
  file1.txt:  0.143:1, 56.000 bits/byte, -600.00% saved, 7 in, 49 out.
  file2.txt:  0.143:1, 56.000 bits/byte, -600.00% saved, 7 in, 49 out.
  file3.txt:  0.143:1, 56.000 bits/byte, -600.00% saved, 7 in, 49 out.
~$ ls
file1.txt  file2.txt  file3.txt  file1.txt.bz2  file2.txt.bz2  file3.txt.bz2
```

- `-d` for decompress >> [[#`bunzip2`|bunzip2]]
```bash
~$ bzip2 -dkv file*.txt.bz2
  file1.txt.bz2: done
  file2.txt.bz2: done
  file3.txt.bz2: done
```

---
# `bunzip2`

Alias for `bzip2 -d`.

- `-k` for keep
- `-v` for verbose
```bash
~$ bunzip2 -kv file1.txt.bz2
  file1.txt.bz2: done
```

---

# `xz`

> [[#`unxz`|unxz]]
> [[zcat, bzcat, xzcat#`xzcat`|xzcat]]

- `-k` for keep
- `-v` for verbose
```bash
~$ xz -kv file*.txt
file1.txt (1/3)
  100 %                  64 B / 7 B = 9.143

file2.txt (2/3)
  100 %                  64 B / 7 B = 9.143

file3.txt (3/3)
  100 %                  64 B / 7 B = 9.143
```
⬇️
```bash
~$ ls
file1.txt  file2.txt  file3.txt  file1.txt.xz  file2.txt.xz  file3.txt.xz
```

- `-d` for decompress >> [[#`unxz`|unxz]]
```bash
~$ xz -dkv file*.txt.xz
file1.txt.xz (1/3)
  100 %                  64 B / 7 B = 9.143

file2.txt.xz (2/3)
  100 %                  64 B / 7 B = 9.143

file3.txt.xz (3/3)
  100 %                  64 B / 7 B = 9.143
```

---
# `unxz`

Alias for `xz -d`.
- `-k` for keep
- `-v` for verbose
```bash
~$ unxz -kv file1.txt.xz
file1.txt.xz (1/1)
  100 %                  64 B / 7 B = 9.143
```