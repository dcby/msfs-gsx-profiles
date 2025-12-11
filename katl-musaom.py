# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def b26(aircraftData):

  table = {
    "A321": 0,
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
    26: (CustomizedName("Concourse B|Gate B#"), b26),
  },
  GATE_E: {
    10: (CustomizedName("Concourse E|Gate E#"), e10),
  },
}
