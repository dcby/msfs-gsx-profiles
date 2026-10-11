# -- coding: utf-8 --

msfs_mode = 1
icao = "eddm"

def HandleAircraftOffsets(aircraftData, specificTables, genericTable):
    major_id = aircraftData.idMajor
    minor_id = aircraftData.idMinor

    if major_id in specificTables:
        specific_table, fallback_key = specificTables[major_id]
        result = specific_table.get(minor_id)
        if result is None:
            result = specific_table.get(fallback_key)
    else:
        result = genericTable.get(major_id, 0)

    return result

@AlternativeStopPositions
def customOffsetequal(aircraftData):

    table = {
        0: 0,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )
    
@AlternativeStopPositions
def customOffset14(aircraftData):

    table = {
        0: 0,
        10: 8,
        11: 10,
        300: 10,
        310: 8,
        321: 2,
        20000: 10,
        380: 16.2,
    }

    table787 = {
        8: 10,
        9: 12,
        10: 14,
    }

    table777 = {
        200: 12,
        300: 14,
    }

    table767 = {
        200: 6,
        300: 8,
        400: 12,
    }

    table757 = {
        200: 8,
        300: 10,
    }

    table747 = {
        400: 10,
        800: 14,
    }

    table737 = {
        800: 0,
        900: 2,
    }

    table330 = {
        200: 10,
        300: 12,
        800: 10,
        900: 12,
    }

    table340 = {
        200: 10,
        300: 12,
        500: 14,
        600: 16,
    }

    table350 = {
        800: 10,
        900: 12,
        1000: 14,
    }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            787 : (table787, 8),
            777 : (table777, 200),
            767 : (table767, 200),
            757 : (table757, 200),
            747 : (table747, 400),
            737 : (table737, 800),
            330 : (table330, 200),
            340 : (table340, 200),
            350 : (table350, 800),
        },
        table) )

@AlternativeStopPositions
def customOffset14short(aircraftData):

    table = {
        0: 0,
        300: 10,
        310: 8,
        320: 4,
        321: 6,
        20000: 10,
    }

    table767 = {
        200: 8,
        300: 10,
        400: 12,
    }

    table757 = {
        200: 10,
        300: 12,
    }

    table737 = {
        700: 0,
        800: 4,
        900: 6,
    }


    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 700),
            757 : (table757, 200),
            767 : (table767, 200),
        },
        table) )

@AlternativeStopPositions
def customOffset14for380(aircraftData):

    table = {
        0: 0,
        10: 14,
        11: 16,
        300: 10,
        310: 8,
        321: 2,
        20000: 10,
        380: 12.1,
    }

    table787 = {
        8: 14,
        9: 18,
        10: 20,
    }

    table777 = {
        200: 16,
        300: 18,
    }

    table767 = {
        200: 10,
        300: 12,
        400: 16,
    }

    table757 = {
        200: 8,
        300: 10,
    }

    table747 = {
        400: 18,
        800: 20,
    }

    table737 = {
        800: 0,
        900: 2,
    }

    table330 = {
        200: 14,
        300: 16,
        800: 14,
        900: 16,
    }

    table340 = {
        200: 14,
        300: 16,
        500: 18,
        600: 20,
    }

    table350 = {
        800: 12,
        900: 16,
        1000: 18,
    }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            787 : (table787, 8),
            777 : (table777, 200),
            767 : (table767, 200),
            757 : (table757, 200),
            747 : (table747, 400),
            737 : (table737, 800),
            330 : (table330, 200),
            340 : (table340, 200),
            350 : (table350, 800),
        },
        table) )


@AlternativeStopPositions
def customOffset35p37(aircraftData):

    table = {
        0: 0,
        10: 14,
        11: 16,
        300: 9.7,
        310: 8,
        321: 1.8,
        20000: 10,
        380: 13.8,
    }

    table787 = {
        8: 9.7,
        9: 11.7,
        10: 13.8,
    }

    table777 = {
        200: 11.7,
        300: 13.8,
    }

    table767 = {
        200: 9.7,
        300: 11.7,
        400: 11.7,
    }

    table757 = {
        200: 7.7,
        300: 7.7,
    }

    table747 = {
        400: 11.7,
        800: 13.8,
    }

    table737 = {
        800: 0,
        900: 1.8,
    }

    table330 = {
        200: 7.7,
        300: 9.7,
        800: 7.7,
        900: 9.7,
    }

    table340 = {
        200: 7.7,
        300: 9.7,
        500: 11.7,
        600: 13.6,
    }

    table350 = {
        800: 10.7,
        900: 12.7,
        1000: 12.7,
    }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            787 : (table787, 8),
            777 : (table777, 200),
            767 : (table767, 200),
            757 : (table757, 200),
            747 : (table747, 400),
            737 : (table737, 800),
            330 : (table330, 200),
            340 : (table340, 200),
            350 : (table350, 800),
        },
        table) )



