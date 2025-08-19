# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _16(aircraftData):

  table = {
    "B772": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    16: (CustomizedName("Pier B|Gate #"), _16),
  },
}
