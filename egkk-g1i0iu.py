# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _21(aircraftData):

  table = {
    "A320": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    None: (CustomizedName("Default|Gate #§"), ),
    21: (CustomizedName("Pier 2|Gate #"), _21),
    33: (CustomizedName("Pier 3|Gate # (Heavy)"), ),
  },
}
