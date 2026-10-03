# ============================================================
# LOWW Enhanced GSX Handler
# Version: 5.2
# Date: 2026-09-13
# Author: https://flightsim.to/profile/AUA9085
#
# Original CDM / VDGS / SimBrief integration:
# Based on "CDM-to-VDGS-link" by Likeusb
# https://github.com/likeusb/CDM-to-VDGS-link
# Many thanks!
#
# This handler contains modified and extended logic
# based on the original work of the respective authors.
#
# Additional features include:
# - Automatic jetway connection
# - Automatic stairs connection
# - Bundled GSX remote session for Jetway + Stairs
# - GSX profile-ready callback guard before automated menu actions
# - Current-gate preparation guard using selectGate(getGate())
# - Docs-aligned startup: no module-level runAsync/startup task
# - Correct GSX service state enum handling
# - Conservative LOWW vehicle model radius guard for utility services
# - Gate-jump-safe async handling
# - Persistent automation configuration
# - Runtime automation switching
# - Dynamic SimBrief API integration
# - Live OFP change detection
# - Dynamic VDGS data updates
# - Custom CDM/SimBrief fallback handling
# - Enhanced GSX VDGS messaging logic
#
#
# Redistribution, modification, or reuse of this file
# or substantial portions of its custom logic is not
# permitted without explicit permission from the author(s).
#
# Original credits must be preserved.
# ============================================================
msfs_mode = 1
settings = getSettings()
sb_username = settings.simbrief_username 
userVarVATSIMCID = '<CID>'
varVATSIMCID = getGlobalPersistentVariable('vatsim_cid')
userVarAutoStairs = '<ASK>'
varAutoStairs = getGlobalPersistentVariable('loww_automation_enabled')
verboseLog = False
jetwayDebug = False
showChockandGate = False
showPaxCargoFuel = False
showDataSource = False
airportATC = ['LOWW_ATIS', 'LOWW_D_ATIS', 'LOWW_A_ATIS', 'LOWW_DEL', 'LOWW_GND', 'LOWW_TWR', 'LOWW_APP'] 
vdgsDuration = 7000
vdgsPages = 3 
handlerID = "LOWWHandlerLOG: "
handlerCycleRunning = False
gateChangeFlag=False
gateWakeupSent=False
abortCDM=False
handlerActive=False
stairsRunning=False
stairsGeneration=0
jetwayRunning=False
jetwayGeneration=0
lastVDGSData = ''
lastSID = ''
lastTOBT = ''
lastCDMSID = ''
lastCDMTOBT = ''
currentAirport = ''
vatsimCIDSetupDone = False
automationSetupDone = False
startupRunning = False
vatsimCIDPromptRunning = False
gateJumpVDGSRefreshRunning = False
gateSetupPromptRunning = False
gateServiceStartRequested = False
gateSessionActive = False
servicesStopRequested = False
cdmRefreshIntervalMs = 60000
vdgsCountdownRefreshMs = 5000
vdgsCountdownRunning = False
lastVDGSPayload = None
lastVDGSCountdown = ''
jetwayGSXRequestObserved = False
jetwayGSXConnectedObserved = False
jetwayGSXDisconnectedObserved = False
stairsGSXRequestObserved = False
stairsGSXConnectedObserved = False
gsxMenuOperationRunning = False
gateServicesBundleRunning = False
gateServicesBundleGeneration = 0
gsxProfileSettleWaitMs = 22000
gsxProfileReadyTimeoutMs = 45000
gsxProfilePostVehicleSelectDelayMs = 6000
gsxProfileStandStableRequired = 6
gsxVehicleSelectReady = False
gsxVehicleSelectReadyAt = 0
gsxVehicleSelectReadyContext = ''
gsxVehicleSelectReadyStand = ''
gsxProfilePrepareAttempted = False

GSX_SERVICE_AVAILABLE = 1
GSX_SERVICE_UNAVAILABLE = 2
GSX_SERVICE_BYPASSED = 3
GSX_SERVICE_REQUESTED = 4
GSX_SERVICE_PERFORMING = 5
GSX_SERVICE_COMPLETED = 6
GSX_SERVICE_COMPLETING = 7
		
def vLog(msg):

    if verboseLog:
        print(msg)

def isLOWW():

    try:
        return getAirport().icao == "LOWW"
    except:
        return currentAirport == "LOWW"

def shouldRunHandler():

    return handlerActive and isLOWW()


def normalizeGSXServiceState(state):

    try:
        return int(float(state))
    except:
        return -1


def isGSXServiceCompleted(state):

    return normalizeGSXServiceState(state) == GSX_SERVICE_COMPLETED


def isGSXServiceBusy(state):

    return normalizeGSXServiceState(state) in [GSX_SERVICE_REQUESTED, GSX_SERVICE_PERFORMING, GSX_SERVICE_COMPLETING]


def isGSXServiceRequestableIdle(state):

    return normalizeGSXServiceState(state) in [0, GSX_SERVICE_AVAILABLE]


def isGateSessionActive():

    return shouldRunHandler() and gateSessionActive and not servicesStopRequested and not gateChangeFlag


def waitForActiveGate(totalMs, stepMs=250):

    waited = 0

    while waited < totalMs:

        if not isGateSessionActive():

            return False

        waitNow = min(stepMs, totalMs - waited)
        truewait(waitNow)
        waited += waitNow

    return True


def resetGSXVehicleSelectionReady():

    global gsxVehicleSelectReady
    global gsxVehicleSelectReadyAt
    global gsxVehicleSelectReadyContext
    global gsxVehicleSelectReadyStand
    global gsxProfilePrepareAttempted

    gsxVehicleSelectReady = False
    gsxVehicleSelectReadyAt = 0
    gsxVehicleSelectReadyContext = ''
    gsxVehicleSelectReadyStand = ''
    gsxProfilePrepareAttempted = False


def markGSXVehicleSelectionReady(context='onAirportBeforeVehicleSelect'):

    global gsxVehicleSelectReady
    global gsxVehicleSelectReadyAt
    global gsxVehicleSelectReadyContext
    global gsxVehicleSelectReadyStand

    gsxVehicleSelectReady = True
    gsxVehicleSelectReadyAt = time.time()
    gsxVehicleSelectReadyContext = str(context)

    try:
        gsxVehicleSelectReadyStand = getCurrentStandName()
    except:
        gsxVehicleSelectReadyStand = ''



def requestCurrentGatePreparationIfPossible():

    # v5.1: Ask GSX to prepare the already detected gate once, before the
    # automation touches service menu choices. selectGate() is documented as
    # deferred/safe from callbacks and equivalent to choosing the gate from GSX.
    # If GSX already prepared the gate or services are already active, this is
    # harmless and simply returns False/None depending on the live state.

    global gsxProfilePrepareAttempted

    if gsxProfilePrepareAttempted:
        return

    gsxProfilePrepareAttempted = True

    try:
        gate = getGate()
    except:
        gate = None

    if not gate:
        vLog(f"{handlerID} GSX current-gate prepare skipped - getGate() unavailable")
        return

    try:
        result = selectGate(gate)
        vLog(f"{handlerID} GSX current-gate prepare requested via selectGate(getGate()), result={result}")
    except Exception as e:
        vLog(f"{handlerID} GSX current-gate prepare failed: {e}")



def waitForGSXProfileSettle(totalMs=None, stepMs=500):

    # v5.1: Use the documented GSX gate/vehicle-selection lifecycle as the
    # readiness signal. onAirportBeforeVehicleSelect fires when GSX has assigned
    # the gate and is about to select operators/vehicles. We then wait a small
    # post-callback grace period before touching GSX_MENU_OPEN / MENU_CHOICE.
    # If the callback is not observed, fall back to the old stand-stability delay
    # instead of faking GSX service states.

    global gsxProfileSettleWaitMs
    global gsxProfileReadyTimeoutMs
    global gsxProfilePostVehicleSelectDelayMs
    global gsxProfileStandStableRequired
    global gsxVehicleSelectReady
    global gsxVehicleSelectReadyAt
    global gsxVehicleSelectReadyContext
    global gsxVehicleSelectReadyStand

    if totalMs == None:

        totalMs = gsxProfileReadyTimeoutMs

    requestCurrentGatePreparationIfPossible()

    waited = 0
    lastStand = ''
    stableCount = 0

    while waited < totalMs:

        if not isGateSessionActive():

            return False

        stand = ''

        try:

            stand = getCurrentStandName()

        except:

            stand = ''

        if stand != '' and stand == lastStand:

            stableCount += 1

        else:

            lastStand = stand
            stableCount = 1 if stand != '' else 0

        if gsxVehicleSelectReady and gsxVehicleSelectReadyAt:

            ageMs = int((time.time() - gsxVehicleSelectReadyAt) * 1000)

            if ageMs >= gsxProfilePostVehicleSelectDelayMs:

                print(
                    f"{handlerID} GSX profile ready via {gsxVehicleSelectReadyContext} - stand={gsxVehicleSelectReadyStand}, age={ageMs}ms"
                )

                return True

        # Fallback: if the official ready callback was not seen, keep the older
        # conservative stand-stability guard. This prevents deadlocks on GSX
        # builds/aircraft where the callback is not exposed to the airport tier.
        if waited >= gsxProfileSettleWaitMs and lastStand != '' and stableCount >= gsxProfileStandStableRequired:

            print(
                f"{handlerID} GSX profile ready by stand stability fallback - stand={lastStand}, waited={waited}ms"
            )

            return True

        truewait(stepMs)
        waited += stepMs

    print(
        f"{handlerID} GSX profile ready timeout - continuing without state faking, waited={waited}ms, stand={lastStand}"
    )

    return True


def waitForCDMSafe(totalMs, stepMs=1000):

    waited = 0

    while waited < totalMs:

        if abortCDM or servicesStopRequested or not shouldRunHandler():

            return False

        waitNow = min(stepMs, totalMs - waited)
        truewait(waitNow)
        waited += waitNow

    return True



def vdgsCountdownLoop():

    global vdgsCountdownRunning
    global gsxMenuOperationRunning
    global jetwayGSXRequestObserved
    global jetwayGSXConnectedObserved
    global jetwayGSXDisconnectedObserved
    global stairsGSXRequestObserved
    global stairsGSXConnectedObserved
    global gsxVehicleSelectReady
    global gsxVehicleSelectReadyAt
    global gsxVehicleSelectReadyContext
    global gsxVehicleSelectReadyStand

    if vdgsCountdownRunning:

        return

    vdgsCountdownRunning = True

    try:

        # Wait a short moment after the first VDGS write so we don't immediately
        # rewrite the same value. After that, this loop keeps only the red value moving.
        truewait(vdgsCountdownRefreshMs)

        while True:

            if lastVDGSPayload == None:

                return

            if abortCDM or servicesStopRequested or not shouldRunHandler():

                return

            updateVDGSCountdownOnly()

            truewait(vdgsCountdownRefreshMs)

    except Exception as e:

        vLog(
            f"{handlerID} VDGS countdown ticker failed: {e}"
        )

    finally:

        vdgsCountdownRunning = False

def updateVDGSCountdownOnly():

    global lastVDGSPayload
    global lastVDGSCountdown

    if lastVDGSPayload == None:

        return False

    if abortCDM or servicesStopRequested or not shouldRunHandler():

        return False

    try:

        TOBT, TSAT, isCTOT, EoCVar, SID, RWY, AircraftType, dataType = lastVDGSPayload

        newCountdown = compareTime(TOBT, False)

        if newCountdown == lastVDGSCountdown:

            return True

        vLog(
            f"{handlerID} VDGS countdown refresh {lastVDGSCountdown} -> {newCountdown}"
        )

        setVDGS(
            TOBT,
            TSAT,
            isCTOT,
            EoCVar,
            newCountdown,
            SID,
            RWY,
            AircraftType,
            dataType
        )

        return True

    except Exception as e:

        vLog(
            f"{handlerID} VDGS countdown refresh failed: {e}"
        )

        return False


def waitForVDGSCountdownAndCDMSafe(totalMs):

    global vdgsCountdownRefreshMs

    waited = 0

    while waited < totalMs:

        waitNow = min(vdgsCountdownRefreshMs, totalMs - waited)

        if not waitForCDMSafe(waitNow):

            return False

        waited += waitNow

        # Lightweight local refresh only: no SimBrief/VATSIM/CDM API calls here.
        # This keeps the red countdown moving while avoiding the old 20s/60s freeze pattern.
        updateVDGSCountdownOnly()

    return True


