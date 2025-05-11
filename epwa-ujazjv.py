# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _4(aircraftData):

  table = {
    "B738": 1.10
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _21(aircraftData):

  table = {
    "B738": 0.95
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _32(aircraftData):

  table = {
    "A321": 1.50,
    "B738": 2.00,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    4: (CustomizedName("Apron 3|Gate #"), _4),
    21: (CustomizedName("Apron 3|Gate #"), _21),
    32: (CustomizedName("Apron 5A|Parking #"), _32),
  },
}
