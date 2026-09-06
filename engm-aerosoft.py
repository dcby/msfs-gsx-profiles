# -- coding: utf-8 --
# Creator = jbx-profiles, Litos_97, Saurer01, virtualstuff, Aanerud
# Scenery = Aerosoft - ENGM Oslo Gardermoen
# Notes = Based on real life Oslo Gardemoen ENGM

msfs_mode = 1
icao = "engm"
version = "1.8.2"

north = CustomizedName("Terminal - North Pier (60-96) | Gate #§", 1)
east = CustomizedName("Terminal - East Pier (36-58) | Gate #§", 2)
west = CustomizedName("Terminal - West Pier (2-28) | Gate #§", 3)
remote = CustomizedName("Terminal - Remote (171-188) | Stand #§", 4)
cargo = CustomizedName("Cargo | Stand #§", 5)
ga = CustomizedName("General Aviation | Stand #§", 6)
ga_north = CustomizedName("GA North | Gate #§", 7)
military = CustomizedName("Military | Gate #§", 8)

@AlternativeStopPositions
def custom_stops_9_12(aircraftData):
    tableIcao = {
        "B733": 0,
        "B734": 0,
        "B735": 0,
        "B736": 0,
        "B737": 0,
        "B738": 0,
        "B739": 0,
        "B37M": 0,
        "B38M": 0,
        "B39M": 0,
        "B3XM": 0,
        "A319": -1,
        "A19N": -1,
        "A320": -1,
        "A20N": -1,
        "A321": -1,
        "AT43": -2.8,
        "AT45": -2.8,
        "AT72": -2.8,
        "DH8A": -2.8,
        "DH8B": -2.8,
        "DH8C": -2.8,
        "DH8C": -2.8,
        "CRJ1": -2.8,
        "CRJ2": -2.8,
        "CRJ7": -2.8,
        "CRJ9": -2.8
    }

    tableGroup = {
        "ARC-A": -2.8,
        "ARC-B": -2.8,
        "ARC-C": -1,
        "ARC-D": -0,
        "ARC-E": 0,
        "ARC-F": 0,
        "Unknown": -1
    }

    try:
        return Distance.fromMeters(tableIcao.get(aircraftData.icaoTypeDesignator,tableGroup.get(aircraftData.aircraftGroup, -1)))
    except:
        return Distance.fromMeters()

@AlternativeStopPositions
def custom_stops_13_45(aircraftData):
    tableIcao = {
        "RJ85": 0,
        "RJ1H": 0,
        "MD81": -0.85,
        "BCS1": -0.85,
        "BCS3": -0.85,
        "B717": -0.85,
        "B733": -1.82,
        "B734": -1.82,
        "B735": -1.82,
        "B736": -1.82,
        "B737": -1.82,
        "B738": -1.82,
        "B739": -1.82,
        "B37M": -1.82,
        "B38M": -1.82,
        "B39M": -1.82,
        "B3XM": -1.82,
        "E170": -1.82,
        "E190": -1.82,
        "E195": -1.82,
        "F70": -2.20,
        "F100": -2.20,
        "E290": -2.20,
        "A319": -2.78,
        "A19N": -2.78,
        "A320": -2.78,
        "A20N": -2.78,
        "A321": -2.78,
        "A21N": -2.78,
        "RJ70": -5.75,
        "E135": -5.75,
        "E145": -5.75,
        "F50": -5.75,
        "AT43": -5.75,
        "AT45": -5.75,
        "AT72": -5.75,
        "DH8A": -5.75,
        "DH8B": -5.75,
        "DH8C": -5.75,
        "DH8C": -5.75,
        "CRJ1": -5.75,
        "CRJ2": -5.75,
        "CRJ7": -5.75,
        "CRJ9": -5.75
    }

    tableGroup = {
        "ARC-A": -5.75,
        "ARC-B": -5.75,
        "ARC-C": -2.20,
        "ARC-D": -0.85,
        "ARC-E": 0,
        "ARC-F": 0,
        "Unknown": -2.20
    }

    try:
        return Distance.fromMeters(tableIcao.get(aircraftData.icaoTypeDesignator,tableGroup.get(aircraftData.aircraftGroup, -2.20)))
    except:
        return Distance.fromMeters()
    
