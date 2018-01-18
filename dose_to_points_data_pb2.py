# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dose-to-points-data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dose-to-points-data.proto',
  package='ProtoFileGenerator',
  syntax='proto3',
  serialized_pb=_b('\n\x19\x64ose-to-points-data.proto\x12\x12ProtoFileGenerator\"\x82\x01\n\x04\x42\x65\x61m\x12\n\n\x02Id\x18\x01 \x01(\t\x12\r\n\x05JawX1\x18\x02 \x01(\x01\x12\r\n\x05JawX2\x18\x03 \x01(\x01\x12\r\n\x05JawY1\x18\x04 \x01(\x01\x12\r\n\x05JawY2\x18\x05 \x01(\x01\x12\x19\n\x11StartBeamletIndex\x18\x06 \x01(\x05\x12\x17\n\x0f\x45ndBeamletIndex\x18\x07 \x01(\x05\"f\n\x07\x42\x65\x61mlet\x12\r\n\x05Index\x18\x01 \x01(\x05\x12\x0e\n\x06\x42\x65\x61mId\x18\x02 \x01(\t\x12\r\n\x05XSize\x18\x03 \x01(\x02\x12\r\n\x05YSize\x18\x04 \x01(\x02\x12\x0e\n\x06XStart\x18\x05 \x01(\x02\x12\x0e\n\x06YStart\x18\x06 \x01(\x02\"*\n\x0b\x42\x65\x61mletDose\x12\r\n\x05Index\x18\x01 \x01(\x05\x12\x0c\n\x04\x44ose\x18\x02 \x01(\x02\"\x8d\x02\n\x10\x44oseToPointsData\x12\x10\n\x08\x46ileGUID\x18\x01 \x01(\t\x12\x31\n\nStructures\x18\x02 \x03(\x0b\x32\x1d.ProtoFileGenerator.Structure\x12\'\n\x05\x42\x65\x61ms\x18\x03 \x03(\x0b\x32\x18.ProtoFileGenerator.Beam\x12)\n\x06Points\x18\x04 \x03(\x0b\x32\x19.ProtoFileGenerator.Point\x12-\n\x08\x42\x65\x61mlets\x18\x05 \x03(\x0b\x32\x1b.ProtoFileGenerator.Beamlet\x12\x31\n\nPointDoses\x18\x06 \x03(\x0b\x32\x1d.ProtoFileGenerator.PointDose\"L\n\x05Point\x12\r\n\x05Index\x18\x01 \x01(\x05\x12\x13\n\x0bStructureId\x18\x02 \x01(\t\x12\t\n\x01X\x18\x03 \x01(\x02\x12\t\n\x01Y\x18\x04 \x01(\x02\x12\t\n\x01Z\x18\x05 \x01(\x02\"Q\n\tPointDose\x12\r\n\x05Index\x18\x01 \x01(\x05\x12\x35\n\x0c\x42\x65\x61mletDoses\x18\x02 \x03(\x0b\x32\x1f.ProtoFileGenerator.BeamletDose\"a\n\tStructure\x12\n\n\x02Id\x18\x01 \x01(\t\x12\x18\n\x10pointsDistanceCM\x18\x02 \x01(\x01\x12\x17\n\x0fStartPointIndex\x18\x03 \x01(\x05\x12\x15\n\rEndPointIndex\x18\x04 \x01(\x05\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BEAM = _descriptor.Descriptor(
  name='Beam',
  full_name='ProtoFileGenerator.Beam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Id', full_name='ProtoFileGenerator.Beam.Id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='JawX1', full_name='ProtoFileGenerator.Beam.JawX1', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='JawX2', full_name='ProtoFileGenerator.Beam.JawX2', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='JawY1', full_name='ProtoFileGenerator.Beam.JawY1', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='JawY2', full_name='ProtoFileGenerator.Beam.JawY2', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StartBeamletIndex', full_name='ProtoFileGenerator.Beam.StartBeamletIndex', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='EndBeamletIndex', full_name='ProtoFileGenerator.Beam.EndBeamletIndex', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=180,
)


_BEAMLET = _descriptor.Descriptor(
  name='Beamlet',
  full_name='ProtoFileGenerator.Beamlet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Index', full_name='ProtoFileGenerator.Beamlet.Index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BeamId', full_name='ProtoFileGenerator.Beamlet.BeamId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='XSize', full_name='ProtoFileGenerator.Beamlet.XSize', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='YSize', full_name='ProtoFileGenerator.Beamlet.YSize', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='XStart', full_name='ProtoFileGenerator.Beamlet.XStart', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='YStart', full_name='ProtoFileGenerator.Beamlet.YStart', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=182,
  serialized_end=284,
)


_BEAMLETDOSE = _descriptor.Descriptor(
  name='BeamletDose',
  full_name='ProtoFileGenerator.BeamletDose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Index', full_name='ProtoFileGenerator.BeamletDose.Index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Dose', full_name='ProtoFileGenerator.BeamletDose.Dose', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=286,
  serialized_end=328,
)


_DOSETOPOINTSDATA = _descriptor.Descriptor(
  name='DoseToPointsData',
  full_name='ProtoFileGenerator.DoseToPointsData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='FileGUID', full_name='ProtoFileGenerator.DoseToPointsData.FileGUID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Structures', full_name='ProtoFileGenerator.DoseToPointsData.Structures', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Beams', full_name='ProtoFileGenerator.DoseToPointsData.Beams', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Points', full_name='ProtoFileGenerator.DoseToPointsData.Points', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Beamlets', full_name='ProtoFileGenerator.DoseToPointsData.Beamlets', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PointDoses', full_name='ProtoFileGenerator.DoseToPointsData.PointDoses', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=331,
  serialized_end=600,
)


