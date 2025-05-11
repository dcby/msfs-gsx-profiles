# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def gate_45(aircraftData):

  table = {
    "A320": 5.80,
    "B738": 4.80
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  PARKING: {
    45: (CustomizedName("Terminal 3|Parking #"), gate_45),
  },
}
