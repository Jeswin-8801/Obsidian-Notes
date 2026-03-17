
# `sed`

Stream Editor

[[#Example Table]]

- replace
```bash
~$ sed 's/Male/Female/g' table.csv
Index,First Name,Sex,Date of birth
9,Dave,Female,2018-10-06
10,Isaiah,Female,1964-09-20
11,Sheila,Female,2008-03-20
12,Stacy,Female,1980-10-20
13,Mandy,Female,2007-12-08
```

- replace remove
```bash
~$ sed 's/Female//g' table.csv
Index,First Name,Sex,Date of birth
9,Dave,Male,2018-10-06
10,Isaiah,Male,1964-09-20
11,Sheila,,2008-03-20
12,Stacy,Male,1980-10-20
13,Mandy,Male,2007-12-08
```

- use extended regular expressions
```bash
~$ sed -E 's/(Male|Famale)/Apple/g' table.csv
Index,First Name,Sex,Date of birth
9,Dave,Apple,2018-10-06
10,Isaiah,Apple,1964-09-20
11,Sheila,Apple,2008-03-20
12,Stacy,Apple,1980-10-20
13,Mandy,Apple,2007-12-08
```

- replaces only on the `Nth` line
```bash
~$ sed '5s/1/ $ /g' table.csv
Index,First Name,Sex,Date of birth
9,Dave,Male,2018-10-06
10,Isaiah,Male,1964-09-20
11,Sheila,Female,2008-03-20
 $ 2,Stacy,Male, $ 980- $ 0-20
13,Mandy,Male,2007-12-08
```

- print lines `1`, `4-6`
```bash
~$ sed -n '1p;4,6p' table.csv
Index,First Name,Sex,Date of birth
11,Sheila,Female,2008-03-20
12,Stacy,Male,1980-10-20
13,Mandy,Male,2007-12-08
```

- print all matching lines that end with `nologin` (`p` stands for pattern)
```bash
~$ sed -n '/nologin$/p' /etc/passwd
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
games:x:5:60:games:/usr/games:/usr/sbin/nologin
.
.
.
```

- delete all lines that end with `nologin` (`d` stands for delete)
```bash
~$ sed '/nologin$/d' /etc/passwd
root:x:0:0:root:/root:/bin/bash
sync:x:4:65534:sync:/bin:/bin/sync
dhcpcd:x:100:65534:DHCP Client Daemon,,,:/usr/lib/dhcpcd:/bin/false
pollinate:x:102:1::/var/cache/pollinate:/bin/false
tss:x:106:108:TPM software stack,,,:/var/lib/tpm:/bin/false
jeswins:x:1000:1000:Jeswin:/home/jeswins:/bin/bash
```

---
# `split`

[[#Example Table]]

- Splits the file into multiple files of 10 bits each
- `-b` stands for bits
```bash
~$ split -b 10 table.csv
```
⬇️
```bash
~$ ls
table.csv  xaa  xab  xac  xad  xae  xaf  xag  xah  xai  xaj  xak  xal  xam  xan  xao  xap  xaq
```
⬇️
```bash
~$ cat xaa
Index,Firs
~$ cat xab
t Name,Sex
```
⬇️
```bash
~$ cat xa*
Index,First Name,Sex,Date of birth
9,Dave,Male,2018-10-06
10,Isaiah,Male,1964-09-20
11,Sheila,Female,2008-03-20
12,Stacy,Male,1980-10-20
13,Mandy,Male,2007-12-08
```

---

# `awk`

Manipulate or extract data, generate reports, match patterns, perform calculations, and more.

[[#Example Table]]

- print all lines
```bash
~$ awk '{ print }' table.csv
Index,First Name,Sex,Date of birth
9,Dave,Male,2018-10-06
10,Isaiah,Male,1964-09-20
11,Sheila,Female,2008-03-20
12,Stacy,Male,1980-10-20
13,Mandy,Male,2007-12-08
```

> [!Note]
> Default field separator is `\t`

```bash
~$ awk -F ',' '{ print $2 }' table.csv
First Name
Dave
Isaiah
Sheila
Stacy
Mandy
```

```bash
~$ awk -F ',' '{ printf("%-15s %s\n", $2, $4) }' table.csv
First Name      Date of birth
Dave            2018-10-06
Isaiah          1964-09-20
Sheila          2008-03-20
Stacy           1980-10-20
Mandy           2007-12-08
```

[For more info](https://www.redhat.com/sysadmin/beginners-guide-gawk)

---

# Example Table

```bash
~$ cat table.csv
Index,First Name,Sex,Date of birth
9,Dave,Male,2018-10-06
10,Isaiah,Male,1964-09-20
11,Sheila,Female,2008-03-20
12,Stacy,Male,1980-10-20
13,Mandy,Male,2007-12-08
```