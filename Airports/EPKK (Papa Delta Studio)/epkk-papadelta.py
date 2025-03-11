version = 0.9
msfs_mode = 1


@AlternativeStopPositions
def offsetStandMediumOption1(aircraftData):
    offsets = {
        0: 0, # STOP POINT
        221: 0,   # A220-100
        223: 0,   # A220-300
        190: 0,   # E190
        195: 0,   # E195
        320: 0,   # A320
        321: 0,   # A321
        737: 0,   # B737
        900: 0,   # CRJ900
        1000: 0,   # CRJ1000

        170: -5.45,   # E170
        175: -5.45,   # E175
        318: -5.45,   # A318
        319: -5.45,   # A319
        700: -5.45,   # CRJ700

        42: -8.55,   # ATR-42
        72: -8.55,   # ATR-72
        146: -8.55,   # BAe-146
        600: -8.55,   # DHC-6 Twin Otter
        1008: -8.55,   # DHC-8 DASH-8
    }
    try:
        return Distance.fromMeters(offsets.get(aircraftData.idMajor))
    except:
        return Distance.fromMeters(0)



@AlternativeStopPositions
def offsetStandMediumOption2(aircraftData):
    offsets = {
        0: 0, # STOP POINT
        221: 0,   # A220-100
        223: 0,   # A220-300
        190: 0,   # E190
        195: 0,   # E195
        320: 0,   # A320
        321: 0,   # A321
        737: 0,   # B737
        900: 0,   # CRJ900
        1000: 0,   # CRJ1000

        170: -7,   # E170
        175: -7,   # E175
        318: -7,   # A318
        319: -7,   # A319
        700: -7,   # CRJ700
        42: -7,   # ATR-42
        72: -7,   # ATR-72
        146: -7,   # BAe-146
        600: -7,   # DHC-6 Twin Otter
        1008: -7,   # DHC-8 DASH-8
    }
    try:
        return Distance.fromMeters(offsets.get(aircraftData.idMajor))
    except:
        return Distance.fromMeters(0)


@AlternativeStopPositions
def offsetStandLargeOption1(aircraftData):
    offsets = {
        0: 0, # STOP POINT

        737: 0, #B737
        300: 0, # A300
        310: 0, # A310,

        757: 6.1, # B757
        330: 6.1, # A330
        350: 6.1, # A350
        # 783 - minor required, aircraft not available in MSFS as of 2024-07

        340: 10.8, # A340-300 -500
        747: 10.8, # B747-400
        767: 10.8, # B767-400
        787: 10.8, # B787

        777: 12.7, # B777-300
    }
    try:
        return Distance.fromMeters(offsets.get(aircraftData.idMajor))
    except:
        return Distance.fromMeters(0)




@AlternativeStopPositions
def offsetStandLargeOption2(aircraftData):
    offsets = {
        0: 6.1, # DEFAULT (737)
        
        300: 0, # A300
        310: 0, # A310,
        318: 0,   # A318
        319: 0,   # A319
        320: 0,   # A320
        42: 0,   # ATR-42
        72: 0,   # ATR-72
        600: 0,   # DHC-6 Twin Otter
        1008: 0,   # DHC-8 DASH-8

        146: 6.1,   # BAe-146
        170: 6.1,   # E170
        175: 6.1,   # E175
        190: 6.1,   # E190
        195: 6.1,   # E195
        221: 6.1,   # A220-100
        223: 6.1,   # A220-300
        737: 6.1, # B737
        757: 6.1, # B757
        700: 6.1,   # CRJ700
        900: 6.1,   # CRJ900
        1000: 6.1,   # CRJ1000

        330: 10.8, # A330
        340: 10.8, # A340-300 -500
        350: 10.8, # A350
        747: 10.8, # B747-400
        767: 10.8, # B767-400

        787: 12.7, # B787
        777: 12.7, # B777-300
    }
    try:
        return Distance.fromMeters(offsets.get(aircraftData.idMajor))
    except:
        return Distance.fromMeters(0)


@AlternativeStopPositions
def offsetStandOnePoint(aircraftData):
    return Distance.fromMeters(0)


prioGates = 1
prioApronCivil = 2
prioApronMilitary = 3


