# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _4(aircraftData):

  table = {
    "A321": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    4: (CustomizedName("Terminal|Gate #"), _4),
  },
}
