# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _10(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  0: {
    10: (CustomizedName("(c) Terminal|Gate #"), _10),
  },
}
