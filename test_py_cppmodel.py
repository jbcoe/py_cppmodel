import clang
import os
import py_cppmodel
import unittest

from ctypes.util import find_library

LIBCLANG_PATH = os.environ.get("PY_CPPMODEL_LIBCLANG_PATH")
if not LIBCLANG_PATH:
    raise RuntimeError("PY_CPPMODEL_LIBCLANG_PATH is unset")

clang.cindex.Config.set_library_file(LIBCLANG_PATH)  # type: ignore

from clang.cindex import TranslationUnit

COMPILER_ARGS = [
    "-x",
    "c++",
    "-std=c++20",
    "-I/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/c++/v1",
    "-I/Library/Developer/CommandLineTools/usr/include",
]


class TestCppModel(unittest.TestCase):
    def setUp(self):
        tu = TranslationUnit.from_source(
            "sample.cc",
            COMPILER_ARGS,
        )
        self.model = py_cppmodel.Model(tu)

    def test_filename(self):
        self.assertEqual(self.model.filename, "sample.cc")

    def test_functions(self):
        self.assertEqual(len(self.model.functions), 2)
        self.assertEqual(
            str(self.model.functions[0]), "<py_cppmodel.Function double bar(double)>"
        )
        self.assertEqual(
            str(self.model.functions[1]), "<py_cppmodel.Function int main()>"
        )

    def test_classes(self):
        self.assertEqual(len(self.model.classes), 1)
        self.assertEqual(str(self.model.classes[0]), "<py_cppmodel.Class A>")

        self.assertEqual(len(self.model.classes[0].annotations), 1)
        self.assertEqual(self.model.classes[0].annotations[0], "A")

        self.assertEqual(len(self.model.classes[0].members), 3)
        self.assertEqual(
            str(self.model.classes[0].members[0]),
            "<py_cppmodel.Member <py_cppmodel.Type int> a>",
        )
        self.assertEqual(
            str(self.model.classes[0].members[1]),
            "<py_cppmodel.Member <py_cppmodel.Type double> b>",
        )
        self.assertEqual(
            str(self.model.classes[0].members[2]),
            "<py_cppmodel.Member <py_cppmodel.Type char[8]> c>",
        )

        self.assertEqual(len(self.model.classes[0].methods), 1)
        self.assertEqual(
            str(self.model.classes[0].methods[0]), "<py_cppmodel.Method int foo(int)>"
        )
        self.assertEqual(len(self.model.classes[0].methods[0].annotations), 1)
        self.assertEqual(self.model.classes[0].methods[0].annotations[0], "foo")

        self.assertEqual(len(self.model.unmodelled_nodes), 2)
        self.assertEqual(
            str(self.model.unmodelled_nodes[0]),
            "<py_cppmodel.Unmodelled z <SourceLocation file 'sample.cc', line 1, column 5>>",
        )
        self.assertEqual(
            str(self.model.unmodelled_nodes[1]),
            "<py_cppmodel.Unmodelled B<T> <SourceLocation file 'sample.cc', line 12, column 7>>",
        )


if __name__ == "__main__":
    unittest.main()