@AlternativeStopPositions
def custom_stops_28(aircraftData):
    tableIcao = {
        "B717": 0,
        "BCS1": 0,
        "BCS3": 0,
        "MD87": 0,
        "B733": -1,
        "B734": -1,
        "B735": -1,
        "B736": -1,
        "B737": -1,
        "B738": -1,
        "B739": -1,
        "B37M": -1,
        "B38M": -1,
        "B39M": -1,
        "B3XM": -1,
        "E170": -1,
        "E190": -1,
        "E195": -1,
        "A319": -2,
        "A19N": -2,
        "A320": -2,
        "A20N": -2,
        "A321": -2,
        "A21N": -2,
        "RJ70": -5,
        "E135": -5,
        "E145": -5,
        "F50": -5,
        "AT43": -5,
        "AT45": -5,
        "AT72": -5,
        "DH8A": -5,
        "DH8B": -5,
        "DH8C": -5,
        "DH8C": -5,
        "D328": -5,
        "E135": -5,
        "E145": -5,
        "F50": -5,
        "F50": -5,
        "F100": -5,
        "J328": -5,
    }

    tableGroup = {
        "ARC-A": -5,
        "ARC-B": -5,
        "ARC-C": -2,
        "ARC-D": -1,
        "ARC-E": 0,
        "ARC-F": 0,
        "Unknown": -2
    }

    try:
        return Distance.fromMeters(tableIcao.get(aircraftData.icaoTypeDesignator,tableGroup.get(aircraftData.aircraftGroup, -2)))
    except:
        return Distance.fromMeters()
    
@AlternativeStopPositions
def custom_stops_36_38(aircraftData):
    tableIcao = {
        "B717": 0,
        "BCS1": 0,
        "BCS3": 0,
        "MD87": 0,
        "B733": -0.96,
        "B734": -0.96,
        "B735": -0.96,
        "B736": -0.96,
        "B737": -0.96,
        "B738": -0.96,
        "B739": -0.96,
        "B37M": -0.96,
        "B38M": -0.96,
        "B39M": -0.96,
        "B3XM": -0.96,
        "E170": -0.96,
        "E190": -0.96,
        "E195": -0.96,
        "A319": -1.93,
        "A19N": -1.93,
        "A320": -1.93,
        "A20N": -1.93,
        "A321": -1.93,
        "A21N": -1.93,
        "RJ70": -3.93,
        "E135": -3.93,
        "E145": -3.93,
        "F50": -3.93,
        "AT43": -3.93,
        "AT45": -3.93,
        "AT72": -3.93,
        "DH8A": -3.93,
        "DH8B": -3.93,
        "DH8C": -3.93,
        "DH8C": -3.93,
        "D328": -3.93,
        "E135": -3.93,
        "E145": -3.93,
        "F50": -3.93,
        "F50": -3.93,
        "F100": -3.93,
        "J328": -3.93,
    }

    tableGroup = {
        "ARC-A": -3.93,
        "ARC-B": -3.93,
        "ARC-C": -1.93,
        "ARC-D": -0.96,
        "ARC-E": 0,
        "ARC-F": 0,
        "Unknown": -1.93
    }

    try:
        return Distance.fromMeters(tableIcao.get(aircraftData.icaoTypeDesignator,tableGroup.get(aircraftData.aircraftGroup, -1.93)))
    except:
        return Distance.fromMeters()
    
