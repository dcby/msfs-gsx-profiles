# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def gate_83(aircraftData):

  table = {
    "A320": -0.7
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    83: (CustomizedName("Airside 4|Gate #"), gate_83),
  },
}
