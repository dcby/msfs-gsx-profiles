# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def e13(aircraftData):

  table = {
    "A321": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_E: {
    13: (CustomizedName("Terminal E|Gate E#"), e13),
  },
}
