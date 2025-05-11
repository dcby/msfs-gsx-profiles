# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _346(aircraftData):

  table = {
    "A321": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def t13(aircraftData):

  table = {
    "A320": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_T: {
    None: (CustomizedName("Default|Gate T#"), ),
    13: (CustomizedName("Terminal 1|Gate T#"), t13),
  },
}
