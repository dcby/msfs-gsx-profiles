# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _5a(aircraftData):

  table = {
    "A320": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  0: {
    "5A": (CustomizedName("Terminal|Gate 5"), _5a),
  },
}