@AlternativeStopPositions
def custom_stops_40(aircraftData):
    tableIcao = {
        "A35K": 0,
        "B773": 0,
        "B77W": 0,
        "B779": 0,
        "A346": -1.8,
        "A359": -1.8,
        "B764": -1.8,
        "B78X": -1.8,
        "B743": -6.6,
        "B744": -6.6,
        "B752": -6.6,
        "B753": -6.6,
        "B772": -6.6,
        "B778": -6.6,
        "B789": -6.6,
        "A332": -8.6,
        "A333": -8.6,
        "A338": -8.6,
        "A339": -8.6,
        "A342": -8.6,
        "A343": -8.6,
        "A345": -8.6,
        "A358": -8.6,
        "B763": -8.6,
        "B788": -8.6,
        "B762": -11,
        "BCS1": -12.3,
        "BCS3": -12.3,
        "A319": -12.3,
        "A19N": -12.3,
        "A320": -12.3,
        "A20N": -12.3,
        "A321": -12.3,
        "A21N": -12.3,
        "B733": -12.3,
        "B734": -12.3,
        "B735": -12.3,
        "B736": -12.3,
        "B737": -12.3,
        "B738": -12.3,
        "B739": -12.3,
        "B37M": -12.3,
        "B38M": -12.3,
        "B39M": -12.3,
        "B3XM": -12.3,
        "E170": -12.3,
        "E190": -12.3,
        "E195": -12.3,
        "E290": -12.3,
        "E295": -12.3,
        "SU95": -12.3
    }

    tableGroup = {
        "ARC-A": 0,
        "ARC-B": 0,
        "ARC-C": 0,
        "ARC-D": 0,
        "ARC-E": 0,
        "ARC-F": 0,
        "Unknown": 0
    }

    try:
        return Distance.fromMeters(tableIcao.get(aircraftData.icaoTypeDesignator,tableGroup.get(aircraftData.aircraftGroup, 0)))
    except:
        return Distance.fromMeters()
    
@AlternativeStopPositions
def custom_stops_46(aircraftData):
    tableIcao = {
        "B717": 0,
        "MD81": 0,
        "MD90": 0,
        "B752": -2.7,
        "B753": -2.7,
        "RJ70": -6.3,
        "RJ85": -6.3,
        "RJ1H": -6.3,
        "A319": -7.9,
        "A19N": -7.9,
        "A320": -7.9,
        "A20N": -7.9,
        "A321": -7.9,
        "A21N": -7.9,
        "B733": -7.9,
        "B734": -7.9,
        "B735": -7.9,
        "B736": -7.9,
        "B737": -7.9,
        "B738": -7.9,
        "B739": -7.9,
        "B37M": -7.9,
        "B38M": -7.9,
        "B39M": -7.9,
        "B3XM": -7.9,
        "CRJ1": -7.9,
        "CRJ2": -7.9,
        "CRJ7": -7.9,
        "CRJ9": -7.9,
        "CRJX": -7.9,
        "BCS1": -7.9,
        "BCS3": -7.9,
        "E170": -7.9,
        "E190": -7.9,
        "E195": -7.9,
        "F70": -7.9,
        "F100": -7.9,
        "SU95": -7.9,
        "AT43": -8.8,
        "AT45": -8.8,
        "AT72": -8.8,
        "D328": -8.8,
        "J328": -8.8,
        "DH8A": -8.8,
        "DH8B": -8.8,
        "DH8C": -8.8,
        "DH8D": -8.8,
        "E135": -8.8,
        "E145": -8.8,
        "F50": -8.8,
    }

    tableGroup = {
        "ARC-A": 0,
        "ARC-B": 0,
        "ARC-C": 0,
        "ARC-D": 0,
        "ARC-E": 0,
        "ARC-F": 0,
        "Unknown": 0
    }

    try:
        return Distance.fromMeters(tableIcao.get(aircraftData.icaoTypeDesignator,tableGroup.get(aircraftData.aircraftGroup, 0)))
    except:
        return Distance.fromMeters()
    
@AlternativeStopPositions
def custom_stops_default(aircraftData):
    return Distance.fromMeters(0)

