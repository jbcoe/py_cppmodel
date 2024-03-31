#!/usr/bin/env bash

set -x


python3 -m venv .venv           # Create a Python virtual env
source ./.venv/bin/activate     # Activate the virtual env for bash by source.

mypy *.py --check-untyped-defs  # Run mypy to check type hints
unittest discover .             # Run tests
