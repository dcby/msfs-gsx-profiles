# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _21(aircraftData):

  table = {
    # "A320": -2.45,
    "B738": 0.10
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    21: (CustomizedName("Terminal|Gate #"), _21),
  },
}
