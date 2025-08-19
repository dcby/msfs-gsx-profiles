# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _57L(aircraftData):

  table = {
    "A320": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    "57L": (CustomizedName("Terminal Apron|Gate #§"), _57L),
  },
}
