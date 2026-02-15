# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _18(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    18: (CustomizedName("(c) Terminal 4|Stand #"), _18),
  },
}
