# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def b11(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def c19(aircraftData):

  table = {
    # "A320": -2.45,
    "B738": 1.35
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_B: {
    11: (CustomizedName("(c) B Gates|Gate B#"), b11),
  },
  GATE_C: {
    19: (CustomizedName("(c) C Gates|Gate C#"), c19),
  },
}
