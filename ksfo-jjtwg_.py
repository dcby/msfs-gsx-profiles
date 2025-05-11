# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def b13(aircraftData):

  table = {
    # "A320": -2.45,
    "B738": -1.85
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_B: {
    13: (CustomizedName("Boarding Area B|Gate B#"), b13),
  },
}
