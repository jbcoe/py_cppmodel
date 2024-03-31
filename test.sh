#!/usr/bin/env bash

set -x


python3 -m venv .venv           # Create a Python virtual env
source ./.venv/bin/activate     # Activate the virtual env for bash by source.

python -m mypy *.py --check-untyped-defs  # Run mypy to check type hints
PY_CPPMODEL_LIBCLANG_PATH=/Library/Developer/CommandLineTools/usr/lib/libclang.dylib \
python -m unittest discover .             # Run tests
