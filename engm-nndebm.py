# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _45(aircraftData):

  table = {
    "A320": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _47(aircraftData):

  table = {
    "A320": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _58(aircraftData):

  table = {
    "A359": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _64(aircraftData):

  table = {
    "A321": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    45: (CustomizedName("Civil Terminal|Gate #"), _45),
    47: (CustomizedName("Civil Terminal|Gate #"), _47),
    48: (CustomizedName("Civil Terminal|Gate #"), ),
    56: (CustomizedName("Civil Terminal|Gate # (Heavy)"), ),
    58: (CustomizedName("Civil Terminal|Gate # (Heavy)"), _58),
    64: (CustomizedName("Civil Terminal|Gate #"), _64),
  },
}
