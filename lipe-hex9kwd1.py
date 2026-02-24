# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _107(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  PARKING: {
    107: (CustomizedName("(c) Apron 1|Stand #"), _107),
  },
}
