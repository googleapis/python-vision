# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/vision_v1p2beta1/proto/text_annotation.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.cloud.vision_v1p2beta1.proto import (
    geometry_pb2 as google_dot_cloud_dot_vision__v1p2beta1_dot_proto_dot_geometry__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/vision_v1p2beta1/proto/text_annotation.proto",
    package="google.cloud.vision.v1p2beta1",
    syntax="proto3",
    serialized_options=_b(
        "\n!com.google.cloud.vision.v1p2beta1B\023TextAnnotationProtoP\001ZCgoogle.golang.org/genproto/googleapis/cloud/vision/v1p2beta1;vision\370\001\001"
    ),
    serialized_pb=_b(
        '\n9google/cloud/vision_v1p2beta1/proto/text_annotation.proto\x12\x1dgoogle.cloud.vision.v1p2beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x32google/cloud/vision_v1p2beta1/proto/geometry.proto"\xb2\x04\n\x0eTextAnnotation\x12\x32\n\x05pages\x18\x01 \x03(\x0b\x32#.google.cloud.vision.v1p2beta1.Page\x12\x0c\n\x04text\x18\x02 \x01(\t\x1a=\n\x10\x44\x65tectedLanguage\x12\x15\n\rlanguage_code\x18\x01 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x1a\xdc\x01\n\rDetectedBreak\x12S\n\x04type\x18\x01 \x01(\x0e\x32\x45.google.cloud.vision.v1p2beta1.TextAnnotation.DetectedBreak.BreakType\x12\x11\n\tis_prefix\x18\x02 \x01(\x08"c\n\tBreakType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05SPACE\x10\x01\x12\x0e\n\nSURE_SPACE\x10\x02\x12\x12\n\x0e\x45OL_SURE_SPACE\x10\x03\x12\n\n\x06HYPHEN\x10\x04\x12\x0e\n\nLINE_BREAK\x10\x05\x1a\xbf\x01\n\x0cTextProperty\x12Z\n\x12\x64\x65tected_languages\x18\x01 \x03(\x0b\x32>.google.cloud.vision.v1p2beta1.TextAnnotation.DetectedLanguage\x12S\n\x0e\x64\x65tected_break\x18\x02 \x01(\x0b\x32;.google.cloud.vision.v1p2beta1.TextAnnotation.DetectedBreak"\xbd\x01\n\x04Page\x12L\n\x08property\x18\x01 \x01(\x0b\x32:.google.cloud.vision.v1p2beta1.TextAnnotation.TextProperty\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0e\n\x06height\x18\x03 \x01(\x05\x12\x34\n\x06\x62locks\x18\x04 \x03(\x0b\x32$.google.cloud.vision.v1p2beta1.Block\x12\x12\n\nconfidence\x18\x05 \x01(\x02"\x82\x03\n\x05\x42lock\x12L\n\x08property\x18\x01 \x01(\x0b\x32:.google.cloud.vision.v1p2beta1.TextAnnotation.TextProperty\x12\x41\n\x0c\x62ounding_box\x18\x02 \x01(\x0b\x32+.google.cloud.vision.v1p2beta1.BoundingPoly\x12<\n\nparagraphs\x18\x03 \x03(\x0b\x32(.google.cloud.vision.v1p2beta1.Paragraph\x12\x42\n\nblock_type\x18\x04 \x01(\x0e\x32..google.cloud.vision.v1p2beta1.Block.BlockType\x12\x12\n\nconfidence\x18\x05 \x01(\x02"R\n\tBlockType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04TEXT\x10\x01\x12\t\n\x05TABLE\x10\x02\x12\x0b\n\x07PICTURE\x10\x03\x12\t\n\x05RULER\x10\x04\x12\x0b\n\x07\x42\x41RCODE\x10\x05"\xe4\x01\n\tParagraph\x12L\n\x08property\x18\x01 \x01(\x0b\x32:.google.cloud.vision.v1p2beta1.TextAnnotation.TextProperty\x12\x41\n\x0c\x62ounding_box\x18\x02 \x01(\x0b\x32+.google.cloud.vision.v1p2beta1.BoundingPoly\x12\x32\n\x05words\x18\x03 \x03(\x0b\x32#.google.cloud.vision.v1p2beta1.Word\x12\x12\n\nconfidence\x18\x04 \x01(\x02"\xe3\x01\n\x04Word\x12L\n\x08property\x18\x01 \x01(\x0b\x32:.google.cloud.vision.v1p2beta1.TextAnnotation.TextProperty\x12\x41\n\x0c\x62ounding_box\x18\x02 \x01(\x0b\x32+.google.cloud.vision.v1p2beta1.BoundingPoly\x12\x36\n\x07symbols\x18\x03 \x03(\x0b\x32%.google.cloud.vision.v1p2beta1.Symbol\x12\x12\n\nconfidence\x18\x04 \x01(\x02"\xbb\x01\n\x06Symbol\x12L\n\x08property\x18\x01 \x01(\x0b\x32:.google.cloud.vision.v1p2beta1.TextAnnotation.TextProperty\x12\x41\n\x0c\x62ounding_box\x18\x02 \x01(\x0b\x32+.google.cloud.vision.v1p2beta1.BoundingPoly\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\x12\n\nconfidence\x18\x04 \x01(\x02\x42\x82\x01\n!com.google.cloud.vision.v1p2beta1B\x13TextAnnotationProtoP\x01ZCgoogle.golang.org/genproto/googleapis/cloud/vision/v1p2beta1;vision\xf8\x01\x01\x62\x06proto3'
    ),
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_cloud_dot_vision__v1p2beta1_dot_proto_dot_geometry__pb2.DESCRIPTOR,
    ],
)


