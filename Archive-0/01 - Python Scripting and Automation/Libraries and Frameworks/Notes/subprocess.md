---
tags:
  - tempFile
  - bash
  - cmd
  - pwsh
  - stdio
---

## Timer Example Program

```python title:timer.py
from argparse import ArgumentParser
from time import sleep

parser = ArgumentParser()
parser.add_argument("time", type=int)
args = parser.parse_args()
print(f"Starting timer of {args.time} seconds")
for _ in range(args.time):
    print(".", end="", flush=True)
    sleep(1)
print("Done!")
```

- `_` used as a throwaway variable because its value is not used in the loop

Checkout [[argparse vs sys.argv#Using `argparse`|argparse]]

> output
![[20240503192909_timer_gif.gif]]

```python  ln:False
>>> import subprocess
>>> subprocess.run(["python", "timer.py", "5"])
Starting timer of 5 seconds
.....Done!
CompletedProcess(args=['python', 'timer.py', '5'], returncode=0)
```

With the Python `subprocess` module, you have to break up the command into tokens manually. But, we can use `shlex` to help out with this
```python ln:False
>>> import subprocess, shlex
>>> subprocess.run(shlex.split('python timer.py 5'))
```

```python ln:False
>>> shlex.split("echo 'Hello, World!'")
['echo', 'Hello, World!']
```

> [!warning] 
> `shlex` does not work well with Windows as it is POSIX compatible

> [!note] 
> With `subprocess`, you can call any desktop based application.
> ```python ln:False
> >>> subprocess.run([code])
> ```

The process has a return code that indicates failure, but it doesn’t raise an <mark style="background: #FF5582A6;">exception</mark>. Typically, when a `subprocess` process fails, you’ll always want an exception to be raised, which you can do by passing in a `check=True` argument.

```python ln:False
>>> import subprocess
>>> completed_process = subprocess.run(["python", "timer.py"])
usage: timer.py [-h] time
timer.py: error: the following arguments are required: time

>>> completed_process.returncode
2
```

```python ln:False
>>> completed_process = subprocess.run(
...     ["python", "timer.py"],
...     check=True
... )
...
usage: timer.py [-h] time
timer.py: error: the following arguments are required: time
Traceback (most recent call last):
  ...
subprocess.CalledProcessError: Command '['python', 'timer.py']' returned
                               non-zero exit status 2.
```
> The `CalledProcessError` is raised as soon as the subprocess runs into a non-zero return code.

- `TimeoutExpired` for Processes That Take Too Long
```python ln:False {6}
>>> import subprocess
>>> subprocess.run(["python", "timer.py", "5"], timeout=1)
Starting timer of 5 seconds
.Traceback (most recent call last):
  ...
subprocess.TimeoutExpired: Command '['python', 'timer.py', '5']' timed out after 1.0 seconds
```

---
## Exception Handling

> example of how you might handle the three main exceptions raised by the `subprocess` module.
```python {7,9,14}
import subprocess

try:
    subprocess.run(
        ["python", "timer.py", "5"], timeout=10, check=True
    )
except FileNotFoundError as exc:
    print(f"Process failed because the executable could not be found.\n{exc}")
except subprocess.CalledProcessError as exc:
    print(
        f"Process failed because did not return a successful return code. "
        f"Returned {exc.returncode}\n{exc}"
    )
except subprocess.TimeoutExpired as exc:
    print(f"Process timed out.\n{exc}")
```


## `subprocess` With UNIX-Based Shells

```python ln:False
>>> import subprocess
>>> subprocess.run(["bash", "-c", "ls /usr/bin | grep pycode"])
pycodestyle
pycodestyle-3
pycodestyle-3.10
CompletedProcess(args=['bash', '-c', 'ls /usr/bin | grep pycode'], returncode=0)
```
- `-c` flag stands for _command_
alternatively
- The `shell=True` argument uses `["sh", "-c", ...]` behind the scenes
```python ln:False
>>> subprocess.run(["ls /usr/bin | grep pycode"], shell=True)
```


## `subprocess` With Windows Shells

```python ln:False
>>> import subprocess
>>> subprocess.run(["pwsh", "-Command", "ls C:\RealPython"])

    Directory: C:\RealPython

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---            09/05/22    10:41            237 basics.py
-a---            18/05/22    17:28            486 hello_world.py

CompletedProcess(args=['pwsh', '-Command', 'ls'], returncode=0)
```

- for CMD
```python ln:False
>>> subprocess.run(["cmd", "/c", "dir C:\RealPython"])
```

---
## Communication With Processes using Standard I/O Streams

#### Example program

```python title:magic_number.py
from random import randint

print(randint(0, 1000))
```

- use `capture_output=True` to grab the output
```python ln:False
>>> import subprocess
>>> magic_number_process  = subprocess.run(
...     ["python", "magic_number.py"], capture_output=True
... )
>>> magic_number_process .stdout
b'769\n'
```
> returns a byte object

```python ln:False
>>> import subprocess
>>> sum(
...     int(
...         subprocess.run(
...             ["python", "magic_number.py"], capture_output=True
...         ).stdout
...     )
...     for _ in range(2)
... )
1085
```
> runs the `magic_number.py` script twice, captures its output each time, converts it to an integer, and then sums those two integers.

---
## Decoding of Standard Streams

```python ln:False
>>> magic_number_process = subprocess.run(
...     ["python", "magic_number.py"], capture_output=True, encoding="utf-8"
... )
...
>>> magic_number_process.stdout
'647\n'
```
> returns a string object

---

## Using Pipes

```python ln:False
>>> ls_process = subprocess.run(
... 	["ls", "/usr/bin"],
... 	stdout = subprocess.PIPE,
... )
>>> grep_process = subprocess.run(
... 	["grep", "zip"],
... 	input = ls_process.stdout,
... 	capture_output=True
... )
>>> print(grep_process.stdout.decode("utf-8"))
bunzip2
bzip2
bzip2recover
funzip
gpg-zip
gunzip
gzip
streamzip
unzip
unzipsfx
zipdetails
zipgrep
zipinfo
...
```

Alternatively, we can use Temporary Files

```python ln:False
>>> import subprocess
>>> from tempfile import TemporaryFile
>>> with TemporaryFile() as f:
...     ls_process = subprocess.run(["ls", "/usr/bin"], stdout = f)
...     f.seek(0)
...     grep_process = subprocess.run(
...         ["grep", "zip"], stdin = f, stdout = subprocess.PIPE
...     )
...
0
>>> print(grep_process.stdout.decode("utf-8"))
bunzip2
bzip2
bzip2recover
funzip
gpg-zip
gunzip
gzip
streamzip
unzip
unzipsfx
zipdetails
zipgrep
zipinfo
```

- `f.seek(0)` moves the file pointer back to the start of the file so that `grep_process` can read its contents from the beginning

---

## `subprocess.pOpen()`

When compared to `run()`, rather than waiting until the process is finished, it’ll run the process in parallel.

```python title:popen_pipe.py
import subprocess

ls_process = subprocess.Popen(["ls", "/usr/bin"], stdout=subprocess.PIPE)
grep_process = subprocess.Popen(
    ["grep", "zip"], stdin=ls_process.stdout, stdout=subprocess.PIPE
)

for line in grep_process.stdout:
    print(line.decode("utf-8").strip())
```

```bash ln:False
$ python popen_pipe.py
bunzip2
bzip2
bzip2recover
funzip
gpg-zip
gunzip
gzip
streamzip
unzip
unzipsfx
zipdetails
zipgrep
zipinfo
```

> [!note] 
> `run()` returns a `CompletedProcess` object, while the `Popen()` constructor returns a `Popen` object

A good example use case of using `pOpen()` over `run()` is [[Dynamically Interact with a Process|Reaction Game Program example]]