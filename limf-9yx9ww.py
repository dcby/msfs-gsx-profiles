# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _107(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    107: (CustomizedName("(c) Main Apron / North Area|Stand #"), _107),
    111: (CustomizedName("(c) Main Apron / Middle Area|Gate #"), ),
  },
}
