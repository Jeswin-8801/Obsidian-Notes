
# `nl`

Show contents of a file with line numbers.

[[#Example]]

```bash
~/temp$ nl file.txt
     1  The Forgotten Umbrella:
     2  The umbrella leaned against the wall, its fabric faded and its handle chipped, waiting for rain that never came.

     3  Midnight Conversations:
     4  In the quiet hours, the moon whispered secrets to the owl, who hooted back in cryptic riddles.

     5  Lost Socks:
     .
     .
     .
```

> By default empty lines are not numbered

- `-b` stands for body numbering with style `a` (stands for all lines)
```bash
~/temp$ nl -b a file.txt
     1  The Forgotten Umbrella:
     2  The umbrella leaned against the wall, its fabric faded and its handle chipped, waiting for rain that never came.
     3
     4  Midnight Conversations:
     5  In the quiet hours, the moon whispered secrets to the owl, who hooted back in cryptic riddles.
     6
     7  Lost Socks:
    .
    .
    .
```

---
# `wc`

[[#Example]]

```bash
~$ wc file.txt
 14  97 625 file.txt
```
- `14` lines
-  `97` words
-  `625` bytes

`-l` for lines
```bash
~$ wc -l file.txt
14 file.txt
```

`-w` for words
```bash
~$ wc -w file.txt
97 file.txt
```

---

# `od`

Stands for `Octal Dump`. Dumps a file in the specified format.

> default format is Octal

```bash
~$ od file.txt
0000000 064124 020145 067506 063562 072157 062564 020156 066525
0000020 071142 066145 060554 005072 064124 020145 066565 071142
0000040 066145 060554 066040 060545 062556 020144 063541 064541
0000060 071556 020164 064164 020145 060567 066154 020054 072151
.
.
.
```

- To display the file as characters (`-c`)
```bash
~$ od -c file.txt
0000000   T   h   e       F   o   r   g   o   t   t   e   n       U   m
0000020   b   r   e   l   l   a   :  \n   T   h   e       u   m   b   r
0000040   e   l   l   a       l   e   a   n   e   d       a   g   a   i
0000060   n   s   t       t   h   e       w   a   l   l   ,       i   t
0000100   s       f   a   b   r   i   c       f   a   d   e   d       a
0000120   n   d       i   t   s       h   a   n   d   l   e       c   h
.
.
.
```

- To display the file as binary (`-b`)
```bash
~$ od -b file.txt
0000000 124 150 145 040 106 157 162 147 157 164 164 145 156 040 125 155
0000020 142 162 145 154 154 141 072 012 124 150 145 040 165 155 142 162
0000040 145 154 154 141 040 154 145 141 156 145 144 040 141 147 141 151
0000060 156 163 164 040 164 150 145 040 167 141 154 154 054 040 151 164
.
.
.
```

- To display the file as hexadecimal (`-h`)
- To display the file as ASCII (`-a`)

---

# Example
```
~$ cat file.txt
The Forgotten Umbrella:
The umbrella leaned against the wall, its fabric faded and its handle chipped, waiting for rain that never came.

Midnight Conversations:
In the quiet hours, the moon whispered secrets to the owl, who hooted back in cryptic riddles.

Lost Socks:
The laundry room harbored a conspiracy—the socks conspired to escape, one by one, leaving their partners bereft.

Coffee Shop Alchemy:
Baristas stirred dreams into lattes, and customers sipped inspiration with every foamy sip.

Library Ghosts:
The old librarian claimed she could hear the rustle of forgotten stories as she shelved books late at night.
```