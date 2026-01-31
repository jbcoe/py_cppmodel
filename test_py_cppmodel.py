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

SOURCE = """\
int z = 0;

struct __attribute__((annotate("A"))) A {
  int a;
  double b;
  char c[8];

  __attribute__((annotate("foo"))) int foo(int);
};

template <class T>
class B {
  T t;
  T wibble(T);
};

double bar(double);

int main() {}
"""


@pytest.fixture
def model():
    tu = TranslationUnit.from_source(
        "sample.cc",
        COMPILER_ARGS,
        unsaved_files=[("sample.cc", SOURCE)],
    )
    return py_cppmodel.Model(tu)


def test_filename(model):
    assert model.filename == "sample.cc"


def test_functions(model):
    assert len(model.functions) == 2
    assert str(model.functions[0]) == "<py_cppmodel.Function double bar(double)>"
    assert str(model.functions[1]) == "<py_cppmodel.Function int main()>"


def test_classes(model):
    assert len(model.classes) == 1
    assert str(model.classes[0]) == "<py_cppmodel.Class A>"

    assert len(model.classes[0].annotations) == 1
    assert model.classes[0].annotations[0] == "A"


def test_class_members(model):
    assert len(model.classes[0].members) == 3
    assert str(model.classes[0].members[0]) == "<py_cppmodel.Member <py_cppmodel.Type int> a>"
    assert str(model.classes[0].members[1]) == "<py_cppmodel.Member <py_cppmodel.Type double> b>"
    assert str(model.classes[0].members[2]) == "<py_cppmodel.Member <py_cppmodel.Type char[8]> c>"

    assert len(model.classes[0].methods) == 1
    assert str(model.classes[0].methods[0]) == "<py_cppmodel.Method int foo(int)>"
    assert len(model.classes[0].methods[0].annotations) == 1
    assert model.classes[0].methods[0].annotations[0] == "foo"


def test_unmodelled_nodes(model):
    assert len(model.unmodelled_nodes) == 2
    assert (
        str(model.unmodelled_nodes[0])
        == "<py_cppmodel.Unmodelled z <SourceLocation file 'sample.cc', line 1, column 5>>"
    )
    assert (
        str(model.unmodelled_nodes[1])
        == "<py_cppmodel.Unmodelled B<T> <SourceLocation file 'sample.cc', line 12, column 7>>"
    )
