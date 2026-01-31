#!/usr/bin/env bash

set -eu

# Install dependencies
uv sync

# Linting
uv run ruff check . --fix

# Type checks
uv run ty check .

# Unit tests
uv run pytest
