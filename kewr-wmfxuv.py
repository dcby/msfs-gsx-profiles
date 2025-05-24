# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _35(aircraftData):

  table = {
    "B77L": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  PARKING: {
    35: (CustomizedName("Fedex Ramp|Stand #"), _35),
  },
}
