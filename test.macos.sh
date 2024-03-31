#!/usr/bin/env bash

# Virtual environment setup
python3 -m venv .venv           # Create a Python virtual env
source ./.venv/bin/activate     # Activate the virtual env for bash by source.
python3 -m pip install -r requirements.txt # Install latest requirements.

# Type checks
python3 -m mypy *.py --check-untyped-defs  # Run mypy to check type hints

# Unit tests
PY_CPPMODEL_LIBCLANG_PATH=/Library/Developer/CommandLineTools/usr/lib/libclang.dylib \
python3 -m unittest discover --verbose .             # Run tests
