# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _12(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    12: (CustomizedName("(c) Terminal|Gate #"), _12),
  },
}
