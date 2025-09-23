# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _9(aircraftData):

  table = {
    "A320": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  PARKING: {
    9: (CustomizedName("Main Apron|Stand #"), _9),
  },
}
