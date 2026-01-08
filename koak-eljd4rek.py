# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _23(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  0: {
    23: (CustomizedName("(c) Terminal 2|Gate #"), _23),
  },
}
