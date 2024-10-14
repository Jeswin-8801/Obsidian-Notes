
</br>

## Using `sys.argv` to Build a Minimal CLI

- using the walrus operator in `line 4`, returns as well as assigns at the same time.
```python title:ls_argv.py {4}
import sys
from pathlib import Path

if (args_count := len(sys.argv)) > 2:
    print(f"One argument expected, got {args_count - 1}")
    raise SystemExit(2)
elif args_count < 2:
    print("You must specify the target directory")
    raise SystemExit(2)

target_dir = Path(sys.argv[1])

if not target_dir.is_dir():
    print("The target directory doesn't exist")
    raise SystemExit(1)

for entry in target_dir.iterdir():
    print(entry.name)
```
- running the script
```bash ln:False
$ python ls_argv.py sample/
hello.txt
lorem.md
realpython.md

$ python ls_argv.py
You must specify the target directory

$ python ls_argv.py sample/ other_dir/
One argument expected, got 2

$ python ls_argv.py non_existing/
The target directory doesn't exist
```

> Checkout [[sys#Accessing Command Line Arguments|sys.argv]]

</br>

## Using `argparse`

```python title:ls_argparse.py hl:1,4,6,8
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument("path")

args = parser.parse_args()

target_dir = Path(args.path)

if not target_dir.exists():
    print("The target directory doesn't exist")
    raise SystemExit(1)

for entry in target_dir.iterdir():
    print(entry.name)
```

1. Import `argparse`.
2. Create an **argument parser** by instantiating [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser).
3. Add **arguments** and **options** to the parser using the [`.add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument) method.
4. Call [`.parse_args()`](https://docs.python.org/3/library/argparse.html?highlight=argparse#argparse.ArgumentParser.parse_args) on the parser to get the [`Namespace`](https://docs.python.org/3/library/argparse.html#namespace) of arguments.

> Requires a lot less code.
> `argparse` automatically checks the presence of arguments for you.

```bash ln:False
$ python ls_argparse.py sample/
lorem.md
realpython.md
hello.txt

$ python ls_argparse.py
usage: ls_argparse.py [-h] path
ls_argparse.py: error: the following arguments are required: path

$ python ls_argparse.py sample/ other_dir/
usage: ls_argparse.py [-h] path
ls_argparse.py: error: unrecognized arguments: other_dir/

$ python ls_argparse.py non_existing/
The target directory doesn't exist
```

The program also accepts an optional `-h` flag.

```bash ln:False
$ python ls_argparse.py -h
usage: ls.py [-h] path

positional arguments:
  path

options:
  -h, --help  show this help message and exit
```

<mark style="background: #BBFABBA6;">Therefore, <mark style="background: #FFF3A3A6;color:black">argparse</mark> is objectively better than <mark style="background: #FFF3A3A6;color:black">sys.argv</mark></mark>