msfs_mode = 1

# ============================================================
# EDIT THIS PER AIRPORT
# ============================================================

AIRPORT_ICAO = "KDEN"
SCENERY_TITLE = "X-Codr Designs KDEN Denver International Airport"

# Handling operator selection (SimBrief ICAO airline -> GSX operator code)
_AIRLINE_TO_HANDLER = {
	"FFT": "FFT",
	"DAL": "DL",
	"UAL": "UA",
	"AAL": "AA",
	"SWA": "WN_WHITE",
	"DLH": "WFS",
	

}

# If no match is found, allow GSX to pick from these (comma-separated list is valid)
_FALLBACK_HANDLERS = "FFT,DL,UA,AA,WN_WHITE,MENZ,SWISSPORT,JBU,WFS,"

# Catering operator selection (SimBrief ICAO airline -> GSX catering operator)
_CATERING_BY_AIRLINE = {
	"SWA": "SWA",
	"UAL": "GGOURMET",
	"DAL": "LSG",
	"FFT": "LSG",
	"JBU": "LSG",
	"AMX": "LSG",
	"DLH": "LSG",

}

# If no match is found, allow GSX to pick from these (comma-separated list is valid)
_CATERING_FALLBACK = "LSG"


# Airlines (SimBrief ICAO code) for which GSX's PIGS should be disabled.
_DISABLE_PIGS_FOR_AIRLINES = {
	"FFT",
}


# Vehicle preferences (per-airport)
# Add more blocks per vehicleType if you needed (e.g. "Pushback", "FollowMe", etc.)
AIRPORT_VEHICLE_PREFERENCES = {
}


# Aviramp
def isAvirampGate():
	gate = getGate()

	return gate and getattr(gate, "aviramp", False)


def setupAvirampGate(self):
	if isAvirampGate():
		disableExit(EXIT_PASSENGERS, 3)
		self.aviramp = True
		self.avirampExits = [0]
	else:
		self.aviramp = None
		self.avirampExits = None


# ============================================================
# SHARED CODE (DON'T TOUCH)
# ============================================================

_PKEY_MODE = "imranasyraff_handling_mode"
_cached_mode = None


def _is_this_airport():
	a = getAirport()
	return bool(a and getattr(a, "icao", None) == AIRPORT_ICAO)


def _get_icao_airline_from_simbrief():
	sb = getSimbrief()
	if not sb:
		return None
	if getattr(sb, "last_error", None):
		return None
	code = getattr(sb, "icao_airline", None)
	if not code:
		return None
	return str(code).strip().upper()


def _ensure_user_mode_choice():
	global _cached_mode

	if _cached_mode in ("auto", "manual"):
		return

	mode = getGlobalPersistentVariable(_PKEY_MODE, None)
	if mode in ("auto", "manual"):
		_cached_mode = mode
		return

	result = choiceBox(
		"WELCOME TO %s!\n\n"
		"NEW FEATURE:\n"
		"This profile can automatically select the ground handling and catering\n"
		"company based on your airline.\n\n"
		"WHICH METHOD WOULD YOU LIKE TO USE?\n\n"
		"AUTOMATIC (SIMBRIEF):\n"
		"- Reads your SimBrief airline ICAO code\n"
		"- Auto-selects the correct company at this airport\n"
		"- If there’s no match, GSX will show the operator list\n\n"
		"MANUAL (OPERATOR LIST):\n"
		"- GSX always shows the operator list\n"
		"- You choose the company each time\n\n"
		"Your choice is remembered for future visits\n"
		"with this feature." % SCENERY_TITLE,
		"%s - GSX Profile" % SCENERY_TITLE,
		["AUTOMATIC (RECOMMENDED)", "MANUAL"],
		default=0,
	)

	if result is None:
		_cached_mode = "auto"
		return

	_cached_mode = "auto" if result == 0 else "manual"
	setGlobalPersistentVariable(_PKEY_MODE, _cached_mode)


