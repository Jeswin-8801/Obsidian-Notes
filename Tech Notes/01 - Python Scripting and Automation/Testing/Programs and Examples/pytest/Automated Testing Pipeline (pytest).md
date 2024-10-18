
```text ln:False
my-project/
├── README.md
├── src
│   └── my_project/
│       ├── __init__.py
│       ├── leetcode.py
│       └── sorting_examples.py
├── pyproject.toml
├── Makefile
└── tests/
    ├── __init__.py
    ├── sort/
    │   ├── __init__.py
    │   ├── conftest.py
    │   └── test_benchmark.py
    └── leetcode/
        ├── __init__.py
        ├── conftest.py
        ├── test_roman_to_integer.py
        └── test_shortest_completing_word.py
```

> [!attention] 
> Checkout the entire project in the current parent folder in `my-project`

</br>

```makefile title:Makefile
# color
BLUE=\033[0;34m
NC=\033[0m

check-is-pdm-installed:
	$(call print_message, "Setting up PDM", "—")
	@echo "Using Python interpreter: $(BLUE)$(shell which python)$(NC)\n"
	@if python -m pip show pdm >/dev/null; then \
    	echo "$(BLUE)pdm$(NC) is already installed"; \
	else \
    	echo "$(BLUE)pdm$(NC) is not installed. Installing now..."; \
    	python -m pip install pdm; \
	fi

create-virtual-environment: check-is-pdm-installed
	$(call print_message, "Create Virtual Environment", "—")
	@if pdm venv activate >/dev/null 2>&1; then \
		echo "A virtual environment already exists. Skipping creation"; \
	else \
		echo ">>> $(BLUE)pdm venv create --name venv python$(NC)\n\n"; \
		pdm venv create --name venv python; \
	fi

install-dependencies: create-virtual-environment
	$(call print_message, "Installing dependencies", "—")
	@echo ">>> $(BLUE)pdm install$(NC)\n"
	@pdm install

linting: install-dependencies
	$(call print_message, "Running linting", "—")
	@echo ">>> $(BLUE)ruff check$(NC)\n"
	@$(shell pdm info --python) -m ruff check

# Run tests
test: install-dependencies
	$(call print_message, "Running Tests", "—")
	@echo -n ">>> $(BLUE)pytest -m leetcode$(NC)\n\n"
	@$(shell pdm info --python) -m pytest -m leetcode
	@echo -n "\n>>> $(BLUE)pytest -m \"sort_small or sort_large\" -q$(NC)\n\n"
	@$(shell pdm info --python) -m pytest -m "sort_small or sort_large" -q

# Security benchmarks
security-check: test
	$(call print_message, "Running Security Checks", "—")
	@echo -n ">>> $(BLUE)bandit -c pyproject.toml -r . -q$(NC)\n"
	@$(shell pdm info --python) -m bandit -c pyproject.toml -r . -q

finished: security-check
	$(call print_message, "FINISHED", "⁙")

# Default target
all: check-is-pdm-installed create-virtual-environment install-dependencies linting test security-check finished

define print_message
	$(eval MESSAGE_LEN := $(shell expr $(shell echo -n $(1) | wc -c) + 2))
	$(eval SCREEN_WIDTH := $(shell stty size | cut -d' ' -f2))
	$(eval PADDING_LEN := $(shell expr $(shell expr $(SCREEN_WIDTH) - $(MESSAGE_LEN)) / 2))
	$(eval PADDING_STR := $(shell expr $(shell seq -s$(2) $(PADDING_LEN) | tr -d '[:digit:]')))
	$(eval EXTRA_PADDING := $(if $(shell [ $$(($(shell expr $(MESSAGE_LEN) % 2) ^ $(shell expr $(SCREEN_WIDTH) % 2))) -eq 1 ] && echo 1), $(2)))
	@echo "\n"$(PADDING_STR) $(1) $(PADDING_STR)$(EXTRA_PADDING)"\n"
endef
```

- Checkout [[PDM]]

