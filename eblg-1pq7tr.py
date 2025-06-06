# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _26e(aircraftData):

  table = {
    "B77L": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  PARKING: {
    "26E": (CustomizedName("Apron P2|Stand #§"), _26e),
  },
}
