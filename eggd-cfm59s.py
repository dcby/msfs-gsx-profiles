# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _25(aircraftData):

  table = {
    "A320": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    None: (CustomizedName("Default|Gate #"), ),
    25: (CustomizedName("West Apron|Gate #"), _25),
  },
}