```bash ln:False
make all

————————————————————————————————————————————————————————————————————————————————————————————————————————————— Setting up PDM —————————————————————————————————————————————————————————————————————————————————————————————————————————————

Using Python interpreter: /usr/local/bin/python

pdm is already installed

——————————————————————————————————————————————————————————————————————————————————————————————————————— Create Virtual Environment ———————————————————————————————————————————————————————————————————————————————————————————————————————

>>> pdm venv create --name venv python


Virtualenv /home/jeswins/.local/share/pdm/venvs/my-project-HG2zNj1Y-venv is created successfully

———————————————————————————————————————————————————————————————————————————————————————————————————————— Installing dependencies —————————————————————————————————————————————————————————————————————————————————————————————————————————

>>> pdm install

WARNING: Lockfile does not exist
Updating the lock file...
INFO: Virtualenv /home/jeswins/.local/share/pdm/venvs/my-project-HG2zNj1Y-venv is reused.
Changes are written to pdm.lock.
  0:00:05 🔒 Lock successful.
Synchronizing working set with resolved packages: 15 to add, 0 to update, 0 to remove

  ✔ Install pluggy 1.5.0 successful
  ✔ Install packaging 24.1 successful
  ✔ Install mdurl 0.1.2 successful
  ✔ Install py-cpuinfo 9.0.0 successful
  ✔ Install iniconfig 2.0.0 successful
  ✔ Install pytest-benchmark 4.0.0 successful
  ✔ Install pbr 6.1.0 successful
  ✔ Install markdown-it-py 3.0.0 successful
  ✔ Install bandit 1.7.10 successful
  ✔ Install stevedore 5.3.0 successful
  ✔ Install pytest 8.3.3 successful
  ✔ Install pyyaml 6.0.2 successful
  ✔ Install rich 13.9.2 successful
  ✔ Install pygments 2.18.0 successful
  ✔ Install ruff 0.7.0 successful

  0:00:04 🎉 All complete! 15/15

———————————————————————————————————————————————————————————————————————————————————————————————————————————— Running linting —————————————————————————————————————————————————————————————————————————————————————————————————————————————

>>> ruff check

All checks passed!

————————————————————————————————————————————————————————————————————————————————————————————————————————————— Running Tests ——————————————————————————————————————————————————————————————————————————————————————————————————————————————

>>> pytest -m leetcode

=========================================================================================================== test session starts ============================================================================================================
platform linux -- Python 3.12.6, pytest-8.3.3, pluggy-1.5.0
benchmark: 4.0.0 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
rootdir: /home/jeswins/Downloads/my-project
configfile: pyproject.toml
plugins: benchmark-4.0.0
collected 16 items / 6 deselected / 10 selected

tests/leetcode/test_roman_to_integer.py .....                                                                                                                                                                                        [ 50%]
tests/leetcode/test_shortest_completing_word.py .....                                                                                                                                                                                [100%]

===================================================================================================== 10 passed, 6 deselected in 0.07s =====================================================================================================

>>> pytest -m "sort_small or sort_large" -q

......                                                                                                                                                                                                                               [100%]

------------------------------------------------------------------------------------------------- benchmark: 6 tests -------------------------------------------------------------------------------------------------
Name (time in ns)                    Min                     Max                  Mean                StdDev                Median                 IQR            Outliers  OPS (Kops/s)            Rounds  Iterations
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_quick_sort_large           210.9882 (1.0)       44,829.9979 (1.0)        348.5144 (1.07)       688.2908 (1.30)       316.9989 (1.0)        0.9895 (68.00)     91;6778    2,869.3217 (0.93)      40077           1
test_quick_sort_small           210.9882 (1.0)       64,919.0042 (1.45)       325.6774 (1.0)        527.7108 (1.0)        316.9989 (1.0)        0.0146 (1.0)      60;12214    3,070.5230 (1.0)       37532           1
test_insertion_sort_small       633.9978 (3.00)     133,538.9970 (2.98)       941.2043 (2.89)     1,309.8414 (2.48)       846.0047 (2.67)     105.0212 (>1000.0)  345;2141    1,062.4686 (0.35)      96507           1
test_bubble_sort_small          739.9940 (3.51)     171,707.9867 (3.83)       951.0848 (2.92)     1,356.0631 (2.57)       950.9968 (3.00)     105.9962 (>1000.0)   196;896    1,051.4309 (0.34)      59859           1
test_insertion_sort_large     1,162.9891 (5.51)      88,814.0057 (1.98)     1,901.4398 (5.84)     2,104.8851 (3.99)     1,585.9987 (5.00)     212.0069 (>1000.0)  313;6430      525.9173 (0.17)      34645           1
test_bubble_sort_large        1,267.9957 (6.01)      54,663.0035 (1.22)     1,733.9772 (5.32)     1,522.7893 (2.89)     1,585.9987 (5.00)     105.9962 (>1000.0)  568;3039      576.7089 (0.19)      25289           1
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
6 passed, 10 deselected in 2.12s

———————————————————————————————————————————————————————————————————————————————————————————————————————— Running Security Checks —————————————————————————————————————————————————————————————————————————————————————————————————————————

>>> bandit -c pyproject.toml -r . -q

⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙ FINISHED ⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙⁙
```

## Revert all extra files

> [[PDM#Remove Virtual Environment|Remove Virtual Environment]]

> Remove files and folders
```bash ln:False
$ rm -rf .pytest_cache/ src/my_project/__pycache__ tests/leetcode/__pycache__/ tests/sort/__pycache__/  tests/__pycache__/ .pdm-python .ruff_cache/ pdm.lock .benchmarks/ .ruff_cache/ .pytest_cache/ .venv/
```

