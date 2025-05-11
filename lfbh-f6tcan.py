# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def f2(aircraftData):

  table = {
    "A320": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  PARKING: {
    "2C": (CustomizedName("Parking F|Stand F2"), f2),
  },
}