@AlternativeStopPositions
def custom_stops_49(aircraftData):
    tableIcao = {
        "MD81": 0,
        "B717": 0,
        "A332": -0.8,
        "A333": -0.8,
        "A338": -0.8,
        "A339": -0.8,
        "B752": -2,
        "B753": -2,
        "B762": -2,
        "B763": -2,
        "B764": -2,
        "B788": -2,
        "B789": -2,
        "B78X": -2,
        "F70" : -2,
        "F100": -2,
        "SU95": -3,
        "E135": -3,
        "E145": -3,
        "B733": -3.6,
        "B734": -3.6,
        "B735": -3.6,
        "B736": -3.6,
        "B737": -3.6,
        "B738": -3.6,
        "B739": -3.6,
        "B37M": -3.6,
        "B38M": -3.6,
        "B39M": -3.6,
        "B3XM": -3.6,
        "E170": -3.6,
        "E190": -3.6,
        "E195": -3.6,
        "T204": -3.6,
        "CRJ1": -4.8,
        "CRJ2": -4.8,
        "CRJ7": -4.8,
        "CRJ9": -4.8,
        "AT43": -4.8,
        "AT45": -4.8,
        "AT72": -4.8,
        "RJ70": -4.8,
        "RJ85": -4.8,
        "RJ1H": -4.8,
        "F50" : -4.8,
        "A30B": -4.8,
        "A306": -4.8,
        "A310": -4.8,
        "DC10": -4.8,
        "D328": -4.8,
        "J328": -4.8,
        "BCS1": -4.8,
        "BCS3": -4.8,
        "A319": -4.8,
        "A19N": -4.8,
        "A320": -4.8,
        "A20N": -4.8,
        "A321": -4.8,
        "A21N": -4.8,
        "DH8A": -4.8,
        "DH8B": -4.8,
        "DH8C": -4.8,
        "DH8D": -4.8
    }

    tableGroup = {
        "ARC-A": 0,
        "ARC-B": 0,
        "ARC-C": 0,
        "ARC-D": 0,
        "ARC-E": 0,
        "ARC-F": 0,
        "Unknown": 0
    }

    try:
        return Distance.fromMeters(tableIcao.get(aircraftData.icaoTypeDesignator,tableGroup.get(aircraftData.aircraftGroup, 0)))
    except:
        return Distance.fromMeters()

@AlternativeStopPositions
def custom_stops_51(aircraftData):
    tableIcao = {
        "A359": 0,
        "B764": -2.6,
        "B772": -2.6,
        "B789": -2.6,
        "B78X": -2.6,
        "A333": -3.8,
        "A338": -3.8,
        "A339": -3.8,
        "B774": -3.8,
        "A332": -7.6,
        "B752": -7.6,
        "B753": -7.6,
        "B788": -7.6,
        "BCS1": -15.6,
        "BCS3": -15.6,
        "A319": -15.6,
        "A19N": -15.6,
        "A320": -15.6,
        "A20N": -15.6,
        "A321": -15.6,
        "A21N": -15.6,
        "B733": -15.6,
        "B734": -15.6,
        "B735": -15.6,
        "B736": -15.6,
        "B737": -15.6,
        "B738": -15.6,
        "B739": -15.6,
        "B37M": -15.6,
        "B38M": -15.6,
        "B39M": -15.6,
        "B3XM": -15.6,
        "E170": -15.6,
        "E190": -15.6,
        "E195": -15.6,
        "E290": -15.6,
        "E295": -15.6,
        "SU95": -15.6
    }

    tableGroup = {
        "ARC-A": 0,
        "ARC-B": 0,
        "ARC-C": 0,
        "ARC-D": 0,
        "ARC-E": 0,
        "ARC-F": 0,
        "Unknown": 0
    }

    try:
        return Distance.fromMeters(tableIcao.get(aircraftData.icaoTypeDesignator,tableGroup.get(aircraftData.aircraftGroup, 0)))
    except:
        return Distance.fromMeters()
    
@AlternativeStopPositions
def custom_stops_52(aircraftData):
    tableIcao = {
        "A35K": 0,
        "B779": -2,
        "B773": -2,
        "A359": -4,
        "A388": -4,
        "B764": -4,
        "B773": -4,
        "B77W": -4,
        "B781": -4,
        "B743": -8.6,
        "B744": -8.6,
        "B753": -8.6,
        "B763": -8.6,
        "B772": -8.6,
        "B778": -8.6,
        "B789": -8.6,
        "B78X": -8.6,
        "A332": -10.7,
        "A333": -10.7,
        "A338": -10.7,
        "A339": -10.7,
        "A342": -10.7,
        "A343": -10.7,
        "A345": -10.7,
        "B762": -10.7,
        "B788": -10.7,
        "B752": -10.7
    }

    tableGroup = {
        "ARC-A": 0,
        "ARC-B": 0,
        "ARC-C": 0,
        "ARC-D": 0,
        "ARC-E": 0,
        "ARC-F": 0,
        "Unknown": 0
    }

    try:
        return Distance.fromMeters(tableIcao.get(aircraftData.icaoTypeDesignator,tableGroup.get(aircraftData.aircraftGroup, 0)))
    except:
        return Distance.fromMeters()
    
