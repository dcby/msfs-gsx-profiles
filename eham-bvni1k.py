# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def d16(aircraftData):

  table = {
    "B738": 0.80
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def f5(aircraftData):

  table = {
    "B77W": -4
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def h3(aircraftData):

  table = {
    "A320": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def r80(aircraftData):

  table = {
    "B77L": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_D: {
    16: (CustomizedName("D-Pier|Gate D#"), d16),
  },
  GATE_F: {
    # None: (CustomizedName("Default|Gate #§"), ),
    5: (CustomizedName("F-Pier|Gate F#"), f5),
  },
  GATE_H: {
    3: (CustomizedName("H-Apron|Gate H#"), h3),
  },
  GATE_R: {
    80: (CustomizedName("R-Apron|Stand R#"), r80),
  },
}
