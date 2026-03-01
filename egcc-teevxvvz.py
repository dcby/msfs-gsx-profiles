# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _49(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _52(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    49: (CustomizedName("(c) Terminal 3, Pier A|Stand #"), _49),
  },
  PARKING: {
    52: (CustomizedName("(c) Terminal 3|Stand #"), _52),
  },
}
