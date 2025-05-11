# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _303(aircraftData):

  table = {
    "A321": -7.2,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  PARKING: {
    303: (CustomizedName("South Apron|Parking #"), _303),
  },
}
