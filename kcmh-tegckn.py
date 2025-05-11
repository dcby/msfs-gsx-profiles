# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _35(aircraftData):

  table = {
    "A321": 0.3
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    35: (CustomizedName("Concourse B|Gate #A"), _35),
  },
}
