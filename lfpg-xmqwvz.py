# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def d16(aircraftData):

  table = {
    "B738": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

@AlternativeStopPositions
def x1(aircraftData):

  table = {
    "A321": 1,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_D: {
    16: (CustomizedName("(c) Terminal 2|Gate D#"), d16),
  },
  GATE_X: {
    1: (CustomizedName("(c) Terminal 1|Gate X#"), x1),
  },
}
