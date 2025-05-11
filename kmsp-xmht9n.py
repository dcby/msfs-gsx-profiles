# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def f14(aircraftData):

  table = {
    "A359": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_F: {
    14: (CustomizedName("Concourse F|Gate F#"), f14),
  },
}
