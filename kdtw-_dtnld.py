# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def a34(aircraftData):

  table = {
    "A333": -2.6,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def a60(aircraftData):

  table = {
    "A359": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_A: {
    34: (CustomizedName("Concourse A|Gate A#"), a34),
    60: (CustomizedName("Concourse A|Gate A#"), a60),
  },
}