@AlternativeStopPositions
def customOffset22p24(aircraftData):

    table = {
        0: 0,
        10: 14,
        11: 16,
        300: 10,
        310: 8,
        321: 2,
        20000: 10,
        380: 18.1,
    }

    table787 = {
        8: 14,
        9: 18,
        10: 20,
    }

    table777 = {
        200: 16,
        300: 18,
    }

    table767 = {
        200: 10,
        300: 12,
        400: 16,
    }

    table757 = {
        200: 8,
        300: 10,
    }

    table747 = {
        400: 18,
        800: 20,
    }

    table737 = {
        800: 0,
        900: 2,
    }

    table330 = {
        200: 14,
        300: 16,
        800: 14,
        900: 16,
    }

    table340 = {
        200: 14,
        300: 16,
        500: 18,
        600: 20,
    }

    table350 = {
        800: 12,
        900: 16,
        1000: 18,
    }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            787 : (table787, 8),
            777 : (table777, 200),
            767 : (table767, 200),
            757 : (table757, 200),
            747 : (table747, 400),
            737 : (table737, 800),
            330 : (table330, 200),
            340 : (table340, 200),
            350 : (table350, 800),
        },
        table) )

@AlternativeStopPositions
def customOffsetsmall(aircraftData):

    table = {
        0: 0,
        72: 1.8,
        170: 1.8,
        175: 1.8,
        190: 5.8,
        195: 5.8,
        700: 3.9,
        900: 5.8,
        1000: 7.6,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )

@AlternativeStopPositions
def customOffsets6(aircraftData):

    table = {
        0: 0,
        190: 4,
        195: 4,
        900: 1.8,
        1000: 6.1,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )
    
Apron1Gate = CustomizedName("Apron 1 East (110-135)| Gate #",1)
Apron1GateA = CustomizedName("Apron 1 East (110-135)| Gate #",1)
Apron1GateB = CustomizedName("Apron 1 East (110-135)| Gate #",1)
Apron1Remote = CustomizedName("Apron 1 West (161-196)| Gate #",2)


Apron2T = CustomizedName("Apron 2 (201-224 + 231-234 + 261-263)| Gate #",3)
Apron2TA = CustomizedName("Apron 2 (201-224 + 231-234 + 261-263)| Gate #",3)
Apron2TB = CustomizedName("Apron 2 (201-224 + 231-234 + 261-263)| Gate #",3) 

Apron2Sat = CustomizedName("Apron 2 Satelite (244-256)| Gate #",4)
Apron2SatA = CustomizedName("Apron 2 Satelite (244-256)| Gate #",4)
Apron2SatB = CustomizedName("Apron 2 Satelite (244-256)| Gate #",4)

Apron3 = CustomizedName("Apron 3 (321-330 + 341-349)| Gate #",5)
Apron3Sat = CustomizedName("Apron 3 Satelite (301-318)| Gate #",6)
Apron3SatA = CustomizedName("Apron 3 Satelite (301-318)| Gate #",6)
Apron3SatB = CustomizedName("Apron 3 Satelite (301-318)| Gate #",6)


Apron5 = CustomizedName("Apron 5 (581-595)| Stand #",7)
Apron6 = CustomizedName("Apron 6 (601-607)| Stand #",8)
Apron7 = CustomizedName("Apron 7 (701-703)| Stand #",9)
Apron8 = CustomizedName("Apron 8 (801-805)| Stand #",10) 
Apron9 = CustomizedName("Apron 9 (901-907)| Stand #",11)
Apron13 = CustomizedName("Apron 13 (G11-G14 + G21-G24)| Stand #",12)
Apron35 = CustomizedName("Apron 35 (352-372 + 511-523)| Stand #",13)

