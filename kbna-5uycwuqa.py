# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def c22(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_C: {
    22: (CustomizedName("(c) Concourse C|Gate C#"), c22),
  },
}