_TEXTANNOTATION_DETECTEDBREAK_BREAKTYPE = _descriptor.EnumDescriptor(
    name="BreakType",
    full_name="google.cloud.vision.v1p2beta1.TextAnnotation.DetectedBreak.BreakType",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="UNKNOWN", index=0, number=0, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="SPACE", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="SURE_SPACE", index=2, number=2, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="EOL_SURE_SPACE", index=3, number=3, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="HYPHEN", index=4, number=4, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="LINE_BREAK", index=5, number=5, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=444,
    serialized_end=543,
)
_sym_db.RegisterEnumDescriptor(_TEXTANNOTATION_DETECTEDBREAK_BREAKTYPE)

_BLOCK_BLOCKTYPE = _descriptor.EnumDescriptor(
    name="BlockType",
    full_name="google.cloud.vision.v1p2beta1.Block.BlockType",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="UNKNOWN", index=0, number=0, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="TEXT", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="TABLE", index=2, number=2, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="PICTURE", index=3, number=3, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="RULER", index=4, number=4, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="BARCODE", index=5, number=5, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1236,
    serialized_end=1318,
)
_sym_db.RegisterEnumDescriptor(_BLOCK_BLOCKTYPE)


_TEXTANNOTATION_DETECTEDLANGUAGE = _descriptor.Descriptor(
    name="DetectedLanguage",
    full_name="google.cloud.vision.v1p2beta1.TextAnnotation.DetectedLanguage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="language_code",
            full_name="google.cloud.vision.v1p2beta1.TextAnnotation.DetectedLanguage.language_code",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="confidence",
            full_name="google.cloud.vision.v1p2beta1.TextAnnotation.DetectedLanguage.confidence",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=259,
    serialized_end=320,
)

_TEXTANNOTATION_DETECTEDBREAK = _descriptor.Descriptor(
    name="DetectedBreak",
    full_name="google.cloud.vision.v1p2beta1.TextAnnotation.DetectedBreak",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="type",
            full_name="google.cloud.vision.v1p2beta1.TextAnnotation.DetectedBreak.type",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="is_prefix",
            full_name="google.cloud.vision.v1p2beta1.TextAnnotation.DetectedBreak.is_prefix",
            index=1,
            number=2,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_TEXTANNOTATION_DETECTEDBREAK_BREAKTYPE],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=323,
    serialized_end=543,
)

