# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _214(aircraftData):

  table = {
    "B77L": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  PARKING: {
    214: (CustomizedName("Apron Z|Stand #"), _214),
    "214L": (CustomizedName("Apron Z|Stand #L"), ),
    "214R": (CustomizedName("Apron Z|Stand #R"), ),
  },
}
