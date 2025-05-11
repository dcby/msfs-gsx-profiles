# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _210b(aircraftData):

  table = {
    "A321": -0.6,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _211(aircraftData):

  table = {
    "A321": -0.3,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    211: (CustomizedName("Apron 2|Gate #"), _211),
  },
  GATE_B: {
    210: (CustomizedName("Apron 2|Gate #B"), _210b),
  },
}
