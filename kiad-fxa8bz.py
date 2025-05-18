# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def c7(aircraftData):

  table = {
    "B772": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_C: {
    7: (CustomizedName("C Concourse|Gate C#"), c7),
  },
}
