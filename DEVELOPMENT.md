# Developer Guide

## Using pre-commit for git hooks

This repository uses the Python `pre-commit` library to manage git hook run as
part of the commit process.  Use the following steps from the project root to
install a virtual environment with pre-commmit set up, and then use precommit to
install git hooks it to your local repository:

```bash
uv sync                         # Install dependencies
uv run pre-commit install       # Use pre-commit to install git hooks into the working repository.
```

pre-commit is configured with .pre-commit-config.yaml which contains some
additional documentation.
