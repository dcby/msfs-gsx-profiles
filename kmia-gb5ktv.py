# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def n58(aircraftData):

  table = {
    "B77L": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_N: {
    58: (CustomizedName("Cargo Area|Stand #"), n58),
  },
}
