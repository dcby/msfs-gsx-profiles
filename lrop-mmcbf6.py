# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _109(aircraftData):

  table = {
    "A359": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    None: (CustomizedName("Default|Gate #"), ),
    109: (CustomizedName("Terminal|Gate #"), _109),
  },
}
