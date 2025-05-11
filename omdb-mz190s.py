# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def a4(aircraftData):

  table = {
    "A388": -3.10
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def c64(aircraftData):

  table = {
    "B77W": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_A: {
    4: (CustomizedName("Apron A|Gate A#"), a4),
  },
  GATE_C: {
    64: (CustomizedName("Apron C|Gate C#"), c64),
  },
  GATE_D: {
    1: (CustomizedName("Apron D|Gate D#"), ),
  },
}
