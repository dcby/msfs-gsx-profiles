# -- coding: utf-8 --

msfs_mode = 1
icao = "kden"

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
def customOffsetA1(aircraftData):
	table = {
		0: 0,
		223: 1.7,
		320: 1.85,
		319: 1.85,
		321: 8.05,
		200: 0,
		550: 0,
		700: 0,
		900: 5.4,
		1000: 5.4,
		170: -0.05,
		175: -0.05,
		190: 6.9,
		195: 6.9,
		82: 5.55,
		83: 5.55,
		88: 5.55,
		
	}

	table737 = {
		600: 1.875,
		700: 1.875,
		800: 8,
		900: 8,
	}


	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, 
		{ 
			737 : (table737, 0),
		},
		table) )

@AlternativeStopPositions
def customOffsetA2(aircraftData):
	table = {
		0: 0,
		223: -0.15,
		320: 0,
		319: 0,
		321: 5.2,
		550: 0,
		700: 0,
		900: 3.1,
		1000: 3.1,
		170: -0.05,
		175: -0.05,
		190: 3.05,
		195: 3.05,
		82: 3.2,
		83: 3.2,
		88: 3.2,
	}

	table737 = {
		600: 0.025,
		700: 0.025,
		800: 5.15,
		900: 5.15,
	}


	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, 
		{ 
			737 : (table737, 0),
		},
		table) )

@AlternativeStopPositions
def customOffsetA3(aircraftData):
	table = {
		0: 0,
		223: -0.15,
		320: 0,
		319: 0,
		321: 3.55,
		550: 0,
		700: 0,
		900: 3.5,
		1000: 3.5,
		380: 8,
		170: -0.05,
		175: -0.05,
		190: 3.5,
		195: 3.5,
		82: 3.65,
		83: 3.65,
		88: 3.65,
	}


	table737 = {
		600: 0.025,
		700: 0.025,
		800: 3.5,
		900: 3.5,
	}

	table777 = {
		0: 5.8,
		200: 5.8,
		300: 8,

	}

	table787 = {
		0: 5.6,
		8: 5.6,
		9: 5.6,
		10: 8,

	}

	table330 = {
		0: 5.7,
		200: 5.7,
		300: 5.9,
		800: 5.7,
		900: 5.9,
	}

	table340 = {
		300: 5.8,
		600: 0,
	}

	table350 = {
		0: 5.8,
		900: 5.8,
		1000: 8,

	}


	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, 
		{ 
			737 : (table737, 0),
			777 : (table777, 0),
			787 : (table787, 0),
			330 : (table330, 0),
			340 : (table340, 0),
			350 : (table350, 0),
		},
		table) )


@AlternativeStopPositions
def customOffsetA4(aircraftData):
	table = {
		0: 0,
		223: -0.15,
		320: 0,
		319: 0,
		321: 3.6,
		550: 0,
		700: 0,
		900: 2,
		1000: 2,
		170: -2.6,
		175: -2.6,
		190: 1.95,
		195: 1.95,
		82: 2.15,
		83: 2.15,
		88: 2.15,
	}

	table737 = {
		600: -2.6,
		700: -2.6,
		800: 3.55,
		900: 3.55,
	}


	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, 
		{ 
			737 : (table737, 0),
		},
		table) )


@AlternativeStopPositions
def customOffsetA5(aircraftData):
	table = {
		0: 0,
		223: -0.15,
		320: 0,
		319: 0,
		321: 0,
		550: 0,
		700: 0,
		900: 0,
		1000: 0,
		380: 12.45,
		170: -0.05,
		175: -0.05,
		190: -0.05,
		195: -0.05,
		82: 0.15,
		83: 0.15,
		88: 0.15,
	}

	table737 = {
		600: -0.05,
		700: -0.05,
		800: -0.05,
		900: -0.05,
	}

	table777 = {
		0: 8.95,
		200: 8.95,
		300: 12.45,

	}

	table787 = {
		0: 8.8,
		8: 8.8,
		9: 8.8,
		10: 12.3,

	}

	table330 = {
		0: 8.85,
		200: 8.85,
		300: 9.05,
		800: 8.85,
		900: 9.05,
	}

	table340 = {
		0: 0,
		300: 8.95,
		600: -14.9,

	}

	table350 = {
		0: 8.95,
		900: 8.95,
		1000: 12.45,

	}


	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, 
		{ 
			737 : (table737, 0),
			777 : (table777, 0),
			787 : (table787, 0),
			330 : (table330, 0),
			340 : (table340, 0),
			350 : (table350, 0),
		},
		table) )


@AlternativeStopPositions
def customOffsetA41(aircraftData):
	table = {
		0: 0,
		223: -0.15,
		320: 0,
		319: 0,
		321: 3.6,
		550: -8,
		700: -8,
		900: 2,
		1000: 2,
		170: 1.95,
		175: 1.95,
		190: 1.95,
		195: 1.95,
		82: 2.15,
		83: 2.15,
		88: 2.15,
	}

	table737 = {
		600: 3.65,
		700: 3.65,
		800: 3.55,
		900: 3.55,
	}


	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, 
		{ 
			737 : (table737, 0),
		},
		table) )


