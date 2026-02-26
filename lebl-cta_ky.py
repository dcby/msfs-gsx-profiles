# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _107(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

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
    107: (CustomizedName("(c) Terminal T2, Ramp R-2|Gate #"), _107),
    226: (CustomizedName("(c) Terminal T1, Ramp R-12|Gate #"), _226),
    234: (CustomizedName("(c) Terminal T1, Ramp R-12|Gate #"), _234),
  },
  PARKING: {
    137: (CustomizedName("(c) Cargo, Ramp R-3|Stand #"), _137),
  }
}
