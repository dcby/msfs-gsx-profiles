msfs_mode = 1
version = "1.5.0"

HANDLERS = {
    "AEE": "LSAS",
    "EIN": "WAS",
    "ABY": "WAS",
    "BTI": "WAS",
    "CCA": "LSAS",
    "AFR": "WAS",
    "AUA": "WAS",
    "BAW": "WAS",
    "BEL": "WAS",
    "CAI": "LSAS",
    "UAE": "WAS",
    "ENT": "LSAS",
    "ETH": "LSAS",
    "ETD": "WAS",
    "EWG": "WAS",
    "FIN": "WAS",
    "FDB": "LSAS",
    "KLM": "WAS",
    "LOT": "LSAS",
    "DLH": "WAS",
    "NOS": "LSAS",
    "NOZ": "WAS",
    "NSZ": "WAS",
    "PGT": "LSAS",
    "QTR": "LSAS",
    "RYR": "FR_ASP",
    "RYS": "FR_ASP",
    "LDA": "FR_ASP",
    "MAY": "FR_ASP",
    "SAS": "WAS",
    "SWU": "LSAS",
    "SEH": "LSAS",
    "TVS": "WAS",
    "TVL": "WAS",
    "TVP": "WAS",
    "TVQ": "WAS",
    "ELY": "WAS",
    "SXS": "WAS",
    "SWR": "WAS",
    "TAP": "LSAS",
    "THY": "LSAS",
    "WZZ": "WAS",
    "WMT": "WAS",
    "WUK": "WAS"
}

FALLBACKS = "FR_ASP,LSAS,WAS"

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

    gate.handlingTexture = handler
    gate.cateringTexture = "DOCO,FERIER,POLTRANS"
    gate.fuelTruckTexture = "ORLEN"

def onAirportBeforeVehicleSelect(self):
    apply_handler()

def onVehicleCandidatesScored(self, vehicleType, candidates):
    if vehicleType not in ["Staircase", "BaggageTractor", "BaggageLoader", "PassengerBus"]:
        return

    if vehicleType == "Staircase":
        for c in candidates:
            if 'CDS' in c.title and '2445' in c.title:
                c.boostScore(10)
            if 'FW2458PE' in c.title:
                c.boostScore(-10)
    if vehicleType == "BaggageTractor":
        for c in candidates:
            if 'TLD_JET_16' in c.title or 'Endurance' in c.title:
                c.boostScore(10)
    if vehicleType == "BaggageLoader":
        for c in candidates:
            if 'CHAMP' in c.title:
                c.boostScore(10)
    if vehicleType == "PassengerBus":
        gate = getGate()
        if not gate:
            return
        handler = None
        try:
            handler = (gate.preferredTextures or {}).get("handling")
        except:
            pass
        if not handler:
            handler = gate.handlingTexture
        for c in candidates:
            if "LSAS" in handler and "LSASWW" in c.title:
                c.boostScore(10)
            if "WAS" in handler and "WASWW" in c.title:
                c.boostScore(10)
            if handler == "FR_ASP" and "RYR" in c.title:
                c.boostScore(100)