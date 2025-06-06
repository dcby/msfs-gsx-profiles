# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def c06(aircraftData):

  table = {
    "B772": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def v91a(aircraftData):

  table = {
    "B772": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_C: {
    6: (CustomizedName("Terminal|Gate 0#§"), c06),
  },
  GATE_V: {
    "91A": (CustomizedName("Apron West|Gate #§"), v91a),
  },
}
