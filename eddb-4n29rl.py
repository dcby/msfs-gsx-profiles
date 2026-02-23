# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def a7(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def c5(aircraftData):

  table = {
    "A320": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_A: {
    7: (CustomizedName("(c) Apron A|Stand A#"), a7),
  },
  GATE_C: {
    5: (CustomizedName("(c) Apron C|Gate C#"), c5),
  },
}
