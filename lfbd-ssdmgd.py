# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def d2(aircraftData):

  table = {
    "A320": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_D: {
    None: (CustomizedName("Default|Gate #"), ),
    2: (CustomizedName("Apron D|Gate D#"), d2),
  },
}
