# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def b3(aircraftData):

  table = {
    "B738": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    "3B": (CustomizedName("(c) Concourse B|Gate B#"), b3),
  },
}
