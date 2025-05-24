# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _558(aircraftData):

  table = {
    "B77L": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  0: {
    558: (CustomizedName("Fedex Ramp|Stand #"), _558),
  },
}
