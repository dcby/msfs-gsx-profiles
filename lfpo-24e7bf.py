# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def p13(aircraftData):

  table = {
    "A320": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def p42(aircraftData):

  table = {
    "A320": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_P: {
    13: (CustomizedName("Orly 1|Gate P#"), p13),
    42: (CustomizedName("Orly 1|Gate P#"), p42),
  },
}
