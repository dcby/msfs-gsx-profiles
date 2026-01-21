# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def b7(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_B: {
    7: (CustomizedName("(c) Terminal|Gate B#"), b7),
  },
}
