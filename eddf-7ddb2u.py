# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def a21(aircraftData):

  table = {
    "A321": 0.1,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def a38(aircraftData):

  table = {
    "A321": 1.7,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def c8(aircraftData):

  table = {
    "A333": -0.6
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def v114(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_A: {
    21: (CustomizedName("(c) Terminal 1|Gate A#"), a21),
    38: (CustomizedName("(c) Terminal 1|Gate A#"), a38),
  },
  GATE_C: {
    8: (CustomizedName("(c) Terminal 1|Gate C#"), c8),
  },
  GATE_V: {
    114: (CustomizedName("(c) Terminal 2|Stand V#"), v114),
  },
}
