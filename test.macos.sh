#!/usr/bin/env bash

# Install dependencies
uv sync

# Type checks
uv run mypy *.py --check-untyped-defs

# Unit tests
PY_CPPMODEL_LIBCLANG_PATH=/Library/Developer/CommandLineTools/usr/lib/libclang.dylib \
uv run python -m unittest discover --verbose .
