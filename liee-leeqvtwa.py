# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _21(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  PARKING: {
    21: (CustomizedName("(c) Terminal|Stand #"), _21),
  },
}
