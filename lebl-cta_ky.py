# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _137(aircraftData):

  table = {
    "B77L": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _226(aircraftData):

  table = {
    "A321": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _234(aircraftData):

  table = {
    "A321": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    226: (CustomizedName("Terminal T1, Ramp R-12|Gate #"), _226),
    234: (CustomizedName("Terminal T1, Ramp R-12|Gate #"), _234),
  },
  PARKING: {
    137: (CustomizedName("Ramp R-3|Stand #"), _137),
  }
}