@AlternativeStopPositions
def custom_stops_53(aircraftData):
    tableIcao = {
        "A35K": 0,
        "B779": 0,
        "B773": 0,
        "B77W": 0,
        "A359": -1.6,
        "B764": -1.6,
        "B773": -1.6,
        "B781": -1.6,
        "B753": -5.05,
        "B772": -5.05,
        "B778": -5.05,
        "B789": -5.05,
        "B78X": -5.05,
        "A332": -6.6,
        "A333": -6.6,
        "A338": -6.6,
        "A339": -6.6,
        "B763": -6.6,
        "B788": -6.6,
        "B752": -7.8,
        "BCS1": -13.7,
        "BCS3": -13.7,
        "A319": -13.7,
        "A19N": -13.7,
        "A320": -13.7,
        "A20N": -13.7,
        "A321": -13.7,
        "A21N": -13.7,
        "B733": -13.7,
        "B734": -13.7,
        "B735": -13.7,
        "B736": -13.7,
        "B737": -13.7,
        "B738": -13.7,
        "B739": -13.7,
        "B37M": -13.7,
        "B38M": -13.7,
        "B39M": -13.7,
        "B3XM": -13.7,
        "E170": -13.7,
        "E190": -13.7,
        "E195": -13.7,
        "E290": -13.7,
        "E295": -13.7,
        "SU95": -13.7
    }

    tableGroup = {
        "ARC-A": 0,
        "ARC-B": 0,
        "ARC-C": 0,
        "ARC-D": 0,
        "ARC-E": 0,
        "ARC-F": 0,
        "Unknown": 0
    }

    try:
        return Distance.fromMeters(tableIcao.get(aircraftData.icaoTypeDesignator,tableGroup.get(aircraftData.aircraftGroup, 0)))
    except:
        return Distance.fromMeters()
    
@AlternativeStopPositions
def custom_stops_56_58(aircraftData):
    tableIcao = {
        "A35K": 0,
        "B779": 0,
        "B773": 0,
        "B77W": 0,
        "A346": -2,
        "A359": -2,
        "B764": -2,
        "B781": -2,
        "B743": -6.6,
        "B744": -6.6,
        "B752": -6.6,
        "B753": -6.6,
        "B772": -6.6,
        "B778": -6.6,
        "B789": -6.6,
        "B78X": -6.6,
        "A332": -8.8,
        "A333": -8.8,
        "A338": -8.8,
        "A339": -8.8,
        "A342": -8.8,
        "A343": -8.8,
        "A345": -8.8,
        "B763": -8.8,
        "B788": -8.8,
        "B762": -11.3,
        "BCS1": -12.9,
        "BCS3": -12.9,
        "A319": -12.9,
        "A19N": -12.9,
        "A320": -12.9,
        "A20N": -12.9,
        "A321": -12.9,
        "A21N": -12.9,
        "B733": -12.9,
        "B734": -12.9,
        "B735": -12.9,
        "B736": -12.9,
        "B737": -12.9,
        "B738": -12.9,
        "B739": -12.9,
        "B37M": -12.9,
        "B38M": -12.9,
        "B39M": -12.9,
        "B3XM": -12.9,
        "E170": -12.9,
        "E190": -12.9,
        "E195": -12.9,
        "E290": -12.9,
        "E295": -12.9,
        "SU95": -12.9
    }

    tableGroup = {
        "ARC-A": 0,
        "ARC-B": 0,
        "ARC-C": 0,
        "ARC-D": 0,
        "ARC-E": 0,
        "ARC-F": 0,
        "Unknown": 0
    }

    try:
        return Distance.fromMeters(tableIcao.get(aircraftData.icaoTypeDesignator,tableGroup.get(aircraftData.aircraftGroup, 0)))
    except:
        return Distance.fromMeters()
    
