# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def c4(aircraftData):

  table = {
    "B738": -1.00
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_C: {
    4: (CustomizedName("Pier C|Gate C#"), c4),
  },
}
