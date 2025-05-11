# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _3(aircraftData):

  table = {
    "B738": -4.00
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    3: (CustomizedName("Terminal|Gate #"), _3),
  },
}
