# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _6(aircraftData):

  table = {
    "A320": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    None: (CustomizedName("Default|Gate #"), ),
    6: (CustomizedName("Terminal|Gate 6A"), _6),
  },
}
