# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _15(aircraftData):

  table = {
    "A388": -11.40,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    15: (CustomizedName("Apron 3|Gate #"), _15),
  },
}
