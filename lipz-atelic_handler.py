msfs_mode = 1


AIRPORT_ICAO = "LIPZ"
SCENERY_TITLE = "Atelic LIPZ Venice Marco Polo Airport"

_AIRLINE_TO_HANDLER = {
	"MAC": "VENEZIA",
	"AEA": "VENEZIA",
	"AFR": "VENEZIA",
	"HOP": "VENEZIA",
	"ASL": "VENEZIA",
	"BEL": "VENEZIA",
	"CFG": "VENEZIA",
	"CTN": "VENEZIA",
	"DAL": "VENEZIA",
	"EZY": "VENEZIA",
	"EJU": "VENEZIA",
	"EZS": "VENEZIA",
	"UAE": "VENEZIA",
	"EWG": "VENEZIA",
	"EWE": "VENEZIA",
	"ITY": "VENEZIA",
	"EXS": "VENEZIA",
	"KLM": "VENEZIA",
	"NOS": "VENEZIA",
	"RAM": "VENEZIA",
	"RYR": "VENEZIA",
	"RUK": "VENEZIA",
	"RYS": "VENEZIA",
	"MAY": "VENEZIA",
	"LDM": "VENEZIA",
	"SXS": "VENEZIA",
	"SWT": "VENEZIA",
	"TCX": "VENEZIA",
	"TVS": "VENEZIA",
	"TAR": "VENEZIA",
	"UAL": "VENEZIA",
	"VOE": "VENEZIA",
	"AEE": "AVIATIONSERVICES",
	"EIN": "AVIATIONSERVICES",
	"BTI": "AVIATIONSERVICES",
	"ACA": "AVIATIONSERVICES",
	"DLA": "AVIATIONSERVICES",
	"ANE": "AVIATIONSERVICES",
	"TSC": "AVIATIONSERVICES",
	"LAV": "AVIATIONSERVICES",
	"AAL": "AVIATIONSERVICES",
	"AUA": "AVIATIONSERVICES",
	"BAW": "AVIATIONSERVICES",
	"BCS": "AVIATIONSERVICES",
	"ELY": "AVIATIONSERVICES",
	"ENT": "AVIATIONSERVICES",
	"FIN": "AVIATIONSERVICES",
	"HYM": "AVIATIONSERVICES",
	"HYE": "AVIATIONSERVICES",
	"IBE": "AVIATIONSERVICES",
	"LOT": "AVIATIONSERVICES",
	"DLH": "AVIATIONSERVICES",
	"CLH": "AVIATIONSERVICES",
	"VIM": "AVIATIONSERVICES",
	"LGL": "AVIATIONSERVICES",
	"ICE": "AVIATIONSERVICES",
	"CYP": "AVIATIONSERVICES",
	"PGT": "AVIATIONSERVICES",
	"NAX": "AVIATIONSERVICES",
	"NOZ": "AVIATIONSERVICES",
	"NSZ": "AVIATIONSERVICES",
	"MSR": "AVIATIONSERVICES",
	"CCA": "AVIATIONSERVICES",
	"CES": "AVIATIONSERVICES",
	"QTR": "AVIATIONSERVICES",
	"TVF": "AVIATIONSERVICES",
	"THY": "AVIATIONSERVICES",
	"WZZ": "AVIATIONSERVICES",
	"WMT": "AVIATIONSERVICES",
	"VLG": "AVIATIONSERVICES",
	"SWR": "AVIATIONSERVICES",
	"TAP": "AVIATIONSERVICES",
	"SAS": "AVIATIONSERVICES",
}
_FALLBACK_HANDLERS = "VENEZIA,AVIATIONSERVICES"

_CATERING_BY_AIRLINE = {}
_CATERING_FALLBACK = "DNATA,GGOURMET"

_FUELING_BY_AIRLINE = {}
_FUELING_FALLBACK = ""

AIRPORT_VEHICLE_PREFERENCES = {
	"BaggageTractor": {
		"prefer_title_contains": ["TLD"],
		"boost": 50,
	},
}
HANDLER_VEHICLE_PREFERENCES = {}
AIRLINE_VEHICLE_PREFERENCES = {}

_AUTO_SELECT_OPERATOR_ON_MATCH = True

