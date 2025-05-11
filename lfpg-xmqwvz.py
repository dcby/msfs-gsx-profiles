# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def x1(aircraftData):

  table = {
    "A321": 1,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE_X: {
    1: (CustomizedName("Terminal 1|Gate X#"), x1),
  },
}
