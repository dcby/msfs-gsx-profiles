# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _52L(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _214(aircraftData):

  table = {
    "B77L": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    "52L": (CustomizedName("(c) Apron C|Stand #§"), _52L),
  },
  PARKING: {
    214: (CustomizedName("(c) Apron Z|Stand #"), _214),
    "214L": (CustomizedName("(c) Apron Z|Stand #L"), ),
    "214R": (CustomizedName("(c) Apron Z|Stand #R"), ),
  },
}
