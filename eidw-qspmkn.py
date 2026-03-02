# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _123(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _616c(aircraftData):

  table = {
    "B772": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  PARKING: {
    123: (CustomizedName("(c) Pier 1|Stand #"), _123),
    "616C": (CustomizedName("(c) West Apron|Stand #C"), _616c),
  },
}
