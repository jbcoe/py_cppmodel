import clang
import os
import py_cppmodel
import unittest
from parameterized import parameterized

from ctypes.util import find_library

from clang.cindex import TranslationUnit

COMPILER_ARGS = [
    "-x",
    "c++",
    "-std=c++20",
    "-I/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/c++/v1",
    "-I/Library/Developer/CommandLineTools/usr/include",
]


def _custom_name_func(testcase_func, _, param):
    return "%s_%s" % (testcase_func.__name__, parameterized.to_safe_name(param.args[0]))


class TestStandardLibraryIncludes(unittest.TestCase):
    @parameterized.expand(
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
        name_func=_custom_name_func,
    )
    def test_include(self, include):
        source = f"#include <{include}>"
        tu = TranslationUnit.from_source(
            "t.cc",
            COMPILER_ARGS,
            unsaved_files=[("t.cc", source)],
        )

        # This should not raise an exception.
        self.model = py_cppmodel.Model(tu)


if __name__ == "__main__":
    unittest.main()
