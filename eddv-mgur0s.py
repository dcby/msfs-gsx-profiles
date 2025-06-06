# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _6(aircraftData):

  table = {
    "B772": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _7(aircraftData):

  table = {
    "B772": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _27a(aircraftData):

  table = {
    "B77F": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  0: {
    "27A": (CustomizedName("Parking|Stand #§"), _27a),
  },
  GATE: {
    7: (CustomizedName("Terminal|Gate #§"), _7),
    6: (CustomizedName("Terminal|Gate #§"), _6),
  },
}
