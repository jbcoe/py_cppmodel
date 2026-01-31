#!/usr/bin/env bash

# Install dependencies
uv sync

# Type checks
uv run mypy *.py --check-untyped-defs

# Unit tests
uv run python -m unittest discover --verbose .
