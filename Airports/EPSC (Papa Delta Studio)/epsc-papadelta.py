version = 0.9
msfs_mode = 1


@AlternativeStopPositions
def offsetStandMediumOption1(aircraftData):
    offsets = {
        170: -6,   # E170
        175: -6,   # E175
        42: -6,   # ATR-42
        72: -6,   # ATR-72
        146: -6,   # BAe-146
        600: -6,   # DHC-6 Twin Otter
        1008: -6,   # DHC-8 DASH-8
        
        221: -0.65,   # A220-100
        223: -0.65,   # A220-300
        318: -0.65,   # A318
        319: -0.65,   # A319
        320: -0.65,   # A320
        321: -0.65,   # A321

        0: 0, # STOP POINT
        190: 0,   # E190
        195: 0,   # E195
        737: 0,   # B737
        700: 0,   # CRJ700
        900: 0,   # CRJ900
        1000: 0,   # CRJ1000
    }
    try:
        return Distance.fromMeters(offsets.get(aircraftData.idMajor))
    except:
        return Distance.fromMeters(0)


@AlternativeStopPositions
def offsetStandLargeOption1(aircraftData):
    offsets = {
        221: -0.65,   # A220-100
        223: -0.65,   # A220-300
        300: -0.65, # A300 (D)
        310: -0.65, # A310 (D)
        318: -0.65,   # A318
        319: -0.65,   # A319
        320: -0.65,   # A320
        321: -0.65,   # A321

        0: 0, # STOP POINT
        #737: 0, # B737 (C)

        757: 6, # B757 (D)
        330: 6, # A330 (E)
        350: 6, # A350 (E)

        340: 12, # A340-300 -500 (E)
        747: 12, # B747, max 747-400 (E) - minor not available in MSFS as of 2024-10
        767: 12, # B767-400 (D)
        787: 12, # B787, max 787-300 (E) - minor not available in MSFS as of 2024-10
        777: 12, # B777 (E)
    }
    try:
        return Distance.fromMeters(offsets.get(aircraftData.idMajor))
    except:
        return Distance.fromMeters(0)


@AlternativeStopPositions
def offsetStandOnePoint(aircraftData):
    return Distance.fromMeters(0)


prioTerminal = 1
prioApronGA = 2
prioApron3 = 3
prioApron4 = 4
prioApronHEMS = 5


parkings = {
    PARKING : {
        None : (),
        1 : (CustomizedName("Terminal|Stand #", prioTerminal), offsetStandMediumOption1),
        2 : (CustomizedName("Terminal|Stand #", prioTerminal), offsetStandMediumOption1),
        3 : (CustomizedName("Terminal|Stand #", prioTerminal), offsetStandMediumOption1),
        4 : (CustomizedName("Terminal|Stand #", prioTerminal), offsetStandMediumOption1),
        5 : (CustomizedName("Terminal|Stand #", prioTerminal), offsetStandMediumOption1),
        6 : (CustomizedName("Terminal|Stand #", prioTerminal), offsetStandMediumOption1),

        7 : (CustomizedName("Terminal|Stand #", prioTerminal), offsetStandLargeOption1),

        201 : (CustomizedName("Apron GA|Stand #", prioApronGA), offsetStandOnePoint),
        202 : (CustomizedName("Apron GA|Stand #", prioApronGA), offsetStandOnePoint),
        203 : (CustomizedName("Apron GA|Stand #", prioApronGA), offsetStandOnePoint),
        204 : (CustomizedName("Apron GA|Stand #", prioApronGA), offsetStandOnePoint),
        205 : (CustomizedName("Apron GA|Stand #", prioApronGA), offsetStandOnePoint),
        206 : (CustomizedName("Apron GA|Stand #", prioApronGA), offsetStandOnePoint),
        207 : (CustomizedName("Apron GA|Stand #", prioApronGA), offsetStandOnePoint),
        208 : (CustomizedName("Apron GA|Stand #", prioApronGA), offsetStandOnePoint),
        209 : (CustomizedName("Apron GA|Stand #", prioApronGA), offsetStandOnePoint),
        210 : (CustomizedName("Apron GA|Stand #", prioApronGA), offsetStandOnePoint),
        211 : (CustomizedName("Apron GA|Stand #", prioApronGA), offsetStandOnePoint),
        212 : (CustomizedName("Apron GA|Stand #", prioApronGA), offsetStandOnePoint),
        213 : (CustomizedName("Apron GA|Stand #", prioApronGA), offsetStandOnePoint),
        214 : (CustomizedName("Apron GA|Stand #", prioApronGA), offsetStandOnePoint),
        215 : (CustomizedName("Apron GA|Stand #", prioApronGA), offsetStandOnePoint),

        301 : (CustomizedName("Apron 3 (Cargo)|Stand #", prioApron3), offsetStandOnePoint),
        302 : (CustomizedName("Apron 3 (Cargo)|Stand #", prioApron3), offsetStandOnePoint),
        303 : (CustomizedName("Apron 3 (Cargo)|Stand #", prioApron3), offsetStandOnePoint),

        401 : (CustomizedName("Apron 4|Stand #", prioApron4), offsetStandOnePoint),
        402 : (CustomizedName("Apron 4|Stand #", prioApron4), offsetStandOnePoint),
        403 : (CustomizedName("Apron 4|Stand #", prioApron4), offsetStandOnePoint),
        404 : (CustomizedName("Apron 4|Stand #", prioApron4), offsetStandOnePoint),

        501 : (CustomizedName("Apron HEMS|Helipad #", prioApronHEMS), offsetStandOnePoint),
        502 : (CustomizedName("Apron HEMS|Helipad #", prioApronHEMS), offsetStandOnePoint),
        503 : (CustomizedName("Apron HEMS|Helipad #", prioApronHEMS), offsetStandOnePoint),
        504 : (CustomizedName("Apron HEMS|Stand #", prioApronHEMS), offsetStandOnePoint),
    }
}
