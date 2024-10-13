
## The major subdirectories of the `/usr` directory

```
 /usr/
  ├── bin/
 *├── css/
  ├── include/
  ├── lib/
  ├── lib64/
  ├── local/
  ├── sbin/
  ├── share/
  └── src/
```

| `/usr/bin`     | [[⁄bin and ⁄sbin#[`/usr/bin`](http //www.pathname.com/fhs/pub/fhs-2.3.html USRBINMOSTUSERCOMMANDS)\|About /usr/bin]]                                                                                                  |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/usr/ccs`     | Contains unbundled development package binaries.                                                                                                                                                                      |
| `/usr/include` | Contains include, or header files for `C programs`.                                                                                                                                                                   |
| `/usr/lib`     | [[⁄lib and related directories#[/usr/lib](https //refspecs.linuxfoundation.org/FHS_3.0/fhs/ch04s06.html)\|About /usr/lib]]                                                                                            |
| `/usr/local`   | [[⁄opt and ⁄usr⁄local#`/usr/local`\|About /usr/local]]                                                                                                                                                                |
| `/usr/sbin`    | Contains utilities used in system administration, including System Management Interface Tool (SMIT) commands. Most of the commands that once resided in the `/etc` directory now reside in the `/usr/sbin` directory. |
| `/usr/share`   | [[#`/usr/share`\|About /usr/share]]                                                                                                                                                                                   |
| `/usr/src`     | Contains the Linux header files, kernel sources, and documentation                                                                                                                                                    |

---

## `/usr/share`

- The `/usr/share` directory contains architecture-independent shareable text files. 
- The contents of this directory can be shared by all machines, regardless of hardware architecture.

The `/usr/share` directory includes the following subdirectories:

```
 /usr/share/
  ├── man/
  ├── dict/
  ├── lib/
  └── lpp/
```

| `/usr/share/man`  | Contains the manual pages if they have been loaded                                            |
| ----------------- | --------------------------------------------------------------------------------------------- |
| `/usr/share/dict` | Contains the spelling dictionary and its indexes                                              |
| `/usr/share/lib`  | Contains architecture-independent data files, including terminfo, learn, tmac, me, and macros |
| `/usr/share/lpp`  | Contains data and information about optionally installable products on the system             |
