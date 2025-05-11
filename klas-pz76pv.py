# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def c19(aircraftData):

  table = {
    # "A320": -2.45,
    "B738": 1.35
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_C: {
    19: (CustomizedName("Concourse C|Gate C#"), c19),
  },
}
