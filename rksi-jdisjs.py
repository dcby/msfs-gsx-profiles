# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _10(aircraftData):

  table = {
    "A388": -0.40,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    10: (CustomizedName("Apron 1|Gate #"), _10),
  },
}