_TEXTANNOTATION_TEXTPROPERTY = _descriptor.Descriptor(
    name="TextProperty",
    full_name="google.cloud.vision.v1p2beta1.TextAnnotation.TextProperty",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="detected_languages",
            full_name="google.cloud.vision.v1p2beta1.TextAnnotation.TextProperty.detected_languages",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="detected_break",
            full_name="google.cloud.vision.v1p2beta1.TextAnnotation.TextProperty.detected_break",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=546,
    serialized_end=737,
)

_TEXTANNOTATION = _descriptor.Descriptor(
    name="TextAnnotation",
    full_name="google.cloud.vision.v1p2beta1.TextAnnotation",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="pages",
            full_name="google.cloud.vision.v1p2beta1.TextAnnotation.pages",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="text",
            full_name="google.cloud.vision.v1p2beta1.TextAnnotation.text",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[
        _TEXTANNOTATION_DETECTEDLANGUAGE,
        _TEXTANNOTATION_DETECTEDBREAK,
        _TEXTANNOTATION_TEXTPROPERTY,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=175,
    serialized_end=737,
)


_PAGE = _descriptor.Descriptor(
    name="Page",
    full_name="google.cloud.vision.v1p2beta1.Page",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="property",
            full_name="google.cloud.vision.v1p2beta1.Page.property",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="width",
            full_name="google.cloud.vision.v1p2beta1.Page.width",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="height",
            full_name="google.cloud.vision.v1p2beta1.Page.height",
            index=2,
            number=3,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="blocks",
            full_name="google.cloud.vision.v1p2beta1.Page.blocks",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="confidence",
            full_name="google.cloud.vision.v1p2beta1.Page.confidence",
            index=4,
            number=5,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=740,
    serialized_end=929,
)


_BLOCK = _descriptor.Descriptor(
    name="Block",
    full_name="google.cloud.vision.v1p2beta1.Block",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="property",
            full_name="google.cloud.vision.v1p2beta1.Block.property",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="bounding_box",
            full_name="google.cloud.vision.v1p2beta1.Block.bounding_box",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="paragraphs",
            full_name="google.cloud.vision.v1p2beta1.Block.paragraphs",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="block_type",
            full_name="google.cloud.vision.v1p2beta1.Block.block_type",
            index=3,
            number=4,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="confidence",
            full_name="google.cloud.vision.v1p2beta1.Block.confidence",
            index=4,
            number=5,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_BLOCK_BLOCKTYPE],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=932,
    serialized_end=1318,
)


_PARAGRAPH = _descriptor.Descriptor(
    name="Paragraph",
    full_name="google.cloud.vision.v1p2beta1.Paragraph",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="property",
            full_name="google.cloud.vision.v1p2beta1.Paragraph.property",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="bounding_box",
            full_name="google.cloud.vision.v1p2beta1.Paragraph.bounding_box",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="words",
            full_name="google.cloud.vision.v1p2beta1.Paragraph.words",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="confidence",
            full_name="google.cloud.vision.v1p2beta1.Paragraph.confidence",
            index=3,
            number=4,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1321,
    serialized_end=1549,
)


_WORD = _descriptor.Descriptor(
    name="Word",
    full_name="google.cloud.vision.v1p2beta1.Word",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="property",
            full_name="google.cloud.vision.v1p2beta1.Word.property",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="bounding_box",
            full_name="google.cloud.vision.v1p2beta1.Word.bounding_box",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="symbols",
            full_name="google.cloud.vision.v1p2beta1.Word.symbols",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="confidence",
            full_name="google.cloud.vision.v1p2beta1.Word.confidence",
            index=3,
            number=4,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1552,
    serialized_end=1779,
)


_SYMBOL = _descriptor.Descriptor(
    name="Symbol",
    full_name="google.cloud.vision.v1p2beta1.Symbol",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="property",
            full_name="google.cloud.vision.v1p2beta1.Symbol.property",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="bounding_box",
            full_name="google.cloud.vision.v1p2beta1.Symbol.bounding_box",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="text",
            full_name="google.cloud.vision.v1p2beta1.Symbol.text",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="confidence",
            full_name="google.cloud.vision.v1p2beta1.Symbol.confidence",
            index=3,
            number=4,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1782,
    serialized_end=1969,
)

