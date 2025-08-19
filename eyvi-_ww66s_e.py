# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _210w(aircraftData):

  table = {
    "B772": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  0: {
    "210W": (CustomizedName("Ramp|Stand #§"), _210w),
  },
}