def hardStopServices(reason):

    global gateSessionActive
    global servicesStopRequested
    global jetwayGSXRequestObserved
    global jetwayGSXConnectedObserved
    global jetwayGSXDisconnectedObserved
    global stairsGSXRequestObserved
    global stairsGSXConnectedObserved
    global abortCDM
    global gateChangeFlag
    global gateWakeupSent
    global stairsGeneration
    global jetwayGeneration
    global gateServiceStartRequested
    global lastVDGSPayload
    global lastVDGSCountdown
    global vdgsCountdownRunning
    global gsxMenuOperationRunning
    global gateServicesBundleRunning
    global gateServicesBundleGeneration
    global jetwayGSXRequestObserved
    global jetwayGSXConnectedObserved
    global jetwayGSXDisconnectedObserved
    global stairsGSXRequestObserved
    global stairsGSXConnectedObserved

    servicesStopRequested = True
    gateSessionActive = False
    abortCDM = True
    gateChangeFlag = True
    gateWakeupSent = False
    gateServiceStartRequested = False
    lastVDGSPayload = None
    lastVDGSCountdown = ''
    jetwayGSXRequestObserved = False
    jetwayGSXConnectedObserved = False
    jetwayGSXDisconnectedObserved = False
    stairsGSXRequestObserved = False
    stairsGSXConnectedObserved = False
    gsxMenuOperationRunning = False
    gateServicesBundleRunning = False
    gateServicesBundleGeneration += 1

    try:
        forceGSXRemoteControlOff(f'hard stop: {reason}')
    except:
        pass

    # Invalidate all pending service tasks.
    stairsGeneration += 1
    jetwayGeneration += 1

    vLog(
        f"{handlerID} HARD STOP SERVICES: {reason}"
    )


def callSuperIfPresent(self, methodName, *args):

    try:

        superMethod = getattr(self, f"_super_{methodName}", None)

        if superMethod:

            return superMethod(*args)

    except Exception as e:

        vLog(
            f"{handlerID} super callback {methodName} failed: {e}"
        )

    return None


def jLog(msg):

    return


def debugReadLVar(name):

    try:

        return executeCalculatorCode(
            f"(L:{name}, Number)"
        )

    except Exception as e:

        return f"ERR:{e}"


def debugGateJetwaySnapshot(context):

    return

def debugArgs(args):

    try:
        return ', '.join([str(arg) for arg in args])
    except:
        return '<args error>'

def getGSXRemoteControlState():

    try:

        return int(
            executeCalculatorCode(
                "(L:FSDT_GSX_SET_REMOTECONTROL, Number)"
            )
        )

    except Exception as e:

        vLog(
            f"{handlerID} GSX Remote Control read failed: {e}"
        )

        return 0


def setGSXRemoteControlState(value):

    try:

        executeCalculatorCode(
            f"{int(value)} (>L:FSDT_GSX_SET_REMOTECONTROL, Number)"
        )

        vLog(
            f"{handlerID} GSX Remote Control set={int(value)}"
        )

        return True

    except Exception as e:

        vLog(
            f"{handlerID} GSX Remote Control set failed: {e}"
        )

        return False


def restoreGSXRemoteControlState(oldRemoteControl):

    try:

        truewait(300)

        setGSXRemoteControlState(oldRemoteControl)

        vLog(
            f"{handlerID} GSX Remote Control restored={int(oldRemoteControl)}"
        )

    except Exception as e:

        vLog(
            f"{handlerID} GSX Remote Control restore failed: {e}"
        )


def forceGSXRemoteControlOff(reason=''):

    try:

        setGSXRemoteControlState(0)

        if reason != '':
            jLog(
                f"GSX Remote Control forced OFF: {reason}"
            )

        return True

    except Exception as e:

        vLog(
            f"{handlerID} GSX Remote Control force off failed: {e}"
        )

        return False


def acquireGSXMenuLock(owner, timeoutMs=30000):

    global gsxMenuOperationRunning

    waited = 0

    while gsxMenuOperationRunning and waited < timeoutMs:

        if not isGateSessionActive():
            return False

        truewait(250)
        waited += 250

    if gsxMenuOperationRunning:

        jLog(
            f"GSX menu lock timeout for {owner}"
        )

        return False

    gsxMenuOperationRunning = True

    jLog(
        f"GSX menu lock acquired by {owner}"
    )

    return True


def releaseGSXMenuLock(owner):

    global gsxMenuOperationRunning

    gsxMenuOperationRunning = False

    jLog(
        f"GSX menu lock released by {owner}"
    )


def getVATSIMCIDForUse():

    global varVATSIMCID

    currentCID = getGlobalPersistentVariable('vatsim_cid')

    if currentCID != None and currentCID != '' and currentCID != '<CID>':

        varVATSIMCID = currentCID

        return varVATSIMCID


    if userVarVATSIMCID != '<CID>':

        varVATSIMCID = userVarVATSIMCID

        setGlobalPersistentVariable(
            'vatsim_cid',
            userVarVATSIMCID
        )

        return varVATSIMCID


    # IMPORTANT:
    # Missing CID must NEVER block VDGS / Jetway / Stairs.
    # Return 0 so VATSIM/CDM is skipped and SimBrief fallback continues.
    varVATSIMCID = '0'

    return varVATSIMCID


def promptVATSIMCID():

    global varVATSIMCID
    global vatsimCIDSetupDone
    global vatsimCIDPromptRunning

    if vatsimCIDPromptRunning:

        return

    vatsimCIDPromptRunning = True

    try:

        truewait(3000)

        if not shouldRunHandler():

            return

        currentCID = getGlobalPersistentVariable('vatsim_cid')

        if currentCID != None and currentCID != '' and currentCID != '<CID>':

            varVATSIMCID = currentCID
            vatsimCIDSetupDone = True

            return

        if vatsimCIDSetupDone:

            return

        vatsimCIDSetupDone = True

        if userVarVATSIMCID == '<CID>':

            choiceBox(
                """>>> WARNING <<<
NO VATSIM CID SET!

Without setting a VATSIM CID your VDGS will not be updated with VATSIM data.

VDGS, Jetway and Stairs will still work with SimBrief fallback.

You can enter your VATSIM CID in the next window.""",
                "Gaya Simulations LOWW v2 GSX Profil",
                ["UNDERSTOOD"],
                default=0,
            )

            userMenuInput = inputBox(
                "Enter your VATSIM CID or set to 0 if you don't use VATSIM:",
                'Gaya Simulations LOWW v2 - Vienna / Wien GSX Profile',
                '0'
            )

            if userMenuInput:

                varVATSIMCID = userMenuInput

                setGlobalPersistentVariable(
                    'vatsim_cid',
                    userMenuInput
                )

            else:

                print(
                    f'{handlerID}No VATSIM CID is set. VATSIM/CDM disabled, using SimBrief fallback.'
                )

                varVATSIMCID = '0'

        else:

            varVATSIMCID = userVarVATSIMCID

            setGlobalPersistentVariable(
                'vatsim_cid',
                userVarVATSIMCID
            )

    except Exception as e:

        print(
            f"{handlerID} VATSIM CID prompt error: {e}"
        )

        varVATSIMCID = '0'

    finally:

        vatsimCIDPromptRunning = False


def setupAutomation():

    global varAutoStairs
    global automationSetupDone

    varAutoStairs = getGlobalPersistentVariable(
        'loww_automation_enabled'
    )

    if varAutoStairs != None:

        automationSetupDone = True

        return varAutoStairs


    if automationSetupDone:

        return varAutoStairs


    automationSetupDone = True


    if userVarAutoStairs == '<ASK>':

        choice = choiceBox(
            "Enable GSX Automation (Jetway/Stairs)?\n\n"
            "YES = Enable permanently\n"
            "NO = Disable permanently\n"
            "LATER = Ask again next time\n\n"
            ">>> IMPORTANT <<<\n"
            "Automation can be enabled or disabled manually.\n\n"
            "Open:\n"
            "%AppData%\\Virtuali\\Handlers\\handler_storage.cfg\n\n"
            "Change:\n"
            "loww_automation_enabled=1 -> ENABLED\n"
            "loww_automation_enabled=0 -> DISABLED\n\n"
            "A GSX restart is required after changing this setting.",
            "Gaya Simulations LOWW v2 GSX Profile",
            ["YES", "NO", "LATER"],
            default=0,
        )

        if choice == 0:

            setGlobalPersistentVariable(
                'loww_automation_enabled',
                '1'
            )

            varAutoStairs = '1'

        elif choice == 1:

            setGlobalPersistentVariable(
                'loww_automation_enabled',
                '0'
            )

            varAutoStairs = '0'

        else:

            varAutoStairs = None

    else:

        setGlobalPersistentVariable(
            'loww_automation_enabled',
            userVarAutoStairs
        )

        varAutoStairs = userVarAutoStairs


    return varAutoStairs


def startup():

    global currentAirport
    global handlerActive
    global abortCDM
    global gateChangeFlag
    global gateWakeupSent
    global startupRunning
    global varAutoStairs

    if startupRunning:

        return

    startupRunning = True

    truewait(1000)

    try:

        try:

            currentAirport = getAirport().icao

        except:

            currentAirport = ""


        if currentAirport != "LOWW":

            handlerActive = False
            abortCDM = True

            print(
                f"{handlerID} STARTUP ignored - airport is {currentAirport}"
            )

            return


        handlerActive = True
        abortCDM = False
        gateChangeFlag = False
        gateWakeupSent = False

        print(
            f"{handlerID} STARTUP LOWW active"
        )

        # Do not overwrite gate.autoSelectOperator globally here.
        # Let the loaded LOWW GSX airport profile own operator and vehicle-layout selection.


        # Startup must not show any popups.
        # Do NOT call setupAutomation() or promptVATSIMCID() here.
        # Jetway, Stairs, CDM and all first-run prompts start only after GSX aircraftEngaged.


    except Exception as e:

        print(
            f"{handlerID} STARTUP ERROR: {e}"
        )

    finally:

        startupRunning = False
        vatsimCIDPromptRunning = False


def normalizeStandName(rawStand):

    try:
        rawStand = str(rawStand).upper()
    except:
        return ''

    rawStand = rawStand.replace(' ', '')
    rawStand = rawStand.replace('-', '')
    rawStand = rawStand.replace('_', '')

    # Extract first pattern like A30, F12, K51 from any longer gate string
    for idx in range(0, len(rawStand) - 2):

        letter = rawStand[idx]

        if letter < 'A' or letter > 'Z':
            continue

        digits = ''

        pos = idx + 1

        while pos < len(rawStand) and rawStand[pos].isdigit():

            digits += rawStand[pos]
            pos += 1

        if len(digits) >= 2:

            return f"{letter}{int(digits):02d}"

    return ''


def getCurrentStandName():

    try:
        gate = getGate()
    except:
        gate = None

    if not gate:
        return ''

    candidates = []
    terminalCandidates = []
    numberCandidates = []

    for attrName in [
        'uiGateName',
        'uiName',
        'uiNameWithParkingSystem',
        'uiGateNameWithParkingSystem',
        'name',
        'parkingName',
        'parking',
        'title',
        'label'
    ]:
        try:
            value = getattr(gate, attrName)
            candidates.append(value)

            # Keep terminal/group strings separately for cases where GSX exposes
            # the stand as number only, e.g. ParkingProxy '8' but uiTerminalName = F.
            if attrName in [
                'uiName',
                'uiNameWithParkingSystem',
                'uiGateNameWithParkingSystem'
            ]:
                terminalCandidates.append(value)

        except:
            pass

    for attrName in [
        'uiTerminalName',
        'uiGroup',
        'uiName',
        'uiNameWithParkingSystem'
    ]:
        try:
            terminalCandidates.append(getattr(gate, attrName))
        except:
            pass

    for attrName in [
        'uiGateName',
        'name',
        'parkingName',
        'parking',
        'title',
        'label'
    ]:
        try:
            numberCandidates.append(getattr(gate, attrName))
        except:
            pass

    try:
        candidates.append(str(gate))
        numberCandidates.append(str(gate))
    except:
        pass

    # First try the old/direct method.
    for candidate in candidates:

        stand = normalizeStandName(candidate)

        if stand != '':

            return stand

    # Fallback for GSX parkings that expose only the number, e.g. "8",
    # while the terminal/group contains the letter, e.g. "F - Parking Positions EVEN".
    terminalLetter = ''

    for candidate in terminalCandidates:

        try:
            candidateString = str(candidate).upper()
        except:
            continue

        for letter in ['A', 'B', 'C', 'D', 'E', 'F', 'H', 'K']:

            if candidateString.startswith(letter) or f"{letter} -" in candidateString or f"{letter}-" in candidateString:

                terminalLetter = letter

                break

        if terminalLetter != '':

            break

    if terminalLetter != '':

        for candidate in numberCandidates:

            try:
                candidateString = str(candidate)
            except:
                continue

            digits = ''

            for ch in candidateString:

                if ch.isdigit():

                    digits += ch

                elif digits != '':

                    break

            if digits != '':

                try:

                    return f"{terminalLetter}{int(digits):02d}"

                except:

                    pass

    return ''

def standInRange(stand, startStand, endStand):

    stand = normalizeStandName(stand)
    startStand = normalizeStandName(startStand)
    endStand = normalizeStandName(endStand)

    if stand == '' or startStand == '' or endStand == '':
        return False

    if stand[0] != startStand[0] or stand[0] != endStand[0]:
        return False

    try:
        standNumber = int(stand[1:])
        startNumber = int(startStand[1:])
        endNumber = int(endStand[1:])
    except:
        return False

    if not (startNumber <= standNumber <= endNumber):
        return False

    # Odd/even matching ONLY if start and end have the same parity.
    # F01-F37 -> odd only
    # F04-F36 -> even only
    # A30-A65 -> mixed range, all stands
    if (startNumber % 2) == (endNumber % 2):

        if (standNumber % 2) != (startNumber % 2):

            return False

    return True


