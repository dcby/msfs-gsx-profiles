msfs_mode = 1
version = "1.8.2"

# Replace the <CID> with your VATSIM CID in just numbers. Ensure that you put in just the number. For example, "userVarVATSIMCID = 1880962". '<CID>' by default.
userVarVATSIMCID = '<CID>'

# If you encounter issues, set this to True. The line should look like: "verboseLog = True". This enables very detailed logging in couatl.log. False by default.
verboseLog = True

# Show the data source (VATSIM or Simbrief) on the VDGS display. True by default
showDataSource = True

# At least one of these need to be online on VATSIM for the handler to ping the CDM API. 
airportATC = ['ENGM_ATIS', 'ENGM_A_ATIS', 'ENGM_D_ATIS', 'ENGM_W_DEL', 'ENGM_E_DEL', 'ENGM_W_GND', 'ENGM_E_GND', 'ENGM_P_GND', 'ENGM_W_TWR', 'ENGM_E_TWR', 'ENGM_W_APP', 'ENGM_E_APP', 'ENGM_D_APP', 'ENGM_F_APP', 'ENOS_CTR', 'ENOS_N_CTR', 'ENOR_S_CTR', 'ENOR_SC_CTR', 'ENOR_CTR', 'ENRC_S_CTR'] 

# This is the prefix for all log messages in couatl.log. These are off by default to prevent flooding the log file, instruct your users to enable it above if they want to see the logs as a troubleshooting measure.
handlerID = "JBX Profiles' ENGM Handler log: "

varVATSIMCID = None
handlerCycleRunning = False

# Input is a string of 4 numbers in HHMM or 6 numbers in HHMMSS, output is a time object that takes real time and adds the hhmmss time to it
def hhmmssToObj(hhmmss):
    irlTimeInt = time.time()
    irlTimeObj = time.gmtime(irlTimeInt)
    irlIntBase = irlTimeInt - irlTimeObj[3] * 3600 - irlTimeObj[4] * 60 - irlTimeObj[5]
    hh = int(hhmmss[0:2])
    mm = int(hhmmss[2:4])
    ss = hhmmss[4:6]

    # ss can be omitted, this is the fallback to ensure that if it is not present, nothing breaks
    if ss == '':
        ss = 0
    else:
        ss = int(ss)
    
    tgtInt = irlIntBase + hh * 3600 + mm * 60 + ss

    # If it detects that target time is more than 12 hours before current time, it adds 24 hours to the integer to have it cross over into the next day. This is a fallback to ensure that people who load in at 2355Z with a TOBT of 0015Z, for instance, don't have "+23 hours" as their TTD but rather have the correct "-20 minutes"
    if (irlTimeInt - tgtInt) > 43200:
        if verboseLog:
            print(f'{handlerID}Adding 24 hours to time to account for day rollover.')
        tgtInt = tgtInt + (24 * 3600)

    if verboseLog:
        print(f'{handlerID}hhmmssToObj function variables:\nInput Time String: {hhmmss}\nCurrent IRL Time (int): {irlTimeInt}\nCurrent IRL Time (obj): {irlTimeObj}\nIRL Time Base (int): {irlIntBase}\nTarget Time (int): {tgtInt}\nTarget Time (obj): {time.gmtime(tgtInt)}')

    return time.gmtime(tgtInt)

# Technically this isn't necessary but having it makes life easier
def splitTime(timeObj):
    return f'{timeObj[3]:02d}{timeObj[4]:02d}'

