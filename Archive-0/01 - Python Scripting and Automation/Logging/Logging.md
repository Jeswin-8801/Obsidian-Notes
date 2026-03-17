
```python ln:False
>>> import logging
>>> logging.warning("Remain calm!")
WARNING:root:Remain calm!
```

- `root` is the name the `logging` module gives to its default logger

| Log Level  | Function             | Description                                                                |
| ---------- | -------------------- | -------------------------------------------------------------------------- |
| `DEBUG`    | `logging.debug()`    | Provides detailed information that’s valuable to you as a developer.       |
| `INFO`     | `logging.info()`     | Provides general information about what’s going on with your program.      |
| `WARNING`  | `logging.warning()`  | Indicates that there’s something you should look into.                     |
| `ERROR`    | `logging.error()`    | Alerts you to an unexpected problem that’s occured in your program.        |
| `CRITICAL` | `logging.critical()` | Tells you that a serious error has occurred and may have crashed your app. |
```python ln:False
>>> logging.debug("This is a debug message")

>>> logging.info("This is an info message")

>>> logging.warning("This is a warning message")
WARNING:root:This is a warning message

>>> logging.error("This is an error message")
ERROR:root:This is an error message

>>> logging.critical("This is a critical message")
CRITICAL:root:This is a critical message
```

> [!note]
> the `debug()` and `info()` messages didn’t get logged because, by default, the logging module logs the messages with a severity level of `WARNING` or above

```python ln:False
>>> import logging

>>> logging.basicConfig(level=logging.DEBUG)
>>> logging.debug("This will get logged.")
DEBUG:root:This will get logged.
```

|Constant|Numeric Value|String Value|
|---|---|---|
|`logging.DEBUG`|`10`|`DEBUG`|
|`logging.INFO`|`20`|`INFO`|
|`logging.WARNING`|`30`|`WARNING`|
|`logging.ERROR`|`40`|`ERROR`|
|`logging.CRITICAL`|`50`|`CRITICAL`|

# Formatting

```python ln:False
>>> import logging
>>> logging.basicConfig(format="%(levelname)s:%(name)s:%(message)s")
>>> logging.warning("Hello, Warning!")
WARNING:root:Hello, Warning!
```

- adding timestamps
```python ln:False
>>> import logging
>>> logging.basicConfig(
...     format="{asctime} - {levelname} - {message}",
...     style="{",
...     datefmt="%Y-%m-%d %H:%M",
... )

>>> logging.error("Something went wrong!")
2024-07-22 09:26 - ERROR - Something went wrong!
```

> displaying variable data

```python ln:False
>>> name = "Samara"
>>> logging.debug(f"{name=}")
2024-07-22 14:49 - DEBUG - name='Samara'
```


# Logging to a File

```python ln:False
>>> import logging
>>> logging.basicConfig(
...     filename="app.log",
...     encoding="utf-8",
...     filemode="a",
...     format="{asctime} - {levelname} - {message}",
...     style="{",
...     datefmt="%Y-%m-%d %H:%M",
... )

>>> logging.warning("Save me!")
```

```text title:app.log
2024-07-22 09:55 - WARNING - Save me!
```


# Capturing Stack Traces

[Exception information](https://realpython.com/python-exceptions/) can be captured if the `exc_info` parameter is passed as `True`.

```python ln:False
>>> import logging
>>> logging.basicConfig(
...     filename="app.log",
...     encoding="utf-8",
...     filemode="a",
...     format="{asctime} - {levelname} - {message}",
...     style="{",
...     datefmt="%Y-%m-%d %H:%M",
... )

>>> donuts = 5
>>> guests = 0
>>> try:
...     donuts_per_guest = donuts / guests
... except ZeroDivisionError:
...     logging.error("DonutCalculationError", exc_info=True)
...
```


# Using Handlers

Used to configure custom loggers.
*For example, when you want to send the log messages to different destinations like the standard output stream or a file.*

> [!note] 
> A logger that you create can have one or more handlers. That means you can send your logs to multiple places when they’re generated.

- declaring multiple handlers
```python ln:False
>>> import logging
>>> logger = logging.getLogger(__name__)
>>> console_handler = logging.StreamHandler()
>>> file_handler = logging.FileHandler("app.log", mode="a", encoding="utf-8")
```
> The `StreamHandler` sends logs to the console
> The `FileHandler` sends logs to a file

- using the logger
```python ln:False
>>> logger.addHandler(console_handler)
>>> logger.addHandler(file_handler)
>>> formatter = logging.Formatter(
...    "{asctime} - {levelname} - {message}",
...     style="{",
...     datefmt="%Y-%m-%d %H:%M",
... )

>>> console_handler.setFormatter(formatter)
>>> logger.warning("Stay calm!")
2024-07-22 15:58 - WARNING - Stay calm!

>>> logger.handlers
[
  <StreamHandler <stderr> (NOTSET)>,
  <FileHandler /Users/RealPython/Desktop/app.log (NOTSET)>
]
```

- Note that the logging level is not set for the handlers
```python ln:False
>>> console_handler.setLevel("DEBUG")
>>> file_handler.setLevel("WARNING")
>>> logger.handlers
[
  <StreamHandler <stderr> (DEBUG)>,
  <FileHandler /Users/RealPython/Desktop/app.log (WARNING)>
]
```

```text title:app.log
Stay calm!
```