def getLOWWTaxiTime(rwy, fallbackTaxiTime=15):

    rwy = str(rwy).upper()
    rwy = rwy.replace('RWY', '')
    rwy = rwy.replace(' ', '')

    if len(rwy) > 2:
        rwy = rwy[-2:]

    stand = getCurrentStandName()

    taxiTable = [
        ('A30', 'A65', {'34': 18, '29': 14, '11': 7,  '16': 16}),
        ('A91', 'A96', {'34': 17, '29': 12, '11': 8,  '16': 16}),
        ('B43', 'B69', {'34': 17, '29': 12, '11': 7,  '16': 13}),
        ('B71', 'B76', {'34': 16, '29': 12, '11': 8,  '16': 13}),
        ('B81', 'B96', {'34': 16, '29': 12, '11': 8,  '16': 13}),
        ('C31', 'C42', {'34': 14, '29': 10, '11': 10, '16': 11}),
        ('D21', 'D29', {'34': 14, '29': 10, '11': 12, '16': 9}),
        ('E41', 'E47', {'34': 13, '29': 8,  '11': 11, '16': 9}),
        ('E48', 'E52', {'34': 12, '29': 6,  '11': 12, '16': 8}),
        ('F01', 'F37', {'34': 11, '29': 7,  '11': 11, '16': 7}),
        ('F08', 'F08', {'34': 14, '29': 8,  '11': 15, '16': 6}),
        ('F04', 'F36', {'34': 14, '29': 9,  '11': 15, '16': 6}),
        ('F42', 'F50', {'34': 12, '29': 7,  '11': 14, '16': 7}),
        ('F43', 'F59', {'34': 11, '29': 7,  '11': 15, '16': 7}),
        ('H41', 'H45', {'34': 12, '29': 8,  '11': 14, '16': 6}),
        ('H46', 'H49', {'34': 14, '29': 9,  '11': 14, '16': 6}),
        ('K41', 'K51', {'34': 13, '29': 9,  '11': 15, '16': 7}),
    ]

    for startStand, endStand, taxiTimes in taxiTable:

        if standInRange(stand, startStand, endStand) and rwy in taxiTimes:

            vLog(
                f"{handlerID} LOWW taxi match: stand={stand}, range={startStand}-{endStand}, rwy={rwy}, taxi={taxiTimes[rwy]}"
            )

            return taxiTimes[rwy]


    vLog(
        f"{handlerID} LOWW taxi fallback used: stand={stand}, rwy={rwy}, fallback={fallbackTaxiTime}"
    )

    return fallbackTaxiTime




def readGSXNumberLVar(name, fallback=None):

    try:

        return int(
            float(
                executeCalculatorCode(
                    f"(L:{name}, Number)"
                )
            )
        )

    except Exception as e:

        vLog(
            f"{handlerID} LVar read failed {name}: {e}"
        )

        return fallback


def requestGSXOperateJetwaysViaMenu(attempt):

    # GSX 4.x must see its own Operate Jetways service request so it can
    # fire onOperateJetwaysRequested/onJetwayConnected and update its internal state.
    # Do NOT fake/set state LVars here.
    owner = f"Jetway#{attempt}"

    if not acquireGSXMenuLock(owner, 20000):

        jLog(
            f"GSX Operate Jetways menu request skipped - menu lock unavailable attempt #{attempt}"
        )

        return False

    oldRemoteControl = 0

    try:

        oldRemoteControl = getGSXRemoteControlState()

        jLog(
            f"Requesting GSX Operate Jetways via MENU_CHOICE=5 attempt #{attempt}, oldRemote={oldRemoteControl}"
        )
        debugGateJetwaySnapshot(f"before GSX Operate Jetways menu attempt #{attempt}")

        if not isGateSessionActive():
            return False

        setGSXRemoteControlState(1)

        if not waitForActiveGate(300):
            return False

        # Open the Parking Services menu and give GSX enough time to really enter menuWaiting.
        # The previous version could send choice 5 while another Stairs menu sequence was still
        # closing, which produced menuWaiting=False and did nothing.
        executeCalculatorCode(
            "1 (>L:FSDT_GSX_MENU_OPEN)"
        )

        if not waitForActiveGate(1600):
            return False

        if not isGateSessionActive():
            return False

        # In the current GSX parking-services menu, choice 5 is Operate Jetways.
        # This is the same path that produces onOperateJetwaysRequested and
        # onJetwayConnected in the debug log.
        executeCalculatorCode(
            "5 (>L:FSDT_GSX_MENU_CHOICE)"
        )

        jLog(
            f"GSX MENU_CHOICE=5 sent for Operate Jetways attempt #{attempt}"
        )
        debugGateJetwaySnapshot(f"after GSX Operate Jetways menu attempt #{attempt}")

        waitForActiveGate(700)

        return True

    except Exception as e:

        jLog(
            f"GSX Operate Jetways menu request failed attempt #{attempt}: {e}"
        )
        debugGateJetwaySnapshot(f"GSX Operate Jetways menu failed #{attempt}")

        return False

    finally:

        try:
            restoreGSXRemoteControlState(oldRemoteControl)
            # The handler owns this automated menu action. Do not leave GSX remote control
            # active because it can steal later user/GSX menu input.
            forceGSXRemoteControlOff(f"after Operate Jetways attempt #{attempt}")
        finally:
            releaseGSXMenuLock(owner)

def waitForGSXGateSessionForJetway(totalMs=24000):

    # Stairs/Assistance services often establish the GSX gate session first.
    # Wait for that if possible, but don't require SetGate_Number forever, because
    # GSX can sometimes operate services while that LVar still looks unset.
    waited = 0

    while waited < totalMs:

        if not isGateSessionActive():
            return False

        gateNumber = readGSXNumberLVar('FSDT_GSX_SetGate_Number', -1)
        stairsState = readGSXNumberLVar('FSDT_GSX_OPERATESTAIRS_STATE', -1)

        if gateNumber != -1:

            jLog(
                f"GSX gate session ready for jetway: SetGate_Number={gateNumber}, stairsState={stairsState}, waited={waited}ms"
            )

            return True

        truewait(500)
        waited += 500

    jLog(
        "GSX SetGate_Number did not become valid before jetway request; trying Operate Jetways anyway"
    )
    debugGateJetwaySnapshot("GSX gate session wait timeout before jetway")

    return isGateSessionActive()

def autoConnectJetway():

    if not shouldRunHandler():
        jLog(
            "autoConnectJetway skipped - handler inactive"
        )
        return

    global jetwayRunning
    global jetwayGeneration
    global jetwayGSXRequestObserved
    global jetwayGSXConnectedObserved
    global jetwayGSXDisconnectedObserved

    if jetwayRunning:
        jLog(
            "autoConnectJetway skipped - JETWAY already running"
        )
        return

    jetwayRunning = True
    jetwayGeneration += 1
    myGen = jetwayGeneration

    jetwayGSXRequestObserved = False
    jetwayGSXConnectedObserved = False
    jetwayGSXDisconnectedObserved = False

    try:

        jLog(
            f"autoConnectJetway ENTER gen={myGen}, mode=GSX_SERVICE_MENU, gateSessionActive={gateSessionActive}, servicesStopRequested={servicesStopRequested}, gateChangeFlag={gateChangeFlag}"
        )
        debugGateJetwaySnapshot("jetway task enter")

        # IMPORTANT:
        # GSX 4.x needs its own Operate Jetways service path, otherwise a plain
        # TOGGLE_JETWAY key can move the sim jetway without GSX recognizing
        # onOperateJetwaysRequested/onJetwayConnected.
        # Therefore this function no longer sends TOGGLE_JETWAY.

        if not waitForActiveGate(3000):
            jLog(
                "Jetway start cancelled - gate session stopped during initial wait"
            )
            debugGateJetwaySnapshot("jetway start cancelled")
            return

        # If GSX already reports fully connected before we touch anything, do not
        # toggle via GSX menu, because Operate Jetways can disconnect an attached jetway.
        initialState = readGSXNumberLVar('FSDT_GSX_OPERATEJETWAYS_STATE', -1)

        if isGSXServiceCompleted(initialState):

            jLog(
                f"Jetway already connected by GSX state={initialState}; no action needed"
            )
            debugGateJetwaySnapshot("jetway already connected before GSX request")
            return

        # Jetway must go FIRST.
        # Do not wait for Stairs to create SetGate_Number, because that makes Stairs steal
        # the fresh GSX menu session and can leave Remote Control active. GSX can create
        # the gate service session from the Operate Jetways menu request itself.
        if not waitForActiveGate(3000):
            jLog(
                "Jetway GSX request cancelled - gate session stopped before first menu request"
            )
            debugGateJetwaySnapshot("jetway cancelled before first GSX menu request")
            return

        attempts = 0
        lastRequestAt = -999
        timeout = 0
        lastLoggedState = None

        while timeout < 120:

            if not isGateSessionActive():
                jLog(
                    f"Jetway stopped - gate session inactive at timeout={timeout}"
                )
                debugGateJetwaySnapshot("jetway stopped inactive")
                return

            if myGen != jetwayGeneration:
                jLog(
                    f"JETWAY TASK INVALIDATED myGen={myGen}, currentGen={jetwayGeneration}, timeout={timeout}"
                )
                debugGateJetwaySnapshot("jetway invalidated")
                return

            state = readGSXNumberLVar('FSDT_GSX_OPERATEJETWAYS_STATE', -1)

            if state != lastLoggedState or (timeout % 5) == 0:
                jLog(
                    f"GSX-SERVICE WATCH t={timeout}s state={state}, requestObserved={jetwayGSXRequestObserved}, connectedObserved={jetwayGSXConnectedObserved}, disconnectedObserved={jetwayGSXDisconnectedObserved}, attempts={attempts}"
                )
                lastLoggedState = state

            if jetwayGSXConnectedObserved:

                jLog(
                    f"Jetway confirmed connected by GSX callback at t={timeout}s"
                )
                debugGateJetwaySnapshot("jetway connected by callback")
                return

            if isGSXServiceCompleted(state) and (jetwayGSXRequestObserved or attempts > 0):

                jLog(
                    f"Jetway confirmed completed by GSX state={state} after GSX request at t={timeout}s"
                )
                debugGateJetwaySnapshot("jetway connected by GSX state after request")
                return

            # 4/5 = requested/operating according to observed GSX menu path. Wait.
            if isGSXServiceBusy(state) or jetwayGSXRequestObserved:

                timeout += 1
                truewait(1000)
                continue

            # 0/1 = available/rest/ready. Request through the GSX service menu,
            # not by key. Retry at most twice, with a long cooldown.
            if isGSXServiceRequestableIdle(state) and attempts < 2 and (timeout - lastRequestAt) >= 25:

                attempts += 1
                lastRequestAt = timeout

                jLog(
                    f"Jetway GSX service request attempt #{attempts} at t={timeout}s, state={state}"
                )

                if requestGSXOperateJetwaysViaMenu(attempts):

                    # Give GSX time to fire onOperateJetwaysRequested and move to state 4/5.
                    if not waitForActiveGate(4000, 500):
                        jLog(
                            "Jetway wait after GSX menu request aborted - gate session stopped"
                        )
                        debugGateJetwaySnapshot("jetway post GSX request aborted")
                        return

                    debugGateJetwaySnapshot(f"4s after GSX Operate Jetways request #{attempts}")

                else:

                    jLog(
                        f"Jetway GSX service request attempt #{attempts} failed"
                    )

            timeout += 1
            truewait(1000)

        jLog(
            "Jetway GSX service watchdog timeout"
        )
        debugGateJetwaySnapshot("jetway GSX service watchdog timeout")

    except Exception as e:

        print(
            f"{handlerID} JETWAY TASK CRASH: {e}"
        )
        debugGateJetwaySnapshot("jetway task crash")

    finally:

        jLog(
            f"autoConnectJetway EXIT gen={myGen}"
        )
        jetwayRunning = False

def waitForJetwayBeforeStairs(totalMs=90000):

    waited = 0

    try:
        gate = getGate()
        hasJetway = bool(getattr(gate, 'hasJetway', False))
    except:
        hasJetway = False

    if not hasJetway:

        vLog(
            f"{handlerID} Stairs wait: no jetway at this gate"
        )

        return waitForActiveGate(12000)

    while waited < totalMs:

        if not isGateSessionActive():
            return False

        state = readGSXNumberLVar('FSDT_GSX_OPERATEJETWAYS_STATE', -1)

        if jetwayGSXConnectedObserved or isGSXServiceCompleted(state):

            vLog(
                f"{handlerID} Stairs wait done - Jetway connected/completed state={state}, waited={waited}ms"
            )

            return True

        # If the jetway task has ended without a request and the state is unavailable,
        # don't block stairs forever.
        if not jetwayRunning and not jetwayGSXRequestObserved and waited >= 30000:

            vLog(
                f"{handlerID} Stairs wait fallback - Jetway not running/requested after {waited}ms, state={state}"
            )

            return True

        truewait(1000)
        waited += 1000

    vLog(
        f"{handlerID} Stairs wait timeout - continuing after {totalMs}ms"
    )

    return isGateSessionActive()


