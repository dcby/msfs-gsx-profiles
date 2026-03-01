# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def b10(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_B: {
    10: (CustomizedName("(c) Apron B|Stand B#"), b10),
  },
}
