# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def gate_9(aircraftData):

  table = {
    # "A320": -2.45,
    "B738": 0.15
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  GATE: {
    9: (CustomizedName("Terminal 1|Gate #"), gate_9),
    49: (CustomizedName("International Gates|Gate #"), ),
  },
}
