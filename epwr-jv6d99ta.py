# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _9(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  0: {
    9: (CustomizedName("(c) Apron 2|Gate #"), _9),
  },
}
