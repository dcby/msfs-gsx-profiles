# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _4(aircraftData):

  table = {
    "A320": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _15(aircraftData):

  table = {
    "A320": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  0: {
    4: (CustomizedName("North Apron|Gate #§"), _4),
  },
  PARKING: {
    15: (CustomizedName("North Apron|Stand #§"), _15),
  },
}