@AlternativeStopPositions
def customOffsetB1(aircraftData):
	table = {
		0: 0,
		223: -0.15,
		320: 0,
		319: 0,
		321: 0,
		550: 0,
		700: 0,
		900: 0,
		1000: 0,
		737: -0.05,
		380: 11.9,
		170: -0.05,
		175: -0.05,
		190: -0.05,
		195: -0.05,
		82: 0.15,
		83: 0.15,
		88: 0.15,
	}

	table777 = {
		200: 9.5,
		300: 11.9,
	}

	table787 = {
		0: 7.35,
		9: 7.35,
		10: 9.5,
	}

	table330 = {
		0: 9.35,
		200: 9.35,
		300: 9.55,
		800: 9.35,
		900: 0,
	}

	table340 = {
		300: 9.5,
		600: 0,
	}

	table350 = {
		900: 9.5,
		1000: 11.9,
	}


	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, 
		{ 
			777 : (table777, 0),
			787 : (table787, 0),
			330 : (table330, 0),
			340 : (table340, 0),
			350 : (table350, 0),
		},
		table) )

@AlternativeStopPositions
def customOffsetB2(aircraftData):
	table = {
		0: 0,
		550: 0,
		700: 0,
		900: 0,
		1000: 0,
		170: -0.05,
		175: -0.05,
		190: -0.05,
		195: -0.05,
		82: 0.1,
		83: 0.1,
		88: 0.1,

	}

	table737 = {
		600: 0,
		700: 0,
		800: 2.3,
		900: 2.3,
	}


	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, 
		{ 
			737 : (table737, 0),
		},
		table) )

@AlternativeStopPositions
def customOffsetB3(aircraftData):
	table = {
		0: 0,
		223: -0.15,
		320: 0,
		319: 0,
		321: 3.55,
		777: 5.8,
		350: 5.8,
		550: 0,
		700: 0,
		900: 3.5,
		1000: 3.5,
		380: 5.8,
		170: -0.05,
		175: -0.05,
		190: 3.5,
		195: 3.5,
		82: 3.6,
		83: 3.6,
		88: 3.6,
	}


	table737 = {
		600: 0.025,
		700: 0.025,
		800: 3.5,
		900: 3.5,
	}


	table787 = {
		0: 5.6,
		8: 5.6,
		9: 5.6,
		10: 8,

	}

	table330 = {
		0: 5.7,
		200: 5.7,
		300: 5.9,
		800: 5.7,
		900: 5.9,
	}

	table340 = {
		300: 5.8,
		600: 0,
	}



	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, 
		{ 
			737 : (table737, 0),
			787 : (table787, 0),
			330 : (table330, 0),
			340 : (table340, 0),
		},
		table) )

@AlternativeStopPositions
def customOffsetC1(aircraftData):
	table = {
		0: 0,
		223: -0.1,
		320: 0.05,
		319: 0.05,
		321: 0.05,
		170: -3.2,
		175: -3.2,
		190: 0,
		195: 0,
	}

	table737 = {
		600: -3.2,
		700: -3.2,
		800: 0,
		900: 0,
	}


	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, 
		{ 
			737 : (table737, 0),
		},
		table) )

@AlternativeStopPositions
def customOffsetFrontier(aircraftData):
	table = {
		0: 0,
		223: -0.15,
		320: 0,
		319: 0,
		321: 0,
		550: 0,
		700: 0,
		900: 0,
		1000: 0,
		170: -0.05,
		175: -0.05,
		190: -0.05,
		195: -0.05,
		82: 0.15,
		83: 0.15,
		88: 0.15,
	}

	table737 = {
		600: 0.025,
		700: 0.025,
		800: 5.15,
		900: 5.15,
	}


	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, 
		{ 
			737 : (table737, 0),
		},
		table) )

@AlternativeStopPositions
def customOffsetCargo(aircraftData):
	table = {
		0: 0,
		223: -0.1,
		320: 0.05,
		319: 0.05,
		321: 0.05,
		200: 0,
		550: 0,
		700: 0,
		900: 0,
		1000: 0,
		170: 0,
		175: 0,
		190: 0,
		195: 0,
		777: 0.05,
		11: 0.05,
		
	}

	table737 = {
		600: 0.1,
		700: 0.1,
		800: 0,
		900: 0,
	}


	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, 
		{ 
			737 : (table737, 0),
		},
		table) )



