# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _16(aircraftData):

  table = {
    "B772": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _23(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _26(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    16: (CustomizedName("(c) Pier B|Gate #"), _16),
    23: (CustomizedName("(c) Pier C|Gate #"), _23),
    26: (CustomizedName("(c) Terminal 2|Gate #"), _26),
  },
}