@AlternativeStopPositions
def custom_stops_60_81(aircraftData):
    tableIcao = {
        "B717": 0,
        "BCS1": 0,
        "BCS3": 0,
        "B733": -1,
        "B734": -1,
        "B735": -1,
        "B736": -1,
        "B737": -1,
        "B738": -1,
        "B739": -1,
        "B37M": -1,
        "B38M": -1,
        "B39M": -1,
        "B3XM": -1,
        "E170": -1,
        "E190": -1,
        "E195": -1,
        "A318": -2,
        "A319": -2,
        "A19N": -2,
        "A320": -2,
        "A20N": -2,
        "AT43": -6.5,
        "AT45": -6.5,
        "AT72": -6.5,
        "RJ70": -6.5,
        "RJ85": -6.5,
        "DH8A": -6.5,
        "DH8B": -6.5,
        "DH8C": -6.5,
        "DH8D": -6.5,
        "D328": -6.5,
        "E135": -6.5,
        "E145": -6.5,
        "CRJ1": -6.5,
        "CRJ2": -6.5,
        "CRJ7": -6.5,
        "CRJ9": -6.5,
        "F50": -6.5,
        "J328": -6.5
    }

    tableGroup = {
        "ARC-A": 0,
        "ARC-B": 0,
        "ARC-C": 0,
        "ARC-D": 0,
        "ARC-E": 0,
        "ARC-F": 0,
        "Unknown": 0
    }

    try:
        return Distance.fromMeters(tableIcao.get(aircraftData.icaoTypeDesignator,tableGroup.get(aircraftData.aircraftGroup, 0)))
    except:
        return Distance.fromMeters()
    
@AlternativeStopPositions
def custom_stops_76(aircraftData):
    tableIcao = {
        "B717": 0,
        "MD87": 0,
        "A30B": 0,
        "A306": 0,
        "B762": 0,
        "B763": 0,
        "B764": 0,
        "B772": 0,
        "B773": 0,
        "B77W": 0,
        "B788": 0,
        "B789": 0,
        "B78X": 0,
        "A310": -1.8,
        "B752": -1.8,
        "B753": -1.8,
        "A332": -1.8,
        "A333": -1.8,
        "A342": -1.8,
        "A343": -1.8,
        "A345": -1.8,
        "A346": -1.8,
        "A359": -1.8,
        "A319": -4.6,
        "A19N": -4.6,
        "A320": -4.6,
        "A20N": -4.6,
        "A321": -4.6,
        "A21N": -4.6,
        "B733": -4.6,
        "B734": -4.6,
        "B735": -4.6,
        "B736": -4.6,
        "B737": -4.6,
        "B738": -4.6,
        "B739": -4.6,
        "B37M": -4.6,
        "B38M": -4.6,
        "B39M": -4.6,
        "B3XM": -4.6,
        "CRJ1": -4.6,
        "CRJ2": -4.6,
        "CRJ7": -4.6,
        "CRJ9": -4.6,
        "E170": -4.6,
        "E190": -4.6,
        "E195": -4.6,
        "F70": -4.6,
        "F100": -4.6,
        "B741": -4.6,
        "B742": -4.6,
        "B743": -4.6,
        "B744": -4.6,
        "B748": -4.6,
        "B74R": -4.6,
        "B74S": -4.6,
        "AT43": -7.1,
        "AT45": -7.1,
        "AT72": -7.1,
        "RJ70": -7.1,
        "RJ85": -7.1,
        "RJ1H": -7.1,
        "DH8A": -7.1,
        "DH8B": -7.1,
        "DH8C": -7.1,
        "DH8D": -7.1,
        "D328": -7.1,
        "E135": -7.1,
        "E145": -7.1,
        "F50": -7.1,
        "J328": -7.1
    }

    tableGroup = {
        "ARC-A": 0,
        "ARC-B": 0,
        "ARC-C": 0,
        "ARC-D": 0,
        "ARC-E": 0,
        "ARC-F": 0,
        "Unknown": 0
    }

    try:
        return Distance.fromMeters(tableIcao.get(aircraftData.icaoTypeDesignator,tableGroup.get(aircraftData.aircraftGroup, 0)))
    except:
        return Distance.fromMeters()
    
@AlternativeStopPositions
def custom_stops_remote(aircraftData):
    tableGroup = {
        42: 1.75,
        72: 1.75,
        146: 1.75,
        1008: 1.75,
        300: 1.75,
        600: 1.75
    }

    return Distance.fromMeters(tableGroup.get(aircraftData.idMajor, 0))

