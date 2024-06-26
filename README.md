# py_cppmodel

[![license][badge.license]][license] [![issues][badge.issues]][issues]
[![pre-commit][badge.pre-commit]][pre-commit]

[badge.license]: https://img.shields.io/badge/license-MIT-blue.svg
[badge.issues]: https://img.shields.io/github/issues/jbcoe/py_cppmodel.svg
[badge.pre-commit]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit

[license]: https://en.wikipedia.org/wiki/MIT_License
[issues]: http://github.com/jbcoe/py_cppmodel/issues
[pre-commit]: https://github.com/pre-commit/pre-commit

`py_cppmodel` is a Python wrapper around clang's python bindings to generate a
simple Python model of a C++ translation unit.

## Limitations

Currently the environment variable `PY_CPPMODEL_LIBCLANG_PATH` must be defined
to specify where libclang can be found. This may be fixed in the future.

## Testing

To run the tests, run:

```sh
python3 -m venv .venv           # Create a Python virtual env.
source ./.venv/bin/activate     # Activate the virtual env for bash by source.

mypy *.py --check-untyped-defs  # Run mypy to check type hints.
unittest discover .             # Run tests.
```

## Attribution

We've made considerable use of the following in putting this together:

* <http://szelei.me/code-generator>
* <http://blog.glehmann.net/2014/12/29/Playing-with-libclang>
* <http://eli.thegreenplace.net/tag/llvm-clang>

Design of the python bindings is taken from clang's cindex.

* <https://github.com/llvm-mirror/clang/tree/master/bindings/python>

Mistakes are our own.
