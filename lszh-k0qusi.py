# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def a15(aircraftData):

  table = {
    "A321": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def e42(aircraftData):

  table = {
    "A333": -5.7,
    "A339": -5.8,
    "A35K": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_A: {
    15: (CustomizedName("Dock A|Gate A#"), a15),
  },
  GATE_E: {
    42: (CustomizedName("Dock E|Gate E#"), e42),
  },
}
