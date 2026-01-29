# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _2(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  PARKING: {
    2: (CustomizedName("(c) Main Apron|Stand #"), _2),
  },
}