parkings = {
	GATE_A : {
		None : (),
			"2E"  : ( CustomizedName("RON Pad A East | Ramp AE2", 17), ),
			"4E"  : ( CustomizedName("RON Pad A East | Ramp AE4", 17), ),
			"6E"  : ( CustomizedName("RON Pad A East | Ramp AE6", 17), ),
			"8E"  : ( CustomizedName("RON Pad A East | Ramp AE8", 17), ),
			"10E" : ( CustomizedName("RON Pad A East | Ramp AE10", 17), ),
			14    : ( CustomizedName("Concourse A South (Gate A14-A84) | Gate A14", 2), customOffsetA1 ),
			15    : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A15", 1), customOffsetA2 ),
			16    : ( CustomizedName("Concourse A South (Gate A14-A84) | Gate A16", 2), customOffsetA1 ),
			"17W" : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A17W", 1), customOffsetA3 ),
			17    : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A17", 1), customOffsetA2 ),
			18    : ( CustomizedName("Concourse A South (Gate A14-A84) | Gate A18", 2), customOffsetA1 ),
			19    : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A19", 1), customOffsetA3 ),
			20    : ( CustomizedName("Concourse A South (Gate A14-A84) | Gate A20", 2), customOffsetA1 ),
			"21W" : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A21W", 1), customOffsetA3 ),
			21    : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A21", 1), customOffsetA2 ),
			22    : ( CustomizedName("Concourse A South (Gate A14-A84) | Gate A22", 2), customOffsetA1 ),
			23    : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A23", 1), customOffsetA3 ),
			24    : ( CustomizedName("Concourse A South (Gate A14-A84) | Gate A24", 2), customOffsetA4 ),
			"25W" : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A25W", 1), customOffsetA3 ),
			25    : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A25", 1), customOffsetA2 ),
			26    : ( CustomizedName("Concourse A South (Gate A14-A84) | Gate A26", 2), customOffsetA4 ),
			27    : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A27", 1), customOffsetA3 ),
			28    : ( CustomizedName("Concourse A South (Gate A14-A84) | Gate A28", 2), customOffsetA4 ),
			29    : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A29", 1), customOffsetA3 ),
			30    : ( CustomizedName("Concourse A South (Gate A14-A84) | Gate A30", 2), customOffsetA4 ),
			"31W" : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A31W", 1), customOffsetA3 ),
			31    : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A31", 1), customOffsetA2 ),
			32    : ( CustomizedName("Concourse A South (Gate A14-A84) | Gate A32", 2), customOffsetA4 ),
			33    : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A33", 1), customOffsetA4 ),
			"33W" : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A33W", 1), customOffsetA5 ),
			34    : ( CustomizedName("Concourse A South (Gate A14-A84) | Gate A34", 2), customOffsetA4 ),
			35    : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A35", 1), customOffsetA4 ),
			36    : ( CustomizedName("Concourse A South (Gate A14-A84) | Gate A36", 2), customOffsetA4 ),
			37    : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A37/A37W", 1), customOffsetA5 ),
			38    : ( CustomizedName("Concourse A South (Gate A14-A84) | Gate A38", 2), customOffsetA4 ),
			39    : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A39", 1), customOffsetA4 ),
			40    : ( CustomizedName("Concourse A South (Gate A14-A84) | Gate A40", 2), customOffsetA4 ),
			41    : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A41", 1), customOffsetA41 ),
			"41W" : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A41W", 1), customOffsetA5 ),
			42    : ( CustomizedName("Concourse A South (Gate A14-A84) | Gate A42", 2), customOffsetA4 ),
			43    : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A43", 1), customOffsetA4 ),
			44    : ( CustomizedName("Concourse A South (Gate A14-A84) | Gate A44", 2), customOffsetA4 ),
			45    : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A45", 1), customOffsetA4 ),
			"45W" : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A45W", 1), customOffsetA5 ),
			46    : ( CustomizedName("Concourse A South (Gate A14-A84) | Gate A46", 2), customOffsetA4 ),
			47    : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A47", 1), customOffsetA4 ),
			48    : ( CustomizedName("Concourse A South (Gate A14-A84) | Gate A48", 2), customOffsetA2 ),
			49    : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A49", 1), customOffsetA2 ),
			"49W" : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A49W", 1), customOffsetA2 ),
			50    : ( CustomizedName("Concourse A South (Gate A14-A84) | Gate A50", 2), customOffsetA2 ),
			51    : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A51", 1), customOffsetA2 ),
			52    : ( CustomizedName("Concourse A South (Gate A14-A84) | Gate A52", 2), customOffsetA2 ),
			53    : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A53", 1), customOffsetA2 ),
			71    : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A71", 1), customOffsetFrontier ),
			72    : ( CustomizedName("Concourse A South (Gate A14-A84) | Gate A72", 2), customOffsetFrontier ),
			73    : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A73", 1), customOffsetFrontier ),
			74    : ( CustomizedName("Concourse A South (Gate A14-A84) | Gate A74", 2), customOffsetFrontier ),
			75    : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A75", 1), customOffsetFrontier ),
			76    : ( CustomizedName("Concourse A South (Gate A14-A84) | Gate A76", 2), customOffsetFrontier ),
			77    : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A77", 1), customOffsetFrontier ),
			78    : ( CustomizedName("Concourse A South (Gate A14-A84) | Gate A78", 2), customOffsetFrontier ),
			79    : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A79", 1), customOffsetFrontier ),
			80    : ( CustomizedName("Concourse A South (Gate A14-A84) | Gate A80", 2), customOffsetFrontier ),
			81    : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A81", 1), customOffsetFrontier ),
			82    : ( CustomizedName("Concourse A South (Gate A14-A84) | Gate A82", 2), customOffsetFrontier ),
			83    : ( CustomizedName("Concourse A North (Gate A15-A83) | Gate A83", 1), customOffsetFrontier ),
			84    : ( CustomizedName("Concourse A South (Gate A14-A84) | Gate A84", 2), customOffsetFrontier ),

			1     : ( CustomizedName("Do Not Use | Stand A1", 21), ),
			"1W"  : ( CustomizedName("Do Not Use | Stand A1W", 21), ),
			2     : ( CustomizedName("Do Not Use | Stand A2", 21), ),
			"2W"  : ( CustomizedName("Do Not Use | Stand A2W", 21), ),
			3     : ( CustomizedName("Do Not Use | Stand A3", 21), ),
			4     : ( CustomizedName("Do Not Use | Stand A4", 21), ),
			"4W"  : ( CustomizedName("Do Not Use | Stand A4W", 21), ),
			5     : ( CustomizedName("Do Not Use | Stand A5", 21), ),
 	},

	GATE_B : {
		None : (),
			7    : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B7", 3), customOffsetA1 ),
			8    : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B8", 4), customOffsetA1 ),
			9    : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B9", 3), customOffsetA1 ),
			10   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B10", 4), customOffsetA1 ),
			11   : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B11", 3), customOffsetA1 ),
			12   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B12", 4), customOffsetA1 ),
			15   : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B15", 3), customOffsetA2 ),
			16   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B16", 4), customOffsetA2 ),
			17   : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B17", 3), customOffsetA2 ),
			18   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B18", 4), customOffsetA2 ),
			19   : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B19", 3), customOffsetA2 ),
			20   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B20", 4), customOffsetB1 ),
			21   : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B21", 3), customOffsetA2 ),
			22   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B22", 4), customOffsetB1 ),
			23   : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B23", 3), customOffsetA2 ),
			24   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B24", 4), customOffsetA2 ),
			25   : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B25", 3), customOffsetA2 ),
			26   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B26", 4), customOffsetA2 ),
			27   : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B27", 3), customOffsetA2 ),
			28   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B28", 4), customOffsetA2 ),
			29   : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B29", 3), customOffsetA2 ),
			31   : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B31", 3), customOffsetA3 ),
			32   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B32W", 4), customOffsetB1 ),
			35   : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B35", 3), customOffsetA3 ),
			36   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B36W", 4), customOffsetB1 ),
			37   : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B37", 3), customOffsetA3 ),
			38   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B38W", 4), customOffsetB1 ),
			39   : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B39/B39W", 3), customOffsetB3 ),
			41   : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B41", 3), customOffsetB3 ),
			42   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B42W", 4), customOffsetB1 ),
			43   : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B43/B43W", 3), customOffsetB3 ),
			44   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B44", 4), customOffsetA2 ),
			45   : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B45", 3), customOffsetB3 ),
			46   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B46", 4), customOffsetA2 ),
			47   : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B47", 3), customOffsetB3 ),
			48   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B48", 4), customOffsetA2 ),
			49   : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B49", 3), customOffsetB3 ),
			50   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B50", 4), customOffsetB2 ),
			51   : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B51", 3), customOffsetB2 ),
			52   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B52", 4), customOffsetA2 ),
			53   : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B53", 3), customOffsetA2 ),
			54   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B54", 4), customOffsetB2 ),
			55   : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B55", 3), customOffsetA2 ),
			56   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B56", 4), customOffsetB2 ),
			57   : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B57", 3), customOffsetB2 ),
			58   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B58", 4), customOffsetB2 ),
			59   : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B59", 3), customOffsetB2 ),
			60   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B60", 4), customOffsetB2 ),
			61   : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B61", 3), customOffsetB2 ),
			63   : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B63", 3), customOffsetA1 ),
			64   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B62", 4), customOffsetB2 ),
			65   : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B65", 3), customOffsetA1 ),
			66   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B64", 4), customOffsetB2 ),
			67   : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B67", 3), customOffsetA1 ),
			68   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B66", 4), customOffsetB2 ),
			69   : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B69", 3), customOffsetA1 ),
			70   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B68", 4), customOffsetB2 ),
			71   : ( CustomizedName("Concourse B North (Gate B7-B71) | Gate B71", 3), customOffsetA1 ),
			72   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B70", 4), customOffsetB2 ),
			80   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B80", 4), customOffsetB2 ),
			82   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B82", 4), customOffsetB2 ),
			84   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B84", 4), customOffsetB2 ),
			86   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B86", 4), customOffsetB2 ),
			88   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B88", 4), customOffsetB2 ),
			90   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B90", 4), customOffsetB2 ),
			92   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B92", 4), customOffsetB2 ),
			94   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B94", 4), customOffsetB2 ),
			95   : ( CustomizedName("Concourse B South (Gate B8-B95) | Gate B95", 4), customOffsetB2 ),

			"1W" : ( CustomizedName("Do Not Use | Stand B1W", 21), ),
			2    : ( CustomizedName("Do Not Use | Stand B2", 21), ),
			3    : ( CustomizedName("Do Not Use | Stand B3", 21), ),
			4    : ( CustomizedName("Do Not Use | Stand B4", 21), ),
			5    : ( CustomizedName("Do Not Use | Stand B5", 21), ),

 	},

	GATE_C : {
		None : (),
			"16E" : ( CustomizedName("RON Pad C East | Ramp CE1", 18), ),
			"2E"  : ( CustomizedName("RON Pad C East | Ramp CE2", 18), ),
			"3E"  : ( CustomizedName("RON Pad C East | Ramp CE3", 18), ),
			"4E"  : ( CustomizedName("RON Pad C East | Ramp CE4", 18), ),
			"5E"  : ( CustomizedName("RON Pad C East | Ramp CE5", 18), ),
			"6E"  : ( CustomizedName("RON Pad C East | Ramp CE6", 18), ),
			"7E"  : ( CustomizedName("RON Pad C East | Ramp CE7", 18), ),
			"8E"  : ( CustomizedName("RON Pad C East | Ramp CE8", 18), ),
			"10E" : ( CustomizedName("RON Pad C East | Ramp CE10", 18), ),
			"12E" : ( CustomizedName("RON Pad C East | Ramp CE12", 18), ),
			23    : ( CustomizedName("Concourse C North (Gate C23-C67) | Gate C23", 5), customOffsetC1 ),
			24    : ( CustomizedName("Concourse C South (Gate C24-C68) | Gate C24", 6), customOffsetC1 ),
			25    : ( CustomizedName("Concourse C North (Gate C23-C67) | Gate C25", 5), customOffsetC1 ),
			26    : ( CustomizedName("Concourse C South (Gate C24-C68) | Gate C26", 6), customOffsetC1 ),
			27    : ( CustomizedName("Concourse C North (Gate C23-C67) | Gate C27", 5), customOffsetC1 ),
			28    : ( CustomizedName("Concourse C South (Gate C24-C68) | Gate C28", 6), customOffsetC1 ),
			29    : ( CustomizedName("Concourse C North (Gate C23-C67) | Gate C29", 5), customOffsetC1 ),
			30    : ( CustomizedName("Concourse C South (Gate C24-C68) | Gate C30", 6), customOffsetC1 ),
			31    : ( CustomizedName("Concourse C North (Gate C23-C67) | Gate C31", 5), customOffsetC1 ),
			32    : ( CustomizedName("Concourse C South (Gate C24-C68) | Gate C32", 6), customOffsetC1 ),
			33    : ( CustomizedName("Concourse C North (Gate C23-C67) | Gate C33", 5), customOffsetC1 ),
			34    : ( CustomizedName("Concourse C South (Gate C24-C68) | Gate C34", 6), customOffsetC1 ),
			35    : ( CustomizedName("Concourse C North (Gate C23-C67) | Gate C35", 5), customOffsetC1 ),
			36    : ( CustomizedName("Concourse C South (Gate C24-C68) | Gate C36", 6), customOffsetC1 ),
			37    : ( CustomizedName("Concourse C North (Gate C23-C67) | Gate C37", 5), customOffsetC1 ),
			38    : ( CustomizedName("Concourse C South (Gate C24-C68) | Gate C38", 6), customOffsetC1 ),
			39    : ( CustomizedName("Concourse C North (Gate C23-C67) | Gate C39", 5), customOffsetC1 ),
			40    : ( CustomizedName("Concourse C South (Gate C24-C68) | Gate C40", 6), customOffsetC1 ),
			41    : ( CustomizedName("Concourse C North (Gate C23-C67) | Gate C41", 5), customOffsetC1 ),
			42    : ( CustomizedName("Concourse C South (Gate C24-C68) | Gate C42", 6), customOffsetC1 ),
			43    : ( CustomizedName("Concourse C North (Gate C23-C67) | Gate C43", 5), customOffsetC1 ),
			44    : ( CustomizedName("Concourse C South (Gate C24-C68) | Gate C44", 6), customOffsetC1 ),
			45    : ( CustomizedName("Concourse C North (Gate C23-C67) | Gate C45", 5), customOffsetC1 ),
			46    : ( CustomizedName("Concourse C South (Gate C24-C68) | Gate C46", 6), customOffsetC1 ),
			47    : ( CustomizedName("Concourse C North (Gate C23-C67) | Gate C47", 5), customOffsetC1 ),
			48    : ( CustomizedName("Concourse C South (Gate C24-C68) | Gate C48", 6), customOffsetC1 ),
			49    : ( CustomizedName("Concourse C North (Gate C23-C67) | Gate C49", 5), customOffsetC1 ),
			50    : ( CustomizedName("Concourse C South (Gate C24-C68) | Gate C50", 6), customOffsetC1 ),
			51    : ( CustomizedName("Concourse C North (Gate C23-C67) | Gate C51", 5), customOffsetC1 ),
			52    : ( CustomizedName("Concourse C South (Gate C24-C68) | Gate C52", 6), customOffsetC1 ),
			53    : ( CustomizedName("Concourse C North (Gate C23-C67) | Gate C53", 5), customOffsetC1 ),
			54    : ( CustomizedName("Concourse C South (Gate C24-C68) | Gate C54", 6), customOffsetC1 ),
			55    : ( CustomizedName("Concourse C North (Gate C23-C67) | Gate C55", 5), customOffsetC1 ),
			56    : ( CustomizedName("Concourse C South (Gate C24-C68) | Gate C56", 6), customOffsetC1 ),
			57    : ( CustomizedName("Concourse C North (Gate C23-C67) | Gate C57", 5), customOffsetC1 ),
			58    : ( CustomizedName("Concourse C South (Gate C24-C68) | Gate C58", 6), customOffsetC1 ),
			59    : ( CustomizedName("Concourse C North (Gate C23-C67) | Gate C59", 5), customOffsetC1 ),
			60    : ( CustomizedName("Concourse C South (Gate C24-C68) | Gate C60", 6), customOffsetC1 ),
			61    : ( CustomizedName("Concourse C North (Gate C23-C67) | Gate C61", 5), customOffsetC1 ),
			62    : ( CustomizedName("Concourse C South (Gate C24-C68) | Gate C62", 6), customOffsetC1 ),
			63    : ( CustomizedName("Concourse C North (Gate C23-C67) | Gate C63", 5), customOffsetC1 ),
			64    : ( CustomizedName("Concourse C South (Gate C24-C68) | Gate C64", 6), customOffsetC1 ),
			65    : ( CustomizedName("Concourse C North (Gate C23-C67) | Gate C65", 5), customOffsetC1 ),
			66    : ( CustomizedName("Concourse C South (Gate C24-C68) | Gate C66", 6), customOffsetC1 ),
			67    : ( CustomizedName("Concourse C North (Gate C23-C67) | Gate C67", 5), customOffsetC1 ),
			"68A" : ( CustomizedName("Concourse C East (Gate C68-C71) | Gate C68A", 7), customOffsetB2 ),
			"68B" : ( CustomizedName("Concourse C East (Gate C68-C71) | Gate C68B", 7), customOffsetB2 ),
			"68C" : ( CustomizedName("Concourse C East (Gate C68-C71) | Gate C70B", 7), customOffsetB2 ),
			"68D" : ( CustomizedName("Concourse C East (Gate C68-C71) | Gate C70A", 7), customOffsetB2 ),
			"68E" : ( CustomizedName("Concourse C East (Gate C68-C71) | Gate C71B", 7), customOffsetB2 ),
			"68F" : ( CustomizedName("Concourse C East (Gate C68-C71) | Gate C71A", 7), customOffsetB2 ),
			"68G" : ( CustomizedName("Concourse C East (Gate C68-C71) | Gate C69B", 7), customOffsetB2 ),

			1    : ( CustomizedName("Do Not Use | Stand C1", 21), ),
			"1W" : ( CustomizedName("Do Not Use | Stand C1W", 21), ),
			2    : ( CustomizedName("Do Not Use | Stand C2", 21), ),
			"2W" : ( CustomizedName("Do Not Use | Stand C2W", 21), ),
			3    : ( CustomizedName("Do Not Use | Stand C3", 21), ),
			4    : ( CustomizedName("Do Not Use | Stand C4", 21), ),
			"4W" : ( CustomizedName("Do Not Use | Stand C4W", 21), ),
			5    : ( CustomizedName("Do Not Use | Stand C5", 21), ),

 	},

	E_PARKING : {
		None : (),
			1 : ( CustomizedName("Do Not Use | Stand E1", 21), ),
			2 : ( CustomizedName("Do Not Use | Stand E2", 21), ),
			3 : ( CustomizedName("Do Not Use | Stand E3", 21), ),

 	},

	GATE_J : {
		None : (),
			1    : ( CustomizedName("Do Not Use | Stand J1", 21), ),
			"1W" : ( CustomizedName("Do Not Use | Stand J1W", 21), ),
			2    : ( CustomizedName("Do Not Use | Stand J2", 21), ),
			3    : ( CustomizedName("Do Not Use | Stand J3", 21), ),
			"3W" : ( CustomizedName("Do Not Use | Stand J3W", 21), ),
			4    : ( CustomizedName("Do Not Use | Stand J4", 21), ),
			5    : ( CustomizedName("Do Not Use | Stand J5", 21), ),
			"5W" : ( CustomizedName("Do Not Use | Stand J5W", 21), ),
			6    : ( CustomizedName("Do Not Use | Stand J6", 21), ),

 	},

	GATE_W : {
		None : (),
			1    : ( CustomizedName("Do Not Use | Stand W1", 21), ),
			"1W" : ( CustomizedName("Do Not Use | Stand W1W", 21), ),
			2    : ( CustomizedName("Do Not Use | Stand W2", 21), ),
			3    : ( CustomizedName("Do Not Use | Stand W3", 21), ),
			"3W" : ( CustomizedName("Do Not Use | Stand W3W", 21), ),
			4    : ( CustomizedName("Do Not Use | Stand W4", 21), ),
			5    : ( CustomizedName("Do Not Use | Stand W5", 21), ),
			"5W" : ( CustomizedName("Do Not Use | Stand W5W", 21), ),
			6    : ( CustomizedName("Do Not Use | Stand W6", 21), ),

 	},

	S_PARKING : {
		None : (),
			1    : ( CustomizedName("Do Not Use | Stand S1", 21), ),
			"1W" : ( CustomizedName("Do Not Use | Stand S1W", 21), ),
			2    : ( CustomizedName("Do Not Use | Stand S2", 21), ),
			3    : ( CustomizedName("Do Not Use | Stand S3", 21), ),
			"3W" : ( CustomizedName("Do Not Use | Stand S3W", 21), ),


 	},

	GATE_D : {
		None : (),
			1     : ( CustomizedName("RON Pad DS West | Ramp DS1", 19), ),
			2     : ( CustomizedName("RON Pad DS West | Ramp DS2", 19), ),
			3     : ( CustomizedName("RON Pad DS West | Ramp DS3", 19), ),
			4     : ( CustomizedName("RON Pad DS West | Ramp DS4", 19), ),
			5     : ( CustomizedName("RON Pad DS West | Ramp DS5", 19), ),
			6     : ( CustomizedName("RON Pad DS West | Ramp DS6", 19), ),
			7     : ( CustomizedName("RON Pad DS West | Ramp DS7", 19), ),
			8     : ( CustomizedName("RON Pad DS West | Ramp DS8", 19), ),
			9     : ( CustomizedName("RON Pad DS West | Ramp DS9", 19), ),
			10    : ( CustomizedName("RON Pad DS West | Ramp DS10", 19), ),
			11    : ( CustomizedName("RON Pad DS West | Ramp DS11", 19), ),
			12    : ( CustomizedName("RON Pad DS East | Ramp DS12", 20), ),
			13    : ( CustomizedName("RON Pad DS East | Ramp DS13", 20), ),
			14    : ( CustomizedName("RON Pad DS East | Ramp DS14", 20), ),
			15    : ( CustomizedName("RON Pad DS East | Ramp DS15", 20), ),
			16    : ( CustomizedName("RON Pad DS East | Ramp DS16", 20), ),
			17    : ( CustomizedName("RON Pad DS East | Ramp DS17", 20), ),
			18    : ( CustomizedName("RON Pad DS East | Ramp DS18", 20), ),
			19    : ( CustomizedName("RON Pad DS East | Ramp DS19", 20), ),
			"20S" : ( CustomizedName("RON Pad DS East | Ramp DS20", 20), ),

 	},

	PARKING : {
		None : (),
			0  : ( CustomizedName("UPS Cargo | Cargo Ramp 20/20W", 10), customOffsetCargo ),
			1  : ( CustomizedName("UPS Cargo (Small) | Cargo Ramp 1", 11), customOffsetCargo ),
			2  : ( CustomizedName("UPS Cargo (Small) | Cargo Ramp 2", 11), customOffsetCargo ),
			3  : ( CustomizedName("UPS Cargo (Small) | Cargo Ramp 3", 11), customOffsetCargo ),
			4  : ( CustomizedName("UPS Cargo (Small) | Cargo Ramp 4", 11), customOffsetCargo ),
			5  : ( CustomizedName("UPS Cargo (Small) | Cargo Ramp 5", 11), customOffsetCargo ),
			6  : ( CustomizedName("UPS Cargo (Small) | Cargo Ramp 6", 11), customOffsetCargo ),
			7  : ( CustomizedName("UPS Cargo (Small) | Cargo Ramp 7", 11), customOffsetCargo ),
			8  : ( CustomizedName("UPS Cargo (Small) | Cargo Ramp 8", 11), customOffsetCargo ),
			9  : ( CustomizedName("UPS Cargo (Small) | Cargo Ramp 9", 11), customOffsetCargo ),
			10 : ( CustomizedName("UPS Cargo (Small) | Cargo Ramp 10", 11), customOffsetCargo ),
			11 : ( CustomizedName("UPS Cargo (Small) | Cargo Ramp 11", 11), customOffsetCargo ),
			12 : ( CustomizedName("UPS Cargo (Small) | Cargo Ramp 12", 11), customOffsetCargo ),
			13 : ( CustomizedName("UPS Cargo (Small) | Cargo Ramp 13", 11), customOffsetCargo ),
			14 : ( CustomizedName("UPS Cargo (Small) | Cargo Ramp 14", 11), customOffsetCargo ),
			15 : ( CustomizedName("UPS Cargo (Small) | Cargo Ramp 15", 11), customOffsetCargo ),
			16 : ( CustomizedName("UPS Cargo (Small) | Cargo Ramp 16", 11), customOffsetCargo ),
			17 : ( CustomizedName("UPS Cargo (Small) | Cargo Ramp 17", 11), customOffsetCargo ),
			18 : ( CustomizedName("UPS Cargo (Small) | Cargo Ramp 18", 11), customOffsetCargo ),
			19 : ( CustomizedName("UPS Cargo (Small) | Cargo Ramp 19", 11), customOffsetCargo ),
			20 : ( CustomizedName("UPS Cargo (Small) | Cargo Ramp 20", 11), customOffsetCargo ),
			21 : ( CustomizedName("Amazon/Atlas Air Cargo | Cargo Ramp 16", 8), customOffsetCargo ),
			22 : ( CustomizedName("UPS Cargo | Cargo Ramp 22", 10), customOffsetCargo ),
			23 : ( CustomizedName("Amazon/Atlas Air Cargo | Cargo Ramp 10", 8), customOffsetCargo ),
			24 : ( CustomizedName("UPS Cargo | Cargo Ramp 24", 10), customOffsetCargo ),
			25 : ( CustomizedName("Amazon/Atlas Air Cargo | Cargo Ramp 8", 8), customOffsetCargo ),
			26 : ( CustomizedName("Amazon/Atlas Air Cargo | Cargo Ramp 6", 8), customOffsetCargo ),
			27 : ( CustomizedName("Amazon/Atlas Air Cargo | Cargo Ramp 4", 8), customOffsetCargo ),
			28 : ( CustomizedName("UPS Cargo | Cargo Ramp 28", 10), customOffsetCargo ),
			29 : ( CustomizedName("Amazon/Atlas Air Cargo | Cargo Ramp 2", 8), customOffsetCargo ),
			30 : ( CustomizedName("UPS Cargo | Cargo Ramp 30", 10), customOffsetCargo ),
			31 : ( CustomizedName("Fedex Cargo | Cargo Ramp 3", 9), customOffsetCargo ),
			32 : ( CustomizedName("UPS Cargo | Cargo Ramp 32", 10), customOffsetCargo ),
			33 : ( CustomizedName("Fedex Cargo | Cargo Ramp 5", 9), customOffsetCargo ),
			34 : ( CustomizedName("Fedex Cargo | Cargo Ramp 9", 9), customOffsetCargo ),
			35 : ( CustomizedName("Fedex Cargo | Cargo Ramp 11", 9), customOffsetCargo ),
			36 : ( CustomizedName("Fedex Cargo | Cargo Ramp 17", 9), customOffsetCargo ),
			37 : ( CustomizedName("Fedex Cargo | Cargo Ramp 19", 9), customOffsetCargo ),
			38 : ( CustomizedName("DHL Cargo | Cargo Ramp 31", 12), customOffsetCargo ),
			39 : ( CustomizedName("DHL Cargo | Cargo Ramp 33/33W", 12), customOffsetCargo ),
			40 : ( CustomizedName("DHL Cargo | Cargo Ramp 35", 12), customOffsetCargo ),
			41 : ( CustomizedName("GA Ramp | GA Ramp 41", 13), ),
			42 : ( CustomizedName("GA Ramp | GA Ramp 42", 13), ),
			43 : ( CustomizedName("GA Ramp | GA Ramp 43", 13), ),
			44 : ( CustomizedName("GA Ramp | GA Ramp 44", 13), ),
			45 : ( CustomizedName("GA Ramp | GA Ramp 45", 13), ),
			46 : ( CustomizedName("GA Ramp | GA Ramp 46", 13), ),
			47 : ( CustomizedName("GA Ramp | GA Ramp 47", 13), ),
			48 : ( CustomizedName("GA Ramp | GA Ramp 48", 13), ),
			49 : ( CustomizedName("GA Ramp | GA Ramp 49", 13), ),
			50 : ( CustomizedName("GA Ramp | GA Ramp 50", 13), ),
			51 : ( CustomizedName("GA Ramp | GA Ramp 51", 13), ),
			52 : ( CustomizedName("GA Ramp | GA Ramp 52", 13), ),

 	},

	GATE_S : {
		None : (),
			1 : ( CustomizedName("GA Ramp | GA Ramp 53", 13), ),

 	},

	N_PARKING : {
		None : (),
			1  : ( CustomizedName("United Maintenance | Ramp N1", 14), ),
			2  : ( CustomizedName("United Maintenance | Ramp N2", 14), ),
			3  : ( CustomizedName("United Maintenance | Ramp N3", 14), ),
			4  : ( CustomizedName("United Maintenance | Ramp N4", 14), ),
			5  : ( CustomizedName("United Maintenance | Ramp N5", 14), ),
			6  : ( CustomizedName("United Maintenance | Ramp N6", 14), ),
			7  : ( CustomizedName("United Maintenance | Ramp N7", 14), ),
			8  : ( CustomizedName("United Maintenance | Ramp N8", 14), ),
			9  : ( CustomizedName("United Maintenance | Ramp N9", 14), ),
			10 : ( CustomizedName("United Maintenance | Ramp N10", 14), ),
			11 : ( CustomizedName("United Maintenance | Ramp N11", 14), ),
			12 : ( CustomizedName("United Maintenance | Ramp N12", 14), ),
			13 : ( CustomizedName("United Maintenance | Ramp N13", 14), ),
			14 : ( CustomizedName("United Maintenance | Ramp N14", 14), ),
			15 : ( CustomizedName("Frontier Maintenance | Ramp N15", 15), ),
			16 : ( CustomizedName("Frontier Maintenance | Ramp N16", 15), ),
			17 : ( CustomizedName("Frontier Maintenance | Ramp N17", 15), ),
			18 : ( CustomizedName("Frontier Maintenance | Ramp N18", 15), ),
			19 : ( CustomizedName("Southwest Maintenance | Ramp N19", 16), ),
			20 : ( CustomizedName("Southwest Maintenance | Ramp N20", 16), ),
			21 : ( CustomizedName("Southwest Maintenance | Ramp N21", 16), ),
			22 : ( CustomizedName("Southwest Maintenance | Ramp N22", 16), ),
			23 : ( CustomizedName("Southwest Maintenance | Ramp N23", 16), ),
			24 : ( CustomizedName("Southwest Maintenance | Ramp N24", 16), ),
			25 : ( CustomizedName("Southwest Maintenance | Ramp N25", 16), ),
			26 : ( CustomizedName("Southwest Maintenance | Ramp N26", 16), ),


 	},
}
