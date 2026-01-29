# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _19(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  0: {
    19: (CustomizedName("(c) Terminal|Gate #"), _19),
  },
}
