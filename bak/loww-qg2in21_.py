# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def c34(aircraftData):

  table = {
    "A320": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def b52(aircraftData):

  table = {
    "B77L": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_B: {
    52: (CustomizedName("(c) Cargo Area|Stand B#§"), c34),
  },
  GATE_C: {
    34: (CustomizedName("(c) Pier West|Gate C#§"), c34),
  },
}
