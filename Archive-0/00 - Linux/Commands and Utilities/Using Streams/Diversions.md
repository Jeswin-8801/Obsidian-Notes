
# `<<`

Allows to pass multiline strings.

```bash
~$ wc -l << HEREDOC
> one
> two
> three
> four
> HEREDOC
4
```

> [!Note]
> `HEREDOC` can be any name and upon finishing, the same name must be specified

---
# `<<<`

Allows to pass variables

```bash
~$ VARIABLE=test
~$ tr 'a-z' 'A-Z' <<< $VARIABLE
TEST
```
> [[sort, uniq, tr, cut, paste#`tr`|Learn about tr here]]

---

# `>`

Appends content to a file. If the file already exists, the contents are overwritten.

---

# `>>`

Appends content to a file. (Does not overwrite and only appends)