def _resolve_airline_icao():
	icao = _get_icao_airline_from_simbrief()
	if not icao:
		icao = getattr(aircraft, "icaoAirline", None)
		if icao:
			icao = str(icao).strip().upper()
	return icao


def _resolve_handler_for_airline(icao):
	if icao and icao in _AIRLINE_TO_HANDLER:
		return _AIRLINE_TO_HANDLER[icao]
	return _FALLBACK_HANDLERS


def _pick_textures():
	_ensure_user_mode_choice()

	# Manual mode: never auto-assign anything, always let GSX ask.
	if _cached_mode == "manual":
		return None, None, None

	icao = _resolve_airline_icao()

	# No airline match -> return None instead of the fallback list, so
	# _apply_operators() below leaves the gate untouched and GSX prompts
	# you with its own operator selection menu instead of silently
	# resolving one from the fallback list on its own.
	handling_texture = _AIRLINE_TO_HANDLER.get(icao) if icao else None
	catering_texture = _CATERING_BY_AIRLINE.get(icao) if icao else None

	return handling_texture, catering_texture, icao


# Tracks whether the auto operator selection has already been applied for
# the CURRENT arrival. Without this, onAirportBeforeVehicleSelect re-applies
# the SimBrief-matched operator every time it fires (which can be more than
# once per flight), silently overwriting any manual re-selection you make
# in the GSX menu in between. Reset on onExitAirport so the next arrival
# gets a fresh auto-pick.
_operators_applied = [False]


def _apply_operators():
	if _operators_applied[0]:
		return

	gate = getGate()
	if not gate:
		return

	handling_texture, catering_texture, icao = _pick_textures()

	if handling_texture:
		gate.handlingTexture = handling_texture
	if catering_texture:
		gate.cateringTexture = catering_texture

	_operators_applied[0] = True

	print("%s: mode=%s airline=%s handling=%s catering=%s" % (
		AIRPORT_ICAO,
		_cached_mode,
		icao or "None",
		handling_texture or "None (GSX will prompt - fallback list: %s)" % _FALLBACK_HANDLERS,
		catering_texture or "None (GSX will prompt - fallback list: %s)" % _CATERING_FALLBACK
	))


def _apply_gate_distance_threshold():
	if _GATE_DISTANCE_THRESHOLD_METERS is None:
		return

	gate = getGate()
	if not gate:
		return

	try:
		d = Distance.fromMeters(_GATE_DISTANCE_THRESHOLD_METERS)
	except Exception:
		return

	try:
		gate.__setattr__("gateDistanceThreshold", d)
	except Exception:
		pass


def onAirportBeforeVehicleSelect(self):
	if not _is_this_airport():
		return
	_apply_operators()
	setupAvirampGate(self)
	_apply_gate_distance_threshold()


def onExitAirport(self):
	# Reset so the next arrival at KDEN asks/auto-picks fresh, instead of
	# carrying over this arrival's applied-flag (and skipping the auto-pick).
	_operators_applied[0] = False


# ------------------------------------------------------------------
# Force the rear door shut if it gets opened anyway.
#
# disableExit(EXIT_PASSENGERS, 3) (in setupAvirampGate above) only stops
# GSX's own equipment (stairs/aviramp/jetway) from using the rear exit -
# it does NOT stop the aircraft itself from opening that door as part of
# its own automatic door-open logic when boarding/deboarding starts.
# Since front-only stairs/aviramp are already working correctly, this
# just watches the rear exit for a short window after boarding is
# called and toggles it back closed if it opens.
# ------------------------------------------------------------------

_REAR_DOOR_WATCH_HANDLE = [None]


def _close_rear_door_if_open():
	try:
		rear_exits = aircraft.exits.get(EXIT_PASSENGERS, [])
	except Exception:
		return

	if len(rear_exits) <= 3:
		return

	rear = rear_exits[3]
	if rear and getattr(rear, "doorState", 0):
		try:
			executeCalculatorCode(rear.toggle)
		except Exception:
			pass


