# -- coding: utf-8 --

msfs_mode = 1
icao = "egss"

@AlternativeStopPositions
def customOffsetStands1line(aircraftData):

	table = {
		0: 0,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )

@AlternativeStopPositions
def customOffsetHeavy22(aircraftData):

	table = {
		0: 0,
		777: 14.5,
		787: 7.72,
		767: 7.72,
		330: 12.74,
		11: 12.74,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )

def MyStandNames(name, letter, priority):
	return CustomizedName( "%s|Stand %s#§" % (name, letter), priority )

AApronNames = MyStandNames("Apron A (Stands 1-15)", "", 1)
BApronNames = MyStandNames("Apron B (Stands 20-34)", "", 2)
CApronNames = MyStandNames("Apron C (Stands 40-53)", "", 3)
DApronNames = MyStandNames("Apron D (Stands 61-74)", "", 4)
EApronNames = MyStandNames("Apron E (Stands 81-93)", "", 5)
ZApronNames = MyStandNames("Apron Z (Stands 204-214)", "", 6)
OtherNames = MyStandNames("Other Parkings", "", 7)

parkings = {
	GATE : {
		None : ( ),
		1 : (AApronNames, customOffsetStands1line),
		"1L" : (AApronNames, customOffsetStands1line),
		"1R" : (AApronNames, customOffsetStands1line),
		2 : (AApronNames, customOffsetStands1line),
		3 : (AApronNames, customOffsetStands1line),
		4 : (AApronNames, customOffsetStands1line),
		5 : (AApronNames, customOffsetStands1line),
		6 : (AApronNames, customOffsetStands1line),
		7 : (AApronNames, customOffsetStands1line),
		8 : (AApronNames, customOffsetStands1line),
		9 : (AApronNames, customOffsetStands1line),
		"9L" : (AApronNames, customOffsetStands1line),
		"9R" : (AApronNames, customOffsetStands1line),
		10 : (AApronNames, customOffsetStands1line),
		11 : (AApronNames, customOffsetStands1line),
		"11R" : (AApronNames, customOffsetStands1line),
		"11L" : (AApronNames, customOffsetStands1line),
		12 : (AApronNames, customOffsetStands1line),
		"12R" : (AApronNames, customOffsetStands1line),
		"12L" : (AApronNames, customOffsetStands1line),
		13 : (AApronNames, customOffsetStands1line),
		"13R" : (AApronNames, customOffsetStands1line),
		"13L" : (AApronNames, customOffsetStands1line),
		14 : (AApronNames, customOffsetStands1line),
		15 : (AApronNames, customOffsetStands1line),
		"15R" : (AApronNames, customOffsetStands1line),
		"15L" : (AApronNames, customOffsetStands1line),
		20 : (BApronNames, customOffsetStands1line),
		21 : (BApronNames, customOffsetStands1line),
		"22R" : (BApronNames, customOffsetStands1line),
		22 : (BApronNames, customOffsetHeavy22),
		"22L" : (BApronNames, customOffsetStands1line),
		23 : (BApronNames, customOffsetStands1line),
		"23L" : (BApronNames, customOffsetStands1line),
		"23R" : (BApronNames, customOffsetStands1line),
		24 : (BApronNames, customOffsetStands1line),
		"25R" : (BApronNames, customOffsetStands1line),
		"25L" : (BApronNames, customOffsetStands1line),
		30 : (BApronNames, customOffsetStands1line),
		31 : (BApronNames, customOffsetStands1line),
		32 : (BApronNames, customOffsetStands1line),
		"32R" : (BApronNames, customOffsetStands1line),
		"32L" : (BApronNames, customOffsetStands1line),
		33 : (BApronNames, customOffsetStands1line),
		"33R" : (BApronNames, customOffsetStands1line),
		"33L" : (BApronNames, customOffsetStands1line),
		34 : (BApronNames, customOffsetStands1line),
		"34R" : (BApronNames, customOffsetStands1line),
		"34L" : (BApronNames, customOffsetStands1line),
		40 : (CApronNames, customOffsetStands1line),
		41 : (CApronNames, customOffsetStands1line),
		"42L" : (CApronNames, customOffsetStands1line),
		42 : (CApronNames, customOffsetStands1line),
		"42R" : (CApronNames, customOffsetStands1line),
		43 : (CApronNames, customOffsetStands1line),
		"43R" : (CApronNames, customOffsetStands1line),
		"43L" : (CApronNames, customOffsetStands1line),
		44 : (CApronNames, customOffsetStands1line),
		"44R" : (CApronNames, customOffsetStands1line),
		"44L" : (CApronNames, customOffsetStands1line),
		"45R" : (CApronNames, customOffsetStands1line),
		"45L" : (CApronNames, customOffsetStands1line),
		"50R" : (CApronNames, customOffsetStands1line),
		"50L" : (CApronNames, customOffsetStands1line),
		"51R" : (CApronNames, customOffsetStands1line),
		"51L" : (CApronNames, customOffsetStands1line),
		"52R" : (CApronNames, customOffsetStands1line),
		"52L" : (CApronNames, customOffsetStands1line),
		"53R" : (CApronNames, customOffsetStands1line),
		"53L" : (CApronNames, customOffsetStands1line),
		"61R" : (DApronNames, customOffsetStands1line),
		"61L" : (DApronNames, customOffsetStands1line),
		"62R" : (DApronNames, customOffsetStands1line),
		"62L" : (DApronNames, customOffsetStands1line),
		"63R" : (DApronNames, customOffsetStands1line),
		"63L" : (DApronNames, customOffsetStands1line),
		"64L" : (DApronNames, customOffsetStands1line),
		"64R" : (DApronNames, customOffsetStands1line),
		"65R" : (DApronNames, customOffsetStands1line),
		"65L" : (DApronNames, customOffsetStands1line),
		"70L" : (DApronNames, customOffsetStands1line),
		"70R" : (DApronNames, customOffsetStands1line),
		"71R" : (DApronNames, customOffsetStands1line),
		"71L" : (DApronNames, customOffsetStands1line),
		"72L" : (DApronNames, customOffsetStands1line),
		"72R" : (DApronNames, customOffsetStands1line),
		"73R" : (DApronNames, customOffsetStands1line),
		"73L" : (DApronNames, customOffsetStands1line),
		74 : (DApronNames, customOffsetStands1line),
		"81R" : (EApronNames, customOffsetStands1line),
		81 : (EApronNames, customOffsetStands1line),
		"81L" : (EApronNames, customOffsetStands1line),
		"82R" : (EApronNames, customOffsetStands1line),
		82 : (EApronNames, customOffsetStands1line),
		"82L" : (EApronNames, customOffsetStands1line),
		"83R" : (EApronNames, customOffsetStands1line),
		"83L" : (EApronNames, customOffsetStands1line),
		"84R" : (EApronNames, customOffsetStands1line),
		84 : (EApronNames, customOffsetStands1line),
		"85L" : (EApronNames, customOffsetStands1line),
		"85R" : (EApronNames, customOffsetStands1line),
		"90R" : (EApronNames, customOffsetStands1line),
		90 : (EApronNames, customOffsetStands1line),
		"90L" : (EApronNames, customOffsetStands1line),
		91 : (EApronNames, customOffsetStands1line),
		"91L" : (EApronNames, customOffsetStands1line),
		"91R" : (EApronNames, customOffsetStands1line),
		"92R" : (EApronNames, customOffsetStands1line),
		92 : (EApronNames, customOffsetStands1line),
		"92L" : (EApronNames, customOffsetStands1line),
		"93R" : (EApronNames, customOffsetStands1line),
		93 : (EApronNames, customOffsetStands1line),
		"93L" : (EApronNames, customOffsetStands1line),
		"100S" : (OtherNames, ),
	},
	GATE_H : {
		None : (OtherNames, ),
	},
	PARKING : {
		None : (OtherNames, ),
		204 : (ZApronNames, customOffsetStands1line),
		"204L" : (ZApronNames, customOffsetStands1line),
		"204F" : (ZApronNames, customOffsetStands1line),
		"204R" : (ZApronNames, customOffsetStands1line),
		205 : (ZApronNames, customOffsetStands1line),
		"205L" : (ZApronNames, customOffsetStands1line),
		"205R" : (ZApronNames, customOffsetStands1line),
		213 : (ZApronNames, customOffsetStands1line),
		"213L" : (ZApronNames, customOffsetStands1line),
		"213R" : (ZApronNames, customOffsetStands1line),
		214 : (ZApronNames, customOffsetStands1line),
		"214L" : (ZApronNames, customOffsetStands1line),
		"214R" : (ZApronNames, customOffsetStands1line),
	},
}