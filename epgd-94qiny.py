# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _26(aircraftData):

  table = {
    "A320": 1.6,
    "A321": 1.6,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    26: (CustomizedName("Apron 3|Gate #"), _26),
  },
}
