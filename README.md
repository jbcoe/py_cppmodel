# py_cppmodel

`py_cppmodel` is a Python wrapper around clang's python bindings to generate a
simple Python model of a C++ translation unit.

## Limitations

Currently `clang.cindex.Config.set_library_path()` must be called before
attempting to load a translation unit. This is because the libclang shared
library is not in a standard location. This may be fixed in the future.

## Testing

To run the tests, run:

```sh
python3 -m venv .venv           # Create a Python virtual env
source ./.venv/bin/activate     # Activate the virtual env for bash by source.

mypy *.py --check-untyped-defs  # Run mypy to check type hints
unittest discover .             # Run tests
```
