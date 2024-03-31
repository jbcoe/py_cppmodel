#!/usr/bin/env bash

# Virtual environment setup
python3 -m venv .venv           # Create a Python virtual env
source ./.venv/bin/activate     # Activate the virtual env for bash by source.

# Type checks
python -m mypy *.py --check-untyped-defs  # Run mypy to check type hints

Unit tests
PY_CPPMODEL_LIBCLANG_PATH=/Library/Developer/CommandLineTools/usr/lib/libclang.dylib \
python -m unittest discover --verbose .             # Run tests
