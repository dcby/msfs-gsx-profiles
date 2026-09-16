# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def b26(aircraftData):

  table = {
    "A321": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def c14(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def e10(aircraftData):

  table = {
    "A333": -1.1,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_B: {
    26: (CustomizedName("(c) Concourse B|Gate B#"), b26),
  },
  GATE_C: {
    14: (CustomizedName("(c) Concourse C|Gate C#"), c14),
  },
  GATE_E: {
    10: (CustomizedName("(c) Concourse E|Gate E#"), e10),
  },
}
