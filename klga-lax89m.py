# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _3(aircraftData):

  table = {
    "A321": 2.3,
    "A333": 3,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    3: (CustomizedName("Terminal A|Gate #"), _3),
  },
}
