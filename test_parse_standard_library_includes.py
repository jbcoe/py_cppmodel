import pytest
from clang.cindex import TranslationUnit

import py_cppmodel

COMPILER_ARGS = [
    "-x",
    "c++",
    "-std=c++20",
    "-I/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/c++/v1",
    "-I/Library/Developer/CommandLineTools/usr/include",
]


@pytest.mark.parametrize(
    "include",
    [
        "algorithm",
        "any",
        "array",
        "deque",
        "forward_list",
        "functional",
        "iterator",
        "list",
        "map",
        "memory",
        "numeric",
        "optional",
        "queue",
        "set",
        "stack",
        "string",
        "tuple",
        "type_traits",
        "unordered_map",
        "unordered_set",
        "utility",
        "variant",
        "vector",
    ],
)
def test_include(include):
    source = f"#include <{include}>"
    tu = TranslationUnit.from_source(
        "t.cc",
        COMPILER_ARGS,
        unsaved_files=[("t.cc", source)],
    )

    # This should not raise an exception.
    py_cppmodel.Model(tu)
