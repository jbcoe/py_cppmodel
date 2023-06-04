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
python -m unittest discover -s .
```
