# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def b18(aircraftData):

  table = {
    "B738": 0.40,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_B: {
    18: (CustomizedName("Concourse B|Gate B#"), b18),
  },
}
