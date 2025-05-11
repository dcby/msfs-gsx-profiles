# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def w16(aircraftData):

  table = {
    "A321": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_W: {
    16: (CustomizedName("Terminal T4|Gate W#"), w16),
  },
}
