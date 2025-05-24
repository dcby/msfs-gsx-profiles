# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _616c(aircraftData):

  table = {
    "B772": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  PARKING: {
    "616C": (CustomizedName("West Apron|Stand #C"), _616c),
  },
}
