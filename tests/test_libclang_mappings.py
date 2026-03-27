"""
Tests to ensure all relevant libclang AST attributes are explicitly mapped in cppmodel.
"""

import inspect

import pytest
from clang.cindex import Cursor
from clang.cindex import TranslationUnit
from clang.cindex import Type as ClangType

import xyz.cppmodel

COMPILER_ARGS = [
    "-x",
    "c++",
    "-std=c++20",
]

SOURCE = """\
int z = 0;

class A {
  int a;
  void foo();
};
"""


@pytest.fixture
def model():
    tu = TranslationUnit.from_source(
        "sample.cc",
        COMPILER_ARGS,
        unsaved_files=[("sample.cc", SOURCE)],
    )
    return xyz.cppmodel.Model(tu)


def get_public_attributes(cls):
    """Returns a list of public attribute names for a given class."""
    return [name for name, _ in inspect.getmembers(cls) if not name.startswith("_")]


LIBCLANG_CURSOR_ATTRS = [attr for attr in get_public_attributes(Cursor) if attr not in ("data", "xdata")]

LIBCLANG_TYPE_ATTRS = [attr for attr in get_public_attributes(ClangType) if attr not in ("data", "xdata")]


def is_mapped(wrapper, attr):
    """Check if an attribute is accessible, handling exceptions from property evaluation."""
    if attr in dir(wrapper):
        return True
    try:
        getattr(wrapper, attr)
        return True
    except AttributeError:
        return False
    except BaseException:
        # Any other exception (AssertionError, Exception) means the property exists
        # but evaluation failed for this specific instance's state.
        return True


@pytest.mark.parametrize("attr", LIBCLANG_CURSOR_ATTRS)
def test_cursor_mappings(model, attr):
    """Ensure all public attributes of libclang's Cursor are accessible on cppmodel wrappers."""
    # Get different wrappers that mirror Cursor
    wrappers = [
        model.classes[0],  # Class
        model.classes[0].methods[0],  # Method
        model.classes[0].members[0],  # Member
        model.unmodelled_nodes[0],  # Unmodelled
    ]

    for wrapper in wrappers:
        assert is_mapped(wrapper, attr), f"Missing Cursor attribute '{attr}' on {type(wrapper).__name__}"


@pytest.mark.parametrize("attr", LIBCLANG_TYPE_ATTRS)
def test_type_mappings(model, attr):
    """Ensure all public attributes of libclang's Type are accessible on cppmodel's Type wrapper."""
    # Get a wrapper that mirrors Type
    type_wrapper = model.classes[0].members[0].type

    assert is_mapped(wrapper=type_wrapper, attr=attr), (
        f"Missing Type attribute '{attr}' on {type(type_wrapper).__name__}"
    )
