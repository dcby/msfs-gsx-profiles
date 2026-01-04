# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def e12(aircraftData):

  table = {
    "B738": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_E: {
    12: (CustomizedName("(c) Terminal 2|Gate E#"), e12),
  },
}
