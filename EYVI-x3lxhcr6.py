# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _23(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _48(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _103(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  PARKING: {
    23: (CustomizedName("(c) Apron|Stand #"), _23),
    48: (CustomizedName("(c) Terminal|Gate #"), _48),
    103: (CustomizedName("(c) Terminal|Gate #"), _103),
  },
}
