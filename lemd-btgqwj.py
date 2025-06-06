# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _155(aircraftData):

  table = {
    "B77L": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

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

@AlternativeStopPositions
def t20(aircraftData):

  table = {
    "B772": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    155: (CustomizedName("Ramp R-5|Stand #"), _155),
  },
  GATE_T: {
    None: (CustomizedName("Default|Gate T#"), ),
    13: (CustomizedName("Ramp R-3|Gate T#"), t13),
    20: (CustomizedName("Ramp R-2|Gate T#"), t20),
  },
}
