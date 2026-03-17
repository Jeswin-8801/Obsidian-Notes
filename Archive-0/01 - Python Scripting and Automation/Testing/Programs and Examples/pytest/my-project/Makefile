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