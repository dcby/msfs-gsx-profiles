# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _8(aircraftData):

  table = {
    # "A320": -2.45,
    "B738": 3.60
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    8: (CustomizedName("Terminal|Gate #"), _8),
  },
}
