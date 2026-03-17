
### Installation

```bash title:check_pdm_install.sh
#!/bin/bash

# Define the package name as the first argument
PACKAGE="pdm"

# Print the Python interpreter path
PYTHON_PATH=$(which python)
echo "Using Python interpreter: $PYTHON_PATH"

# Check if the package is installed
if python -m pip show $PACKAGE &> /dev/null; then
    echo "$PACKAGE is already installed"
else
    echo "$PACKAGE is not installed. Installing now..."
    python -m pip install $PACKAGE
    echo "$PACKAGE has been installed"
fi
```

---
### Create from scratch

```bash ln:False
$ pdm init
```

</br>

---

### Use an Existing PDM config

> [!note] 
> Set the venv folder to be created in the local cache dir instead of the project home dir.
> ```bash ln:False
> $ pdm config venv.in_project false
> ```

- create virtual environment
```bash ln:False
$ pdm venv create
```

- install dependencies
```bash ln:False
$ pdm install
```

---
### Activate Virtual Environment

```bash ln:False
$ eval $(pdm venv activate)
```

---
### Exit Virtual Environment

```bash ln:False
$ deactivate
```

---

### Remove Virtual Environment

```bash ln:False
$ pdm venv remove venv
```

---
### PDM Config Info

```bash ln:False
$ pdm info
PDM version:
  2.19.2
Python Interpreter:
  /home/jeswins/Downloads/my-project/.venv/bin/python (3.12)
Project Root:
  /home/jeswins/Downloads/my-project
Local Packages:
```

---

### PDM Virtual Env Info

```bash ln:False
$ pdm info --env
{
  "implementation_name": "cpython",
  "implementation_version": "3.12.6",
  "os_name": "posix",
  "platform_machine": "x86_64",
  "platform_release": "5.15.153.1-microsoft-standard-WSL2",
  "platform_system": "Linux",
  "platform_version": "#1 SMP Fri Mar 29 23:14:13 UTC 2024",
  "python_full_version": "3.12.6",
  "platform_python_implementation": "CPython",
  "python_version": "3.12",
  "sys_platform": "linux"
}
```