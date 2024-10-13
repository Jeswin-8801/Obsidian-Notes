
**Generator functions** are a special kind of function that return a [lazy iterator](https://en.wikipedia.org/wiki/Lazy_evaluation). These are objects that you can loop over like a [list](https://realpython.com/python-lists-tuples/). However, unlike lists, lazy iterators do not store their contents in memory.

## Common Use cases

### 1. Reading Large Files
- using the function below for a file larger than the present memory, we would get the error `Memory Error`
```python
def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result
```

```bash title:output ln:false
Traceback (most recent call last):
  File "example.py", line 6, in csv_reader
    result = file.read().split("\n")
MemoryError
```

- Instead we can handle it using `yeild`
```python
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row
```

> [!note]
> - Using [[#`yeild`|yeild]] will result in a generator object.
> - Using `return` will result in the first line of the file _only_.

### 2. Generating an Infinite Sequence
- to get a finite sequence, you call [`range()`](https://realpython.com/python-range/) and evaluate it in a list context
```python
>>> a = range(5)
>>> list(a)
[0, 1, 2, 3, 4]
```

- Generating an **infinite sequence**, however, will require the use of a generator, since your computer memory is finite:
```python
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
```
- continues to print unless stopped manually
```python
>>> for i in infinite_sequence():
...     print(i, end=" ")
...
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
30 31 32 33 34 35 36 37 38 39 40 41 42
[...]
6157818 6157819 6157820 6157821 6157822 6157823 6157824 6157825 6157826 6157827
6157828 6157829 6157830 6157831 6157832 6157833 6157834 6157835 6157836 6157837
6157838 6157839 6157840 6157841 6157842
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyboardInterrupt
```
- another way to use the generator is using `next()`
```python
>>> gen = infinite_sequence()
>>> next(gen)
0
>>> next(gen)
1
>>> next(gen)
2
>>> next(gen)
3
```

### 3. Detecting Palindromes
```python
def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0
	
    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10
	
    if num == reversed_num:
        return num
    else:
        return False
```
- using the infinite sequence generator used above ([[#2. Generating an Infinite Sequence|infinite_sequence()]])
```python
>>> for i in infinite_sequence():
...     pal = is_palindrome(i)
...     if pal:
...         print(i)
...
11
22
33
[...]
99799
99899
99999
100001
101101
102201
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 5, in is_palindrome
KeyboardInterrupt
```

> [!note]
> In practice, you’re unlikely to write your own infinite sequence generator. The [`itertools`](https://realpython.com/python-itertools/) module provides a very efficient infinite sequence generator with `itertools.count()`.

---
## Building Generators With Generator Expressions

- functions the same way as [[List Compressions]]
- with the advantage of creating them without building and holding the entire object in memory before iteration.

```python
>>> nums_squared_lc = [num**2 for num in range(5)]
>>> nums_squared_gc = (num**2 for num in range(5))
```

```python
>>> nums_squared_lc
[0, 1, 4, 9, 16]
>>> nums_squared_gc
<generator object <genexpr> at 0x107fbbc78>
```

> [!note]
> If the list is smaller than the running machine’s available memory, then list comprehensions can be ==faster to evaluate== than the equivalent generator expression

Checkout [[cProfile#An example of performance monitoring for List Compressions list compression and Generators Building Generators With Generator Expressions generator compression|An example of performance monitoring for List Compressions list compression and Generators Building Generators With Generator Expressions generator compression]]

---
## `yeild`

Controls the flow of a generator function in a way that’s similar to `return` statements.

> When `yeild` is called, the program ==suspends function execution== and returns the yielded value to the caller. (In contrast, `return` stops function execution completely)

```python
def multi_yield():
	yield_str = "This will print the first string"
	yield yield_str
	yield_str = "This will print the second string"
	yield yield_str
```

```python ln:False
>>> multi_obj = multi_yield()
>>> print(next(multi_obj))
This will print the first string
>>> print(next(multi_obj))
This will print the second string
>>> print(next(multi_obj))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

- custom loop with finite generator
```python
>>> letters = ["a", "b", "c", "y"]
>>> it = iter(letters)
>>> while True:
...     try:
...         letter = next(it)
...     except StopIteration:
...         break
...     print(letter)
...
a
b
c
y
```

---

## send(), throw() and close()

#### `.send()` to send data to a generator

> using the [[#3. Detecting Palindromes|is_palindrome()]] function as an example below

- The program only yields a value once a palindrome is found.
```python
def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)
            if i is not None:
                num = i
        num += 1
```

- for `101` it sends `10^len(101)` to the generator which will compute a 4 digit palindrome.
```python
>>> pal_gen = infinite_palindromes()
>>> for i in pal_gen:
...     digits = len(str(i))
...     pal_gen.send(10 ** (digits))
...
101
1001
10001
100001
1000001
10000001
100000001
1000000001
10000000001
100000000001
1000000000001
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in infinite_palindromes
  File "<stdin>", line 8, in is_palindrome
KeyboardInterrupt
```

#### `.throw()` to raise generator exceptions

```python
>>> pal_gen = infinite_palindromes()
>>> for i in pal_gen:
...     print(i)
...     digits = len(str(i))
...     if digits == 5:
...         pal_gen.throw(ValueError("We don't like large palindromes"))
...     pal_gen.send(10 ** (digits))
...
11
101
111
1001
1111
10001
10101
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
  File "<stdin>", line 5, in infinite_palindromes
ValueError: We don't like large palindromes
```

#### `.close()` to stop a generator’s iteration

```python
>>> pal_gen = infinite_palindromes()
>>> for i in pal_gen:
...     print(i)
...     digits = len(str(i))
...     if digits == 5:
...         pal_gen.close()
...     pal_gen.send(10 ** (digits))
...
11
101
111
1001
1111
10001
10101
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
StopIteration
```


---
## Creating Data Pipelines With Generators

Data pipelines allow you to string together code to process large datasets or streams of data without maxing out your machine’s memory.
#### Example: Build a generator pipeline to efficiently process large CSV files

```python
file_name = "techcrunch.csv"
lines = (line for line in open(file_name))
list_line = (s.rstrip().split(",") for s in lines)
cols = next(list_line)
company_dicts = (dict(zip(cols, data)) for data in list_line)
funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)
total_series_a = sum(funding)
print(f"Total series A fundraising: ${total_series_a}")
```

- **Line 2** reads in each line of the file.
- **Line 3** splits each line into values and puts the values into a list.
- **Line 4** uses `next()` to store the column names in a list.
- **Line 5** creates dictionaries and unites them with a `zip()` call:
    - **The keys** are the column names `cols` from line 4.
    - **The values** are the rows in list form, created in line 3.
- **Line 6** gets each company’s series A funding amounts. It also filters out any other raised amount.
- **Line 11** begins the iteration process by calling `sum()` to get the total amount of series A funding found in the CSV.