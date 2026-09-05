# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def m4(aircraftData):

  table = {
    "BCS3": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def m9(aircraftData):

  table = {
    "B738": 0.50
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_M: {
    4: (CustomizedName("Apron M|Gate M#"), m4),
    9: (CustomizedName("Apron M|Gate M#"), m9),
  },
}
