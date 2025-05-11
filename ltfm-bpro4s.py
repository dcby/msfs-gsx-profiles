# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def b6(aircraftData):

  table = {
    "A359": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_B: {
    None: (CustomizedName("Default|Gate #§"), ),
    6: (CustomizedName("Concourse B|Gate B#"), b6),
  },
}
