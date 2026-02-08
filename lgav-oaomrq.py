# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def a3(aircraftData):

  table = {
    "A339": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def a34(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def b9(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_A: {
    3: (CustomizedName("(c) Main Terminal|Gate A#"), a3),
    34: (CustomizedName("(c) Satillite Terminal|Gate A#"), a34),
  },
  GATE_B: {
    9: (CustomizedName("(c) Main Terminal|Gate B#"), b9),
  },
}
