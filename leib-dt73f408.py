# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _22(aircraftData):

  table = {
    "A320": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    22: (CustomizedName("Terminal|Gate #§"), _22),
  },
}
