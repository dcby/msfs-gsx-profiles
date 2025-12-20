# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _21(aircraftData):

  table = {
    "A320": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _101(aircraftData):

  table = {
    "A320": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    21: (CustomizedName("(c) Pier 2|Gate #"), _21),
    33: (CustomizedName("(c) Pier 3|Gate # (Heavy)"), ),
    101: (CustomizedName("(c) Pier 6|Gate #"), _101),
  },
}
