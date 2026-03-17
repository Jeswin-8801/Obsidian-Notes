
# `sort`

[[#Example Table]]

```bash
~$ sort table.csv
10,Isaiah,virginiaterrell@example.org,1964-09-20
11,Sheila,huangcathy@example.com,2008-03-20
12,Stacy,rayleroy@example.org,1980-10-20
13,Mandy,jefferynoble@example.org,2007-12-08
8,Ricardo,wyattbishop@example.com,1924-03-26
9,Dave,nmccann@example.net,2018-10-06
```

> By default sorts based on the first character

- numerical sort
```bash
8,Ricardo,wyattbishop@example.com,1924-03-26
9,Dave,nmccann@example.net,2018-10-06
10,Isaiah,virginiaterrell@example.org,1964-09-20
11,Sheila,huangcathy@example.com,2008-03-20
12,Stacy,rayleroy@example.org,1980-10-20
13,Mandy,jefferynoble@example.org,2007-12-08
```

- sort based on column 2
- `-t` stands for field separator
- `-k` stands for key (column number)
```bash
~$ sort -t ',' -k2 table.csv
9,Dave,nmccann@example.net,2018-10-06
10,Isaiah,virginiaterrell@example.org,1964-09-20
13,Mandy,jefferynoble@example.org,2007-12-08
8,Ricardo,wyattbishop@example.com,1924-03-26
11,Sheila,huangcathy@example.com,2008-03-20
12,Stacy,rayleroy@example.org,1980-10-20
```

---
# `uniq`

[[#Example Text File]]

```bash
$ uniq file.txt
Tomato
Banana
Apple
Banana
Tomato
```

- Along with count `-c`
```bash
$ uniq -c file.txt
      2 Tomato
      1 Banana
      3 Apple
      2 Banana
      1 Tomato
```

- Spaced grouping of same values
```bash
$ uniq --group file.txt
Tomato
Tomato

Banana

Apple
Apple
Apple

Banana
Banana

Tomato
```

---

# `tr`

Abbreviation for `translate`

> [!Note]
> Cannot be used alone.
> Must be used with a `|`

[[#Example Table]]

- remove
```bash
~$ cat table.csv | tr -d ','
11Sheilahuangcathy@example.com2008-03-20
8Ricardowyattbishop@example.com1924-03-26
12Stacyrayleroy@example.org1980-10-20
13Mandyjefferynoble@example.org2007-12-08
9Davenmccann@example.net2018-10-06
10Isaiahvirginiaterrell@example.org1964-09-20
```

- replace
```bash
~$ cat table.csv | tr ',' '\t'
11      Sheila  huangcathy@example.com  2008-03-20
8       Ricardo wyattbishop@example.com 1924-03-26
12      Stacy   rayleroy@example.org    1980-10-20
13      Mandy   jefferynoble@example.org        2007-12-08
9       Dave    nmccann@example.net     2018-10-06
10      Isaiah  virginiaterrell@example.org     1964-09-20
```

- case change
```bash
~$ cat table.csv | tr 'a-z' 'A-Z'
11,SHEILA,HUANGCATHY@EXAMPLE.COM,2008-03-20
8,RICARDO,WYATTBISHOP@EXAMPLE.COM,1924-03-26
12,STACY,RAYLEROY@EXAMPLE.ORG,1980-10-20
13,MANDY,JEFFERYNOBLE@EXAMPLE.ORG,2007-12-08
9,DAVE,NMCCANN@EXAMPLE.NET,2018-10-06
10,ISAIAH,VIRGINIATERRELL@EXAMPLE.ORG,1964-09-20
```

---

# `cut`

Removes sections from a file

[[#Example Table]]

- `-d` is the delimiter and `-f` determines the `Nth` selection
```bash
~$ cut -d ',' -f 2 table.csv
Sheila
Ricardo
Stacy
Mandy
Dave
Isaiah
```

- select multiple columns
```
~$ cut -d ',' -f 1,4 table.csv
11,2008-03-20
8,1924-03-26
12,1980-10-20
13,2007-12-08
9,2018-10-06
10,1964-09-20
```

> [!Note]
> By default, `\t` is considered as the delimiter.

---
# `paste`

[[#Example Text Files (2)]]

```bash
~$ paste paste1.txt paste2.txt
001     Monday
002     Tuesday
003     Wednesday
004     Thursday
005     Friday
```

---

# Example Table

```bash
~$ cat table.csv
11,Sheila,huangcathy@example.com,2008-03-20
8,Ricardo,wyattbishop@example.com,1924-03-26
12,Stacy,rayleroy@example.org,1980-10-20
13,Mandy,jefferynoble@example.org,2007-12-08
9,Dave,nmccann@example.net,2018-10-06
10,Isaiah,virginiaterrell@example.org,1964-09-20
```

# Example Text File

```bash
$ cat file.txt
Tomato
Tomato
Banana
Apple
Apple
Apple
Banana
Banana
Tomato
```

# Example Text Files (2)

```bash
$ cat paste1.txt paste2.txt
001
002
003
004
005
Monday
Tuesday
Wednesday
Thursday
Friday
```