_TEXTANNOTATION_DETECTEDLANGUAGE.containing_type = _TEXTANNOTATION
_TEXTANNOTATION_DETECTEDBREAK.fields_by_name[
    "type"
].enum_type = _TEXTANNOTATION_DETECTEDBREAK_BREAKTYPE
_TEXTANNOTATION_DETECTEDBREAK.containing_type = _TEXTANNOTATION
_TEXTANNOTATION_DETECTEDBREAK_BREAKTYPE.containing_type = _TEXTANNOTATION_DETECTEDBREAK
_TEXTANNOTATION_TEXTPROPERTY.fields_by_name[
    "detected_languages"
].message_type = _TEXTANNOTATION_DETECTEDLANGUAGE
_TEXTANNOTATION_TEXTPROPERTY.fields_by_name[
    "detected_break"
].message_type = _TEXTANNOTATION_DETECTEDBREAK
_TEXTANNOTATION_TEXTPROPERTY.containing_type = _TEXTANNOTATION
_TEXTANNOTATION.fields_by_name["pages"].message_type = _PAGE
_PAGE.fields_by_name["property"].message_type = _TEXTANNOTATION_TEXTPROPERTY
_PAGE.fields_by_name["blocks"].message_type = _BLOCK
_BLOCK.fields_by_name["property"].message_type = _TEXTANNOTATION_TEXTPROPERTY
_BLOCK.fields_by_name[
    "bounding_box"
].message_type = (
    google_dot_cloud_dot_vision__v1p2beta1_dot_proto_dot_geometry__pb2._BOUNDINGPOLY
)
_BLOCK.fields_by_name["paragraphs"].message_type = _PARAGRAPH
_BLOCK.fields_by_name["block_type"].enum_type = _BLOCK_BLOCKTYPE
_BLOCK_BLOCKTYPE.containing_type = _BLOCK
_PARAGRAPH.fields_by_name["property"].message_type = _TEXTANNOTATION_TEXTPROPERTY
_PARAGRAPH.fields_by_name[
    "bounding_box"
].message_type = (
    google_dot_cloud_dot_vision__v1p2beta1_dot_proto_dot_geometry__pb2._BOUNDINGPOLY
)
_PARAGRAPH.fields_by_name["words"].message_type = _WORD
_WORD.fields_by_name["property"].message_type = _TEXTANNOTATION_TEXTPROPERTY
_WORD.fields_by_name[
    "bounding_box"
].message_type = (
    google_dot_cloud_dot_vision__v1p2beta1_dot_proto_dot_geometry__pb2._BOUNDINGPOLY
)
_WORD.fields_by_name["symbols"].message_type = _SYMBOL
_SYMBOL.fields_by_name["property"].message_type = _TEXTANNOTATION_TEXTPROPERTY
_SYMBOL.fields_by_name[
    "bounding_box"
].message_type = (
    google_dot_cloud_dot_vision__v1p2beta1_dot_proto_dot_geometry__pb2._BOUNDINGPOLY
)
DESCRIPTOR.message_types_by_name["TextAnnotation"] = _TEXTANNOTATION
DESCRIPTOR.message_types_by_name["Page"] = _PAGE
DESCRIPTOR.message_types_by_name["Block"] = _BLOCK
DESCRIPTOR.message_types_by_name["Paragraph"] = _PARAGRAPH
DESCRIPTOR.message_types_by_name["Word"] = _WORD
DESCRIPTOR.message_types_by_name["Symbol"] = _SYMBOL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TextAnnotation = _reflection.GeneratedProtocolMessageType(
    "TextAnnotation",
    (_message.Message,),
    dict(
        DetectedLanguage=_reflection.GeneratedProtocolMessageType(
            "DetectedLanguage",
            (_message.Message,),
            dict(
                DESCRIPTOR=_TEXTANNOTATION_DETECTEDLANGUAGE,
                __module__="google.cloud.vision_v1p2beta1.proto.text_annotation_pb2",
                __doc__="""Detected language for a structural component.
    Attributes:
        language_code:
            The BCP-47 language code, such as "en-US" or "sr-Latn". For
            more information, see http://www.unicode.org/reports/tr35/#Uni
            code\_locale\_identifier.
        confidence:
            Confidence of detected language. Range [0, 1].
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.vision.v1p2beta1.TextAnnotation.DetectedLanguage)
            ),
        ),
        DetectedBreak=_reflection.GeneratedProtocolMessageType(
            "DetectedBreak",
            (_message.Message,),
            dict(
                DESCRIPTOR=_TEXTANNOTATION_DETECTEDBREAK,
                __module__="google.cloud.vision_v1p2beta1.proto.text_annotation_pb2",
                __doc__="""Detected start or end of a structural component.
    Attributes:
        type:
            Detected break type.
        is_prefix:
            True if break prepends the element.
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.vision.v1p2beta1.TextAnnotation.DetectedBreak)
            ),
        ),
        TextProperty=_reflection.GeneratedProtocolMessageType(
            "TextProperty",
            (_message.Message,),
            dict(
                DESCRIPTOR=_TEXTANNOTATION_TEXTPROPERTY,
                __module__="google.cloud.vision_v1p2beta1.proto.text_annotation_pb2",
                __doc__="""Additional information detected on the structural component.
    Attributes:
        detected_languages:
            A list of detected languages together with confidence.
        detected_break:
            Detected start or end of a text segment.
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.vision.v1p2beta1.TextAnnotation.TextProperty)
            ),
        ),
        DESCRIPTOR=_TEXTANNOTATION,
        __module__="google.cloud.vision_v1p2beta1.proto.text_annotation_pb2",
        __doc__="""TextAnnotation contains a structured representation of OCR extracted
  text. The hierarchy of an OCR extracted text structure is like this:
  TextAnnotation -> Page -> Block -> Paragraph -> Word -> Symbol Each
  structural component, starting from Page, may further have their own
  properties. Properties describe detected languages, breaks etc..
  Please refer to the [TextAnnotation.TextProperty][google.cloud.vision.
  v1p2beta1.TextAnnotation.TextProperty] message definition below for
  more detail.
  Attributes:
      pages:
          List of pages detected by OCR.
      text:
          UTF-8 text detected on the pages.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.vision.v1p2beta1.TextAnnotation)
    ),
)
_sym_db.RegisterMessage(TextAnnotation)
_sym_db.RegisterMessage(TextAnnotation.DetectedLanguage)
_sym_db.RegisterMessage(TextAnnotation.DetectedBreak)
_sym_db.RegisterMessage(TextAnnotation.TextProperty)

