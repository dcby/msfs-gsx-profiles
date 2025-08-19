# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _7(aircraftData):

  table = {
    "B772": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    7: (CustomizedName("Pier A|Gate #§"), _7),
  },
}
