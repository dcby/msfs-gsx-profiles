# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _1(aircraftData):

  table = {
    "A320": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _5(aircraftData):

  table = {
    "A320": 0,
    "A321": 2.3,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    1: (CustomizedName("Terminal 1|Gate #"), _1),
    5: (CustomizedName("Terminal 1|Gate #"), _5),
  },
}
