#!/usr/bin/env bash

# Install dependencies
uv sync

# Type checks
uv run ty check .

# Unit tests
uv run python -m unittest discover --verbose .