def compareTime(ttc, isGameTime):
    # ttc - Time to compare
    timeRef = 0

    if isGameTime:
        timeInt0AD = executeCalculatorCode('(E:ABSOLUTE TIME, seconds)') # Gets the absolute time in seconds since 1/1/1 AD

        timeRef = timeInt0AD - 62135596800 # - 62135596800 converts the time from seconds since 1/1/1 AD to seconds since 1/1/1970
        
    else:
        timeRef = time.time()

    ttcCompared = calendar.timegm(ttc) - timeRef

    # Converts seconds to HHMM. :02d formats it such that there is a leading zero if needed
    if ttcCompared > 0:
        timeRemainingM = int(ttcCompared // 60)

        ttcReturn = f'-{timeRemainingM:02d}'

    if ttcCompared < 0:
        timeRemainingM = int(-ttcCompared // 60)

        ttcReturn = f'{timeRemainingM:02d}'

    if ttcCompared == 0:
        ttcReturn = '0'

    if verboseLog:
        print(f'{handlerID}Time comparison function variables:\nTime to Compare: {ttc}\nIs Game Time: {isGameTime}\nReference Time: {timeRef}\nCompared Time (seconds): {ttcCompared}\nTime Remaining (M): {timeRemainingM}\nReturned TTD: {ttcReturn}')

    return ttcReturn

def getSimbriefData():
    sbDataPresent = False
    sbTOBT = ''
    sbEoC = [0,0,0,0,0]
    sbTimeToEoC = ''
    sbCallsign = ''
    sbRWY = ''

    sb = getSimbrief()

    if sb:
        if sb.last_error:
            print(f'{handlerID}Simbrief Error: {sb.last_error}')
        else:
            sbCallsign = sb.callsign

            sbTOBT = sb.sched_out
            sbEoC = sb.sched_off
            sbTimeToTOBT = compareTime(sb.sched_out, True)
            sbRWY = sb.plan_rwy

            sbDataPresent = True

    if verboseLog:
        print(f'{handlerID}Simbrief function variable log:\nSimbrief Data Present: {sbDataPresent}\nCallsign: {sbCallsign}\n\nTOBT: {sbTOBT}\nEoC: {sbEoC}\nTime to TOBT: {sbTimeToTOBT}\nRunway: {sbRWY}')

    return sbDataPresent, sbCallsign, sbTOBT, sbEoC, sbTimeToTOBT, sbRWY

def testVATSIM(cid):
    VATSIMApiReturn = fetchJson('https://data.vatsim.net/v3/vatsim-data.json', 10, True)
    vtDataPresent = False
    vtCallsign = ''
    vtICAO = ''
    airportOnline = False

    # This never happens but in case VATSIM like disintegrates or something I guess it's a good fallback. I added it during testing with a local API
    if VATSIMApiReturn == None:
        print(f'{handlerID}VATSIM datafile returned no data.')

    else:
        for pilot in VATSIMApiReturn['pilots']:
            if pilot['cid'] == int(cid):
                if pilot['flight_plan'] == None:
                    print(f'{handlerID}No flight plan has been filed on VATSIM.')
                
                else:
                    vtCallsign = pilot['callsign']
                    vtICAO = pilot['flight_plan']['aircraft_short']
                    vtDataPresent = True

        # Check if ENGM is online. If not, don't ping CDM because if ESSA is offline then CDM is going to be empty
        for controller in VATSIMApiReturn["controllers"]:
            if controller['callsign'] in airportATC:
                airportOnline = True

        for atis in VATSIMApiReturn["atis"]:
            if atis['callsign'] in airportATC:
                airportOnline = True

    if verboseLog:
        print(f'{handlerID}VATSIM function variable log:\nVATSIM API Data Present: {vtDataPresent}\ENGM Online on VATSIM: {airportOnline}\nCallsign: {vtCallsign}\nAircraft ICAO: {vtICAO}')

    return vtDataPresent, vtCallsign, vtICAO, airportOnline, vtCallsign

def getCDM(callsign):
    CDMEoC = [0,0,0,0,0]
    CDMTimeToTOBT = ''
    CDMTOBT = ''
    CDMTSAT = ''
    CDMisCtot = False
    CDMDepInfo = ''
    CDMRWY = ''
    CDMAPIOffline = False

    CDMAPIReturn = fetchJson(f'https://cdm-server-production.up.railway.app/ifps/callsign?callsign={callsign}', timeout=10, etag=True)

    # CDM API can, on rare occasions, be down, this is a fallback for that
    if CDMAPIReturn == None:
        print(f'{handlerID}CDM API returned no data.')
        CDMAPIOffline = True
    else:
        # It's possible that TOBT and TSAT fields will be empty if CDM isn't applied so this handles that edgecase as EOBT should always be defined
        if (CDMAPIReturn['cdmData'])['tobt'] == '':
            CDMTOBT = hhmmssToObj(CDMAPIReturn['eobt'])
        else:
            CDMTOBT = hhmmssToObj((CDMAPIReturn['cdmData'])['tobt'])

        if (CDMAPIReturn['cdmData'])['tsat'] == '':
            CDMTSAT = CDMTOBT
        else:
            CDMTSAT = hhmmssToObj((CDMAPIReturn['cdmData'])['tsat'])

        # TTOT can be given if CDM in use but defaults to using TSAT + taxi time if it's not present
        if (CDMAPIReturn['cdmData'])['ttot'] == '':
            CDMEoC = time.gmtime(calendar.timegm(CDMTSAT) + (CDMAPIReturn['taxi'] * 60))
            CDMisCtot = False
        else:
            CDMEoC = hhmmssToObj((CDMAPIReturn['cdmData'])['ttot'])
            CDMisCtot = True

        sb = getSimbrief()

        if (CDMAPIReturn['cdmData'])['depInfo'] != '':
            CDMDepInfo = ((CDMAPIReturn['cdmData'])['depInfo']).split('/')
            
            CDMRWY = CDMDepInfo[0]
        
        else:
            if sb:
                if sb.last_error:
                    print(f'{handlerID}Simbrief Error: {sb.last_error}')
                else:
                    CDMRWY = sb.plan_rwy

        CDMTimeToTOBT = compareTime(CDMTOBT, False)

    return CDMEoC, CDMTimeToTOBT, CDMTOBT, CDMTSAT, CDMRWY, CDMisCtot, CDMAPIOffline

def CDMHandlerHub():
    global showChockandGate, showPaxCargoFuel
    sbPass = False
    blockScript = False # Troubleshooting variable

    varVATSIMCID = getGlobalPersistentVariable('vatsim_cid')
    if varVATSIMCID == None:
        if (userVarVATSIMCID == '<CID>') and (getGlobalPersistentVariable('vatsim_cid') == None):
            userMenuInput = inputBox('Enter your VATSIM CID or set to 0 if you don\'t use VATSIM:', 'ENGM Aerosoft GSX Profile Handler', '0')
            if userMenuInput:
                varVATSIMCID = userMenuInput
                setGlobalPersistentVariable('vatsim_cid', userMenuInput)
            else:
                print('No VATSIM CID is set in the script. Please set one.')
                varVATSIMCID = 0
        else:
            setGlobalPersistentVariable('vatsim_cid', userVarVATSIMCID)
            varVATSIMCID = userVarVATSIMCID

    if verboseLog:
        print(f'{handlerID}VATSIM CID used for handler: {varVATSIMCID}. Global persistent variable return: {getGlobalPersistentVariable("vatsim_cid")}')

    # Only run the script if the VDGS system is the SafeDockT42 or SafeDockT24
    if (("SafeDockTS24Screen" not in (getGate().parkingSystem)) and ("SafeDockT42Screen" not in (getGate().parkingSystem))) or blockScript:
        print(f'{handlerID}VDGS System is not supported.')
    else:
        # Delay to give GSX time to initialize
        truewait(2500)

        while True:
            # Checks to make sure Simbrief data is valid, if not, tell the user to refresh it
            if not sbPass:
                sbData = getSimbrief()
                if sbData.last_error:
                        truewait(10000)
                        pass
                else:
                    sbPass = True

            if sbPass:
                if verboseLog:
                    print(f'{handlerID}Starting handler cycle')

                vTestVATSIM = testVATSIM(varVATSIMCID)
                vGetSB = getSimbriefData()

                if verboseLog:
                    print(f'{handlerID}VATSIM Data Present: {vTestVATSIM[0]}, Airport online on VATSIM: {vTestVATSIM[3]}, Simbrief Data Present: {vGetSB[0]}')

                if (vTestVATSIM[0] == True) and (vTestVATSIM[3] == True):
                    vGetCDM = getCDM(vTestVATSIM[1])
                    if vGetCDM[6] == True:
                        if verboseLog:
                            print(f'{handlerID}CDM API is offline, using Simbrief data as fallback.')
                        setVDGS(vGetSB[2], vGetSB[4], vGetSB[2], vGetSB[3], vGetSB[1], vGetSB[5], 'SIMBRIEF', False)
                    else:
                        print('')
                        setVDGS(vGetCDM[2], vGetCDM[1], vGetCDM[3], vGetCDM[0], vTestVATSIM[4], vGetCDM[4], 'VATSIM', vGetCDM[5])

                else:
                    if vGetSB[0] == True:
                        print('')
                        setVDGS(vGetSB[2], vGetSB[4], vGetSB[2], vGetSB[3], vGetSB[1], vGetSB[5], 'SIMBRIEF', False)

                truewait(30000)
                
def setVDGS(TOBT, TimeToTOBT, TSAT, EoCVar, Callsign, RWY, dataType, isCTOT):
    global showDataSource

    if not showDataSource:
        dataType = ''

    TOBT = splitTime(TOBT)
    TSAT = splitTime(TSAT)
    EoC = splitTime(EoCVar)

    if isCTOT:
        EoCType = 'CTOT'
    else:
        EoCType = 'ETD'

    if verboseLog:
        print(f'{handlerID}Data received by setVDGS():\n TOBT: {TOBT}\nTime to TOBT: {TimeToTOBT}\nTSAT: {TSAT}\nEoC: {EoC}\nCallsign: {Callsign}\nRunway: {RWY}\nData Source: {dataType}\nIs CTOT: {isCTOT}')

    addVdgsMessage({
        "id": "chock_and_gate_display",
        "display": {"flex": {"pages": [{"lines": [''], "duration": 0}]}, "wide": {"pages": [{"lines": [''], "duration": 0}]}}
    })

    addVdgsMessage({
        "id": "connections_display",
        "display": {"flex": {"pages": [{"lines": [''], "duration": 0}]}, "wide": {"pages": [{"lines": [''], "duration": 0}]}}
    })

    addVdgsMessage({
        "id": "passenger_cargo_info",
        "display": {"flex": {"pages": [{"lines": [''], "duration": 0}]}, "wide": {"pages": [{"lines": [''], "duration": 0}]}}
    })

    addVdgsMessage({
        "id": "flight_information",
        "display": {
            "wide": {
                "pages": [
                    {"lines": [
                        f'TOBT {TOBT}',
                        f'TSAT {TSAT}',
                        f'{EoCType} {EoC}',
                        Callsign,
                        f'RWY {RWY}',
                        dataType
                    ], "duration": 15000},
                    {"lines": [
                        f'TOBT {TimeToTOBT}',
                        f'TSAT {TSAT}',
                        f'{EoCType} {EoC}',
                        Callsign,
                        f'RWY {RWY}',
                        dataType
                    ], "duration": 15000}
                ]
            },
            "flex": {
                "pages": [
                    {"lines": [
                        f'TOBT {TOBT}',
                        f'TSAT {TSAT}',
                        f'{EoCType} {EoC}',
                        Callsign,
                        f'RWY {RWY}',
                        dataType
                    ], "duration": 15000},
                    {"lines": [
                        f'TOBT {TimeToTOBT}',
                        f'TSAT {TSAT}',
                        f'{EoCType} {EoC}',
                        Callsign,
                        f'RWY {RWY}',
                        dataType
                    ], "duration": 15000}
                ]
            }
        }
    })

# Locks the handler cycle to prevent multiple instances of the cycle running at the same time
def CDMHandlerCycleLock():
    global handlerCycleRunning
    if verboseLog:
        print(f'{handlerID}Handler cycle running: {handlerCycleRunning}')
    if not handlerCycleRunning:
        handlerCycleRunning = True
        CDMHandlerHub()

SIMULTANEOUS_IDS = [737, 318, 319, 320, 321, 170, 175, 190, 195]

HANDLERS = {
    "AEE": "WIF",
    "BTI": "MENZ",
    "AFR": "SK_WHITE",
    "ASL": "WIF",
    "FLI": "WIF",
    "AUA": "SK_WHITE",
    "BRX": "WIF",
    "BIX": "WIF",
    "BAW": "MENZ",
    "BEL": "SK_WHITE",
    "DTR": "WIF",
    "EZY": "MENZ",
    "EJU": "MENZ",
    "EZS": "MENZ",
    "UAE": "MENZ",
    "ENT": "MENZ",
    "ETH": "MENZ",
    "EWG": "MENZ",
    "FIN": "MENZ",
    "CHH": "MENZ",
    "IBE": "MENZ",
    "ICE": "WIF",
    "KLM": "SK_WHITE",
    "LOG": "MENZ",
    "LOT": "MENZ",
    "DLH": "SK_WHITE",
    "LGL": "WIF",
    "NBT": "WIF",
    "UBT": "WIF",
    "NOZ": "MENZ",
    "NSZ": "MENZ",
    "PGT": "MENZ",
    "QTR": "MENZ",
    "RYR": "MENZ",
    "SAS": "SK_WHITE",
    "SUS": "MENZ",
    "SXS": "MENZ",
    "SWR": "SK_WHITE",
    "TAP": "MENZ",
    "THA": "WIF",
    "TRA": "WIF",
    "TVF": "WIF",
    "THY": "MENZ",
    "VOE": "MENZ",
    "VLG": "MENZ",
    "WIF": "WIF",
    "WZZ": "MENZ",
    "WMT": "MENZ",
    "WUK": "MENZ"
}

FALLBACKS = "MENZ,SK_WHITE,WIF"

def get_acft_icao():
    sb = getSimbrief()
    
    code = str(getattr(sb, "icao_airline", None)).strip().upper()
    acft_code = str(getattr(aircraft, "icaoAirline", None)).strip().upper()

    if not code and not acft_code:
        return None

    if code != acft_code:
        choice = showChoiceMenu("Simbrief and aircraft airline ICAOs don't match, select the correct one:", [f"Simbrief: {code}", f"aircraft: {acft_code}"])
        if choice == 0:
            return code
        if choice == 1:
            return acft_code
    elif code == acft_code:
        return code
    
    return None

def get_handler():
    icao = get_acft_icao()
    
    if icao and icao in HANDLERS:
        return HANDLERS[icao]
    
    return FALLBACKS

def apply_handler():
    gate = getGate()
    
    if not gate:
        return
    
    handler = get_handler()

    gate.fuelTruckTexture = "SKYTANKING,AFSN"
    gate.handlingTexture = handler
    if aircraft.idMajor not in SIMULTANEOUS_IDS:
        gate.simultaneousBoarding = False
    else:
        gate.simultaneousBoarding = True

def onAirportBeforeVehicleSelect(self):
    apply_handler()

def onAircraftEngaged(self):
    runAsync(CDMHandlerCycleLock)

def onBoardingRequested(self):
    runAsync(CDMHandlerCycleLock)

def onRefuelingRequested(self):
    runAsync(CDMHandlerCycleLock)

def onVehicleCandidatesScored(self, vehicleType, candidates):
    if vehicleType == "Staircase":
        for c in candidates:
            if 'CDS' in c.title and '2445' in c.title:
                c.boostScore(10)
            if 'FW2458PE':
                c.boostScore(-10)
    if vehicleType == "BaggageTractor":
        for c in candidates:
            if 'JET_16' in c.title:
                c.boostScore(10)
    if vehicleType == "BaggageLoader":
        for c in candidates:
            if 'CHAMP' in c.title:
                c.boostScore(10)
    if vehicleType == "PushBack":
        for c in candidates:
            if 'TPX_100_E' in c.title:
                c.boostScore(10)
    if vehicleType == "BaggageWagon":
        for c in candidates:
            if 'Open' in c.title:
                c.boostScore(10)