def autoConnectStairs():

    if not shouldRunHandler():
        vLog(
            f"{handlerID} Stairs skipped - handler inactive"
        )
        return

    global stairsRunning
    global stairsGeneration

    if stairsRunning:
        vLog(
            f"{handlerID} STAIRS already running"
        )
        return

    stairsRunning = True

    stairsGeneration += 1
    myGen = stairsGeneration

    try:

        # Jetway must go first, because GSX 4.x only recognizes the jetway properly
        # when its own Operate Jetways service path is started without Stairs using
        # the GSX menu at the same time. Wait until Jetway is connected/completed,
        # already connected, or until a safe timeout is reached.
        if not waitForJetwayBeforeStairs(90000):
            vLog(
                f"{handlerID} Stairs start cancelled - gate session stopped while waiting for Jetway"
            )
            return

        if not waitForActiveGate(2500):
            vLog(
                f"{handlerID} Stairs start cancelled - gate session stopped after Jetway wait"
            )
            return

        # Gate jump protection
        if myGen != stairsGeneration:
            vLog(
                f"{handlerID} OLD STAIRS TASK KILLED"
            )
            return

        stable = 0
        timeout = 0

        while timeout < 20:

            if not isGateSessionActive():
                vLog(
                    f"{handlerID} Stairs stopped - gate session inactive"
                )
                return

            # New gate jump detected
            if myGen != stairsGeneration:
                vLog(
                    f"{handlerID} TASK INVALIDATED"
                )
                return

            try:
                state = executeCalculatorCode(
                    "(L:FSDT_GSX_OPERATESTAIRS_STATE, Number)"
                )

                vLog(
                    f"{handlerID} STATE={state}"
                )

                # 5 = operating
                # 6 = connected
                if state >= 5:
                    vLog(
                        f"{handlerID} STAIRS already active"
                    )
                    return

                # 1 = request pending
                if state == 1:
                    stable += 1
                else:
                    stable = 0

                if stable >= 2:
                    break

            except Exception as e:
                vLog(
                    f"{handlerID} STAIRS STATE ERROR: {e}"
                )

            timeout += 1
            truewait(300)

        if timeout >= 20:
            vLog(
                f"{handlerID} TIMEOUT"
            )
            return

        if not waitForActiveGate(700):
            return

        if myGen != stairsGeneration or not isGateSessionActive():
            return

        if not acquireGSXMenuLock('Stairs', 30000):

            vLog(
                f"{handlerID} Stairs request skipped - GSX menu busy"
            )

            return

        oldRemoteControl = 0

        try:

            oldRemoteControl = getGSXRemoteControlState()

            vLog(
                f"{handlerID} GSX Remote Control old={oldRemoteControl}"
            )

            if not isGateSessionActive():
                return

            setGSXRemoteControlState(1)

            if not waitForActiveGate(300):
                return

            if not isGateSessionActive():
                return

            executeCalculatorCode(
                "1 (>L:FSDT_GSX_MENU_OPEN)"
            )

            if not waitForActiveGate(800):
                return

            if not isGateSessionActive():
                return

            executeCalculatorCode(
                "-2 (>L:FSDT_GSX_MENU_CHOICE)"
            )

            if not waitForActiveGate(400):
                return

            if not isGateSessionActive():
                return

            executeCalculatorCode(
                "6 (>L:FSDT_GSX_MENU_CHOICE)"
            )

            if not waitForActiveGate(400):
                return

            if not isGateSessionActive():
                return

            executeCalculatorCode(
                "0 (>L:FSDT_GSX_MENU_CHOICE)"
            )

            waitForActiveGate(700)

        finally:

            try:
                restoreGSXRemoteControlState(oldRemoteControl)
                forceGSXRemoteControlOff('after Stairs request')
            finally:
                releaseGSXMenuLock('Stairs')

        vLog(
            f"{handlerID} STAIRS request sent"
        )

    finally:
        stairsRunning = False


def hasJetwayAtCurrentGate():

    try:
        gate = getGate()
        return bool(getattr(gate, 'hasJetway', False))
    except:
        return False


def isJetwayConnectedOrComplete():

    if not hasJetwayAtCurrentGate():
        return True

    state = readGSXNumberLVar('FSDT_GSX_OPERATEJETWAYS_STATE', -1)

    return jetwayGSXConnectedObserved or isGSXServiceCompleted(state)


def isStairsConnectedOrComplete():

    state = readGSXNumberLVar('FSDT_GSX_OPERATESTAIRS_STATE', -1)

    return stairsGSXConnectedObserved or isGSXServiceCompleted(state)


def sendGSXJetwayAndStairsBundled(myGen, retryLabel='initial'):

    # One controlled GSX Remote-Control session:
    # 1) request Operate Jetways through GSX menu, so GSX owns recognition
    # 2) wait only a short time for the request callback/state 4/5
    # 3) request Stairs through GSX menu
    # 4) force Remote Control off
    #
    # We do NOT fake any GSX service state LVars.

    owner = f"GateServicesBundle-{retryLabel}"

    if not acquireGSXMenuLock(owner, 20000):

        jLog(
            f"Bundled gate-services request skipped - menu lock unavailable ({retryLabel})"
        )

        return False

    oldRemoteControl = 0
    sentSomething = False

    try:

        oldRemoteControl = getGSXRemoteControlState()

        jLog(
            f"Bundled GSX remote session START ({retryLabel}), oldRemote={oldRemoteControl}"
        )
        debugGateJetwaySnapshot(f"bundled remote start {retryLabel}")

        if not isGateSessionActive() or myGen != gateServicesBundleGeneration:
            return False

        setGSXRemoteControlState(1)

        if not waitForActiveGate(500):
            return False

        # --- Jetway first, but without waiting for full attach ---
        jetState = readGSXNumberLVar('FSDT_GSX_OPERATEJETWAYS_STATE', -1)

        if not isJetwayConnectedOrComplete() and not isGSXServiceBusy(jetState):

            executeCalculatorCode(
                "1 (>L:FSDT_GSX_MENU_OPEN)"
            )

            if not waitForActiveGate(1600):
                return sentSomething

            if not isGateSessionActive() or myGen != gateServicesBundleGeneration:
                return sentSomething

            executeCalculatorCode(
                "5 (>L:FSDT_GSX_MENU_CHOICE)"
            )

            sentSomething = True

            jLog(
                f"Bundled GSX MENU_CHOICE=5 sent for Operate Jetways ({retryLabel})"
            )
            debugGateJetwaySnapshot(f"after bundled Jetway choice 5 {retryLabel}")

            # Short gap only: wait until GSX has had a chance to register
            # onOperateJetwaysRequested/state 4/5, not until full physical attach.
            waited = 0
            while waited < 3500:

                if not isGateSessionActive() or myGen != gateServicesBundleGeneration:
                    return sentSomething

                jetState = readGSXNumberLVar('FSDT_GSX_OPERATEJETWAYS_STATE', -1)

                # Keep a small minimum gap so GSX can close/settle the Jetway menu
                # before the Stairs menu sequence starts. This replaces the old large
                # Jetway->Stairs gap with only ~2.5-3.5 seconds.
                if waited >= 2500 and (jetwayGSXRequestObserved or isGSXServiceBusy(jetState) or jetwayGSXConnectedObserved or isGSXServiceCompleted(jetState)):
                    break

                truewait(250)
                waited += 250

            jLog(
                f"Bundled Jetway short wait done ({retryLabel}): waited={waited}ms, state={readGSXNumberLVar('FSDT_GSX_OPERATEJETWAYS_STATE', -1)}, requestObserved={jetwayGSXRequestObserved}, connectedObserved={jetwayGSXConnectedObserved}"
            )

        else:

            jLog(
                f"Bundled Jetway request skipped ({retryLabel}) - already connected/operating state={jetState}, connectedObserved={jetwayGSXConnectedObserved}"
            )

        if not waitForActiveGate(700):
            return sentSomething

        if not isGateSessionActive() or myGen != gateServicesBundleGeneration:
            return sentSomething

        # --- Stairs second, in the same remote-control ownership window ---
        stairState = readGSXNumberLVar('FSDT_GSX_OPERATESTAIRS_STATE', -1)

        if not isStairsConnectedOrComplete() and not isGSXServiceBusy(stairState):

            executeCalculatorCode(
                "1 (>L:FSDT_GSX_MENU_OPEN)"
            )

            if not waitForActiveGate(900):
                return sentSomething

            if not isGateSessionActive() or myGen != gateServicesBundleGeneration:
                return sentSomething

            # Keep the working LOWW Stairs sequence, but run it after the Jetway
            # request and inside the same controlled Remote-Control session.
            executeCalculatorCode(
                "-2 (>L:FSDT_GSX_MENU_CHOICE)"
            )

            if not waitForActiveGate(300):
                return sentSomething

            executeCalculatorCode(
                "6 (>L:FSDT_GSX_MENU_CHOICE)"
            )

            sentSomething = True

            jLog(
                f"Bundled GSX MENU_CHOICE=6 sent for Operate Stairs ({retryLabel})"
            )
            debugGateJetwaySnapshot(f"after bundled Stairs choice 6 {retryLabel}")

            if not waitForActiveGate(400):
                return sentSomething

            executeCalculatorCode(
                "0 (>L:FSDT_GSX_MENU_CHOICE)"
            )

            jLog(
                f"Bundled GSX MENU_CHOICE=0 sent after Stairs ({retryLabel})"
            )

            waitForActiveGate(700)

        else:

            jLog(
                f"Bundled Stairs request skipped ({retryLabel}) - already connected/operating state={stairState}, connectedObserved={stairsGSXConnectedObserved}"
            )

        return sentSomething

    except Exception as e:

        jLog(
            f"Bundled GSX remote session failed ({retryLabel}): {e}"
        )
        debugGateJetwaySnapshot(f"bundled remote failed {retryLabel}")

        return sentSomething

    finally:

        # This automation owns the remote-control session. Always leave GSX menu
        # input under normal/user control afterwards. Do not restore oldRemote=1.
        try:
            forceGSXRemoteControlOff(f"after bundled gate services {retryLabel}")
            truewait(300)
            forceGSXRemoteControlOff(f"final remote reset after bundled gate services {retryLabel}")
        finally:
            releaseGSXMenuLock(owner)


def finalCheckGateServices(myGen, totalMs=110000):

    waited = 0
    lastLogSecond = -1
    retryDone = False

    while waited < totalMs:

        if not isGateSessionActive():

            jLog(
                "Bundled final check stopped - gate session inactive"
            )
            debugGateJetwaySnapshot("bundled final check inactive")
            return False

        if myGen != gateServicesBundleGeneration:

            jLog(
                f"Bundled final check invalidated myGen={myGen}, currentGen={gateServicesBundleGeneration}"
            )
            return False

        jetState = readGSXNumberLVar('FSDT_GSX_OPERATEJETWAYS_STATE', -1)
        stairState = readGSXNumberLVar('FSDT_GSX_OPERATESTAIRS_STATE', -1)

        jetwayDone = isJetwayConnectedOrComplete()
        stairsDone = isStairsConnectedOrComplete()

        second = int(waited / 1000)
        if second != lastLogSecond and (second % 5) == 0:

            jLog(
                f"Bundled FINAL CHECK t={second}s jetState={jetState}, stairState={stairState}, jetwayDone={jetwayDone}, stairsDone={stairsDone}, jetReq={jetwayGSXRequestObserved}, stairReq={stairsGSXRequestObserved}, remote={getGSXRemoteControlState()}"
            )
            lastLogSecond = second

        if jetwayDone and stairsDone:

            jLog(
                f"Bundled gate services confirmed: Jetway + Stairs done after {second}s"
            )
            debugGateJetwaySnapshot("bundled services confirmed")
            forceGSXRemoteControlOff('bundled services confirmed')
            return True

        # One gentle recovery: if one request was never even observed and the state is idle,
        # reopen a short controlled remote session. This is not status-faking, just another
        # official GSX menu request.
        if not retryDone and waited >= 20000:

            needJetwayRetry = hasJetwayAtCurrentGate() and (not jetwayDone) and (not jetwayGSXRequestObserved) and isGSXServiceRequestableIdle(jetState)
            needStairsRetry = (not stairsDone) and (not stairsGSXRequestObserved) and isGSXServiceRequestableIdle(stairState)

            if needJetwayRetry or needStairsRetry:

                retryDone = True

                jLog(
                    f"Bundled final check retry: needJetwayRetry={needJetwayRetry}, needStairsRetry={needStairsRetry}"
                )
                debugGateJetwaySnapshot("bundled final check before retry")

                sendGSXJetwayAndStairsBundled(myGen, 'retry')
                forceGSXRemoteControlOff('after bundled final check retry')

        truewait(1000)
        waited += 1000

    jLog(
        "Bundled gate services final check TIMEOUT"
    )
    debugGateJetwaySnapshot("bundled final check timeout")
    forceGSXRemoteControlOff('bundled final check timeout')

    return False


