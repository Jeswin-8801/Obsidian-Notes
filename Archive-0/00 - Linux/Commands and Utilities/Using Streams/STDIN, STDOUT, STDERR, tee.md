
# `STDIN`

Standard Input Stream

Is referred to by the number `0`

> `<` is used to pass information and is considered the standard input stream

```bash
~$ wc -w < output.txt
11
~$ wc -w <0 output.txt
11 output.txt
~$ wc -w 0< output.txt
11
```
> [[nl, wc, od#`wc`|Learn more about wc]]

> [!Note]
> `<` is the same as `0<`


---
# `STDOUT`

Standard Output Stream

Is referred to by the number `1`

> `>` is used to pass information and is considered the standard output stream

```bash
~$ ls / 1> output.txt
```
⬇️
```bash
~$ cat output.txt
bin
bin.usr-is-merged
boot
cdrom
dev
.
.
.
```

> [!Note]
> The above command is the same as `ls / > output.txt`
> i.e. `>` by default used the STDOUT stream

---
# `STDERR`

Is referred to by the number `2`

```bash
~$ ls -? 2> output.txt
```
⬇️
```bash
~$ cat output.txt
ls: invalid option -- '?'
Try 'ls --help' for more information.
```

- using multiple channels
```bash
~$ ll > list.txt 2> error.txt
```

- Both the output of `ls -la`, as well as the errors from the error channel is stored in `output.txt`
```bash
~$ ls -la > output.txt 2>&1
```

---
# `tee`

Reads the standard input and writes it to both the standard output and one or more files

```bash
~$ find / -maxdepth 1 -type l | tee output.txt
/lib
/sbin
/lib64
/bin
```
⬇️
```
~$ cat output.txt
/lib
/sbin
/lib64
/bin
```