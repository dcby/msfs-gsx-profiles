# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def x21(aircraftData):

  table = {
    "B77L": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_X: {
    21: (CustomizedName("Apron 9|Stand #§"), x21),
  },
}
