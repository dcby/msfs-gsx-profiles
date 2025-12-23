# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def a4(aircraftData):

  table = {
    "B738": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_A: {
    4: (CustomizedName("(c) Concourse A|Gate A#"), a4),
  },
}
