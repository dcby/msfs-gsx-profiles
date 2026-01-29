# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _15(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    15: (CustomizedName("(c) Apron 3|Stand #"), _15),
  },
}
