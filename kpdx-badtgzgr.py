# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def e9(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_E: {
    9: (CustomizedName("Concourse E|Gate E#"), e9),
  },
}
