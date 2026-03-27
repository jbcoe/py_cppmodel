"""
Base classes that mirror libclang AST objects to provide self-documenting APIs.

This module contains `_CursorMirror` and `_TypeMirror`, which explicitly map
all relevant properties and methods from `clang.cindex.Cursor` and
`clang.cindex.Type`.

By inheriting from these classes, `cppmodel` wrappers natively expose the full
power of `libclang` while remaining discoverable by IDEs and type-checkers.
"""

from typing import Any

from clang.cindex import Cursor
from clang.cindex import Type as _ClangType


class _CursorMirror:
    _cursor: Cursor

    @property
    def access_specifier(self) -> Any:
        return self._cursor.access_specifier

    @property
    def availability(self) -> Any:
        return self._cursor.availability

    @property
    def brief_comment(self) -> Any:
        return self._cursor.brief_comment

    @property
    def canonical(self) -> Any:
        return self._cursor.canonical

    @property
    def displayname(self) -> Any:
        return self._cursor.displayname

    @property
    def location(self) -> Any:
        return self._cursor.location

    @property
    def type(self) -> Any:
        return self._cursor.type

    @property
    def kind(self) -> Any:
        return self._cursor.kind

    def enum_type(self) -> Any:
        return self._cursor.enum_type

    @property
    def enum_value(self) -> Any:
        return self._cursor.enum_value

    @property
    def exception_specification_kind(self) -> Any:
        return self._cursor.exception_specification_kind

    @property
    def extent(self) -> Any:
        return self._cursor.extent

    @property
    def hash(self) -> Any:
        return self._cursor.hash

    @property
    def lexical_parent(self) -> Any:
        return self._cursor.lexical_parent

    @property
    def linkage(self) -> Any:
        return self._cursor.linkage

    @property
    def mangled_name(self) -> Any:
        return self._cursor.mangled_name

    @property
    def objc_type_encoding(self) -> Any:
        return self._cursor.objc_type_encoding

    @property
    def raw_comment(self) -> Any:
        return self._cursor.raw_comment

    @property
    def referenced(self) -> Any:
        return self._cursor.referenced

    @property
    def result_type(self) -> Any:
        return self._cursor.result_type

    @property
    def semantic_parent(self) -> Any:
        return self._cursor.semantic_parent

    @property
    def spelling(self) -> Any:
        return self._cursor.spelling

    @property
    def storage_class(self) -> Any:
        return self._cursor.storage_class

    @property
    def tls_kind(self) -> Any:
        return self._cursor.tls_kind

    @property
    def translation_unit(self) -> Any:
        return self._cursor.translation_unit

    @property
    def underlying_typedef_type(self) -> Any:
        return self._cursor.underlying_typedef_type

    def from_cursor_result(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.from_cursor_result(*args, **kwargs)

    def from_location(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.from_location(*args, **kwargs)

    def from_result(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.from_result(*args, **kwargs)

    def get_arguments(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.get_arguments(*args, **kwargs)

    def get_bitfield_width(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.get_bitfield_width(*args, **kwargs)

    def get_children(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.get_children(*args, **kwargs)

    def get_definition(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.get_definition(*args, **kwargs)

    def get_field_offsetof(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.get_field_offsetof(*args, **kwargs)

    def get_included_file(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.get_included_file(*args, **kwargs)

    def get_num_template_arguments(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.get_num_template_arguments(*args, **kwargs)

    def get_template_argument_kind(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.get_template_argument_kind(*args, **kwargs)

    def get_template_argument_type(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.get_template_argument_type(*args, **kwargs)

    def get_template_argument_unsigned_value(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.get_template_argument_unsigned_value(*args, **kwargs)

    def get_template_argument_value(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.get_template_argument_value(*args, **kwargs)

    def get_tokens(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.get_tokens(*args, **kwargs)

    def get_usr(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.get_usr(*args, **kwargs)

    def is_abstract_record(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.is_abstract_record(*args, **kwargs)

    def is_anonymous(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.is_anonymous(*args, **kwargs)

    def is_bitfield(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.is_bitfield(*args, **kwargs)

    def is_const_method(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.is_const_method(*args, **kwargs)

    def is_converting_constructor(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.is_converting_constructor(*args, **kwargs)

    def is_copy_assignment_operator_method(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.is_copy_assignment_operator_method(*args, **kwargs)

    def is_copy_constructor(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.is_copy_constructor(*args, **kwargs)

    def is_default_constructor(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.is_default_constructor(*args, **kwargs)

    def is_default_method(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.is_default_method(*args, **kwargs)

    def is_definition(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.is_definition(*args, **kwargs)

    def is_deleted_method(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.is_deleted_method(*args, **kwargs)

    def is_explicit_method(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.is_explicit_method(*args, **kwargs)

    def is_move_assignment_operator_method(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.is_move_assignment_operator_method(*args, **kwargs)

    def is_move_constructor(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.is_move_constructor(*args, **kwargs)

    def is_mutable_field(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.is_mutable_field(*args, **kwargs)

    def is_pure_virtual_method(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.is_pure_virtual_method(*args, **kwargs)

    def is_scoped_enum(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.is_scoped_enum(*args, **kwargs)

    def is_static_method(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.is_static_method(*args, **kwargs)

    def is_virtual_method(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.is_virtual_method(*args, **kwargs)

    def walk_preorder(self, *args: Any, **kwargs: Any) -> Any:
        return self._cursor.walk_preorder(*args, **kwargs)


class _TypeMirror:
    _type: _ClangType

    @property
    def kind(self) -> Any:
        return self._type.kind

    @property
    def element_count(self) -> Any:
        return self._type.element_count

    @property
    def element_type(self) -> Any:
        return self._type.element_type

    @property
    def spelling(self) -> Any:
        return self._type.spelling

    @property
    def translation_unit(self) -> Any:
        return self._type.translation_unit

    def argument_types(self, *args: Any, **kwargs: Any) -> Any:
        return self._type.argument_types(*args, **kwargs)

    def from_result(self, *args: Any, **kwargs: Any) -> Any:
        return self._type.from_result(*args, **kwargs)

    def get_address_space(self, *args: Any, **kwargs: Any) -> Any:
        return self._type.get_address_space(*args, **kwargs)

    def get_align(self, *args: Any, **kwargs: Any) -> Any:
        return self._type.get_align(*args, **kwargs)

    def get_array_element_type(self, *args: Any, **kwargs: Any) -> Any:
        return self._type.get_array_element_type(*args, **kwargs)

    def get_array_size(self, *args: Any, **kwargs: Any) -> Any:
        return self._type.get_array_size(*args, **kwargs)

    def get_canonical(self, *args: Any, **kwargs: Any) -> Any:
        return self._type.get_canonical(*args, **kwargs)

    def get_class_type(self, *args: Any, **kwargs: Any) -> Any:
        return self._type.get_class_type(*args, **kwargs)

    def get_declaration(self, *args: Any, **kwargs: Any) -> Any:
        return self._type.get_declaration(*args, **kwargs)

    def get_exception_specification_kind(self, *args: Any, **kwargs: Any) -> Any:
        return self._type.get_exception_specification_kind(*args, **kwargs)

    def get_fields(self, *args: Any, **kwargs: Any) -> Any:
        return self._type.get_fields(*args, **kwargs)

    def get_named_type(self, *args: Any, **kwargs: Any) -> Any:
        return self._type.get_named_type(*args, **kwargs)

    def get_num_template_arguments(self, *args: Any, **kwargs: Any) -> Any:
        return self._type.get_num_template_arguments(*args, **kwargs)

    def get_offset(self, *args: Any, **kwargs: Any) -> Any:
        return self._type.get_offset(*args, **kwargs)

    def get_pointee(self, *args: Any, **kwargs: Any) -> Any:
        return self._type.get_pointee(*args, **kwargs)

    def get_ref_qualifier(self, *args: Any, **kwargs: Any) -> Any:
        return self._type.get_ref_qualifier(*args, **kwargs)

    def get_result(self, *args: Any, **kwargs: Any) -> Any:
        return self._type.get_result(*args, **kwargs)

    def get_size(self, *args: Any, **kwargs: Any) -> Any:
        return self._type.get_size(*args, **kwargs)

    def get_template_argument_type(self, *args: Any, **kwargs: Any) -> Any:
        return self._type.get_template_argument_type(*args, **kwargs)

    def get_typedef_name(self, *args: Any, **kwargs: Any) -> Any:
        return self._type.get_typedef_name(*args, **kwargs)

    def is_const_qualified(self, *args: Any, **kwargs: Any) -> Any:
        return self._type.is_const_qualified(*args, **kwargs)

    def is_function_variadic(self, *args: Any, **kwargs: Any) -> Any:
        return self._type.is_function_variadic(*args, **kwargs)

    def is_pod(self, *args: Any, **kwargs: Any) -> Any:
        return self._type.is_pod(*args, **kwargs)

    def is_restrict_qualified(self, *args: Any, **kwargs: Any) -> Any:
        return self._type.is_restrict_qualified(*args, **kwargs)

    def is_volatile_qualified(self, *args: Any, **kwargs: Any) -> Any:
        return self._type.is_volatile_qualified(*args, **kwargs)
