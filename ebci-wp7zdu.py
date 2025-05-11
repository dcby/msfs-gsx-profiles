# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _64(aircraftData):

  table = {
    "B738": -0.60
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  0: {
    64: (CustomizedName("Apron P13|Parking #"), _64),
  },
}
