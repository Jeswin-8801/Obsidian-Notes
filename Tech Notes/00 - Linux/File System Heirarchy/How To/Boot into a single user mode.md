
## How to boot into a `single user` Mode from `GRUB`

To boot into `single user` mode you edit the boot instructions for the GRUB menu entry you wish to boot and add the kernel parameter/option `single`. Brief instructions for how to do this are given below.

1. Hold down the `left Shift` key while rebooting to bring up the GRUB menu
2. Select (highlight) the GRUB boot menu entry you wish to use.
3. Press `e` to edit the GRUB boot commands for the selected boot menu entry.
4. Look near the bottom of the list of commands for lines similar to

```
linux /boot/vmlinuz-3.2.0-24-generic root=UUID=bc6f8146-1523-46a6-8b\
6a-64b819ccf2b7 ro  quiet splash
initrd /boot/initrd.img-3.2.0-24-generic
```

5. Change the middle line in (4) by adding the kernel boot parameter `single` to the end of the line (i.e. after `ro quiet splash`).

For this example you would change:

```
6a-64b819ccf2b7 ro  quiet splash
```

to

```
6a-64b819ccf2b7 ro  quiet splash single
```

6. Press either `Ctrl+X` or `F10` to boot using these kernel options.


> [!NOTE] Note
> These changes are **not** persistent. 
> Any change to the kernel boot options made this way will only affect the next boot and only if you start that boot by pressing either `Ctrl+X` or `F10` while still in GRUB edit mode.
