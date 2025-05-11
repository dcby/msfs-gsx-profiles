# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _15(aircraftData):

  table = {
    "A321": -0.6,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    15: (CustomizedName("Terminal|Gate #"), _15),
  },
}