_AUTO_SELECT_ON_SINGLE_OPERATOR = False

_MAX_WAGONS_BY_TYPE = {}

_LOW_COST_WALK_IN_STANDS = {
	323: {
		"enter": (45.505799447472434, 12.341799890661237, -0.008000000000000002),
		"waypoints": [
			(45.50593797149139, 12.34189498433262, -0.012000000000000002),
			(45.50591839426089, 12.341802030369976, -0.012000000000000002),
			(45.50590082914295, 12.341776067626778, -0.012000000000000002),
			(45.50584327701153, 12.341753849250104, -0.012000000000000002),
			(45.505798623700116, 12.341768676427996, -0.008000000000000002),
		],
	},
	324: {
		"enter": (45.50513273497747, 12.341847504888797, -0.008000000000000002),
		"waypoints": [
			(45.505242633473244, 12.342091356687648, -0.008000000000000002),
			(45.505215328411126, 12.341974388498505, -0.008000000000000002),
			(45.50524582178619, 12.341814641016864, -0.012000000000000002),
			(45.50517736745826, 12.341800220923705, -0.012000000000000002),
			(45.50513182341175, 12.34181444734037, -0.012000000000000002),
		],
	},
	329: {
		"enter": (45.50291774114447, 12.341150143001173, -0.008000000000000002),
		"waypoints": [
			(45.50293329059021, 12.341430600417642, -0.008000000000000002),
			(45.502934082280774, 12.341368310828287, -0.008000000000000002),
			(45.50284831369166, 12.341259225484704, -0.008000000000000002),
		],
	},
	330: {
		"enter": (45.50291774114447, 12.341150143001173, -0.008000000000000002),
		"waypoints": [
			(45.50289810380847, 12.341486050913856, -0.008000000000000002),
			(45.50293329059021, 12.341430600417642, -0.008000000000000002),
			(45.502934082280774, 12.341368310828287, -0.008000000000000002),
			(45.50284831369166, 12.341259225484704, -0.008000000000000002),
		],
	},
}

_LOW_COST_AIRLINES = (
	"RYR", "RUK", "RYS", "MAY", "LDM", "EZY",
	"EJU", "EZS", "WZZ", "WMT", "VOE", "VLG",
	"TVF", "EWG", "EWE", "PGT", "NAX", "NOZ",
	"NSZ", "EXS", "SXS", "MAC", "HYM", "HYE",
)

_LOW_COST_VERBOSE = False


_PKEY_MODE = "rwprofiles_handling_mode"
_cached_mode = None


_airport_confirmed = False


def _is_this_airport():
	global _airport_confirmed

	if _airport_confirmed:
		return True

	a = getAirport()
	if a is None:
		return True

	if getattr(a, "icao", None) == AIRPORT_ICAO:
		_airport_confirmed = True
		return True

	return False


def _get_icao_airline_from_simbrief():
	sb = getSimbrief()
	if not sb:
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
		"This profile can automatically select the ground handling, catering\n"
		"and fueling company based on your airline.\n\n"
		"WHICH METHOD WOULD YOU LIKE TO USE?\n\n"
		"AUTOMATIC (SIMBRIEF):\n"
		"- Reads your SimBrief airline ICAO code\n"
		"- Auto-selects the correct company at this airport\n"
		"- Skips the operator picker when a single operator matches\n"
		"- If there’s no match, GSX will show the operator list\n\n"
		"MANUAL (OPERATOR LIST):\n"
		"- GSX always shows the operator list\n"
		"- You choose the company each time\n\n"
		"Your choice is remembered for future visits to all RW GSX Profiles\n"
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


def _resolve_catering_for_airline(icao):
	if icao and icao in _CATERING_BY_AIRLINE:
		return _CATERING_BY_AIRLINE[icao]
	return _CATERING_FALLBACK


def _resolve_fueling_for_airline(icao):
	if icao and icao in _FUELING_BY_AIRLINE:
		return _FUELING_BY_AIRLINE[icao]
	return _FUELING_FALLBACK


