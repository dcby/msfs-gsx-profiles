# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def a5(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_A: {
    5: (CustomizedName("(c) Terminal A|Gate A#"), a5),
  },
}
