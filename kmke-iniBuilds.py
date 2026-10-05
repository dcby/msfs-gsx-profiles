# -- coding: utf-8 --

msfs_mode = 1
icao = "kmke"

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
def customOffsetGateD35(aircraftData):

	table = {
		0: 0,
		200: 2.91,
		700: 2.91,
		900: 2.91,
		757: 7.3,
		767: 7.3,
		350: 7.3,
		300: 7.3,
		310: 7.3,
		717: 9.52,
		747: 9.52,
		777: 9.52,
		82: 9.52,
		83: 9.52,
		87: 9.52,
		90: 9.52,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )

@AlternativeStopPositions
def customOffsetGateD41(aircraftData):

	table = {
		0: 0,
		321: 1,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )

@AlternativeStopPositions
def customOffsetGateD42(aircraftData):

	table = {
		0: 0,
		319: -4,
		320: 0,
		321: 4,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )

@AlternativeStopPositions
def customOffsetGateD43(aircraftData):

	table = {
		0: 0,
		321: 2.42,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )

@AlternativeStopPositions
def customOffsetGateD44(aircraftData):

	table = {
		0: 0,
		319: 0,
		320: 0,
		170: 3.62,
		175: 3.62,
		190: 3.62,
		195: 3.62,
		717: 5.01,
		700: 5.01,
		900: 5.01,
		82: 5.01,
		83: 5.01,
		87: 5.01,
		90: 5.01,
		28: 5.01,
		146: 5.01,
		757: 7.48,
		321: 7.48,
		300: 7.48,
		310: 7.48,
	}

	table737 = {
		300: 0,
		500: 0,
		600: 0,
		700: 0,
		800: 5.01,
		900: 5.01,
	}

	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, {737 : (table737, 800)}, table) )

@AlternativeStopPositions
def customOffsetGateD45(aircraftData):

	table = {
		0: 0,
		321: 2.39,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )

@AlternativeStopPositions
def customOffsetGateD45A(aircraftData):

	table = {
		0: 0,
		321: 3.22,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )

@AlternativeStopPositions
def customOffsetGateD46(aircraftData):

	table = {
		0: 0,
		319: -1.3,
		321: 1.41,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )

@AlternativeStopPositions
def customOffsetGateD47(aircraftData):

	table = {
		0: 0,
		319: -7.02,
		321: 3.85,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )

@AlternativeStopPositions
def customOffsetGateD48(aircraftData):

	table = {
		0: 0,
		321: 2.42,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )

@AlternativeStopPositions
def customOffsetGateD51(aircraftData):

	table = {
		0: 0,
		321: 2.72,
		319: -3.2,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )

@AlternativeStopPositions
def customOffsetGateD52B(aircraftData):

	table = {
		0: 0,
		319: 0,
		320: 0,
		170: 2.75,
		175: 2.75,
		190: 2.75,
		195: 2.75,
		717: 4.97,
		700: 4.97,
		900: 4.97,
		82: 4.97,
		83: 4.97,
		87: 4.97,
		90: 4.97,
		28: 4.97,
		146: 4.97,
		757: 7.5,
		321: 7.5,
		300: 7.5,
		310: 7.5,
	}

	table737 = {
		300: 0,
		500: 0,
		600: 0,
		700: 0,
		800: 4.97,
		900: 4.97,
	}

	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, {737 : (table737, 800)}, table) )

@AlternativeStopPositions
def customOffsetGateD53(aircraftData):

	table = {
		0: 0,
		321: 1.05,
		319: -4.19,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )

@AlternativeStopPositions
def customOffsetGateD54(aircraftData):

	table = {
		0: 0,
		319: 0,
		320: 1.6,
		170: 2.61,
		175: 2.61,
		190: 2.61,
		195: 2.61,
		717: 7.7,
		700: 7.7,
		900: 7.7,
		82: 7.7,
		83: 7.7,
		87: 7.7,
		90: 7.7,
		28: 7.7,
		146: 7.7,
		757: 7.5,
		321: 12.42,
		300: 12.42,
		310: 12.42,
	}

	table737 = {
		300: 1.6,
		500: 1.6,
		600: 1.6,
		700: 1.6,
		800: 2.61,
		900: 2.61,
	}

	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, {737 : (table737, 800)}, table) )

@AlternativeStopPositions
def customOffsetGateD55(aircraftData):

	table = {
		0: 0,
		319: 0,
		320: 0,
		170: 2.11,
		175: 2.11,
		190: 2.11,
		195: 2.11,
		717: 5.15,
		700: 5.15,
		900: 5.15,
		82: 5.15,
		83: 5.15,
		87: 5.15,
		90: 5.15,
		28: 5.15,
		146: 5.15,
		757: 5.15,
		321: 9.9,
		300: 9.9,
		310: 9.9,
	}

	table737 = {
		300: 0,
		500: 0,
		600: 0,
		700: 0,
		800: 5.15,
		900: 5.15,
	}

	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, {737 : (table737, 800)}, table) )

@AlternativeStopPositions
def customOffsetGateD56(aircraftData):

	table = {
		0: 0,
		319: 0,
		320: 1.25,
		170: 5.04,
		175: 5.04,
		190: 5.04,
		195: 5.04,
		717: 6.6,
		700: 6.6,
		900: 6.6,
		82: 6.6,
		83: 6.6,
		87: 6.6,
		90: 6.6,
		28: 6.6,
		146: 6.6,
		757: 6.6,
		321: 11.48,
		300: 11.48,
		310: 11.48,
	}

	table737 = {
		300: 1.25,
		500: 1.25,
		600: 1.25,
		700: 1.25,
		800: 1.25,
		900: 1.25,
	}

	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, {737 : (table737, 800)}, table) )

