# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _9a(aircraftData):

  table = {
    "A321": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  0: {
    "9A": (CustomizedName("Terminal 1A|Gate 9A"), _9a),
  },
}
