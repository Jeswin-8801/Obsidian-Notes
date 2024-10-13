
# Regex

![[Pasted image 20240930122732.png]]

> [!Important]
> [Quick brush up on regex](https://github.com/ziishaned/learn-regex)

---
# `grep`

- search for pattern in a file
```bash
~$ grep jeswin /etc/passwd
jeswins:x:1000:1000:Jeswin:/home/jeswins:/bin/bash
```

- Negation (pattern not in) `-v`
```bash
~$ grep -v nologin /etc/passwd
root:x:0:0:root:/root:/bin/bash
sync:x:4:65534:sync:/bin:/bin/sync
dhcpcd:x:100:65534:DHCP Client Daemon,,,:/usr/lib/dhcpcd:/bin/false
pollinate:x:102:1::/var/cache/pollinate:/bin/false
tss:x:106:108:TPM software stack,,,:/var/lib/tpm:/bin/false
jeswins:x:1000:1000:Jeswin:/home/jeswins:/bin/bash
```

- with line numbers `-n`
```bash
~$ grep -vn nologin /etc/passwd
1:root:x:0:0:root:/root:/bin/bash
5:sync:x:4:65534:sync:/bin:/bin/sync
21:dhcpcd:x:100:65534:DHCP Client Daemon,,,:/usr/lib/dhcpcd:/bin/false
24:pollinate:x:102:1::/var/cache/pollinate:/bin/false
29:tss:x:106:108:TPM software stack,,,:/var/lib/tpm:/bin/false
34:jeswins:x:1000:1000:Jeswin:/home/jeswins:/bin/bash
```

- print only the matching output `-o`
```bash
~$ grep -o '[Jj]es[a-z]*' /etc/passwd
jeswins
Jeswin
jeswins
```

- ignore case `-i`
```bash
~$ grep -oi jeswin /etc/passwd
jeswin
Jeswin
jeswin
```

- Extended regular expression usage `-E`
- For characters like `|` which bash considers as pipe and `+`
 ***OR*** [[grep, egrep, fgrep#`egrep`|egrep]]
 
---

# `egrep`

For grep using extended regular expressions.

*example text*
```
~$ cat regex.txt
This.is.an.example.
{This|is|an|example|too}
[One/More/Example]
aAbBcCdDeEfF
a1b2c3456yYuU987
this is one more example with numbers 1, 2, 3 and 4
wonderful
wonderwoman
```

```bash
~$ egrep 'wonder(ful|woman)$' regex.txt
wonderful
wonderwoman
```

- Not containing `}`, `]`, or `.` at the end of the string.
```bash
~$ egrep -v '(}|]|\.)$' regex.txt
aAbBcCdDeEfF
a1b2c3456yYuU987
this is one more example with numbers 1, 2, 3 and 4
wonderful
wonderwoman
```

---

# `fgrep`

Searches for exactly what is given as the pattern, therefore all regex provided will be considered as patterns to be matched.

```bash
~$ fgrep -no '|too}' regex.txt
2:|too}
```



