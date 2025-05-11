# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def a3(aircraftData):

  table = {
    "A339": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_A: {
    None: (CustomizedName("Main Terminal (Default)|Gate A#"), ),
    3: (CustomizedName("Main Terminal|Gate A#"), a3),
  },
}
