# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _17(aircraftData):

  table = {
    "B738": -1.20
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  PARKING: {
    17: (CustomizedName("Parking|Gate #"), _17),
  },
}
