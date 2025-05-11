# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _13(aircraftData):

  table = {
    "A321": -2,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    13: (CustomizedName("Main Apron|Gate #"), _13),
  },
}
