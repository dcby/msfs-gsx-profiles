# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def _318(aircraftData):

  table = {
    "A35K": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _327(aircraftData):

  table = {
    "A35K": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _335(aircraftData):

  table = {
    "A35K": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _421(aircraftData):

  table = {
    "A320": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def _546(aircraftData):

  table = {
    "B772": 0
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    None: (CustomizedName("Default|Gate #§"), ),
    318: (CustomizedName("Pier 7|Gate #"), _318),
    327: (CustomizedName("Pier 5|Gate #"), _327),
    335: (CustomizedName("Pier 5|Gate #"), _335),
    421: (CustomizedName("Terminal 4|Gate #"), _421),
    546: (CustomizedName("Terminal 5B|Gate #"), _546),
  },
}
