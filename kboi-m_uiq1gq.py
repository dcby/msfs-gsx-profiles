# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def b17(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_B: {
    17: (CustomizedName("Concourse B|Gate B#"), b17),
  },
}