@AlternativeStopPositions
def customOffsetGateC10to15(aircraftData):

	table = {
		0: 0,
		319: -4.12,
		320: 0,
		321: 5.25,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )

@AlternativeStopPositions
def customOffsetGateC9(aircraftData):

	table = {
		0: 0,
		319: 0,
		320: 0,
		170: 3.05,
		175: 3.05,
		190: 3.05,
		195: 3.05,
		717: 4.07,
		700: 4.07,
		900: 4.07,
		82: 4.07,
		83: 4.07,
		87: 4.07,
		90: 4.07,
		28: 4.07,
		146: 4.07,
		757: 9.85,
		321: 9.85,
		300: 9.85,
		310: 9.85,
	}

	table737 = {
		300: 0,
		500: 0,
		600: 0,
		700: 0,
		800: 4.07,
		900: 4.07,
	}

	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, {737 : (table737, 800)}, table) )

@AlternativeStopPositions
def customOffsetSouthwest(aircraftData):

	table = {
		0: 0,
	}

	table737 = {
		300: -4.57,
		500: -4.57,
		600: -4.57,
		700: -4.57,
		800: 0,
		900: 0,
	}

	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, {737 : (table737, 800)}, table) )

def MyStandNames(name, letter, priority):
	return CustomizedName( "%s|Stand %s#§" % (name, letter), priority )

def MyGateNames(name, letter, priority):
	return CustomizedName( "%s|Gate %s#§" % (name, letter), priority )

TerminalCNames = MyGateNames("Terminal - Concourse C (SWA,UAL)", "C", 1)
TerminalDNames = MyGateNames("Terminal - Concourse D (AAL,ACA,JBU,NKS)", "D", 2)
InternationalNames = MyGateNames("International Arrivals", "", 3)
CargoNames = MyStandNames("Cargo Ramp", "", 4)
SkyWestNames = MyStandNames("SkyWest Maintenance", "", 5)
NorthRampNames = MyStandNames("North Ramp (Atlantic FBO)", "", 6)
NortheastGANames = MyStandNames("Northeast Apron", "", 7)
ANGNames = MyStandNames("Wisconsin ANG Apron", "", 8)
SouthRampNames = MyStandNames("South Ramp", "", 9)
SouthwestRampNames = MyStandNames("Southwest Ramp", "", 10)
WestRampNames = MyStandNames("West Ramp", "", 11)
TerminalENames = MyGateNames("Terminal - Concourse E (Defunct)", "E", 12)

parkings = {
	GATE : {
		None : (TerminalCNames, ),
				71 : (InternationalNames, customOffsetStands1line),
	},
	GATE_C : {
		None : (TerminalCNames, customOffsetSouthwest),
				9 : (TerminalCNames, customOffsetGateC9),
				10 : (TerminalCNames, customOffsetGateC10to15),
				11 : (TerminalCNames, customOffsetGateC10to15),
				12 : (TerminalCNames, customOffsetGateC10to15),
				14 : (TerminalCNames, customOffsetGateC10to15),
				15 : (TerminalCNames, customOffsetGateC10to15),
	},
	GATE_D : {
		None : (TerminalDNames, ),
				35 : (TerminalDNames, customOffsetGateD35),
				36 : (TerminalDNames, customOffsetStands1line),
				38 : (TerminalDNames, customOffsetStands1line),
				39 : (TerminalDNames, customOffsetStands1line),
				41 : (TerminalDNames, customOffsetGateD41),
				42 : (TerminalDNames, customOffsetGateD42),
				43 : (TerminalDNames, customOffsetGateD43),
				44 : (TerminalDNames, customOffsetGateD44),
				45 : (TerminalDNames, customOffsetGateD45),
				"45A" : (TerminalDNames, customOffsetGateD45A),
				46 : (TerminalDNames, customOffsetGateD46),
				47 : (TerminalDNames, customOffsetGateD47),
				48 : (TerminalDNames, customOffsetGateD48),
				51 : (TerminalDNames, customOffsetGateD51),
				"52A" : (TerminalDNames, customOffsetStands1line),
				"52B" : (TerminalDNames, customOffsetGateD52B),
				53 : (TerminalDNames, customOffsetGateD53),
				54 : (TerminalDNames, customOffsetGateD54),
				55 : (TerminalDNames, customOffsetGateD55),
				56 : (TerminalDNames, customOffsetGateD56),
	},
	GATE_E : {
		None : (TerminalENames, customOffsetStands1line),
	},
	E_PARKING : {
		None : (NortheastGANames, customOffsetStands1line),
	},
	SE_PARKING : {
		None : (ANGNames, customOffsetStands1line),
	},
	S_PARKING : {
		None : (SouthRampNames, customOffsetStands1line),
	},
	SW_PARKING : {
		None : (SouthwestRampNames, customOffsetStands1line),
	},
	W_PARKING : {
		None : (CargoNames, customOffsetStands1line),
				6 : (SkyWestNames, ),
				7 : (SkyWestNames, ),
				8 : (SkyWestNames, ),
				9 : (SkyWestNames, ),
	},
	PARKING : {
		None  : (NorthRampNames, customOffsetStands1line),
				49 : (WestRampNames, customOffsetStands1line),
				50 : (WestRampNames, customOffsetStands1line),
				51 : (WestRampNames, customOffsetStands1line),
	},
}