# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def s6(aircraftData):

  table = {
    "A321": 0.5,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_S: {
    6: (CustomizedName("Civil Apron|Parking S#"), s6),
  },
}
