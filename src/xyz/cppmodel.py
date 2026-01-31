from typing import Any
from typing import List
from typing import Optional

from clang.cindex import AccessSpecifier as _AccessSpecifier
from clang.cindex import Cursor
from clang.cindex import CursorKind as _CursorKind
from clang.cindex import Diagnostic
from clang.cindex import ExceptionSpecificationKind as _ExceptionSpecificationKind
from clang.cindex import SourceLocation
from clang.cindex import TranslationUnit
from clang.cindex import TypeKind as _TypeKind

# Suppress type checking warnings for clang.cindex kinds.
AccessSpecifier: Any = _AccessSpecifier
CursorKind: Any = _CursorKind
ExceptionSpecificationKind: Any = _ExceptionSpecificationKind
TypeKind: Any = _TypeKind


def _get_annotations(cursor: Cursor) -> List[str]:
    return [c.displayname for c in cursor.get_children() if c.kind == CursorKind.ANNOTATE_ATTR]


class Unmodelled:
    def __init__(self, cursor: Cursor):
        self.location: SourceLocation = cursor.location
        self.name: str = cursor.displayname

    def __repr__(self) -> str:
        return "<xyz.cppmodel.Unmodelled {} {}>".format(self.name, self.location)


class Type:
    def __init__(self, cindex_type):
        self.kind = cindex_type.kind
        self.name = cindex_type.spelling
        self.is_pointer: bool = self.kind == TypeKind.POINTER
        self.is_reference: bool = self.kind == TypeKind.LVALUEREFERENCE
        self.is_const: bool = cindex_type.is_const_qualified()
        if self.is_pointer or self.is_reference:
            self.pointee: Optional[Type] = Type(cindex_type.get_pointee())
        else:
            self.pointee = None

    def __repr__(self) -> str:
        return "<xyz.cppmodel.Type {}>".format(self.name)


class Member:
    def __init__(self, cursor: Cursor):
        self.type: Type = Type(cursor.type)
        self.name: str = cursor.spelling

    def __repr__(self) -> str:
        return "<xyz.cppmodel.Member {} {}>".format(self.type, self.name)


class FunctionArgument:
    def __init__(self, type: Type, name: Optional[str] = None):
        self.type: Type = type
        self.name: Optional[str] = name or None

    def __repr__(self) -> str:
        if self.name is None:
            return "<xyz.cppmodel.FunctionArgument self.type.name>"
        return "<xyz.cppmodel.FunctionArgument {} {}>".format(self.type, self.name)


class _Function:
    def __init__(self, cursor):
        self.name: str = cursor.spelling
        arguments: List[Optional[str]] = [str(x.spelling) or None for x in cursor.get_arguments()]
        argument_types: List[Type] = [Type(x) for x in cursor.type.argument_types()]
        self.is_noexcept: bool = cursor.exception_specification_kind == ExceptionSpecificationKind.BASIC_NOEXCEPT
        self.return_type: Type = Type(cursor.type.get_result())
        self.arguments: List[FunctionArgument] = []
        self.annotations: List[str] = _get_annotations(cursor)

        for t, n in zip(argument_types, arguments, strict=False):
            self.arguments.append(FunctionArgument(t, n))

    def __repr__(self) -> str:
        r = "{} {}({})".format(
            self.return_type.name,
            str(self.name),
            ", ".join([a.type.name for a in self.arguments]),
        )
        if self.is_noexcept:
            r = r + " noexcept"
        return r


class Function(_Function):
    def __init__(self, cursor, namespaces: list[str] | None = None):
        namespaces = namespaces or []
        _Function.__init__(self, cursor)
        self.namespace: str = "::".join(namespaces)
        self.qualified_name: str = self.name
        if self.namespace:
            self.qualified_name = "::".join([self.namespace, self.name])

    def __repr__(self) -> str:
        s = _Function.__repr__(self)
        return "<xyz.cppmodel.Function {}>".format(s)

    def __eq__(self, f) -> bool:
        if self.name != f.name:
            return False
        if self.namespace != f.namespace:
            return False
        if len(self.arguments) != len(f.arguments):
            return False
        for x, fx in zip([arg.type for arg in self.arguments], [arg.type for arg in f.arguments], strict=False):
            if x.name != fx.name:
                return False
        return True


class Method(_Function):
    def __init__(self, cursor):
        _Function.__init__(self, cursor)
        self.is_const: bool = cursor.is_const_method()
        self.is_virtual: bool = cursor.is_virtual_method()
        self.is_pure_virtual: bool = cursor.is_pure_virtual_method()
        self.is_public: bool = cursor.access_specifier == AccessSpecifier.PUBLIC

    def __repr__(self) -> str:
        s = _Function.__repr__(self)
        if self.is_const:
            s = "{} const".format(s)
        if self.is_pure_virtual:
            s = "virtual {} = 0".format(s)
        elif self.is_virtual:
            s = "virtual {}".format(s)
        return "<xyz.cppmodel.Method {}>".format(s)


