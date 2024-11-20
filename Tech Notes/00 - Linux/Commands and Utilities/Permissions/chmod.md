</br>

Stands for <mark style="background: #D2B3FFA6;">change file mode</mark>. Used to change permissions of files and directories.

> Checkout [[Permissions]].

</br>

## Symbolic Mode

In symbolic mode, you use letters to represent permissions and categories.

```sh ln:False
chmod u+r,g-w,o+x filename
```

- `u+r`: Adds read permission for the user.
- `g-w`: Removes write permission for the group.
- `o+x`: Adds execute permission for others.

</br>

## Numeric (Octal) Mode

In numeric mode, permissions are represented by a three-digit octal number. Each digit represents a category (user, group, others) and is the sum of:

- **<mark style="background: #FFB86CA6; color: black;">4</mark>**: Read
- **<mark style="background: #FFB86CA6; color: black;">2</mark>**: Write
- **<mark style="background: #FFB86CA6; color: black;">1</mark>**: Execute

```sh ln:False
chmod 755 filename
```

- User: `7` (read, write, execute)
- Group: `5` (read, execute)
- Others: `5` (read, execute)

---

</br>

## Other Options

**<mark style="background: #FFB86CA6; color: black;">Recursive (-R)</mark>**:
Apply changes to all files and directories within a directory.

```sh ln:False
chmod -R 755 directory
```

</br>

## Example

```sh ln:False hl:4
$ touch abc.txt
$ ll abc.txt
-rw-rw-r-- 1 jeswins jeswins 0 Nov 20 08:15 abc.txt
$ chmod u+rwx,g-w abc.txt
$ ll abc.txt
-rwxr--r-- 1 jeswins jeswins 0 Nov 20 08:15 abc.txt*
```

```sh ln:False
chmod 744 abc.txt
```
> *can also be written as*
```sh ln:False
chmod u=rwx,g=r,o=r abc.txt
```







