
## `/bin` vs `/sbin` vs `/usr/bin` vs `/usr/sbin`

#### [`/bin`](http://www.pathname.com/fhs/pub/fhs-2.3.html#BINESSENTIALUSERCOMMANDBINARIES)

> For binaries usable before the `/usr` partition is mounted. This is used for trivial binaries used in the very early boot stage or ones that you need to have available in booting [[Single User Mode|single user mode]]. 


#### [`/usr/bin`](http://www.pathname.com/fhs/pub/fhs-2.3.html#USRBINMOSTUSERCOMMANDS)

> This is the primary directory of executable commands on the system.

- essentially, `/bin` contains executables which are required by the system for emergency repairs, booting, and [[Single User Mode|single user mode]]. 
- `/usr/bin` contains Application/distribution binaries meant to be accessed by locally logged in users

#### [`/sbin`](https://www.pathname.com/fhs/pub/fhs-2.3.html#SBINSYSTEMBINARIES)

> Binaries needed for booting, low-level system repair, or maintenance (`run level 1` or `S`)


#### [`/usr/sbin`](https://www.pathname.com/fhs/pub/fhs-2.3.html#SBINSYSTEMBINARIES)

> Application/distribution binaries that support or configure stuff in `/sbin`.


> [!IMPORTANT]
> [[⁄bin ⁄lib and ⁄sbin are now symlinks]]
