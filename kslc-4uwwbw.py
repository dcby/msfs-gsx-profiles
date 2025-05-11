# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def gate_b20(aircraftData):

  table = {
    # "A320": -2.45,
    "B738": -2.45
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_B: {
    20: (CustomizedName("Concourse B|Gate B#"), gate_b20),
  },
}
