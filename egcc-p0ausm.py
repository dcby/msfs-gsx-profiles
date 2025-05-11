# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _7(aircraftData):

  table = {
    "A320": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _107(aircraftData):

  table = {
    "A320": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _206(aircraftData):

  table = {
    "A35K": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    None: (CustomizedName("Default|Gate #"), ),
    7: (CustomizedName("Pier B|Gate #"), _7),
    107: (CustomizedName("Pier 1|Gate #"), _107),
    206: (CustomizedName("Terminal 2|Gate #"), _206),
  },
}
