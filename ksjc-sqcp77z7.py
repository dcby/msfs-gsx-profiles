# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _31(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    31: (CustomizedName("(c) Terminal B|Gate #"), _31),
  },
}
