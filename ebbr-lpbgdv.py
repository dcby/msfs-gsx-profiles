# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _144(aircraftData):

  table = {
    "A320": 1.3,
    "A321": 1,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _145r(aircraftData):

  table = {
    "A321": -0.9,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _158(aircraftData):

  table = {
    "A320": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    144: (CustomizedName("Apron 1 North|Gate #"), _144),
    "145R": (CustomizedName("Apron 1 South|Gate #R"), _145r),
    158: (CustomizedName("Apron 1 North|Gate #"), _158),
  },
}
