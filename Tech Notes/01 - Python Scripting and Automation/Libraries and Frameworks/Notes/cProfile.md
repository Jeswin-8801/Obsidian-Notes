Helps collect detailed runtime statistics

[Software profiling](https://en.wikipedia.org/wiki/Profiling_(computer_programming)) is the process of collecting and analyzing various metrics of a running program to identify performance bottlenecks known as **hot spots**. These hot spots can happen due to a number of reasons, including excessive memory use, inefficient CPU utilization, or a suboptimal data layout, which will result in frequent [cache misses](https://en.wikipedia.org/wiki/CPU_cache#Cache_miss) that increase [latency](https://en.wikipedia.org/wiki/Latency_(engineering)).

##### An example of performance monitoring for [[List Compressions|list compression]] and [[Generators#Building Generators With Generator Expressions|generator compression]]

```python
>>> import cProfile
>>> cProfile.run('sum([i * 2 for i in range(10000)])')
         5 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.001    0.001 <string>:1(<listcomp>)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


>>> cProfile.run('sum((i * 2 for i in range(10000)))')
         10005 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    10001    0.002    0.000    0.002    0.000 <string>:1(<genexpr>)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
        1    0.001    0.001    0.003    0.003 {built-in method builtins.sum}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

---
Checkout [[List Directory Tree#Comparing Getting a Directory Listing `os.listdir()` os.listdir() and Getting a Directory Listing `os.scandir()` os.scandir()|Comparing the performance of os.listdir() and os.scandir()]]

---

> checkout [Profiling in Python: How to Find Performance Bottlenecks – Real Python](https://realpython.com/python-profiling/)

---

