# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def c4(aircraftData):

  table = {
    "A320": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_C: {
    4: (CustomizedName("(c) Terminal|Stand C#"), c4),
  },
}
