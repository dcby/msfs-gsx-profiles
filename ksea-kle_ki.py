# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def s1(aircraftData):

  table = {
    "B772": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  S_PARKING: {
    1: (CustomizedName("Cargo Area 3|Stand #"), s1),
  },
}
