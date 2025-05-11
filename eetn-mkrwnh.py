# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def m9(aircraftData):

  table = {
    # "A320": -2.45,
    "B738": 0.50
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_M: {
    9: (CustomizedName("Apron M|Gate M#"), m9),
  },
}