parkings = {
    GATE : {
        None : (),
        3 : (CustomizedName("Gate 3,5,6|Gate #", prioGates), offsetStandLargeOption1),
        5 : (CustomizedName("Gate 3,5,6|Gate #", prioGates), offsetStandLargeOption1),
        6 : (CustomizedName("Gate 3,5,6|Gate #", prioGates), offsetStandLargeOption1),
    },
    PARKING : {
        None : (),

        "1R" : (CustomizedName("Stand 01-06|Stand 1R", prioApronCivil), offsetStandMediumOption2),
        1 : (CustomizedName("Stand 01-06|Stand #", prioApronCivil), offsetStandLargeOption2),
        "1L" : (CustomizedName("Stand 01-06|Stand 1L", prioApronCivil), offsetStandMediumOption2),
        "2R" : (CustomizedName("Stand 01-06|Stand 2R", prioApronCivil), offsetStandMediumOption2),
        2 : (CustomizedName("Stand 01-06|Stand #", prioApronCivil), offsetStandLargeOption2),
        "2L" : (CustomizedName("Stand 01-06|Stand 2L", prioApronCivil), offsetStandMediumOption2),
        4 : (CustomizedName("Stand 01-06|Stand #", prioApronCivil), offsetStandMediumOption1),
        "5L" : (CustomizedName("Stand 01-06|Stand 5L", prioApronCivil), offsetStandMediumOption1),
        "6R" : (CustomizedName("Stand 01-06|Stand 6R", prioApronCivil), offsetStandOnePoint),
        "6L" : (CustomizedName("Stand 01-06|Stand 6L", prioApronCivil), offsetStandMediumOption1),

        "7R" : (CustomizedName("Stand 07-12|Stand 7R", prioApronCivil), offsetStandMediumOption1),
        7 : (CustomizedName("Stand 07-12|Stand #", prioApronCivil), offsetStandLargeOption1),
        8 : (CustomizedName("Stand 07-12|Stand #", prioApronCivil), offsetStandMediumOption1),
        9 : (CustomizedName("Stand 07-12|Stand #", prioApronCivil), offsetStandMediumOption1),
        10 : (CustomizedName("Stand 07-12|Stand #", prioApronCivil), offsetStandMediumOption1),
        11 : (CustomizedName("Stand 07-12|Stand #", prioApronCivil), offsetStandMediumOption1),
        12 : (CustomizedName("Stand 07-12|Stand #", prioApronCivil), offsetStandMediumOption1),

        13 : (CustomizedName("Stand 13-16|Stand #", prioApronCivil), offsetStandMediumOption1),
        14 : (CustomizedName("Stand 13-16|Stand #", prioApronCivil), offsetStandMediumOption1),
        15 : (CustomizedName("Stand 13-16|Stand #", prioApronCivil), offsetStandMediumOption1),
        16 : (CustomizedName("Stand 13-16|Stand #", prioApronCivil), offsetStandMediumOption1),
        
        17 : (CustomizedName("Stand 17-21|Stand #", prioApronCivil), offsetStandMediumOption1),
        18 : (CustomizedName("Stand 17-21|Stand #", prioApronCivil), offsetStandMediumOption1),
        19 : (CustomizedName("Stand 17-21|Stand #", prioApronCivil), offsetStandMediumOption1),
        20 : (CustomizedName("Stand 17-21|Stand #", prioApronCivil), offsetStandMediumOption1),
        21 : (CustomizedName("Stand 17-21|Stand #", prioApronCivil), offsetStandMediumOption1),
        
        22 : (CustomizedName("Stand 22-25|Stand #", prioApronCivil), offsetStandMediumOption1),
        23 : (CustomizedName("Stand 22-25|Stand #", prioApronCivil), offsetStandMediumOption1),
        "24L" : (CustomizedName("Stand 22-25|Stand 24L", prioApronCivil), offsetStandOnePoint),
        24 : (CustomizedName("Stand 22-25|Stand #", prioApronCivil), offsetStandMediumOption1),
        "24R" : (CustomizedName("Stand 22-25|Stand 24R", prioApronCivil), offsetStandOnePoint),
        "25L" : (CustomizedName("Stand 22-25|Stand 25L", prioApronCivil), offsetStandOnePoint),
        25 : (CustomizedName("Stand 22-25|Stand #", prioApronCivil), offsetStandMediumOption1),
        "25R" : (CustomizedName("Stand 22-25|Stand 25R", prioApronCivil), offsetStandOnePoint),

        26 : (CustomizedName("Stand 26-30|Stand #", prioApronCivil), offsetStandMediumOption1),
        27 : (CustomizedName("Stand 26-30|Stand #", prioApronCivil), offsetStandMediumOption1),
        28 : (CustomizedName("Stand 26-30|Stand #", prioApronCivil), offsetStandMediumOption1),
        29 : (CustomizedName("Stand 26-30|Stand #", prioApronCivil), offsetStandMediumOption1),
        30 : (CustomizedName("Stand 26-30|Stand #", prioApronCivil), offsetStandMediumOption1),

        31 : (CustomizedName("Stand 31-35|Stand #", prioApronCivil), offsetStandMediumOption1),
        32 : (CustomizedName("Stand 31-35|Stand #", prioApronCivil), offsetStandMediumOption1),
        33 : (CustomizedName("Stand 31-35|Stand #", prioApronCivil), offsetStandMediumOption1),
        34 : (CustomizedName("Stand 31-35|Stand #", prioApronCivil), offsetStandMediumOption1),
        35 : (CustomizedName("Stand 31-35|Stand #", prioApronCivil), offsetStandMediumOption1),

        101: (CustomizedName("Military Cargo Apron|Stand #", prioApronMilitary), offsetStandOnePoint),
        102: (CustomizedName("Military Cargo Apron|Stand #", prioApronMilitary), offsetStandOnePoint),
        103: (CustomizedName("Military Cargo Apron|Stand #", prioApronMilitary), offsetStandOnePoint),
        104: (CustomizedName("Military Cargo Apron|Stand #", prioApronMilitary), offsetStandOnePoint),
        105: (CustomizedName("Military Cargo Apron|Stand #", prioApronMilitary), offsetStandOnePoint),
        106: (CustomizedName("Military Cargo Apron|Stand #", prioApronMilitary), offsetStandOnePoint),
        107: (CustomizedName("Military Cargo Apron|Stand #", prioApronMilitary), offsetStandOnePoint),
        108: (CustomizedName("Military Cargo Apron|Stand #", prioApronMilitary), offsetStandOnePoint),
        109: (CustomizedName("Military Cargo Apron|Stand #", prioApronMilitary), offsetStandOnePoint),
        110: (CustomizedName("Military Cargo Apron|Stand #", prioApronMilitary), offsetStandOnePoint),
        111: (CustomizedName("Military Cargo Apron|Stand #", prioApronMilitary), offsetStandOnePoint),
        112: (CustomizedName("Military Cargo Apron|Stand #", prioApronMilitary), offsetStandOnePoint),
        113: (CustomizedName("Military Cargo Apron|Stand #", prioApronMilitary), offsetStandOnePoint),
        114: (CustomizedName("Military Cargo Apron|Stand #", prioApronMilitary), offsetStandOnePoint),
        115: (CustomizedName("Military Cargo Apron|Stand #", prioApronMilitary), offsetStandOnePoint),

        121: (CustomizedName("Military Combat Apron|Stand #", prioApronMilitary), offsetStandOnePoint),
        122: (CustomizedName("Military Combat Apron|Stand #", prioApronMilitary), offsetStandOnePoint),
        123: (CustomizedName("Military Combat Apron|Stand #", prioApronMilitary), offsetStandOnePoint),
        124: (CustomizedName("Military Combat Apron|Stand #", prioApronMilitary), offsetStandOnePoint),
        125: (CustomizedName("Military Combat Apron|Stand #", prioApronMilitary), offsetStandOnePoint),

        126: (CustomizedName("Military Cargo Apron|Stand #", prioApronMilitary), offsetStandOnePoint),
        127: (CustomizedName("Military Cargo Apron|Stand #", prioApronMilitary), offsetStandOnePoint),
        128: (CustomizedName("Military Cargo Apron|Stand #", prioApronMilitary), offsetStandOnePoint),
        129: (CustomizedName("Military Cargo Apron|Stand #", prioApronMilitary), offsetStandOnePoint),
    }
}