def autoConnectGateServicesBundled():

    global gateServicesBundleRunning
    global gateServicesBundleGeneration
    global jetwayRunning
    global stairsRunning
    global jetwayGSXRequestObserved
    global jetwayGSXConnectedObserved
    global jetwayGSXDisconnectedObserved
    global stairsGSXRequestObserved
    global stairsGSXConnectedObserved

    if not shouldRunHandler():

        jLog(
            "Bundled gate services skipped - handler inactive"
        )

        return

    if gateServicesBundleRunning:

        jLog(
            "Bundled gate services skipped - already running"
        )

        return

    gateServicesBundleRunning = True
    gateServicesBundleGeneration += 1
    myGen = gateServicesBundleGeneration

    jetwayRunning = True
    stairsRunning = True
    jetwayGSXRequestObserved = False
    jetwayGSXConnectedObserved = False
    jetwayGSXDisconnectedObserved = False
    stairsGSXRequestObserved = False
    stairsGSXConnectedObserved = False

    try:

        jLog(
            f"Bundled gate services ENTER gen={myGen}, gateSessionActive={gateSessionActive}, servicesStopRequested={servicesStopRequested}, gateChangeFlag={gateChangeFlag}"
        )
        debugGateJetwaySnapshot("bundled gate services enter")

        # Let GSX finish aircraftEngaged/profile/vehicle-model activation before
        # the handler sends any GSX menu choices. The gap between Jetway and Stairs
        # stays short; this is only a pre-service profile settle guard.
        if not waitForGSXProfileSettle():

            jLog(
                "Bundled gate services cancelled during GSX profile settle wait"
            )
            return

        sendGSXJetwayAndStairsBundled(myGen, 'initial')

        finalCheckGateServices(myGen, 110000)

    except Exception as e:

        print(
            f"{handlerID} BUNDLED GATE SERVICES CRASH: {e}"
        )
        debugGateJetwaySnapshot("bundled gate services crash")

    finally:

        try:
            forceGSXRemoteControlOff('bundled gate services exit')
        except:
            pass

        jLog(
            f"Bundled gate services EXIT gen={myGen}"
        )

        jetwayRunning = False
        stairsRunning = False
        gateServicesBundleRunning = False


def onEnterAirport(self):

    global currentAirport
    global handlerActive
    global abortCDM
    global varAutoStairs
    global gateChangeFlag
    global gateWakeupSent

    try:
        currentAirport = getAirport().icao
    except:
        currentAirport = ""

    if currentAirport != "LOWW":

        handlerActive = False
        abortCDM = True

        vLog(
            f"{handlerID} Handler inactive - airport is {currentAirport}"
        )

        return

    handlerActive = True
    abortCDM = False
    gateChangeFlag = False
    gateWakeupSent = False
    resetGSXVehicleSelectionReady()

    vLog(
        f"{handlerID} LOWW handler active"
    )

    # Do not overwrite gate.autoSelectOperator globally here.
    # Let the loaded LOWW GSX airport profile own operator and vehicle-layout selection.

    # onEnterAirport only activates LOWW.
    # Do NOT call setupAutomation() or promptVATSIMCID() here, because that can show popups during arrival/taxi-in.
    # Jetway, Stairs, CDM and all first-run prompts start only after GSX aircraftEngaged.


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
        vLog(f'{handlerID}Adding 24 hours to time to account for day rollover.')
        tgtInt = tgtInt + (24 * 3600)

    vLog(f'{handlerID}hhmmssToObj function variables:\nInput Time String: {hhmmss}\nCurrent IRL Time (int): {irlTimeInt}\nCurrent IRL Time (obj): {irlTimeObj}\nIRL Time Base (int): {irlIntBase}\nTarget Time (int): {tgtInt}\nTarget Time (obj): {time.gmtime(tgtInt)}')

    return time.gmtime(tgtInt)

# Technically this isn't necLOWWry but having it makes life easier
def splitTime(timeObj):
    return f'{timeObj[3]:02d}{timeObj[4]:02d}'

