# -- coding: utf-8 --

msfs_mode = 1
icao = "lipz"

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
def customOffsetStands1line(aircraftData):

	table = {
		0: 0,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )

@AlternativeStopPositions
def customOffsetStands2linesType1(aircraftData):

	table = {
		0: 0,
		221: 6.03,
		223: 6.03,
		320: 6.03,
		321: 6.03,
		190: 6.03,
		195: 6.03,
	}

	table737 = {
		0: 0,
		800: 6.03,
		900: 6.03,
	}
	
	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, 
		{ 
			737 : (table737, 0),
		},
		table) )

@AlternativeStopPositions
def customOffsetStands2linesType2(aircraftData):

	table = {
		0: 0,
		221: 5.52,
		223: 5.52,
		320: 5.52,
		321: 5.52,
		190: 5.52,
		195: 5.52,
	}

	table737 = {
		0: 0,
		800: 5.52,
		900: 5.52,
	}
	
	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, 
		{ 
			737 : (table737, 0),
		},
		table) )

@AlternativeStopPositions
def customOffsetStands2linesType3(aircraftData):

	table = {
		0: 0,
		221: 4.27,
		223: 4.27,
		320: 4.27,
		321: 4.27,
		190: 4.27,
		195: 4.27,
	}

	table737 = {
		0: 0,
		800: 4.27,
		900: 4.27,
	}
	
	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, 
		{ 
			737 : (table737, 0),
		},
		table) )

@AlternativeStopPositions
def customOffsetStands2linesType4(aircraftData):

	table = {
		0: 0,
		221: 6.12,
		223: 6.12,
		320: 6.12,
		321: 6.12,
		190: 6.12,
		195: 6.12,
	}

	table737 = {
		0: 0,
		800: 6.12,
		900: 6.12,
	}
	
	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, 
		{ 
			737 : (table737, 0),
		},
		table) )

@AlternativeStopPositions
def customOffsetStands2linesCargo(aircraftData):

	table = {
		0: 0,
		221: 7,
		223: 7,
		320: 7,
		321: 7,
		190: 7,
		195: 7,
	}

	table737 = {
		0: 0,
		800: 7,
		900: 7,
	}
	
	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, 
		{ 
			737 : (table737, 0),
		},
		table) )

@AlternativeStopPositions
def CustomOffsetStand433(aircraftData):
    
    TableGroup = {
        "ARC-D" : 4.67,
        "ARC-E" : 4.67,
        "ARC-F" : 4.67,
        "Unknown" : 0,
    }

    return Distance.fromMeters(TableGroup.get(aircraftData.aircraftGroup, 0))

@AlternativeStopPositions
def CustomOffsetStand441(aircraftData):
    
    TableGroup = {
        "ARC-D" : 8.55,
        "ARC-E" : 12.82,
        "ARC-F" : 12.82,
        "Unknown" : 0,
    }

    return Distance.fromMeters(TableGroup.get(aircraftData.aircraftGroup, 0))

@AlternativeStopPositions
def customOffsetStands5linesCargo(aircraftData):
    
    TableGroup = {
        "ARC-D" : 6,
        "ARC-E" : 8.02,
        "ARC-F" : 10.12,
        "Unknown" : 0,
    }

    return Distance.fromMeters(TableGroup.get(aircraftData.aircraftGroup, 0))

@AlternativeStopPositions
def customOffsetStands3linesCargo(aircraftData):
    
    TableGroup = {
        "ARC-D" : 8.26,
        "ARC-E" : 14.79,
        "ARC-F" : 14.79,
        "Unknown" : 0,
    }

    return Distance.fromMeters(TableGroup.get(aircraftData.aircraftGroup, 0))

@AlternativeStopPositions
def CustomOffsetStand323(aircraftData):
    
    TableGroup = {
		"ARC-C" : 5.05,
        "ARC-D" : 9.22,
        "ARC-E" : 13.78,
        "ARC-F" : 19.38,
        "Unknown" : 0,
    }

    return Distance.fromMeters(TableGroup.get(aircraftData.aircraftGroup, 0))

@AlternativeStopPositions
def CustomOffsetStand324(aircraftData):
    
    TableGroup = {
		"ARC-C" : 12.35,
        "ARC-D" : 12.35,
        "ARC-E" : 17.3,
        "ARC-F" : 23.35,
        "Unknown" : 0,
    }

    return Distance.fromMeters(TableGroup.get(aircraftData.aircraftGroup, 0))

@AlternativeStopPositions
def CustomOffsetStand325(aircraftData):
    
    TableGroup = {
		"ARC-C" : 9.81,
        "ARC-D" : 13.91,
        "ARC-E" : 18.86,
        "ARC-F" : 24.91,
        "Unknown" : 0,
    }

    return Distance.fromMeters(TableGroup.get(aircraftData.aircraftGroup, 0))

@AlternativeStopPositions
def CustomOffsetStand326(aircraftData):
    
    TableGroup = {
        "ARC-D" : 5.1,
        "ARC-E" : 10.18,
        "ARC-F" : 16.78,
        "Unknown" : 0,
    }

    return Distance.fromMeters(TableGroup.get(aircraftData.aircraftGroup, 0))

