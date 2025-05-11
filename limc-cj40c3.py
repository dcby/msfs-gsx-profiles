# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _401(aircraftData):

  table = {
    "A359": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _602(aircraftData):

  table = {
    "A320": 0,
    "A321": 0,
    "A333": 11,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    None: (CustomizedName("Default|Gate #§"), ),
    401: (CustomizedName("Terminal T1|Gate #"), _401),
    602: (CustomizedName("Terminal T1|Gate #"), _602),
  },
}
