# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _12(aircraftData):

  table = {
    "A321": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    None: (CustomizedName("Default|Gate #"), ),
    12: (CustomizedName("Terminal|Gate #"), _12),
  },
}
