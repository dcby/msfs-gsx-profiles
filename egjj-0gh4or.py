# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _13(aircraftData):

  table = {
    "A320": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  0: {
    13: (CustomizedName("Terminal|Gate #"), _13),
  },
}
