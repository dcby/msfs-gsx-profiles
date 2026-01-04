# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _205B(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _303(aircraftData):

  table = {
    "A321": -7.2,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  PARKING: {
    "205B": (CustomizedName("(c) South Apron|Parking #§"), _205B),
    303: (CustomizedName("(c) South Apron|Parking #"), _303),
  },
}