@AlternativeStopPositions
def CustomOffsetStand327(aircraftData):
    
    TableGroup = {
        "ARC-E" : 9.04,
        "ARC-F" : 9.04,
        "Unknown" : 0,
    }

    return Distance.fromMeters(TableGroup.get(aircraftData.aircraftGroup, 0))

@AlternativeStopPositions
def CustomOffsetStand329(aircraftData):
    
    TableGroup = {
        "ARC-E" : 13.78,
        "ARC-F" : 13.78,
        "Unknown" : 0,
    }

    return Distance.fromMeters(TableGroup.get(aircraftData.aircraftGroup, 0))

@AlternativeStopPositions
def CustomOffsetStand176(aircraftData):
    
    TableGroup = {
        "ARC-D" : 3.58,
        "ARC-E" : 3.58,
        "ARC-F" : 3.58,
        "Unknown" : 0,
    }

    return Distance.fromMeters(TableGroup.get(aircraftData.aircraftGroup, 0))

NewTerminal = CustomizedName("New Terminal & 3XX Remotes (322-372) | Stand #",1)
OldTerminal = CustomizedName("Old Terminal (433-441) | Stand #",2)
Remotes = CustomizedName("Remotes (110-176 + 217-220) | Stand #",3)
Cargo = CustomizedName("Cargo (177-191) | Stand #",4)
Ga = CustomizedName("General Aviation | Stand #",5)
Others = CustomizedName("Others | Stand #",6)

parkings = {
	0 : {
		None : ( ),
				2 : (Others, ),
				110 : (Remotes, customOffsetStands2linesType1),
				111 : (Remotes, customOffsetStands2linesType1),
				112 : (Remotes, customOffsetStands2linesType1),
				113 : (Remotes, customOffsetStands2linesType1),
				114 : (Remotes, customOffsetStands2linesType1),
				115 : (Remotes, customOffsetStands2linesType1),
				116 : (Remotes, customOffsetStands2linesType1),
				176 : (Remotes, CustomOffsetStand176),
				177 : (Cargo, customOffsetStands2linesCargo),
				178 : (Cargo, customOffsetStands5linesCargo),
				179 : (Cargo, customOffsetStands2linesCargo),
				180 : (Cargo, customOffsetStands2linesCargo),
				181 : (Cargo, customOffsetStands5linesCargo),
				182 : (Cargo, customOffsetStands2linesCargo),
				183 : (Cargo, customOffsetStands2linesCargo),
				184 : (Cargo, customOffsetStands3linesCargo),
				185 : (Cargo, customOffsetStands2linesCargo),
				186 : (Cargo, customOffsetStands2linesCargo),
				187 : (Cargo, customOffsetStands3linesCargo),
				188 : (Cargo, customOffsetStands2linesCargo),
				189 : (Cargo, customOffsetStands2linesCargo),
				190 : (Cargo, customOffsetStands3linesCargo),
				191 : (Cargo, customOffsetStands2linesCargo),
				217 : (Remotes, customOffsetStands1line),
				218 : (Remotes, customOffsetStands1line),
				219 : (Remotes, customOffsetStands1line),
				220 : (Remotes, customOffsetStands1line),
				322 : (NewTerminal, customOffsetStands2linesType3),
				323 : (NewTerminal, CustomOffsetStand323),
				324 : (NewTerminal, CustomOffsetStand324),
				325 : (NewTerminal, CustomOffsetStand325),
				326 : (NewTerminal, CustomOffsetStand326),
				327 : (NewTerminal, CustomOffsetStand327),
				328 : (NewTerminal, customOffsetStands1line),
				329 : (NewTerminal, CustomOffsetStand329),
				330 : (NewTerminal, customOffsetStands1line),
				362 : (NewTerminal, customOffsetStands1line),
				363 : (NewTerminal, customOffsetStands1line),
				364 : (NewTerminal, customOffsetStands1line),
				365 : (NewTerminal, customOffsetStands2linesType2),
				366 : (NewTerminal, customOffsetStands2linesType2),
				367 : (NewTerminal, customOffsetStands1line),
				370 : (NewTerminal, customOffsetStands2linesType3),
				371 : (NewTerminal, customOffsetStands2linesType3),
				372 : (NewTerminal, customOffsetStands2linesType3),
				433 : (OldTerminal, CustomOffsetStand433),
				434 : (OldTerminal, customOffsetStands2linesType4),
				435 : (OldTerminal, customOffsetStands2linesType4),
				436 : (OldTerminal, customOffsetStands2linesType4),
				437 : (OldTerminal, customOffsetStands2linesType4),
				438 : (OldTerminal, customOffsetStands2linesType4),
				439 : (OldTerminal, customOffsetStands2linesType4),
				440 : (OldTerminal, customOffsetStands2linesType4),
				441 : (OldTerminal, CustomOffsetStand441),
				442 : (Ga, customOffsetStands1line),
				443 : (Ga, customOffsetStands1line),
				544 : (Ga, customOffsetStands1line),
				545 : (Ga, customOffsetStands1line),
				546 : (Ga, customOffsetStands1line),
	},
}