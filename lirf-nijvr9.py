# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _304(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

# @AlternativeStopPositions
# def _312(aircraftData):

#   table = {
#     "A320": 0,
#   }

#   return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

# @AlternativeStopPositions
# def _402(aircraftData):

#   table = {
#     "A321": 2,
#   }

#   return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

# @AlternativeStopPositions
# def _407(aircraftData):

#   table = {
#     "A321": -1,
#   }

#   return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

# @AlternativeStopPositions
# def _409(aircraftData):

#   table = {
#     "A321": 2,
#   }

#   return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

# @AlternativeStopPositions
# def _505(aircraftData):

#   table = {
#     "A320": 0,
#   }

#   return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    304: (CustomizedName("(c) Terminal 1|Gate #"), _304),
    # 312: (CustomizedName("(c) Terminal 1|Gate #"), _312),
    # 402: (CustomizedName("(c) Terminal 1|Gate #"), _402),
    # 407: (CustomizedName("(c) Terminal 1|Gate #"), _407),
    # 409: (CustomizedName("(c) Terminal 1|Gate #"), _409),
    # 505: (CustomizedName("(c) Terminal 1|Gate #"), _505),
  },
}
