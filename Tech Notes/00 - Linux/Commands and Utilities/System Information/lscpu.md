
Displays Information about the CPU architecture.

```shell ln:False
$ lscpu
Architecture:             x86_64
  CPU op-mode(s):         32-bit, 64-bit
  Address sizes:          45 bits physical, 48 bits virtual
  Byte Order:             Little Endian
CPU(s):                   2
  On-line CPU(s) list:    0,1
  
...(Truncated)
```


> ```shell ln:False
> $ lscpu | grep -iE "(architecture|^cpu\(s\)|model name|thread|core)"
> Architecture:                         x86_64
> CPU(s):                               2
> Model name:                           Intel(R) Core(TM) i5-10210U CPU @ 1.60GHz
> Thread(s) per core:                   1
> Core(s) per socket:                   1
> ```

</br>

> [!info] 
> Checkout [[List all ls commands]]
