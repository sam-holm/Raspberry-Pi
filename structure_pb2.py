# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: structure.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='structure.proto',
  package='tutorial',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x0fstructure.proto\x12\x08tutorial\"G\n\x08sens_dat\x12\x0c\n\x04type\x18\x01 \x02(\t\x12\x0c\n\x04unit\x18\x02 \x02(\t\x12\x11\n\ttimestamp\x18\x03 \x02(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x02(\x02')
)




_SENS_DAT = _descriptor.Descriptor(
  name='sens_dat',
  full_name='tutorial.sens_dat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='tutorial.sens_dat.type', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit', full_name='tutorial.sens_dat.unit', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='tutorial.sens_dat.timestamp', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='tutorial.sens_dat.data', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=100,
)

DESCRIPTOR.message_types_by_name['sens_dat'] = _SENS_DAT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

sens_dat = _reflection.GeneratedProtocolMessageType('sens_dat', (_message.Message,), dict(
  DESCRIPTOR = _SENS_DAT,
  __module__ = 'structure_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.sens_dat)
  ))
_sym_db.RegisterMessage(sens_dat)


# @@protoc_insertion_point(module_scope)
