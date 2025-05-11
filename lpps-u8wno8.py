# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def a2(aircraftData):

  table = {
    "A320": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  PARKING: {
    "2A": (CustomizedName("Apron A|Stand A02"), a2),
  },
}
