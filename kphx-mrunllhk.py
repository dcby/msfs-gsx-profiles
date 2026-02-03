# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def c3(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_C: {
    3: (CustomizedName("(c) Concourse S-3|Gate C#"), c3),
  },
}
