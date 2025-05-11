# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _9(aircraftData):

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
def _204(aircraftData):

  table = {
    "A35K": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    107: (CustomizedName("Terminal 2 - Pier 1|Gate #"), _107),
    204: (CustomizedName("Terminal 2|Gate #"), _204),
  },
  PARKING: {
    9: (CustomizedName("Terminal 1 - Pier B|Gate #"), _9),
  },
}