class Class:
    def __init__(self, cursor: Cursor, namespaces: List[str]):
        self.name: str = cursor.spelling
        self.namespace: str = "::".join(namespaces)
        self.qualified_name: str = self.name
        if self.namespace:
            self.qualified_name = "::".join([self.namespace, self.name])
        self.constructors: List[Method] = []
        self.methods: List[Method] = []
        self.members: List[Member] = []
        self.annotations = _get_annotations(cursor)
        self.base_classes = []
        # FIXME: populate these fields with AST info
        self.source_file = str(cursor.location.file)
        self.source_line = int(cursor.location.line)
        self.source_column = int(cursor.location.column)

        for c in cursor.get_children():
            if c.kind == CursorKind.CXX_METHOD and c.type.kind == TypeKind.FUNCTIONPROTO:
                self.methods.append(Method(c))
            elif c.kind == CursorKind.CONSTRUCTOR and c.type.kind == TypeKind.FUNCTIONPROTO:
                self.constructors.append(Method(c))
            elif c.kind == CursorKind.FIELD_DECL:
                self.members.append(Member(c))
            elif c.kind == CursorKind.CXX_BASE_SPECIFIER:
                self.base_classes.append(c.type.spelling)

    def __repr__(self) -> str:
        return "<xyz.cppmodel.Class {}>".format(self.name)


class Model:
    def __init__(self, translation_unit: TranslationUnit):
        """Create a model from a translation unit."""
        self.filename: str = translation_unit.spelling
        self.functions: List[Function] = []
        self.classes: List[Class] = []
        self.unmodelled_nodes: List[Unmodelled] = []
        # Keep a reference to the translation unit to prevent it from being garbage collected.
        self.translation_unit: TranslationUnit = translation_unit

        def is_error_in_current_file(diagnostic: Diagnostic) -> bool:
            if str(diagnostic.location.file) != str(translation_unit.spelling):
                return False
            if diagnostic.severity == Diagnostic.Error:
                return True
            if diagnostic.severity == Diagnostic.Fatal:
                return True
            return False

        errors: List[Diagnostic] = [d for d in translation_unit.diagnostics if is_error_in_current_file(d)]
        if errors:
            joined_errors = "\n".join(str(e) for e in errors)
            raise ValueError(f"Errors in source file:{joined_errors}")

        self._add_child_nodes(translation_unit.cursor, [])

    def __repr__(self) -> str:
        return "<xyz.cppmodel.Model filename={}, classes={}, functions={}>".format(
            self.filename,
            [c.name for c in self.classes],
            [f.name for f in self.functions],
        )

    def extend(self, translation_unit: TranslationUnit):
        # Extend an existing model with contents of a new translation unit.
        m = Model(translation_unit)
        # Check for duplicates and inconsistencies.
        for new_class in m.classes:
            is_new = True
            for old_class in self.classes:
                if new_class.qualified_name == old_class.qualified_name:
                    if new_class.source_file != old_class.source_file:
                        raise Exception(
                            "Class {} is defined in multiple locations: {} {}".format(
                                old_class.qualified_name,
                                old_class.source_file,
                                new_class.source_file,
                            )
                        )
                    # Move on as there can only be one match
                    is_new = False
                    break

            if is_new:
                self.classes.append(new_class)

        # We only look at declarations for functions so won't raise exceptions
        for new_function in m.functions:
            is_new = True
            for old_function in self.functions:
                if new_function == old_function:
                    is_new = False
                    break
            if is_new:
                self.functions.append(new_function)

    def _add_child_nodes(self, cursor: Any, namespaces: List[str] | None = None):
        namespaces = namespaces or []
        for c in cursor.get_children():
            try:
                _ = c.kind
            except ValueError:  # Handle unknown cursor kind
                # TODO(jbcoe): Fix cindex.py upstream to avoid needing to do this.
                continue
            if c.kind == CursorKind.CLASS_DECL or c.kind == CursorKind.STRUCT_DECL:
                if c.location.file.name == self.filename:
                    self.classes.append(Class(c, namespaces))
            elif c.kind == CursorKind.FUNCTION_DECL and c.type.kind == TypeKind.FUNCTIONPROTO:
                if c.location.file.name == self.filename:
                    self.functions.append(Function(c, namespaces))
            elif c.kind == CursorKind.NAMESPACE:
                child_namespaces = list(namespaces)
                child_namespaces.append(c.spelling)

                self._add_child_nodes(c, child_namespaces)
            else:
                if c.location.file.name == self.filename:
                    self.unmodelled_nodes.append(Unmodelled(c))
