# -*- coding: utf-8 -*-

msfs_mode = 1

@AlternativeStopPositions
def customOffset_TM(aircraftData):
    
  TableIcao = {
    "B38M": 0,
    "A319": 0,
    "A321": 0,
    "A332": -0.1,
    "A333": 0.1,
    "BCS3": -0.1,
  }
  return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator, 0) )
  
@AlternativeStopPositions
def customOffset_A3(aircraftData):
    
  TableIcao = {
    "A320": 0,
  }
  return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator, 0) )
  
@AlternativeStopPositions
def customOffset_A1(aircraftData):
    
  TableIcao = {
    "B38M": 0.8,
    "B737": 0.8,
    "B738": 0.8,
    "B735": 0.8,
    "B734": 0.8,
    "B733": 0.8,
    "A319": 0.8,
    "A320": 0.8,
    "A321": 0.8,
    "BCS3": 0.7,
  }
  return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator, 0) )
  
@AlternativeStopPositions
def customOffset_A24(aircraftData):
    
  TableIcao = {
    "A319": -3.7,
    "A320": 1.2,
    "A321": 2.15,
    "B735": -3.7,
    "B734": -3.7,
    "B733": -3.7,
    "BCS3": 1.1,
  }
  return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator, 0) )
  
@AlternativeStopPositions
def customOffset_A28(aircraftData):
    
  TableIcao = {
    "A319": -2.7,
    "A320": 1.2,
    "A321": 2.15,
    "B735": -2.7,
    "B734": -2.7,
    "B733": -2.7,
    "BCS3": 1.15,
  }
  return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator, 0) )
  
@AlternativeStopPositions
def customOffset_A25(aircraftData):
    
  TableIcao = {
    "A320": 0,
    "A321": 2.15,
  }
  return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator, 0) )
  
@AlternativeStopPositions
def customOffset_A267(aircraftData):
    
  TableIcao = {
    "A319": 0.3,
    "A320": 0.3,
    "A321": 2.15,
    "B735": 2.5,
    "B734": 2.5,
    "B733": 2.5,
    "BCS3": 2.4,
  }
  return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator, 0) )
  
@AlternativeStopPositions
def customOffset_A21419(aircraftData):
    
  TableIcao = {
    "A320": 0,
    "A321": 2.15,
    "B735": 2.25,
    "B734": 2.25,
    "B733": 2.25,
    "BCS3": -0.05,
  }
  return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator, 0) )
  
@AlternativeStopPositions
def customOffset_A5CA(aircraftData):
    
  TableIcao = {
    "B738": 0.9,
    "AT76": -2.05,
  }
  return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator, 0) )
  
@AlternativeStopPositions
def customOffset_A5CB(aircraftData):
    
  TableIcao = {
    "B738": 0,
    "B77L": 0.8,
    "A306": 0.75,
    "AT76": -2.5,
  }
  return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator, 0) )