parkings = {

    GATE : {
    None : (),
        21 : (Apron13, ),
    
        110 : (Apron1Gate, customOffset14, ),
        111 : (Apron1Gate, customOffset14, ),
        112 : (Apron1Gate, customOffset14, ),
        116 : (Apron1Gate, customOffset14, ),
        118 : (Apron1Gate, customOffset14, ),
        119 : (Apron1Gate, customOffset14, ),
        120 : (Apron1Gate, customOffset14, ),
        121 : (Apron1Gate, customOffset14, ),
        135 : (Apron1Gate, customOffset14, ),
        
        161 : (Apron1Remote, customOffset14, ),
        162 : (Apron1Remote, customOffset14, ),
        163 : (Apron1Remote, customOffset14, ),
        164 : (Apron1Remote, customOffset14, ),
        165 : (Apron1Remote, customOffset14, ),
        155 : (Apron1Remote, customOffset14, ),
        171 : (Apron1Remote, customOffset14short, ),
        172 : (Apron1Remote, customOffset14short, ),
        173 : (Apron1Remote, customOffset14short, ),
        174 : (Apron1Remote, customOffset14short, ),
        175 : (Apron1Remote, customOffset14short, ),
        181 : (Apron1Remote, customOffset14short, ),
        182 : (Apron1Remote, customOffset14short, ),
        183 : (Apron1Remote, customOffset14short, ),
        184 : (Apron1Remote, customOffset14short, ),
        185 : (Apron1Remote, customOffset14short, ),
        186 : (Apron1Remote, customOffset14short, ),
        187 : (Apron1Remote, customOffset14short, ),
        188 : (Apron1Remote, customOffset14short, ),
        189 : (Apron1Remote, customOffset14short, ),
        191 : (Apron1Remote, customOffset14short, ),
        192 : (Apron1Remote, customOffset14short, ),
        193 : (Apron1Remote, customOffset14short, ),
        194 : (Apron1Remote, customOffset14short, ),
        195 : (Apron1Remote, customOffset14short, ),
        196 : (Apron1Remote, customOffset14short, ),
        
        201 : (Apron2T, customOffset22p24, ),
        203 : (Apron2T, customOffset14, ),
        206 : (Apron2T, customOffset14, ),
        208 : (Apron2T, customOffset14, ),
        211 : (Apron2T, customOffset14, ),
        214 : (Apron2T, customOffset22p24, ),
        216 : (Apron2T, customOffset22p24, ),
        218 : (Apron2T, customOffset22p24, ),
        221 : (Apron2T, customOffset14, ),
        231 : (Apron2T, customOffsetsmall, ),
        232 : (Apron2T, customOffsetsmall, ),
        233 : (Apron2T, customOffsetsmall, ),
        234 : (Apron2T, customOffsetsmall, ),
        
        244 : (Apron2Sat, customOffset22p24, ),
        245 : (Apron2Sat, customOffset22p24, ),
        246 : (Apron2Sat, customOffset22p24, ),
        247 : (Apron2Sat, customOffset22p24, ),
        250 : (Apron2Sat, customOffset22p24, ),
        253 : (Apron2Sat, customOffset22p24, ),
        254 : (Apron2Sat, customOffset22p24, ),
        255 : (Apron2Sat, customOffset22p24, ),
        256 : (Apron2Sat, customOffset22p24, ),
        
        261 : (Apron2T, customOffsetequal, ),
        263 : (Apron2T, customOffsetequal, ),
        
        308 : (Apron3Sat, customOffset14short, ),
        309 : (Apron3Sat, customOffset14short, ),
        310 : (Apron3Sat, customOffset14short, ),
        311 : (Apron3Sat, customOffset14short, ),
        312 : (Apron3Sat, customOffset14short, ),
        313 : (Apron3Sat, customOffset14short, ),
        
        321 : (Apron3, customOffsetequal, ),
        322 : (Apron3, customOffsetequal, ),
        323 : (Apron3, customOffsetequal, ),
        324 : (Apron3, customOffsetequal, ),
        325 : (Apron3, customOffsetequal, ),
        327 : (Apron3, customOffset14short, ),
        328 : (Apron3, customOffset14short, ),
        329 : (Apron3, customOffset14short, ),
        330 : (Apron3, customOffset14short, ),
        341 : (Apron3, customOffsetequal, ),
        342 : (Apron3, customOffsetequal, ),
        343 : (Apron3, customOffsetequal, ),
        344 : (Apron3, customOffsetequal, ),
        345 : (Apron3, customOffsetequal, ),
        346 : (Apron3, customOffsetequal, ),
        347 : (Apron3, customOffsetequal, ),
        348 : (Apron3, customOffsetequal, ),
        349 : (Apron3, customOffsetequal, ),
        
        352 : (Apron35, customOffset35p37, ),
        353 : (Apron35, customOffset35p37, ),
        354 : (Apron35, customOffset35p37, ),
        355 : (Apron35, customOffset35p37, ),
        356 : (Apron35, customOffset35p37, ),
        371 : (Apron35, customOffset35p37, ),
        372 : (Apron35, customOffset35p37, ),
        
        511 : (Apron35, customOffsetequal, ),
        512 : (Apron35, customOffsetequal, ),
        513 : (Apron35, customOffsetequal, ),
        514 : (Apron35, customOffsetequal, ),
        515 : (Apron35, customOffsetequal, ),
        516 : (Apron35, customOffsetequal, ),
        517 : (Apron35, customOffsetequal, ),
        518 : (Apron35, customOffsetequal, ),
        519 : (Apron35, customOffsetequal, ),
        520 : (Apron35, customOffsetequal, ),
        521 : (Apron35, customOffsetequal, ),
        522 : (Apron35, customOffsetequal, ),
        523 : (Apron35, customOffsetequal, ),
        
        581 : (Apron5, customOffsets6, ),
        582 : (Apron5, customOffsets6, ),
        583 : (Apron5, customOffsets6, ),
        584 : (Apron5, customOffsets6, ),
        585 : (Apron5, customOffsets6, ),
        586 : (Apron5, customOffsets6, ),
        591 : (Apron5, customOffsetequal, ),
        592 : (Apron5, customOffsetequal, ),
        593 : (Apron5, customOffsetequal, ),
        594 : (Apron5, customOffsetequal, ),
        595 : (Apron5, customOffsetequal, ),
        
        601 : (Apron6, customOffsetequal, ),
        602 : (Apron6, customOffsetequal, ),
        603 : (Apron6, customOffsetequal, ),
        604 : (Apron6, customOffsetequal, ),
        605 : (Apron6, customOffsetequal, ),
        606 : (Apron6, customOffsetequal, ),
        607 : (Apron6, customOffsetequal, ),
        
        901 : (Apron9, customOffset22p24, ),
        902 : (Apron9, customOffset22p24, ),
        903 : (Apron9, customOffset22p24, ),
        904 : (Apron9, customOffset22p24, ),
        905 : (Apron9, customOffset22p24, ),
        906 : (Apron9, customOffset22p24, ),
        907 : (Apron9, customOffset22p24, ),
    },
    
    GATE_A : {
        None : ( ),
        113 : (Apron1GateA, customOffset14, ),
        115 : (Apron1GateA, customOffset14, ),
        
        204 : (Apron2TA, customOffset22p24, ),
        207 : (Apron2TA, customOffset14, ),
        212 : (Apron2TA, customOffset22p24, ),
        213 : (Apron2TA, customOffset22p24, ),
        215 : (Apron2TA, customOffset22p24, ),
        217 : (Apron2TA, customOffset22p24, ),
        
        248 : (Apron2SatA, customOffset22p24, ),
        249 : (Apron2SatA, customOffset22p24, ),
        252 : (Apron2SatA, customOffset22p24, ),
        
        301 : (Apron3SatA, customOffset14, ),
        302 : (Apron3SatA, customOffset22p24, ),
        317 : (Apron3SatA, customOffset14, ),
        318 : (Apron3SatA, customOffset14, ),
    },
    
    GATE_B : {
        None : ( ),
        117 : (Apron1GateB, customOffset14, ),
        
        202 : (Apron2TB, customOffset14, ),
        205 : (Apron2TB, customOffset14, ),
        209 : (Apron2TB, customOffset22p24, ),
        210 : (Apron2TB, customOffset14, ),
        219 : (Apron2TB, customOffset22p24, ),
        220 : (Apron2TB, customOffset22p24, ),
        222 : (Apron2TB, customOffset22p24, ),
        223 : (Apron2TB, customOffset22p24, ),
        224 : (Apron2TB, customOffset14for380, ),
        
        251 : (Apron2SatB, customOffset14, ),
        
        301 : (Apron3SatB, customOffset14, ),
        302 : (Apron3SatB, customOffset14, ),
        317 : (Apron3SatB, customOffset14, ),
        318 : (Apron3SatB, customOffset14, ),
    }, 
    
    GATE_G : {
        None : ( ),
        11 : (Apron13, customOffsetequal, ),
        12 : (Apron13, customOffsetequal, ),
        13 : (Apron13, customOffsetequal, ),
        14 : (Apron13, customOffsetequal, ),
        22 : (Apron13, customOffsetequal, ),
        23 : (Apron13, customOffsetequal, ),
        24 : (Apron13, customOffsetequal, ),
    },
    
    PARKING : {
        None : ( ),
        262 : (Apron2T, customOffsetequal, ),
        
        701 : (Apron7, customOffsetequal, ),
        702 : (Apron7, customOffsetequal, ),
        703 : (Apron7, customOffsetequal, ),

        801 : (Apron8, customOffsetequal, ),
        802 : (Apron8, customOffsetequal, ),
        803 : (Apron8, customOffsetequal, ),
        804 : (Apron8, customOffsetequal, ),
        805 : (Apron8, customOffsetequal, ),
    },  
    
}