Page = _reflection.GeneratedProtocolMessageType(
    "Page",
    (_message.Message,),
    dict(
        DESCRIPTOR=_PAGE,
        __module__="google.cloud.vision_v1p2beta1.proto.text_annotation_pb2",
        __doc__="""Detected page from OCR.
  Attributes:
      property:
          Additional information detected on the page.
      width:
          Page width. For PDFs the unit is points. For images (including
          TIFFs) the unit is pixels.
      height:
          Page height. For PDFs the unit is points. For images
          (including TIFFs) the unit is pixels.
      blocks:
          List of blocks of text, images etc on this page.
      confidence:
          Confidence of the OCR results on the page. Range [0, 1].
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.vision.v1p2beta1.Page)
    ),
)
_sym_db.RegisterMessage(Page)

Block = _reflection.GeneratedProtocolMessageType(
    "Block",
    (_message.Message,),
    dict(
        DESCRIPTOR=_BLOCK,
        __module__="google.cloud.vision_v1p2beta1.proto.text_annotation_pb2",
        __doc__="""Logical element on the page.
  Attributes:
      property:
          Additional information detected for the block.
      bounding_box:
          The bounding box for the block. The vertices are in the order
          of top-left, top-right, bottom-right, bottom-left. When a
          rotation of the bounding box is detected the rotation is
          represented as around the top-left corner as defined when the
          text is read in the 'natural' orientation. For example:  -
          when the text is horizontal it might look like:     ::
          0----1        |    |        3----2  -  when it's rotated 180
          degrees around the top-left corner it becomes:     ::
          2----3        |    |        1----0  and the vertice order will
          still be (0, 1, 2, 3).
      paragraphs:
          List of paragraphs in this block (if this blocks is of type
          text).
      block_type:
          Detected block type (text, image etc) for this block.
      confidence:
          Confidence of the OCR results on the block. Range [0, 1].
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.vision.v1p2beta1.Block)
    ),
)
_sym_db.RegisterMessage(Block)

