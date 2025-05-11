# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _26(aircraftData):

  table = {
    "A388": -11.50,
    "B77W": -7.85,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    26: (CustomizedName("Western Apron|Gate #"), _26),
  },
}
