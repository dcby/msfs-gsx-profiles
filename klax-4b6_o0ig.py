# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _16(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    16: (CustomizedName("(c) Terminal 1|Gate #"), _16),
  },
}
