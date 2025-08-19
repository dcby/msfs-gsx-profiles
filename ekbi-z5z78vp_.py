# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def sw5(aircraftData):

  table = {
    "B77L": 0,
  }

  return Distance.fromMeters(table.get(aircraftData.icaoTypeDesignator, 0))

parkings = {
  SW_PARKING: {
    5: (CustomizedName("Apron South|Stand #"), sw5),
  },
}
