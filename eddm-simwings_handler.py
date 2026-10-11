# -*- coding: utf-8 -*-
# EDDM Sim-Wings GSX Airport Handler
# Dynamic operator selection is based ONLY on the airline ICAO code reported
# by the currently loaded aircraft/livery (aircraft.icaoAirline).
# SimBrief is intentionally not used.
#
# GSX texture mapping used for this profile:
#   AEROGATE = visual GSX proxy for the dominant AeroGround handling at MUC
#   LH       = Lufthansa Ground Services / Lufthansa-group handling where applicable
#   WISAG    = WISAG Aviapartner Ground Service Munich
#   GGOURMET = Gate Gourmet catering for every airline

AEROGATE = "AEROGATE"
LH = "LH"
WISAG = "WISAG"
GATE_GOURMET = "GGOURMET"

# WISAG / Aviapartner Munich assignments established from the MUC research.
# Includes the IAG carriers handled by WISAG, easyJet, TAP, ITA, Air Serbia,
# Discover and DAT. BCS is included for DHL/EAT cargo operations.
WISAG_ONLY = {
    "ASL", "BAW", "BCS", "DTR", "EIN", "EJU", "EZY", "IBE",
    "ITY", "OCN", "TAP", "VLG"
}

# Lufthansa-group carriers kept on the Lufthansa Ground Services texture.
# Lufthansa mainline itself is deliberately NOT here because AeroGround is the
# documented long-term ramp handler for DLH at Munich; AEROGATE is the GSX proxy.
LH_ONLY = {
    "AUA", "BEL", "CLH", "DLA", "EWG", "LHX", "SWR"
}

# Known/current MUC operators assigned to AeroGround in the researched mapping.
# AEROGATE is used as the available GSX visual proxy because this Sim-Wings
# profile does not provide an AEROGROUND texture.
AEROGATE_ONLY = {
    "AAL", "AEE", "AAW", "ABY", "ACA", "AEA", "AFR", "AIZ", "ANA",
    "AWC", "BBG", "BTI", "CCA", "CCM", "CFG", "CPA", "CTN", "DAL",
    "DLH", "ETD", "EVA", "EVE", "FDX", "FHY", "FHM", "FIA", "FIN",
    "GEC", "GFA", "HVN", "ICE", "IVY", "KAC", "KLM", "KMM", "KNE",
    "LAV", "LBT", "LGL", "LOT", "MGH", "MSC", "MSR", "NIA", "NOZ",
    "NSZ", "OMA", "PGT", "QTR", "RAM", "RJA", "RSX", "SAS", "SDR",
    "SEH", "SIA", "SMR", "STW", "SVA", "SXS", "TAH", "TAR", "THA",
    "THY", "TKJ", "TUI", "TVS", "UAL", "UAE", "UBD", "UPS", "UZB",
    "VOE", "VSV", "WIF"
}


def _airline():
    # Use ONLY the aircraft/livery airline ICAO code reported by GSX/MSFS.
    # No SimBrief dependency: this works even without a current SimBrief plan.
    return (getattr(aircraft, "icaoAirline", "") or "").strip().upper()


def _texture():
    a = _airline()
    if a in WISAG_ONLY:
        return WISAG
    if a in LH_ONLY:
        return LH
    if a in AEROGATE_ONLY:
        return AEROGATE

    # Safe MUC fallback for an unknown/new airline or an unlisted livery code.
    # AeroGround is the dominant real-world handler, represented here by the
    # AEROGATE texture available in this Sim-Wings GSX profile.
    return AEROGATE


def _apply():
    gate = getGate()
    if gate:
        gate.handlingTexture = _texture()
        # EDDM catering: always use Gate Gourmet, regardless of airline.
        gate.cateringTexture = GATE_GOURMET


def onEnterAirport(self):
    # Force all GSX VDGS / marshaller distance readouts at EDDM to meters.
    # Airport-handler scope overrides aircraft-handler and simulator unit settings.
    setVdgsUnits('metric')

    # Apply the airline-dependent handling operator as soon as the EDDM airport
    # handler activates (normal starts / cold & dark included).
    _apply()


def onAirportBeforeVehicleSelect(self):
    # Keep VDGS / marshaller distance readouts metric after gate changes/reselection.
    setVdgsUnits('metric')

    # Re-apply the airline-dependent operator on every vehicle selection.
    _apply()
