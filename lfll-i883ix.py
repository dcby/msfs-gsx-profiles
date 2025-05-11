# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def c81(aircraftData):

  table = {
    "A320": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def l13(aircraftData):

  table = {
    "A320": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  PARKING: {
    None: (CustomizedName("Default|Gate #"), ),
    "13L": (CustomizedName("Terminal 3|Gate L#"), l13),
    "81C": (CustomizedName("Terminal 1|Gate C#"), c81),
  },
}