def _pick_textures():
	_ensure_user_mode_choice()

	if _cached_mode == "manual":
		return _FALLBACK_HANDLERS, _CATERING_FALLBACK, _FUELING_FALLBACK, None

	icao = _resolve_airline_icao()
	handling_texture = _resolve_handler_for_airline(icao)
	catering_texture = _resolve_catering_for_airline(icao)
	fueling_texture = _resolve_fueling_for_airline(icao)

	return handling_texture, catering_texture, fueling_texture, icao


def _apply_auto_select_operator(gate, icao, textures):

	if not _AUTO_SELECT_OPERATOR_ON_MATCH:
		return None

	def _single(v):

		return bool(v) and ("," not in str(v))

	configured = [v for v in textures if v]

	matched = bool(
		icao
		and (
			icao in _AIRLINE_TO_HANDLER
			or icao in _CATERING_BY_AIRLINE
			or icao in _FUELING_BY_AIRLINE
		)
	)

	if not matched and _AUTO_SELECT_ON_SINGLE_OPERATOR:
		matched = True

	skip = bool(
		_cached_mode == "auto"
		and matched
		and configured
		and all(_single(v) for v in configured)
	)

	try:
		gate.autoSelectOperator = skip
	except Exception:
		return None

	return skip


def _apply_operators():
	gate = getGate()
	if not gate:
		return

	handling_texture, catering_texture, fueling_texture, icao = _pick_textures()

	if handling_texture:
		gate.handlingTexture = handling_texture
	if catering_texture:
		gate.cateringTexture = catering_texture
	if fueling_texture:
		try:
			gate.fuelTruckTexture = fueling_texture
		except Exception:
			pass

	skip_picker = _apply_auto_select_operator(
		gate, icao, (handling_texture, catering_texture, fueling_texture))

	print("%s: mode=%s airline=%s handling=%s catering=%s fueling=%s autoselect=%s" % (
		AIRPORT_ICAO,
		_cached_mode,
		icao or "None",
		handling_texture,
		catering_texture,
		fueling_texture,
		skip_picker
	))


def getMaxWagons(self):
	if _MAX_WAGONS_BY_TYPE:
		try:
			icao = str(aircraft.icaoType or "").strip().upper()
		except Exception:
			icao = ""

		wagons = _MAX_WAGONS_BY_TYPE.get(icao)
		if wagons:
			return wagons

	return self._super_getMaxWagons()


def _stand_number(gate):
	for attr in ("bglNameNumber", "number"):
		try:
			value = getattr(gate, attr, None)
		except Exception:
			continue
		if value in (None, ""):
			continue
		digits = "".join(c for c in str(value) if c.isdigit())
		if digits:
			return int(digits)

	for attr in ("uiGateName", "shortName", "uiName", "name"):
		try:
			value = getattr(gate, attr, None)
		except Exception:
			continue
		if not value:
			continue
		tail = str(value).upper().split("|")[-1]
		for token in tail.replace("-", " ").split():
			if token.isdigit():
				return int(token)

	return None


def _apply_low_cost_boarding():
	gate = getGate()
	if not gate:
		return

	number = _stand_number(gate)
	stand = _LOW_COST_WALK_IN_STANDS.get(number)
	if not stand:
		if _LOW_COST_VERBOSE:
			print("%s: stand %s is not a low-cost walk-in stand" % (
				AIRPORT_ICAO, number))
		return

	icao = _resolve_airline_icao()
	if not icao or icao not in _LOW_COST_AIRLINES:
		return

	applied = []
	for name, value in (
			("passengerEnterGatePos", stand["enter"]),
			("passengerWaypoints", stand["waypoints"]),
			("noPassengerBus", True),
			("noPassengerBus_deboarding", True),
			("hasJetway", 0)):
		try:
			gate.__setattr__(name, value)
			applied.append(name)
		except Exception as e:
			print("%s: could not set %s on stand %s (%r)" % (
				AIRPORT_ICAO, name, number, e))

	print("%s: stand %s - low-cost walk-in boarding for %s (%d/5 applied)" % (
		AIRPORT_ICAO, number, icao, len(applied)))


def onAirportBeforeVehicleSelect(self):
	if not _is_this_airport():
		return
	_apply_operators()
	_apply_low_cost_boarding()


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
			AIRPORT_VEHICLE_PREFERENCES.get("*", None)
		))
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
