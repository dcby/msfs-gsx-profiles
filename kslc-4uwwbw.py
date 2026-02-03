# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def b20(aircraftData):

  table = {
    # "A320": -2.45,
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_B: {
    20: (CustomizedName("(c) Concourse B|Gate B#"), b20),
  },
}
