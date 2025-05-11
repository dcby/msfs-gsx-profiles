# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def b3(aircraftData):

  table = {
    "A333": -3
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def f3(aircraftData):

  table = {
    "A333": 4.40
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_B: {
    3: (CustomizedName("Terminal 7|Gate #"), b3),
  },
  GATE_F: {
    3: (CustomizedName("Terminal 7|Gate #"), f3),
  },
}
