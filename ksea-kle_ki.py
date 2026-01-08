# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def b8(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def s1(aircraftData):

  table = {
    "B772": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_B: {
    8: (CustomizedName("(c) Concourse B|Stand B#"), b8),
  },
  S_PARKING: {
    1: (CustomizedName("(c) Cargo Area 3|Stand #"), s1),
  },
}
