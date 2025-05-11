# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def b8(aircraftData):

  table = {
    "B738": -4.45,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def c14(aircraftData):

  table = {
    "A321": -1.30,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_B: {
    8: (CustomizedName("Concourse B|Gate B#"), b8),
  },
  
  GATE_C: {
    14: (CustomizedName("Concourse C|Gate C#"), c14),
  },
}
