# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def c43(aircraftData):

  table = {
    # "A320": -2.45,
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_C: {
    43: (CustomizedName("(c) Concourse C|Gate C#"), c43),
  },
}
