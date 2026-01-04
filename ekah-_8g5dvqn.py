# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _4(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  0: {
    4: (CustomizedName("(c) Terminal|Stand #"), _4),
  },
}
