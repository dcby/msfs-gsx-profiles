# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _5(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    5: (CustomizedName("(c) Apron 1|Stand #"), _5),
  },
}
