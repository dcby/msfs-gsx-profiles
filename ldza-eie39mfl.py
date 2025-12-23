# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def e3(aircraftData):

  table = {
    "B738": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_E: {
    3: (CustomizedName("(c) Apron East|Gate E#"), e3),
  },
}