Paragraph = _reflection.GeneratedProtocolMessageType(
    "Paragraph",
    (_message.Message,),
    dict(
        DESCRIPTOR=_PARAGRAPH,
        __module__="google.cloud.vision_v1p2beta1.proto.text_annotation_pb2",
        __doc__="""Structural unit of text representing a number of words in certain
  order.
  Attributes:
      property:
          Additional information detected for the paragraph.
      bounding_box:
          The bounding box for the paragraph. The vertices are in the
          order of top-left, top-right, bottom-right, bottom-left. When
          a rotation of the bounding box is detected the rotation is
          represented as around the top-left corner as defined when the
          text is read in the 'natural' orientation. For example: \*
          when the text is horizontal it might look like: 0----1 \| \| 3
          ----2 \* when it's rotated 180 degrees around the top-left
          corner it becomes: 2----3 \| \| 1----0 and the vertice order
          will still be (0, 1, 2, 3).
      words:
          List of words in this paragraph.
      confidence:
          Confidence of the OCR results for the paragraph. Range [0, 1].
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.vision.v1p2beta1.Paragraph)
    ),
)
_sym_db.RegisterMessage(Paragraph)

Word = _reflection.GeneratedProtocolMessageType(
    "Word",
    (_message.Message,),
    dict(
        DESCRIPTOR=_WORD,
        __module__="google.cloud.vision_v1p2beta1.proto.text_annotation_pb2",
        __doc__="""A word representation.
  Attributes:
      property:
          Additional information detected for the word.
      bounding_box:
          The bounding box for the word. The vertices are in the order
          of top-left, top-right, bottom-right, bottom-left. When a
          rotation of the bounding box is detected the rotation is
          represented as around the top-left corner as defined when the
          text is read in the 'natural' orientation. For example: \*
          when the text is horizontal it might look like: 0----1 \| \| 3
          ----2 \* when it's rotated 180 degrees around the top-left
          corner it becomes: 2----3 \| \| 1----0 and the vertice order
          will still be (0, 1, 2, 3).
      symbols:
          List of symbols in the word. The order of the symbols follows
          the natural reading order.
      confidence:
          Confidence of the OCR results for the word. Range [0, 1].
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.vision.v1p2beta1.Word)
    ),
)
_sym_db.RegisterMessage(Word)

Symbol = _reflection.GeneratedProtocolMessageType(
    "Symbol",
    (_message.Message,),
    dict(
        DESCRIPTOR=_SYMBOL,
        __module__="google.cloud.vision_v1p2beta1.proto.text_annotation_pb2",
        __doc__="""A single symbol representation.
  Attributes:
      property:
          Additional information detected for the symbol.
      bounding_box:
          The bounding box for the symbol. The vertices are in the order
          of top-left, top-right, bottom-right, bottom-left. When a
          rotation of the bounding box is detected the rotation is
          represented as around the top-left corner as defined when the
          text is read in the 'natural' orientation. For example: \*
          when the text is horizontal it might look like: 0----1 \| \| 3
          ----2 \* when it's rotated 180 degrees around the top-left
          corner it becomes: 2----3 \| \| 1----0 and the vertice order
          will still be (0, 1, 2, 3).
      text:
          The actual UTF-8 representation of the symbol.
      confidence:
          Confidence of the OCR results for the symbol. Range [0, 1].
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.vision.v1p2beta1.Symbol)
    ),
)
_sym_db.RegisterMessage(Symbol)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
