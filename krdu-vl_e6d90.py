# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def c17(aircraftData):

  table = {
    "A320": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_C: {
    17: (CustomizedName("Terminal 2|Gate C#"), c17),
  },
}