parkings = {
   PARKING : {
      None : ( CustomizedName("Apron 2|Stand #"), ),
      204 : ( CustomizedName("Apron 2|Stand #"), customOffset_A24 ),
      205 : ( CustomizedName("Apron 2|Stand #"), customOffset_A25 ),
      206 : ( CustomizedName("Apron 2|Stand #"), customOffset_A267 ),
      207 : ( CustomizedName("Apron 2|Stand #"), customOffset_A267 ),
      208 : ( CustomizedName("Apron 2|Stand #"), customOffset_A28 ),
      214 : ( CustomizedName("Apron 2|Stand #"), customOffset_A21419 ),
      215 : ( CustomizedName("Apron 2|Stand #"), customOffset_A21419 ),
      216 : ( CustomizedName("Apron 2|Stand #"), customOffset_A21419 ),
      217 : ( CustomizedName("Apron 2|Stand #"), customOffset_A21419 ),
      218 : ( CustomizedName("Apron 2|Stand #"), customOffset_A21419 ),
      219 : ( CustomizedName("Apron 2|Stand #"), customOffset_A21419 ),
      227 : ( CustomizedName("Apron 5 (Cargo)|Stand 512"), customOffset_A5CA ),
      228 : ( CustomizedName("Apron 5 (Cargo)|Stand 511"), customOffset_A5CA ),
      302 : ( CustomizedName("Terminal (C Sector) [300-309]|Gate #"), customOffset_TM ),
      303 : ( CustomizedName("Terminal (C Sector) [300-309]|Gate #"), customOffset_TM ),
      304 : ( CustomizedName("Terminal (C Sector) [300-309]|Gate #"), customOffset_TM ),
      305 : ( CustomizedName("Terminal (C Sector) [300-309]|Gate #"), customOffset_TM ),
      306 : ( CustomizedName("Terminal (C Sector) [300-309]|Gate #"), customOffset_TM ),
      307 : ( CustomizedName("Terminal (C Sector) [300-309]|Gate #"), customOffset_TM ),
      308 : ( CustomizedName("Terminal (C Sector) [300-309]|Gate #"), customOffset_TM ),
      309 : ( CustomizedName("Terminal (C Sector) [300-309]|Gate #"), customOffset_TM ),
      311 : ( CustomizedName("Apron 3|Stand #"), customOffset_A3 ),
      312 : ( CustomizedName("Apron 3|Stand #"), customOffset_A3 ),
      313 : ( CustomizedName("Apron 3|Stand #"), customOffset_A3 ),
      314 : ( CustomizedName("Apron 3|Stand #"), customOffset_A3 ),
      315 : ( CustomizedName("Apron 3|Stand #"), customOffset_A3 ),
      316 : ( CustomizedName("Apron 3|Stand #"), customOffset_A3 ),
      317 : ( CustomizedName("Apron 3|Stand #"), customOffset_A3 ),
      321 : ( CustomizedName("Apron 3|Stand #"), customOffset_A3 ),
      322 : ( CustomizedName("Apron 3|Stand #"), customOffset_A3 ),
      323 : ( CustomizedName("Apron 3|Stand #"), customOffset_A3 ),
      324 : ( CustomizedName("Apron 3|Stand #"), customOffset_A3 ),
      325 : ( CustomizedName("Apron 3|Stand #"), customOffset_A3 ),
      326 : ( CustomizedName("Apron 3|Stand #"), customOffset_A3 ),
      327 : ( CustomizedName("Apron 3|Stand #"), customOffset_A3 ),
      102 : ( CustomizedName("Terminal (B Sector) [102-109]|Gate #"), customOffset_TM ),
      104 : ( CustomizedName("Terminal (B Sector) [102-109]|Gate #"), customOffset_TM ),
      105 : ( CustomizedName("Terminal (B Sector) [102-109]|Gate #"), customOffset_TM ),
      106 : ( CustomizedName("Terminal (B Sector) [102-109]|Gate #"), customOffset_TM ),
      107 : ( CustomizedName("Terminal (B Sector) [102-109]|Gate #"), customOffset_TM ),
      108 : ( CustomizedName("Terminal (B Sector) [102-109]|Gate #"), customOffset_TM ),
      109 : ( CustomizedName("Terminal (B Sector) [102-109]|Gate #"), customOffset_TM ),
      101 : ( CustomizedName("Apron 1|Stand #"), ),
      103 : ( CustomizedName("Apron 1|Stand #"), ),
      110 : ( CustomizedName("Apron 1|Stand #"), customOffset_A1 ),
      112 : ( CustomizedName("Apron 1|Stand #"), customOffset_A1 ),
      113 : ( CustomizedName("Apron 1|Stand #"), customOffset_A1 ),
      114 : ( CustomizedName("Apron 1|Stand #"), customOffset_A1 ),
      115 : ( CustomizedName("Apron 1|Stand #"), customOffset_A1 ),
      401 : ( CustomizedName("Apron 4|Stand #"), ),
      402 : ( CustomizedName("Apron 4|Stand #"), ),
      461 : ( CustomizedName("Apron 4|Stand #"), ),
      462 : ( CustomizedName("Apron 4|Stand #"), ),
      467 : ( CustomizedName("Apron 4|Stand #"), ),
      468 : ( CustomizedName("Apron 4|Stand #"), ),
      469 : ( CustomizedName("Apron 4|Stand #"), ),
      470 : ( CustomizedName("Apron 4|Stand #"), ),
      471 : ( CustomizedName("Apron 4|Stand #"), ),
      472 : ( CustomizedName("Apron 4|Stand #"), ),
      473 : ( CustomizedName("Apron 4|Stand #"), ),
      474 : ( CustomizedName("Apron 4|Stand #"), ),
      475 : ( CustomizedName("Apron 4|Stand #"), ),
      476 : ( CustomizedName("Apron 4|Stand #"), ),
      477 : ( CustomizedName("Apron 4|Stand #"), ),
      478 : ( CustomizedName("Apron 4|Stand #"), ),
      479 : ( CustomizedName("Apron 4|Stand #"), ),
      501 : ( CustomizedName("Apron 5 (Cargo)|Stand #"), customOffset_A5CB ),
      502 : ( CustomizedName("Apron 5 (Cargo)|Stand #"), customOffset_A5CB ),
      503 : ( CustomizedName("Apron 5 (Cargo)|Stand #"), customOffset_A5CB ),
   },
   GATE : {
      None : ( CustomizedName("Terminal (C Sector) [300-309]|Gate #"), customOffset_TM ),
   }
}