_POINT = _descriptor.Descriptor(
  name='Point',
  full_name='ProtoFileGenerator.Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Index', full_name='ProtoFileGenerator.Point.Index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StructureId', full_name='ProtoFileGenerator.Point.StructureId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='X', full_name='ProtoFileGenerator.Point.X', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Y', full_name='ProtoFileGenerator.Point.Y', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Z', full_name='ProtoFileGenerator.Point.Z', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=602,
  serialized_end=678,
)


_POINTDOSE = _descriptor.Descriptor(
  name='PointDose',
  full_name='ProtoFileGenerator.PointDose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Index', full_name='ProtoFileGenerator.PointDose.Index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BeamletDoses', full_name='ProtoFileGenerator.PointDose.BeamletDoses', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=680,
  serialized_end=761,
)


_STRUCTURE = _descriptor.Descriptor(
  name='Structure',
  full_name='ProtoFileGenerator.Structure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Id', full_name='ProtoFileGenerator.Structure.Id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pointsDistanceCM', full_name='ProtoFileGenerator.Structure.pointsDistanceCM', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StartPointIndex', full_name='ProtoFileGenerator.Structure.StartPointIndex', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='EndPointIndex', full_name='ProtoFileGenerator.Structure.EndPointIndex', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=763,
  serialized_end=860,
)

_DOSETOPOINTSDATA.fields_by_name['Structures'].message_type = _STRUCTURE
_DOSETOPOINTSDATA.fields_by_name['Beams'].message_type = _BEAM
_DOSETOPOINTSDATA.fields_by_name['Points'].message_type = _POINT
_DOSETOPOINTSDATA.fields_by_name['Beamlets'].message_type = _BEAMLET
_DOSETOPOINTSDATA.fields_by_name['PointDoses'].message_type = _POINTDOSE
_POINTDOSE.fields_by_name['BeamletDoses'].message_type = _BEAMLETDOSE
DESCRIPTOR.message_types_by_name['Beam'] = _BEAM
DESCRIPTOR.message_types_by_name['Beamlet'] = _BEAMLET
DESCRIPTOR.message_types_by_name['BeamletDose'] = _BEAMLETDOSE
DESCRIPTOR.message_types_by_name['DoseToPointsData'] = _DOSETOPOINTSDATA
DESCRIPTOR.message_types_by_name['Point'] = _POINT
DESCRIPTOR.message_types_by_name['PointDose'] = _POINTDOSE
DESCRIPTOR.message_types_by_name['Structure'] = _STRUCTURE

Beam = _reflection.GeneratedProtocolMessageType('Beam', (_message.Message,), dict(
  DESCRIPTOR = _BEAM,
  __module__ = 'dose_to_points_data_pb2'
  # @@protoc_insertion_point(class_scope:ProtoFileGenerator.Beam)
  ))
_sym_db.RegisterMessage(Beam)

Beamlet = _reflection.GeneratedProtocolMessageType('Beamlet', (_message.Message,), dict(
  DESCRIPTOR = _BEAMLET,
  __module__ = 'dose_to_points_data_pb2'
  # @@protoc_insertion_point(class_scope:ProtoFileGenerator.Beamlet)
  ))
_sym_db.RegisterMessage(Beamlet)

BeamletDose = _reflection.GeneratedProtocolMessageType('BeamletDose', (_message.Message,), dict(
  DESCRIPTOR = _BEAMLETDOSE,
  __module__ = 'dose_to_points_data_pb2'
  # @@protoc_insertion_point(class_scope:ProtoFileGenerator.BeamletDose)
  ))
_sym_db.RegisterMessage(BeamletDose)

DoseToPointsData = _reflection.GeneratedProtocolMessageType('DoseToPointsData', (_message.Message,), dict(
  DESCRIPTOR = _DOSETOPOINTSDATA,
  __module__ = 'dose_to_points_data_pb2'
  # @@protoc_insertion_point(class_scope:ProtoFileGenerator.DoseToPointsData)
  ))
_sym_db.RegisterMessage(DoseToPointsData)

Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), dict(
  DESCRIPTOR = _POINT,
  __module__ = 'dose_to_points_data_pb2'
  # @@protoc_insertion_point(class_scope:ProtoFileGenerator.Point)
  ))
_sym_db.RegisterMessage(Point)

PointDose = _reflection.GeneratedProtocolMessageType('PointDose', (_message.Message,), dict(
  DESCRIPTOR = _POINTDOSE,
  __module__ = 'dose_to_points_data_pb2'
  # @@protoc_insertion_point(class_scope:ProtoFileGenerator.PointDose)
  ))
_sym_db.RegisterMessage(PointDose)

Structure = _reflection.GeneratedProtocolMessageType('Structure', (_message.Message,), dict(
  DESCRIPTOR = _STRUCTURE,
  __module__ = 'dose_to_points_data_pb2'
  # @@protoc_insertion_point(class_scope:ProtoFileGenerator.Structure)
  ))
_sym_db.RegisterMessage(Structure)


# @@protoc_insertion_point(module_scope)
