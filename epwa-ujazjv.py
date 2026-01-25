# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _1(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _21(aircraftData):

  table = {
    "B738": 0,
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
    4: (CustomizedName("(c) Apron 3|Gate #"), _4),
    21: (CustomizedName("(c) Apron 3|Gate #"), _21),
    32: (CustomizedName("(c) Apron 5A|Parking #"), _32),
  },
}
