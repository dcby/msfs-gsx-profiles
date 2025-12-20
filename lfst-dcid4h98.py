# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def a6a(aircraftData):

  table = {
    "A320": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_A: {
    "6A": (CustomizedName("Apron A|Stand A#"), a6a),
  },
}
