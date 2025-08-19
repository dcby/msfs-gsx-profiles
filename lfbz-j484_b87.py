# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def c6(aircraftData):

  table = {
    "A320": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_C: {
    6: (CustomizedName("Apron C|Stand C#"), c6),
  },
}