def compareTime(ttc, isGameTime):
    # ttc - Time to compare
    timeRef = 0
    timeRemainingH = 0
    timeRemainingM = 0

    if isGameTime:
        timeInt0AD = executeCalculatorCode('(E:ABSOLUTE TIME, seconds)') # Gets the absolute time in seconds since 1/1/1 AD

        timeRef = timeInt0AD - 62135596800 # - 62135596800 converts the time from seconds since 1/1/1 AD to seconds since 1/1/1970
        
    else:
        timeRef = time.time()

    ttcCompared = calendar.timegm(ttc) - timeRef

    # Converts seconds to HHMM. :02d formats it such that there is a leading zero if needed
    if ttcCompared > 0:
        timeRemainingH = int(ttcCompared // 3600)
        timeRemainingM = int((ttcCompared % 3600) // 60)

        if timeRemainingH > 0:
            ttcReturn = f'-{timeRemainingH}:{timeRemainingM:02d}' 
        else:
            ttcReturn = f'-{timeRemainingM:02d}'

    if ttcCompared < 0:
        timeRemainingH = int(-ttcCompared // 3600)
        timeRemainingM = int((-ttcCompared % 3600) // 60)

        if timeRemainingH > 0:
            ttcReturn = f'{timeRemainingH}:{timeRemainingM:02d}'
        else:
            ttcReturn = f'{timeRemainingM:02d}'

    if ttcCompared == 0:
        ttcReturn = '0'

    vLog(f'{handlerID}Time comparison function variables:\nTime to Compare: {ttc}\nIs Game Time: {isGameTime}\nReference Time: {timeRef}\nCompared Time (seconds): {ttcCompared}\nTime Remaining (H): {timeRemainingH}\nTime Remaining (M): {timeRemainingM}\nReturned TTD: {ttcReturn}')

    return ttcReturn

def getExternalSimbriefData():

    sbDataPresent = False
    sbTOBT = ''
    sbEoC = [0,0,0,0,0]
    sbTimeToEoC = ''
    sbCallsign = ''
    sbCallsignFull = ''
    sbRWY = ''
    sbSID = ''

    try:

        if not sb_username:

            return (
                False,
                '',
                '',
                [0,0,0,0,0],
                '',
                '',
                '',
                ''
            )

        sb = fetchJson(
            f"https://www.simbrief.com/api/xml.fetcher.php?username={sb_username}&json=1",
            timeout=10,
            etag=False
        )

        if not sb:

            return (
                False,
                '',
                '',
                [0,0,0,0,0],
                '',
                '',
                '',
                ''
            )

        sbAircraft = sb['aircraft']['icao_code']

        sbCallsignFull = sb['atc']['callsign']

        if len(sbCallsignFull) > 6:
            sbCallsign = sbCallsignFull[-4:]
        else:
            sbCallsign = sbCallsignFull

        sbRWY = sb['origin']['plan_rwy']

        route = sb['general']['route']

        routeParts = route.split(" ")

        if len(routeParts) > 0:

            if routeParts[0] == 'DCT':

                sbSID = 'NO SID'

            else:

                sbSID = routeParts[0]

        else:

            sbSID = ''

        schedOut = int(sb['times']['sched_out'])
        schedOff = int(sb['times']['sched_off'])

        sbTOBT = time.gmtime(schedOut)

        sbTaxiTime = getLOWWTaxiTime(
            sbRWY,
            15
        )

        sbEoC = time.gmtime(
            schedOut + (sbTaxiTime * 60)
        )

        vLog(
            f"{handlerID} SimBrief TTOT calculated: TOBT={splitTime(sbTOBT)}, RWY={sbRWY}, taxi={sbTaxiTime}, TTOT={splitTime(sbEoC)}"
        )

        sbTimeToEoC = compareTime(
            sbTOBT,
            False
        )
        sbDataPresent = True

        return (
            sbDataPresent,
            sbCallsign,
            sbTOBT,
            sbEoC,
            sbTimeToEoC,
            sbRWY,
            sbSID,
            sbAircraft
        )
        
    except Exception as e:

        print(
            f"{handlerID} External SimBrief error: {e}"
        )

        return (
            sbDataPresent,
            sbCallsign,
            sbTOBT,
            sbEoC,
            sbTimeToEoC,
            sbRWY,
            sbSID,
            sbAircraft
        )
    
def getSimbriefData():
    sbDataPresent = False
    sbTOBT = ''
    sbEoC = [0,0,0,0,0]
    sbTimeToEoC = ''
    sbCallsign = ''
    sbCallsignFull = ''
    sbRWY = ''
    sbSID = ''
    sb = getSimbrief()

    if sb:
        if sb.last_error:
            print(f'{handlerID}Simbrief Error: {sb.last_error}')
        else:
            sbCallsignFull = sb.callsign
            # Prevents 7 character long callsigns from causing issues
            if len(sbCallsignFull) > 6:
                sbCallsign = sbCallsignFull[-4:]
            else:
                sbCallsign = sbCallsignFull

            sbTOBT = sb.sched_out
            sbEoC = time.gmtime(calendar.timegm(sb.sched_off) + 600)
            sbTimeToEoC = compareTime(sb.sched_off, True)
            sbRWY = sb.plan_rwy
            sbSID = sb.sid_ident

            sbDataPresent = True

    vLog(f'{handlerID}Simbrief function variable log:\nSimbrief Data Present: {sbDataPresent}\nCallsign: {sbCallsignFull} shortened to {sbCallsign}\n\nTOBT: {sbTOBT}\nEoC: {sbEoC}\nTime to EoC: {sbTimeToEoC}\nRunway: {sbRWY}\nSID: {sbSID}')

    return sbDataPresent, sbCallsign, sbTOBT, sbEoC, sbTimeToEoC, sbRWY, sbSID

def testVATSIM(cid):
    VATSIMApiReturn = fetchJson('https://data.vatsim.net/v3/vatsim-data.json', 10, True)
    vtDataPresent = False
    vtCallsignFull = ''
    vtCallsign = ''
    vtICAO = ''
    airportOnline = False

    if VATSIMApiReturn == None:
        print(f'{handlerID}VATSIM datafile returned no data.')
                                         

    else:
        for pilot in VATSIMApiReturn['pilots']:
            if str(cid) != '0' and pilot['cid'] == int(cid):
                vtCallsignFull = pilot['callsign']
                if len(vtCallsignFull) > 6:
                    vtCallsign = vtCallsignFull[-4:]
                else:
                    vtCallsign = vtCallsignFull
                vtICAO = pilot['flight_plan']['aircraft_short']
                vtDataPresent = True

        for controller in VATSIMApiReturn["controllers"]:
            if controller['callsign'] in airportATC:
                airportOnline = True

        for atis in VATSIMApiReturn["atis"]:
            if atis['callsign'] in airportATC:
                airportOnline = True
                 

    vLog(f'{handlerID}VATSIM function variable log:\nVATSIM API Data Present: {vtDataPresent}\nESSA Online on VATSIM: {airportOnline}\nCallsign: {vtCallsignFull} shortened to {vtCallsign}\nAircraft ICAO: {vtICAO}')

    return vtDataPresent, vtCallsignFull, vtICAO, airportOnline, vtCallsign                                           

def getCDM(callsign):
    CDMEoC = [0,0,0,0,0]
    CDMTimeToEoC = ''
    CDMTOBT = ''
    CDMTSAT = ''
    CDMisCtot = False
    CDMDepInfo = ''
    CDMRWY = ''
    CDMSID = ''
    CDMAPIOffline = False
    CDMHasEOBT = False

    CDMAPIReturn = fetchJson(
        f'https://cdm-server-production.up.railway.app/ifps/callsign?callsign={callsign}',
        timeout=10,
        etag=True
    )

    if CDMAPIReturn == None:

        print(f'{handlerID}CDM API returned no data.')

        CDMAPIOffline = True

    else:

        cdmData = CDMAPIReturn.get('cdmData', {})

        # A filed EOBT alone is NOT enough for VATSIM/CDM mode.
        # When ATC deletes the TOBT, the API can still keep the EOBT/flightplan.
        # In that case the handler must ignore CDM/VATSIM timing and fall back to SimBrief.
        hasFiledEOBT = (CDMAPIReturn.get('eobt', '') != '')

        # Prefer only an active pilot/ATC TOBT source.
        # IMPORTANT: do NOT fall back to eobt here, otherwise a deleted VATSIM TOBT
        # would still be displayed as if CDM timing was valid.
        cdmTOBTString = (
            cdmData.get('reqTobt', '') or
            CDMAPIReturn.get('reqTobt', '') or
            CDMAPIReturn.get('tobt', '') or
            cdmData.get('tobt', '')
        )

        if not hasFiledEOBT:

            vLog(
                f"{handlerID} CDM ignored: no EOBT filed for {callsign}"
            )

        elif cdmTOBTString == '':

            vLog(
                f"{handlerID} CDM ignored: no active TOBT for {callsign}, using SimBrief fallback"
            )

        else:

            CDMHasEOBT = True

            CDMTOBT = hhmmssToObj(cdmTOBTString)


            if cdmData.get('tsat', '') == '':

                CDMTSAT = CDMTOBT

            else:

                CDMTSAT = hhmmssToObj(cdmData.get('tsat', ''))


            # RWY/SID must be known BEFORE calculating a fallback CTOT.
            # If CDM depInfo is missing, use SimBrief RWY/SID only for RWY/SID,
            # but keep the VATSIM/CDM TOBT for the CTOT calculation.
            if cdmData.get('depInfo', '') != '':

                CDMDepInfo = cdmData.get('depInfo', '').split('/')

                CDMRWY = CDMDepInfo[0]

                if len(CDMDepInfo) > 1:

                    if len(CDMDepInfo[1]) > 6:

                        CDMSID = f'{CDMDepInfo[1][0:4]}{CDMDepInfo[1][-2:]}'

                    else:

                        CDMSID = CDMDepInfo[1]

            else:

                vGetSB = getExternalSimbriefData()

                if vGetSB[0]:

                    CDMRWY = vGetSB[5]

                    CDMSID = vGetSB[6]


            # CTOT/TTOT = expected takeoff time.
            # Only display CTOT when a real CTOT/TTOT value is provided by VATSIM/CDM.
            # If no real CTOT exists, calculate a TTOT fallback.
            # IMPORTANT: If VATSIM/CDM TOBT exists, TTOT fallback uses VATSIM/CDM TOBT + LOWW taxi time, not SimBrief TOBT.
            cdmCTOTString = (
                cdmData.get('ctot', '') or
                CDMAPIReturn.get('ctot', '') or
                cdmData.get('ttot', '') or
                CDMAPIReturn.get('ttot', '')
            )

            if cdmCTOTString == '':

                fallbackTaxi = getLOWWTaxiTime(
                    CDMRWY,
                    CDMAPIReturn.get('taxi', 15)
                )

                CDMEoC = time.gmtime(
                    calendar.timegm(CDMTOBT) + (fallbackTaxi * 60)
                )

                # No real CTOT from VATSIM/CDM: display as TTOT.
                CDMisCtot = False

                vLog(
                    f"{handlerID} CDM CTOT missing, calculated TTOT from VATSIM TOBT + LOWW taxi: TOBT={splitTime(CDMTOBT)}, RWY={CDMRWY}, taxi={fallbackTaxi}, TTOT={splitTime(CDMEoC)}"
                )

            else:

                CDMEoC = hhmmssToObj(cdmCTOTString)

                # Real CTOT/TTOT value received from VATSIM/CDM: display as CTOT.
                CDMisCtot = True


            # Red countdown is ALWAYS time until TOBT, not CTOT/TTOT.
            CDMTimeToEoC = compareTime(CDMTOBT, False)


    return (
        CDMEoC,
        CDMTimeToEoC,
        CDMTOBT,
        CDMTSAT,
        CDMRWY,
        CDMSID,
        CDMisCtot,
        CDMAPIOffline,
        CDMHasEOBT
    )

def writeInitialVDGSFast():

    global lastVDGSData
    global lastSID
    global lastTOBT

    try:

        # Give GSX one very short moment after aircraftEngaged, but do not wait for
        # Jetway state changes. The VDGS must show our handler data immediately,
        # not only after the jetway starts moving.
        if not waitForActiveGate(1000):
            return False

        if not shouldRunHandler() or abortCDM or gateChangeFlag or servicesStopRequested:

            vLog(
                f"{handlerID} Fast VDGS initial write skipped - no active gate session"
            )

            return False

        vGetSB = getExternalSimbriefData()

        if vGetSB[0] == True:

            setVDGS(
                vGetSB[2],
                vGetSB[2],
                False,
                vGetSB[3],
                vGetSB[4],
                vGetSB[6],
                vGetSB[5],
                vGetSB[7],
                'SIMBRF'
            )

            lastVDGSData = (
                f"{vGetSB[2]}|"
                f"{vGetSB[4]}|"
                f"{vGetSB[5]}|"
                f"{vGetSB[6]}"
            )

            lastSID = vGetSB[6]
            lastTOBT = vGetSB[2]

            vLog(
                f"{handlerID} Fast initial VDGS write done with SimBrief data"
            )

            return True

        vLog(
            f"{handlerID} Fast initial VDGS write skipped - no SimBrief data"
        )

        return False

    except Exception as e:

        print(
            f"{handlerID} Fast initial VDGS write error: {e}"
        )

        return False


def CDMHandlerHub():
    global abortCDM
    global lastSID
    global lastTOBT
    global lastCDMSID
    global lastCDMTOBT
    global lastVDGSData
    global showChockandGate
    global showPaxCargoFuel
    global cdmRefreshIntervalMs

    if not shouldRunHandler():
        vLog(
            f"{handlerID} CDM skipped - handler inactive"
        )
        return

    if abortCDM:
        vLog(
            f"{handlerID} CDM ABORTED BEFORE START"
        )
        return

    varVATSIMCID = getVATSIMCIDForUse()

    vLog(
        f'{handlerID}VATSIM CID used for handler: {varVATSIMCID}. Global persistent variable return: {getGlobalPersistentVariable("vatsim_cid")}'
    )

    # Fast first write: do not wait up to 20+ seconds for the jetway/GSX ready check.
    # The normal VATSIM/CDM cycle below can still update/replace this afterwards.
    writeInitialVDGSFast()

    if abortCDM:
        vLog(
            f"{handlerID} CDM ABORTED"
        )
        return

    while True:

        if not shouldRunHandler():
            vLog(
                f"{handlerID} CDM LOOP STOPPED - handler inactive"
            )
            return

        if abortCDM or servicesStopRequested:
            vLog(
                f"{handlerID} CDM LOOP STOPPED - abort/departure requested"
            )
            return

        vLog(
            f'{handlerID}Starting handler cycle'
        )

        varVATSIMCID = getVATSIMCIDForUse()

        if str(varVATSIMCID) == '0':

            vTestVATSIM = (False, '', '', False, '')

        else:

            try:

                vTestVATSIM = testVATSIM(varVATSIMCID)

            except Exception as e:

                print(
                    f"{handlerID} VATSIM check failed, using SimBrief fallback: {e}"
                )

                vTestVATSIM = (False, '', '', False, '')

        if abortCDM or servicesStopRequested:
            vLog(
                f"{handlerID} CDM LOOP STOPPED BEFORE API - abort/departure requested"
            )
            return

        vGetSB = getExternalSimbriefData()

        if abortCDM or servicesStopRequested:
            vLog(
                f"{handlerID} CDM LOOP STOPPED AFTER SimBrief - abort/departure requested"
            )
            return

        vLog(
            f'{handlerID}VATSIM Data Present: {vTestVATSIM[0]}, Airport online on VATSIM: {vTestVATSIM[3]}, Simbrief Data Present: {vGetSB[0]}'
        )

        if vTestVATSIM[0] == True:

            vGetCDM = getCDM(vTestVATSIM[1])

            if (vGetCDM[7] == True) or (vGetCDM[8] == False):

                vLog(
                    f'{handlerID}CDM unavailable or no active TOBT, using SimBrief data as fallback.'
                )

                if vGetSB[0] == True:

                    # Reset CDM change detection while we are in SimBrief fallback.
                    # If a VATSIM TOBT is entered again later, it will be treated as fresh data.
                    lastCDMSID = ''
                    lastCDMTOBT = ''

                    setVDGS(
                        vGetSB[2],
                        vGetSB[2],
                        False,
                        vGetSB[3],
                        vGetSB[4],
                        vGetSB[6],
                        vGetSB[5],
                        vGetSB[7],
                        'SIMBRF'
                    )

            else:

                # Always refresh VDGS with current VATSIM/CDM values.
                # vGetCDM[6] decides label: True = real CTOT, False = calculated TTOT fallback.
                setVDGS(
                    vGetCDM[2],
                    vGetCDM[3],
                    vGetCDM[6],
                    vGetCDM[0],
                    vGetCDM[1],
                    vGetCDM[5],
                    vGetCDM[4],
                    vTestVATSIM[2],
                    'VATSIM'
                )

                currentCDMSID = vGetCDM[5]
                currentCDMTOBT = splitTime(vGetCDM[2])

                if lastCDMSID == '':

                    lastCDMSID = currentCDMSID

                elif currentCDMSID != lastCDMSID:

                    addVdgsMessage({
                        "id": "vatsim_update_sid",
                        "display": {
                            "wide": {
                                "pages": [
                                    {
                                        "lines": [
                                            "UPDATED",
                                            "SID",
                                            "",
                                            currentCDMSID,
                                            ""
                                        ],
                                        "duration": 10000
                                    }
                                ]
                            }
                        }
                    })

                    lastCDMSID = currentCDMSID


                if lastCDMTOBT == '':

                    lastCDMTOBT = currentCDMTOBT

                elif currentCDMTOBT != lastCDMTOBT:

                    addVdgsMessage({
                        "id": "vatsim_update_tobt",
                        "display": {
                            "wide": {
                                "pages": [
                                    {
                                        "lines": [
                                            "UPDATED",
                                            "TOBT",
                                            "",
                                            currentCDMTOBT,
                                            ""
                                        ],
                                        "duration": 10000
                                    }
                                ]
                            }
                        }
                    })

                    lastCDMTOBT = currentCDMTOBT

        else:

            if vGetSB[0] == True:

                newVDGSData = (
                    f"{vGetSB[2]}|"
                    f"{vGetSB[4]}|"
                    f"{vGetSB[5]}|"
                    f"{vGetSB[6]}"
                )

                if newVDGSData != lastVDGSData:

                    lastVDGSData = newVDGSData

                    setVDGS(
                        vGetSB[2],
                        vGetSB[2],
                        False,
                        vGetSB[3],
                        vGetSB[4],
                        vGetSB[6],
                        vGetSB[5],
                        vGetSB[7],
                        'SIMBRF'
                    )

                    if lastSID == '':

                        lastSID = vGetSB[6]

                    elif vGetSB[6] != lastSID:

                        addVdgsMessage({
                            "id": "simbrief_update_sid",
                            "display": {
                                "wide": {
                                    "pages": [
                                        {
                                            "lines": [
                                                "UPDATED",
                                                "SID",
                                                "",
                                                vGetSB[6],
                                                ""
                                            ],
                                            "duration": 5000
                                        }
                                    ]
                                }
                            }
                        })

                        lastSID = vGetSB[6]


                    if lastTOBT == '':

                        lastTOBT = vGetSB[2]

                    elif vGetSB[2] != lastTOBT:

                        addVdgsMessage({
                            "id": "simbrief_update_tobt",
                            "display": {
                                "wide": {
                                    "pages": [
                                        {
                                            "lines": [
                                                "UPDATED",
                                                "TOBT",
                                                "",
                                                splitTime(vGetSB[2]),
                                                ""
                                            ],
                                            "duration": 5000
                                        }
                                    ]
                                }
                            }
                        })

                        lastTOBT = vGetSB[2]

                else:

                    vLog(
                        f"{handlerID} VDGS unchanged"
                    )

        if showChockandGate and showPaxCargoFuel:
            waitMs = cdmRefreshIntervalMs + 16000

        elif showPaxCargoFuel:
            waitMs = cdmRefreshIntervalMs + 12000

        elif showChockandGate:
            waitMs = cdmRefreshIntervalMs + 4000

        else:
            waitMs = cdmRefreshIntervalMs

        if not waitForVDGSCountdownAndCDMSafe(waitMs):
            vLog(
                f"{handlerID} CDM LOOP STOPPED DURING WAIT"
            )
            return


def setVDGS(TOBT, TSAT, isCTOT, EoCVar, TimeToEoC, SID, RWY, AircraftType, dataType):
    global showChockandGate, showPaxCargoFuel, showDataSource
    global lastVDGSPayload
    global lastVDGSCountdown
    global vdgsCountdownRunning
    global gsxMenuOperationRunning
    global jetwayGSXRequestObserved
    global jetwayGSXConnectedObserved
    global jetwayGSXDisconnectedObserved
    global stairsGSXRequestObserved
    global stairsGSXConnectedObserved

    # Store the real time objects before formatting them to HHMM strings.
    # The VDGS red countdown is static text, so it must be refreshed locally
    # without doing a full SimBrief/VATSIM/CDM API cycle every time.
    lastVDGSPayload = (
        TOBT,
        TSAT,
        isCTOT,
        EoCVar,
        SID,
        RWY,
        AircraftType,
        dataType
    )

    lastVDGSCountdown = TimeToEoC

    # Start a lightweight countdown ticker independent from the heavy API loop.
    # The red VDGS countdown is rendered as static text, so it must be re-written
    # periodically even when SimBrief/VATSIM/CDM data itself did not change.
    try:
        if (not vdgsCountdownRunning) and (not abortCDM) and (not servicesStopRequested) and shouldRunHandler():
            runAsync(vdgsCountdownLoop)
    except Exception as e:
        vLog(
            f"{handlerID} VDGS countdown ticker start failed: {e}"
        )

    if not showDataSource:
        dataType = ''

    TOBT = splitTime(TOBT)
    TSAT = splitTime(TSAT)
    EoCVar = splitTime(EoCVar)

    if isCTOT:
        EoC = 'CTOT'
    else:
        EoC = 'TTOT'

    vLog(
        f'{handlerID}Data received by setVDGS():\nTOBT: {TOBT}\nTSAT: {TSAT}\nETD or CTOT Type: {EoC}\nEoC Time: {EoCVar}\nTime to EoC: {TimeToEoC}\nSID: {SID}\nRWY: {RWY}\nData Type (VATSIM or SIMBRF): {dataType}'
    )

    addVdgsMessage({
        "id": "flight_information",
        "display": {
            "wide": {
                "pages": [
                    {"lines": [
                        "${airline}${flight_number}",
                        AircraftType,
                        "",
                        "TOBT",
                        TOBT,
                        {
                            "red": TimeToEoC
                        },
                        dataType
                    ], "duration": vdgsDuration},
                    {"lines": [
                        "${airline}${flight_number}",
                        AircraftType,
                        "",
                        EoC,
                        EoCVar,
                        {
                            "red": TimeToEoC
                        },
                        "",
                        dataType
                    ], "duration": vdgsDuration},
                    {"lines": [
                        "${airline}${flight_number}",
                        AircraftType,
                        "",
                        SID,
                        f"RWY {RWY}",
                        {
                            "red": TimeToEoC
                        },
                        dataType
                    ], "duration": vdgsDuration},
                ]
            }
        }
    })

    if not showChockandGate:
        addVdgsMessage({
            "id": "chock_and_gate_display",
            "display": {
                "wide": {
                    "pages": [
                        {"lines": [
                            ''
                        ], "duration": 0}
                    ]
                }
            }
        })

    if not showPaxCargoFuel:
        addVdgsMessage({
            "id": "passenger_cargo_info",
            "display": {
                "wide": {
                    "pages": [
                        {"lines": [
                            ''
                        ], "duration": 0}
                    ]
                }
            }
        })


def resetVDGSChangeDetection():

    global lastVDGSData
    global lastSID
    global lastTOBT
    global lastCDMSID
    global lastCDMTOBT
    global lastVDGSPayload
    global lastVDGSCountdown

    lastVDGSData = ''
    lastSID = ''
    lastTOBT = ''
    lastCDMSID = ''
    lastCDMTOBT = ''
    lastVDGSPayload = None
    lastVDGSCountdown = ''

    vLog(
        f"{handlerID} VDGS change detection reset after gatejump"
    )


def forceWriteVDGSOnceAfterGateJump(attempt):

    vLog(
        f"{handlerID} Gatejump VDGS force attempt {attempt}"
    )

    # Try to make sure the new parking service/VDGS is alive.
    try:
        state = executeCalculatorCode(
            "(L:FSDT_GSX_OPERATEJETWAYS_STATE, Number)"
        )

        vLog(
            f"{handlerID} Gatejump VDGS GSX ready state={state}"
        )

    except Exception as e:
        vLog(
            f"{handlerID} Gatejump VDGS ready state failed: {e}"
        )


    resetVDGSChangeDetection()

    varVATSIMCID = getVATSIMCIDForUse()

    if str(varVATSIMCID) == '0':

        vTestVATSIM = (False, '', '', False, '')

    else:

        try:

            vTestVATSIM = testVATSIM(varVATSIMCID)

        except Exception as e:

            print(
                f"{handlerID} Gatejump VATSIM check failed, using SimBrief fallback: {e}"
            )

            vTestVATSIM = (False, '', '', False, '')


    vGetSB = getExternalSimbriefData()

    vLog(
        f"{handlerID} Gatejump VDGS force data: VATSIM={vTestVATSIM[0]}, SimBrief={vGetSB[0]}"
    )


    if vTestVATSIM[0] == True:

        try:

            vGetCDM = getCDM(vTestVATSIM[1])

            if (vGetCDM[7] == False) and (vGetCDM[8] == True):

                setVDGS(
                    vGetCDM[2],
                    vGetCDM[3],
                    vGetCDM[6],
                    vGetCDM[0],
                    vGetCDM[1],
                    vGetCDM[5],
                    vGetCDM[4],
                    vTestVATSIM[2],
                    'VATSIM'
                )

                vLog(
                    f"{handlerID} Gatejump VDGS forced with VATSIM/CDM data"
                )

                return True

        except Exception as e:

            print(
                f"{handlerID} Gatejump CDM force failed: {e}"
            )


    if vGetSB[0] == True:

        try:

            setVDGS(
                vGetSB[2],
                vGetSB[2],
                False,
                vGetSB[3],
                vGetSB[4],
                vGetSB[6],
                vGetSB[5],
                vGetSB[7],
                'SIMBRF'
            )

            vLog(
                f"{handlerID} Gatejump VDGS forced with SimBrief data"
            )

            return True

        except Exception as e:

            print(
                f"{handlerID} Gatejump SimBrief VDGS force failed: {e}"
            )


    print(
        f"{handlerID} Gatejump VDGS force attempt {attempt} failed: no usable data"
    )

    return False


def refreshVDGSAfterGateJumpOnly():

    global gateJumpVDGSRefreshRunning
    global handlerCycleRunning
    global abortCDM

    if gateJumpVDGSRefreshRunning:

        vLog(
            f"{handlerID} Gatejump VDGS refresh skipped - already running"
        )

        return

    gateJumpVDGSRefreshRunning = True

    try:

        # DO NOT touch Jetway/Stairs here.
        # GSX often creates the new parking VDGS several seconds after onAircraftEngaged.
        # Therefore use several delayed attempts instead of one single write.
        delays = [8000, 7000, 7000, 10000]

        attempt = 0

        for delay in delays:

            truewait(delay)

            attempt += 1

            if not shouldRunHandler():

                vLog(
                    f"{handlerID} Gatejump VDGS refresh stopped - handler inactive"
                )

                return

            if attempt == 1:

                vLog(
                    f"{handlerID} Gatejump reloadSimbrief started"
                )

                try:

                    sbReload = reloadSimbrief()

                    if sbReload:

                        vLog(
                            f"{handlerID} Gatejump reloadSimbrief successful"
                        )

                    else:

                        print(
                            f"{handlerID} Gatejump reloadSimbrief returned None"
                        )

                except Exception as e:

                    print(
                        f"{handlerID} Gatejump reloadSimbrief error: {e}"
                    )


            # Release a stale sleeping handler lock before the force write.
            if handlerCycleRunning and attempt >= 2:

                vLog(
                    f"{handlerID} Gatejump VDGS forcing stale handler lock reset"
                )

                handlerCycleRunning = False

            abortCDM = False

            success = forceWriteVDGSOnceAfterGateJump(attempt)

            # Also restart the normal loop after each force write so future updates keep working.
            if not handlerCycleRunning:

                runAsync(handlerCycleLock)

            # Do at least two attempts even if the first one claims success,
            # because the first write can hit the old/vanishing VDGS after a gatejump.
            if success and attempt >= 2:

                vLog(
                    f"{handlerID} Gatejump VDGS refresh completed"
                )

                return


        print(
            f"{handlerID} Gatejump VDGS refresh finished without confirmed success"
        )

    finally:

        gateJumpVDGSRefreshRunning = False



def handlerCycleLock():

    global handlerCycleRunning

    if not shouldRunHandler():
        vLog(
            f"{handlerID} handlerCycleLock skipped - handler inactive"
        )
        return

    vLog(f"{handlerID} handlerCycleLock ENTER")
    vLog(f"{handlerID} running={handlerCycleRunning}")

    if handlerCycleRunning:
        vLog(
            f"{handlerID} ABORT already running"
        )
        return

    handlerCycleRunning = True

    vLog(
        f"{handlerID} SET TRUE"
    )

    try:
        vLog(
            f"{handlerID} Starting CDMHandlerHub()"
        )

        if gateChangeFlag:
            vLog(
                f"{handlerID} CDM BLOCKED DURING GATE CHANGE"
            )
        else:
            CDMHandlerHub()

    except Exception as e:
        print(
            f"{handlerID} HANDLER CRASH: {e}"
        )

    finally:
        handlerCycleRunning = False

        vLog(
            f"{handlerID} RESET LOCK"
        )

def onExitedAirport(self):

    global currentAirport
    global handlerActive
    global abortCDM
    global gateChangeFlag
    global gateWakeupSent
    global stairsGeneration
    global jetwayGeneration
    global gateServiceStartRequested
    global gateSessionActive
    global servicesStopRequested
    global jetwayGSXRequestObserved
    global jetwayGSXConnectedObserved
    global jetwayGSXDisconnectedObserved
    global stairsGSXRequestObserved
    global stairsGSXConnectedObserved

    exitedAirport = currentAirport
					   
				 
					   

    if exitedAirport != "LOWW":

        vLog(
            f"{handlerID} Exit ignored - airport was {exitedAirport}"
        )

        currentAirport = ""

        return

    handlerActive = False
    abortCDM = True
    gateChangeFlag = True
    gateWakeupSent = False
    stairsGeneration += 1
    jetwayGeneration += 1
    gateServiceStartRequested = False
    gateSessionActive = False
    servicesStopRequested = True
    currentAirport = ""

    vLog(
        f"{handlerID} LOWW handler inactive - exited LOWW"
    )


def onAircraftDisengaged(self):

    callSuperIfPresent(self, 'onAircraftDisengaged')

    # Some GSX parking/assistance transitions can fire aircraftDisengaged-like
    # callbacks while Departure is still AVAILABLE. Do not kill the gate session
    # in that case, or Jetway/Stairs recognition can be aborted mid-operation.
    depState = readGSXNumberLVar('FSDT_GSX_DEPARTURE_STATE', 1)

    if depState >= 4:

        hardStopServices(f'aircraft disengaged with departure state {depState}')

    else:

        jLog(
            f"aircraft disengaged ignored for service automation; departure state={depState}"
        )
        debugGateJetwaySnapshot("aircraft disengaged ignored")


def onDepartureRequested(self):

    callSuperIfPresent(self, 'onDepartureRequested')

    hardStopServices('departure requested')


def onAirportDepartureRequested(self):

    hardStopServices('airport departure requested')



def onFilterModels(self, couatlType, modelParams):

    # v5.1 LOWW guard:
    # In rare sessions GSX has reported no model for Pushback/Water/Lavatory at LOWW
    # with an extremely small parkingRadius. Do not force any specific model and do
    # not bypass operator scoring. Only lift the radius parameter to a conservative
    # minimum before GSX evaluates model conditions, for the three affected utility
    # service types.

    result = None

    try:
        result = callSuperIfPresent(self, 'onFilterModels', couatlType, modelParams)
    except:
        result = None

    try:
        if not shouldRunHandler():
            return result

        vehicleType = str(couatlType)

        if vehicleType not in ['Pushback', 'WaterTruck', 'LavatoryTruck']:
            return result

        radius = 0.0

        try:
            radius = float(modelParams.get('parkingRadius', 0.0))
        except:
            radius = 0.0

        if radius <= 0.0 or radius >= 14.0:
            return result

        merged = {}

        if isinstance(result, dict):
            merged.update(result)

        params = {}

        if isinstance(merged.get('params'), dict):
            params.update(merged.get('params'))

        params['parkingRadius'] = 14.0
        merged['params'] = params

        vLog(f"{handlerID} LOWW model filter radius guard: {vehicleType} parkingRadius {radius} -> 14.0")

        return merged

    except Exception as e:
        vLog(f"{handlerID} LOWW model filter radius guard failed: {e}")

    return result



def onVehicleMaterialized(self, *args):

    callSuperIfPresent(self, 'onVehicleMaterialized', *args)

    vehicleType = ''

    if len(args) > 0:
        vehicleType = str(args[0]).upper()

    # Do not hard-stop on PushBack vehicle materialization alone.
    # GSX can materialize/prepare tug objects during parking/assistance setup,
    # which previously killed the gate session and aborted Jetway/Stairs.
    if 'PUSH' in vehicleType:
        jLog(
            f"PushBack vehicle materialized observed but not used as hard-stop: {vehicleType}"
        )


def onAirportVehicleMaterialized(self, *args):

    vehicleType = ''

    if len(args) > 0:
        vehicleType = str(args[0]).upper()

    if 'PUSH' in vehicleType:
        jLog(
            f"Airport PushBack vehicle materialized observed but not used as hard-stop: {vehicleType}"
        )


def onGateReset(self, *args):

    callSuperIfPresent(self, 'onGateReset', *args)

    reason = ''

    if len(args) > 0:
        reason = str(args[0]).lower()

    if reason in ['taxied_away', 'user_changed', 'user_revoked', 'airport_exit', 'reposition', 'pushback', 'departure']:
        hardStopServices(f'gate reset: {reason}')


def onAirportGateReset(self, *args):

    reason = ''

    if len(args) > 0:
        reason = str(args[0]).lower()

    if reason in ['taxied_away', 'user_changed', 'user_revoked', 'airport_exit', 'reposition', 'pushback', 'departure']:
        hardStopServices(f'airport gate reset: {reason}')


def onExitAirport(self):

    onExitedAirport(self)


def getStoredAutomationStateForGate():

    global varAutoStairs
    global automationSetupDone

    try:

        storedAuto = getGlobalPersistentVariable(
            'loww_automation_enabled'
        )

    except Exception as e:

        vLog(
            f"{handlerID} Automation persistent read failed: {e}"
        )

        storedAuto = None


    if storedAuto != None and storedAuto != '' and storedAuto != '<ASK>':

        varAutoStairs = str(storedAuto).strip()
        automationSetupDone = True

        return varAutoStairs


    if userVarAutoStairs != '<ASK>':

        setGlobalPersistentVariable(
            'loww_automation_enabled',
            userVarAutoStairs
        )

        varAutoStairs = userVarAutoStairs
        automationSetupDone = True

        return varAutoStairs


    varAutoStairs = None

    return None


def startAutoServicesAfterConsent(reason):

    global gateServiceStartRequested
    global varAutoStairs

    if gateServiceStartRequested:

        vLog(
            f"{handlerID} Auto services start skipped - already requested for this gate"
        )

        return

    gateServiceStartRequested = True

    try:

        # Give the GSX popup/UI one short moment to close before sending service commands.
        if not waitForActiveGate(1000):
            vLog(
                f"{handlerID} Auto services start cancelled during popup close wait"
            )
            return

        if not shouldRunHandler() or gateChangeFlag or servicesStopRequested:

            vLog(
                f"{handlerID} Auto services start cancelled - no active gate session"
            )

            return

        if str(varAutoStairs).strip() != '1':

            vLog(
                f"{handlerID} Auto services not started - automation state={varAutoStairs}"
            )

            return

        print(
            f"{handlerID} AUTO SERVICES ENABLED - waiting for GSX profile settle, then bundled Remote session: Jetway first, short wait, Stairs, final check ({reason})"
        )

        # v4.9: profile settle guard, then one controlled GSX Remote-Control session.
        # Jetway is requested through the official GSX Operate Jetways path, then
        # after a short recognition wait Stairs are requested. Remote Control is
        # forced off afterwards and a final watchdog checks both callbacks/states.
        runAsync(autoConnectGateServicesBundled)

    except Exception as e:

        print(
            f"{handlerID} AUTO SERVICES start error: {e}"
        )


def promptVATSIMCIDAfterDelay(delayMs):

    if not waitForActiveGate(delayMs, 500):
        return

    if not shouldRunHandler() or gateChangeFlag or servicesStopRequested:

        vLog(
            f"{handlerID} VATSIM CID prompt skipped - no active gate session"
        )

        return

    promptVATSIMCID()


def promptVATSIMCIDAfterAutoServices():

    promptVATSIMCIDAfterDelay(30000)


def promptVATSIMCIDAfterNoServices():

    promptVATSIMCIDAfterDelay(3000)


def startAutoServicesFromStoredPreference():

    startAutoServicesAfterConsent('stored preference')


def startAutoServicesFromPopupYes():

    startAutoServicesAfterConsent('popup YES')


def promptAutomationAtGateThenMaybeStart():

    global gateSetupPromptRunning
    global varAutoStairs
    global automationSetupDone

    if gateSetupPromptRunning:

        vLog(
            f"{handlerID} Automation popup skipped - already running"
        )

        return

    gateSetupPromptRunning = True

    try:

        if not shouldRunHandler() or gateChangeFlag:

            vLog(
                f"{handlerID} Automation popup skipped - no active gate session"
            )

            return

        # Re-check before showing the popup. Another handler cycle may have saved it already.
        storedAuto = getStoredAutomationStateForGate()

        if str(storedAuto).strip() == '1':

            runAsync(startAutoServicesFromStoredPreference)
            runAsync(promptVATSIMCIDAfterAutoServices)

            return

        if str(storedAuto).strip() == '0':

            print(
                f"{handlerID} AUTO SERVICES DISABLED"
            )

            runAsync(promptVATSIMCIDAfterNoServices)

            return


        choice = choiceBox(
            "Enable GSX Automation (Jetway/Stairs)?\n\n"
            "YES = Enable permanently and start now\n"
            "NO = Disable permanently\n"
            "LATER = Do not start now, ask again next time\n\n"
            ">>> IMPORTANT <<<\n"
            "Automation will only run after you explicitly select YES.\n"
            "If you select NO or LATER, this handler will not touch Jetway/Stairs.\n\n"
            "CDM / SimBrief / VDGS will continue either way.",
            "Gaya Simulations LOWW v2 GSX Profile",
            ["YES", "NO", "LATER"],
            default=0,
        )

        choiceText = str(choice).strip().upper()

        if choice == 0 or choiceText == 'YES':

            setGlobalPersistentVariable(
                'loww_automation_enabled',
                '1'
            )

            varAutoStairs = '1'
            automationSetupDone = True

            print(
                f"{handlerID} AUTO SERVICES preference saved: ENABLED - starting now"
            )

            runAsync(startAutoServicesFromPopupYes)

            # Do not let the VATSIM CID popup block the fresh Jetway/Stairs start.
            runAsync(promptVATSIMCIDAfterAutoServices)

        elif choice == 1 or choiceText == 'NO':

            setGlobalPersistentVariable(
                'loww_automation_enabled',
                '0'
            )

            varAutoStairs = '0'
            automationSetupDone = True

            print(
                f"{handlerID} AUTO SERVICES preference saved: DISABLED"
            )

            runAsync(promptVATSIMCIDAfterNoServices)

        else:

            # LATER means no consent for this gate session.
            # Therefore do NOT start Jetway/Stairs now and do NOT save a preference.
            varAutoStairs = None

            print(
                f"{handlerID} AUTO SERVICES postponed - not started for this gate"
            )

            runAsync(promptVATSIMCIDAfterNoServices)

    except Exception as e:

        print(
            f"{handlerID} Automation popup error: {e}"
        )

        runAsync(promptVATSIMCIDAfterNoServices)

    finally:

        gateSetupPromptRunning = False



# ============================================================
# Jetway/Stairs recognition callbacks
# Jetway automation now requests the official GSX Operate Jetways service path.
# These callbacks are used to confirm GSX recognition; states are never faked.
# ============================================================
def onOperateJetwaysRequested(self, *args):

    global jetwayGSXRequestObserved

    callSuperIfPresent(self, 'onOperateJetwaysRequested', *args)

    jetwayGSXRequestObserved = True

    jLog(
        f"CALLBACK onOperateJetwaysRequested args=[{debugArgs(args)}]"
    )
    debugGateJetwaySnapshot("callback onOperateJetwaysRequested")


def onAirportOperateJetwaysRequested(self, *args):

    global jetwayGSXRequestObserved

    jetwayGSXRequestObserved = True

    jLog(
        f"CALLBACK onAirportOperateJetwaysRequested args=[{debugArgs(args)}]"
    )
    debugGateJetwaySnapshot("callback onAirportOperateJetwaysRequested")


def onJetwayConnected(self, *args):

    global jetwayGSXConnectedObserved

    callSuperIfPresent(self, 'onJetwayConnected', *args)

    jetwayGSXConnectedObserved = True

    jLog(
        f"CALLBACK onJetwayConnected args=[{debugArgs(args)}]"
    )
    debugGateJetwaySnapshot("callback onJetwayConnected")


def onAirportJetwayConnected(self, *args):

    global jetwayGSXConnectedObserved

    jetwayGSXConnectedObserved = True

    jLog(
        f"CALLBACK onAirportJetwayConnected args=[{debugArgs(args)}]"
    )
    debugGateJetwaySnapshot("callback onAirportJetwayConnected")


def onJetwayDisconnected(self, *args):

    global jetwayGSXConnectedObserved
    global jetwayGSXDisconnectedObserved

    callSuperIfPresent(self, 'onJetwayDisconnected', *args)

    jetwayGSXConnectedObserved = False
    jetwayGSXDisconnectedObserved = True

    jLog(
        f"CALLBACK onJetwayDisconnected args=[{debugArgs(args)}]"
    )
    debugGateJetwaySnapshot("callback onJetwayDisconnected")


def onAirportJetwayDisconnected(self, *args):

    global jetwayGSXConnectedObserved
    global jetwayGSXDisconnectedObserved

    jetwayGSXConnectedObserved = False
    jetwayGSXDisconnectedObserved = True

    jLog(
        f"CALLBACK onAirportJetwayDisconnected args=[{debugArgs(args)}]"
    )
    debugGateJetwaySnapshot("callback onAirportJetwayDisconnected")


def onOperateStairsRequested(self, *args):

    global stairsGSXRequestObserved

    callSuperIfPresent(self, 'onOperateStairsRequested', *args)

    stairsGSXRequestObserved = True

    jLog(
        f"CALLBACK onOperateStairsRequested args=[{debugArgs(args)}]"
    )
    debugGateJetwaySnapshot("callback onOperateStairsRequested")


def onAirportOperateStairsRequested(self, *args):

    global stairsGSXRequestObserved

    stairsGSXRequestObserved = True

    jLog(
        f"CALLBACK onAirportOperateStairsRequested args=[{debugArgs(args)}]"
    )
    debugGateJetwaySnapshot("callback onAirportOperateStairsRequested")


def onAirportBeforeVehicleSelect(self, *args):

    # Official GSX readiness point for airport handlers: gate is available and
    # GSX is about to select operators/vehicles. Do not change profile vehicle
    # layout here; just mark the automation-safe point.

    try:
        callSuperIfPresent(self, 'onAirportBeforeVehicleSelect', *args)
    except:
        pass

    markGSXVehicleSelectionReady('onAirportBeforeVehicleSelect')


def onStairsConnected(self, *args):

    global stairsGSXConnectedObserved

    callSuperIfPresent(self, 'onStairsConnected', *args)

    stairsGSXConnectedObserved = True

    jLog(
        f"CALLBACK onStairsConnected args=[{debugArgs(args)}]"
    )
    debugGateJetwaySnapshot("callback onStairsConnected")


def onAirportStairsConnected(self, *args):

    global stairsGSXConnectedObserved

    stairsGSXConnectedObserved = True

    jLog(
        f"CALLBACK onAirportStairsConnected args=[{debugArgs(args)}]"
    )
    debugGateJetwaySnapshot("callback onAirportStairsConnected")

def onAircraftEngaged(self):

    global gateWakeupSent
    global gateChangeFlag
    global varAutoStairs
    global abortCDM
    global handlerCycleRunning
    global currentAirport
    global handlerActive
    global gateServiceStartRequested
    global gateSessionActive
    global servicesStopRequested
    global jetwayGSXRequestObserved
    global jetwayGSXConnectedObserved
    global jetwayGSXDisconnectedObserved
    global stairsGSXRequestObserved
    global stairsGSXConnectedObserved

    try:
        currentAirport = getAirport().icao
    except:
        pass

    if currentAirport == "LOWW":
        handlerActive = True

    if not shouldRunHandler():
        vLog(
            f"{handlerID} SKIP AIRCRAFT ENGAGED - handler inactive"
        )
        return

    gateServiceStartRequested = False
    servicesStopRequested = False
    gateSessionActive = True
    jetwayGSXRequestObserved = False
    jetwayGSXConnectedObserved = False
    jetwayGSXDisconnectedObserved = False
    stairsGSXRequestObserved = False
    stairsGSXConnectedObserved = False
    resetGSXVehicleSelectionReady()

    # A new gate session must always force a fresh VDGS write.
    # Otherwise the script can think the data is unchanged while the new VDGS is still empty/default.
    resetVDGSChangeDetection()

    vLog(
        f"{handlerID} aircraft engaged"
    )

    if gateChangeFlag:

        vLog(
            f"{handlerID} GATE CHANGE RE-ENGAGE - waiting for old CDM loop to stop"
        )

        # Keep abort active while the old CDM loop exits.
        # Do NOT clear abortCDM before the old loop has had a chance to see it.
        abortCDM = True

        waitLoops = 0

        while handlerCycleRunning and waitLoops < 20:

            truewait(250)

            waitLoops += 1

        if handlerCycleRunning:

            vLog(
                f"{handlerID} OLD CDM LOOP STILL RUNNING - forcing restart lock reset"
            )

            handlerCycleRunning = False

        gateChangeFlag = False
        gateWakeupSent = False

        vLog(
            f"{handlerID} WAKEUP RESET"
        )

        runAsync(refreshVDGSAfterGateJumpOnly)

    # Now start the new gate session.
    abortCDM = False

    runAsync(handlerCycleLock)

    # Automation is consent-based:
    # - saved 1: start immediately
    # - saved 0: never start
    # - no saved setting: ask at the gate; only YES starts services
    storedAuto = getStoredAutomationStateForGate()

    vLog(
        f"{handlerID} RUNTIME AUTO={storedAuto}"
    )

    if str(storedAuto).strip() == '1':

        runAsync(startAutoServicesFromStoredPreference)

        runAsync(promptVATSIMCIDAfterAutoServices)

    elif str(storedAuto).strip() == '0':

        print(
            f"{handlerID} AUTO SERVICES DISABLED"
        )

        runAsync(promptVATSIMCIDAfterNoServices)

    else:

        runAsync(promptAutomationAtGateThenMaybeStart)

# GSX 4.x Handler Guide: do not start tasklets at module load.
# Airport activation is handled by onEnterAirport(); gate services start from onAircraftEngaged().
# runAsync(startup) intentionally disabled.
