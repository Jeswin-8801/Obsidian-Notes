
Using the [[Anagram Example using unittest]] program below

> Directory Structure
```bash ln:False
project/
├── test.py
├── requirements.txt
├── my_scripts
│   ├── __init__.py
└── Makefile
```

```makefile title:Makefile
# Define variables
VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

# color
BLUE=\033[0;34m
NC=\033[0m

# Create virtual environment
create-venv:
	$(call print_message, "Starting Virtual Environment", "—")
	@echo -n ">>> $(BLUE)python -m venv $(VENV)$(NC)\n"
	@python -m venv $(VENV)
	@echo "Entering virtual environment..."

# Install dependencies
install-deps: create-venv
	$(call print_message, "Installing packages from requirements.txt", "—")
	@echo -n ">>> $(BLUE)pip install -q -r requirements.txt$(NC)\n"
	@$(PIP) install -q -r requirements.txt

# Linting
linting: install-deps
	$(call print_message, "Running linting", "—")
	@echo -n ">>> $(BLUE)flake8 . --ignore E305 --exclude $(VENV),.git,__pycache__ --max-line-length=90$(NC)\n"
	@$(PYTHON) -m flake8 . --ignore E305 --exclude $(VENV),.git,__pycache__ --max-line-length=90

# Run tests
test: install-deps
	$(call print_message, "Running Tests", "—")
	@echo -n ">>> $(BLUE)unittest test$(NC)\n"
	@$(PYTHON) -m unittest test
	@echo "$(NC)"

# Security benchmarks
security-check: test
	$(call print_message, "Running Security Checks", "—")
	@echo -n ">>> $(BLUE)bandit -r . -q -x ./$(VENV),./.git,./__pycache__$(NC)\n"
	@$(PYTHON) -m bandit -r . -q -x ./$(VENV),./.git,./__pycache__

finished: security-check
	$(call print_message, "FINISHED", "⁙")

# Default target
all: create-venv install-deps linting test security-check finished

define print_message
	$(eval MESSAGE_LEN := $(shell expr $(shell echo -n $(1) | wc -c) + 2))
	$(eval SCREEN_WIDTH := $(shell stty size | cut -d' ' -f2))
	$(eval PADDING_LEN := $(shell expr $(shell expr $(SCREEN_WIDTH) - $(MESSAGE_LEN)) / 2))
	$(eval PADDING_STR := $(shell expr $(shell seq -s$(2) $(PADDING_LEN) | tr -d '[:digit:]')))
	$(eval EXTRA_PADDING := $(if $(shell [ $$(($(shell expr $(MESSAGE_LEN) % 2) ^ $(shell expr $(SCREEN_WIDTH) % 2))) -eq 1 ] && echo 1), $(2)))
	@echo "\n"$(PADDING_STR) $(1) $(PADDING_STR)$(EXTRA_PADDING)"\n"
endef
```

> Checkout [[Environment Management|Virtual Environment using venv]]

```text title:requirements.txt
flake8
bandit
```

Inside the `project/` run

```bash ln:False
$ make all

—————————————————————— Starting Virtual Environment ———————————————————————

>>> python -m venv .venv
Entering virtual environment...

———————————————— Installing packages from requirements.txt ————————————————

>>> pip install -q -r requirements.txt

————————————————————————————— Running linting —————————————————————————————

>>> flake8 . --ignore E305 --exclude .venv,.git,__pycache__ --max-line-length=90

—————————————————————————————— Running Tests ——————————————————————————————

>>> unittest test
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK


————————————————————————— Running Security Checks —————————————————————————

>>> bandit -r . -q -x ./.venv,./.git,./__pycache__

⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙ FINISHED ⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙
```