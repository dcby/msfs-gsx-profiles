# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _10(aircraftData):

  table = {
    "A320": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _33(aircraftData):

  table = {
    "B772": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    None: (CustomizedName("Default|Gate #"), ),
    10: (CustomizedName("Terminal|Gate #"), _10),
    33: (CustomizedName("Terminal|Gate #"), _33),
  },
}
