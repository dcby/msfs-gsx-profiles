# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def n1(aircraftData):

  table = {
    "B772": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_N: {
    1: (CustomizedName("North Ext Apron|Gate N01"), n1),
  },
}
