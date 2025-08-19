# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _202(aircraftData):

  table = {
    "B77W": 0,
    "B789": -7.6,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  0: {
    202: (CustomizedName("Terminal|Gate 202"), _202),
  },
}