def _watch_rear_door():
	# ~60 seconds of polling is plenty to catch the aircraft's automatic
	# door-open sequence without running forever.
	for _ in range(60):
		wait(1000)
		if not _is_this_airport() or not isAvirampGate():
			return
		_close_rear_door_if_open()


def _start_rear_door_watch():
	if not _is_this_airport() or not isAvirampGate():
		return
	cancelAsync(_REAR_DOOR_WATCH_HANDLE[0])
	_REAR_DOOR_WATCH_HANDLE[0] = runAsync(_watch_rear_door)


def onAirportBoardingRequested(self):
	_start_rear_door_watch()


def onAirportDeboardingRequested(self):
	_start_rear_door_watch()


# ------------------------------------------------------------------
# Disable PIGS for specific airlines.
#
# Note this overrides onStairsConnected, NOT onAirportStairsConnected.
# The onAirport* companion just runs alongside the aircraft handler's
# method and can't stop it from doing anything - but airport handler
# overrides of the plain method name sit on top of every aircraft
# handler tier and fully replace it. The built-in onStairsConnected is
# what creates PIGS objects when stairs connect, so skipping it here
# for a given airline is what turns PIGS off for that airline. Every
# other airline falls through to the original (saved as
# self._super_onStairsConnected) so PIGS keeps working normally.
# ------------------------------------------------------------------

def onStairsConnected(self, stairInstances):
	if _is_this_airport():
		icao = _resolve_airline_icao()
		if icao in _DISABLE_PIGS_FOR_AIRLINES:
			print("%s: PIGS disabled for airline %s" % (AIRPORT_ICAO, icao))
			return

	original = getattr(self, "_super_onStairsConnected", None)
	if original:
		original(stairInstances)


def _normalize_pref_list(pref_block):
	if not pref_block:
		return []

	if isinstance(pref_block, list):
		return pref_block

	if isinstance(pref_block, dict):
		return [pref_block]

	return []


def _collect_preferences(vehicleType, icao, handler_code):
	prefs = []

	try:
		prefs.extend(_normalize_pref_list(
			AIRPORT_VEHICLE_PREFERENCES.get(vehicleType, None)
		))
	except Exception:
		pass

	try:
		handler_block = HANDLER_VEHICLE_PREFERENCES.get(handler_code, None) if handler_code else None
		if handler_block:
			prefs.extend(_normalize_pref_list(
				handler_block.get(vehicleType, None)
			))
	except Exception:
		pass

	try:
		airline_block = AIRLINE_VEHICLE_PREFERENCES.get(icao, None) if icao else None
		if airline_block:
			prefs.extend(_normalize_pref_list(
				airline_block.get(vehicleType, None)
			))
	except Exception:
		pass

	return prefs

def onAirportVehicleCandidatesScored(self, vehicleType, candidates):
	if not _is_this_airport():
		return

	icao = _resolve_airline_icao()
	if icao:
		icao = str(icao).strip().upper()

	handler_code = _resolve_handler_for_airline(icao)

	prefs = _collect_preferences(vehicleType, icao, handler_code)
	if not prefs:
		return

	for c in candidates:
		try:
			title = str(getattr(c, "title", "") or "")
		except Exception:
			title = ""

		try:
			texture = str(getattr(c, "texture", "") or "")
		except Exception:
			texture = ""

		for pref in prefs:
			title_needles = pref.get("prefer_title_contains", [])
			texture_needles = pref.get("prefer_texture_contains", [])
			boost = pref.get("boost", 0)

			if not boost or (not title_needles and not texture_needles):
				continue

			matched = False

			for needle in title_needles:
				if needle and needle in title:
					matched = True
					break

			if not matched:
				for needle in texture_needles:
					if needle and needle in texture:
						matched = True
						break

			if matched:
				c.boostScore(boost)