parkings = {
    0 : {
        None : (),
        0 : (ga_north, ),
        3 : (CustomizedName("Hangars | Hangar 9", 9), ),
        5 : (CustomizedName("Hangars | Hangar 10", 9), ),
        506 : (CustomizedName("Hangars | SAS Hangar Stand 506", 9), ),
        601 : (CustomizedName("Hangars | SAS Hangar Stand 601", 9), )
    },
    GATE : {
        None : (),
        2 : (west, custom_stops_default),
        3 : (west, custom_stops_default),
        7 : (west, custom_stops_default),
        9 : (west, custom_stops_9_12),
        10 : (west, custom_stops_9_12),
        11 : (west, custom_stops_9_12),
        12 : (west, custom_stops_9_12),
        13 : (west, custom_stops_13_45),
        14 : (west, custom_stops_13_45),
        15 : (west, custom_stops_13_45),
        16 : (west, custom_stops_13_45),
        18 : (west, custom_stops_13_45),
        20 : (west, custom_stops_13_45),
        22 : (west, custom_stops_13_45),
        24 : (west, custom_stops_13_45),
        26 : (west, custom_stops_13_45),
        28 : (west, custom_stops_28),
        36 : (east, custom_stops_36_38),
        38 : (east, custom_stops_36_38),
        39 : (east, custom_stops_13_45),
        40 : (east, custom_stops_40),
        41 : (east, custom_stops_13_45),
        43 : (east, custom_stops_13_45),
        44 : (east, custom_stops_13_45),
        45 : (east, custom_stops_13_45),
        46 : (east, custom_stops_46),
        47 : (CustomizedName("Terminal - East Pier (36-58) | Gate 47 (Disabled)", 2), ),
        48 : (east, custom_stops_default),
        49 : (east, custom_stops_49),
        51 : (east, custom_stops_51),
        52 : (east, custom_stops_52),
        53 : (east, custom_stops_53),
        54 : (east, custom_stops_default),
        56 : (east, custom_stops_56_58),
        58 : (east, custom_stops_56_58),
        60 : (north, custom_stops_60_81),
        61 : (north, custom_stops_60_81),
        64 : (north, custom_stops_60_81),
        65 : (north, custom_stops_60_81),
        68 : (north, custom_stops_60_81),
        69 : (north, custom_stops_60_81),
        72 : (north, custom_stops_60_81),
        73 : (north, custom_stops_60_81),
        76 : (north, custom_stops_76),
        77 : (north, custom_stops_60_81),
        80 : (north, custom_stops_default),
        81 : (north, custom_stops_60_81),
        85 : (north, custom_stops_default),
        89 : (north, custom_stops_default),
        93 : (north, custom_stops_default),
        95 : (north, custom_stops_default),
        96 : (north, custom_stops_default),
        "171L" : (remote, custom_stops_default),
        173 : (remote, custom_stops_remote),
        174 : (remote, custom_stops_remote),
        175 : (remote, custom_stops_remote),
        176 : (remote, custom_stops_remote),
        177 : (remote, custom_stops_remote),
        178 : (remote, custom_stops_remote),
        181 : (remote, custom_stops_default),
        182 : (remote, custom_stops_default),
        183 : (remote, custom_stops_default),
        184 : (remote, custom_stops_default),
        185 : (remote, custom_stops_default),
        186 : (remote, custom_stops_default),
        187 : (remote, custom_stops_default),
        189 : (CustomizedName("Terminal - Remote (171-188) | Stand 188", 4), custom_stops_default),
        "201L" : (cargo, custom_stops_default),
        "203L" : (cargo, custom_stops_default),
        205 : (cargo, custom_stops_default),
        206 : (cargo, custom_stops_default),
        207 : (cargo, custom_stops_default),
        208 : (cargo, custom_stops_default)
    },
    GATE_M : {
        None : (military, )
    },
    PARKING : {
        None : (ga, ),
        "1N" : (ga_north, ),
        "2N" : (ga_north, ),
        "3N" : (ga_north, ),
        "4N" : (ga_north, )
    }
}