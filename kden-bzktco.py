# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def gate_c43(aircraftData):

  table = {
    # "A320": -2.45,
    "B738": 3.30
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_C: {
    43: (CustomizedName("Concourse C|Gate C#"), gate_c43),
  },
}
