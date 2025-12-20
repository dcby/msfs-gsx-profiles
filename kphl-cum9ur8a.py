# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def a7(aircraftData):

  table = {
    "A320": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_A: {
    7: (CustomizedName("Concourse A East|Gate A#"), a7),
  },
}
