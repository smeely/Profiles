# -- coding: utf-8 --

version = 1.5
msfs_mode = 1
icao = "eddf"

def HandleAircraftOffsets(aircraftData, specificTables, genericTable):
    major_id = aircraftData.idMajor
    minor_id = aircraftData.idMinor

    if major_id in specificTables:
        specific_table, fallback_key = specificTables[major_id]
        result = specific_table.get(minor_id)
        if result is None:
            result = specific_table.get(fallback_key)
    else:
        result = genericTable.get(major_id, 0)

    return result

@AlternativeStopPositions
def customOffsetequal(aircraftData):

    table = {
        0: 0,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetA1(aircraftData):

    table = {
        0: 0,
        319: -5.9,
    }
    
    table737 = {
        0: 0,
        800: -3.2,
        900: -3.2,
    },
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetA11(aircraftData):

    table = {
        0: 0,
        223: 2.1,
        321: 2.1,
        
        190: 2.1,
        195: 2.1,
        
    }
    
    table737 = {
        0: 0,
        800: 4.85,
        900: 4.85,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetA13(aircraftData):

    table = {
        0: 0,
        321: 3.15,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetA14(aircraftData):

    table = {
        0: 0,
        318: -1.3,
        319: -1.3,
        321: 5.1,
        
        195: 3.85,
    }
    
    table737 = {
        0: 0,
        800: 3.85,
        900: 5.1,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetA15(aircraftData):

    table = {
        0: 0,
        321: 6.1,
        340: 7.3,
        350: 12.5,
        
        777: 8.5,
    }
    
    table330 = {
        0: 6.1,
        300: 7.3,
        900: 7.3,
    }
    
    table757 = {
        0: 6.1,
        300: 8.5,
    }
    
    table767 = {
        0: 0,
        300: 8.5,
        400: 12.5,
    }
    
    table787 = {
        8: 7.3,
        9: 9.6,
        10: 12.5,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            330 : (table330, 0),
            757 : (table757, 0),
            767 : (table767, 0),
            787 : (table787, 8),
        },
        table) )


@AlternativeStopPositions
def customOffsetA16(aircraftData):

    table = {
        0: 0,
        318: -1.6,
        319: -1.6,
        321: 3.95,
        
        195: 2.4,
    }
    
    table737 = {
        0: 0,
        800: 2.4,
        900: 3.95,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetA17(aircraftData):

    table = {
        0: 0,
        321: 5.75,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetA18(aircraftData):

    table = {
        0: 0,
        218: -2.35,
        319: -2.35,
        321: 3.7,
    }
    
    table737 = {
        0: 0,
        800: 3.7,
        900: 3.7,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetA19(aircraftData):

    table = {
        0: 0,
        321: 7.3,
        340: 8.3,
        350: 12.8,
        
        777: 10.2,
    }
    
    table330 = {
        0: 7.3,
        300: 8.3,
        900: 8.3,
    }
    
    table767 = {
        0: 0,
        300: 8.3,
        400: 12,
    }
    
    table787 = {
        0: 8.3,
        9: 10.2,
        10: 12.5,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            330 : (table330, 0),
            767 : (table767, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetA20(aircraftData):

    table = {
        0: 0,
        321: 6.5,
        
        757: 6.5,
        767: 8.2,
        747: 8.2,
    }
    
    table330 = {
        0: 6.5,
        300: 8.2,
        900: 8.2,
    }
    
    table340 = {
        0: 8.2,
        600: 9.9,
    }
    
    table350 = {
        0: 9.9,
        1000: 11,
    }
    
    table777 = {
        0: 8.2,
        300: 9.9,
    }
    
    table787 = {
        0: 8.2,
        10: 9.9,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            330 : (table330, 0),
            340 : (table340, 0),
            350 : (table350, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetA21(aircraftData):

    table = {
        0: 0,
        321: 4,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetA22(aircraftData):

    table = {
        0: 0,
        321: 7.7,
        
        757: 7.7,
        747: 8.8,
    }
    
    table330 = {
        0: 6.8,
        300: 8.8,
        900: 8.8,
    }
    
    table340 = {
        0: 8.8,
        600: 10.1,
    }
    
    table350 = {
        0: 10.1,
        1000: 11.8,
    }
    
    table767 = {
        0: 0,
        300: 7.7,
        400: 10.1,
    }
    
    table777 = {
        0: 8.8,
        300: 10.1,
    }
    
    table787 = {
        0: 8.8,
        10: 10.1,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            330 : (table330, 0),
            340 : (table340, 0),
            350 : (table350, 0),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetA23(aircraftData):

    table = {
        0: 0,
        321: 7.8,
        
        757: 7.8,
        747: 11.2,
    }
    
    table330 = {
        0: 7.8,
        300: 8.1,
        900: 8.1,
    }
    
    table340 = {
        0: 8.1,
        600: 11.2,
    }
    
    table350 = {
        0: 11.2,
        1000: 13.5,
    }
    
    table767 = {
        0: 0,
        300: 8.1,
        400: 11.2,
    }
    
    table777 = {
        0: 8.1,
        300: 11.2,
    }
    
    table787 = {
        0: 8.1,
        10: 11.2,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            330 : (table330, 0),
            340 : (table340, 0),
            350 : (table350, 0),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetA24(aircraftData):

    table = {
        0: 0,
        318: 1.15,
        319: 1.15,
        320: 1.15,
        321: 5.1,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetA25(aircraftData):

    table = {
        0: 0,
        318: -10,
        319: -10,
        320: -10,
        321: -2.4,
        
        737: -10,
        757: 7.8,
        747: 2.2,
    }
    
    table330 = {
        0: -2.4,
        300: 0,
        900: 0,
    }
    
    table340 = {
        0: 0, 
        600: 5.3,
    }
    
    table350 = {
        0: 2.2,
        1000: 6.5,
    }
    
    table767 = {
        0: 0,
        400: 5.3,
    }
    
    table777 = {
        0: 0,
        300: 5.3,
    }
    
    table787 = {
        8: 0,
        9: 2.2,
        10: 11.2,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            330 : (table330, 0),
            340 : (table340, 0),
            350 : (table350, 0),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 8),
        },
        table) )


@AlternativeStopPositions
def customOffsetA26(aircraftData):

    table = {
        0: 0,
        318: -1,
        319: -1,
        321: 4.2,
    }
    
    table737 = {
        0: 0,
        800: 4.2,
        900: 4.2,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetA28(aircraftData):

    table = {
        0: 0,
        318: -1.4,
        319: -1.4,
        321: 2,
    }
    
    table737 = {
        0: 0,
        800: 2,
        900: 2,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetA30(aircraftData):

    table = {
        0: 0,
        318: -1.6,
        319: -1.6,
        321: 1.6,
    }
    
    table737 = {
        0: 0,
        800: 1.6,
        900: 1.6,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetA34(aircraftData):

    table = {
        0: 0,
        318: -2,
        319: -2,
        321: 3.8,
    }
    
    table737 = {
        0: 0,
        800: 3.8,
        900: 3.8,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetA36(aircraftData):

    table = {
        0: 0,
        318: -2.3,
        319: -2.3,
        321: 2.3,
    }
    
    table737 = {
        0: 0,
        800: 2.3,
        900: 2.3,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetA38(aircraftData):

    table = {
        0: 0,
        318: -1.05,
        319: -1.05,
        321: 1.7,
    }
    
    table737 = {
        0: 0,
        800: 1.7,
        900: 1.7,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetA40(aircraftData):

    table = {
        0: 0,
        318: -1.5,
        319: -1.5,
        321: 2.6,
    }
    
    table737 = {
        0: 0,
        800: 2.6,
        900: 2.6,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetV143(aircraftData):

    table = {
        0: 0,
        318: -4,
        319: -4,
        320: -4,
        321: -1.2,
        
        170: -1.2,
        175: -1.2,
        190: -1.2,
        195: -1.2,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetV144(aircraftData):

    table = {
        0: 0,
        318: -4.1,
        319: -4.1,
        320: -4.1,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetA50(aircraftData):

    table = {
        0: 0,
        321: 9.1,
        330: 9.1,
        
        747: 11.1,
        757: 9.1,
    }
    
    table340 = {
        0: 9.1,
        600: 14.5,
    }
    
    table350 = {
        0: 14.5,
        1000: 16.4,
    }
    
    table767 = {
        0: 0,
        300: 11.1,
        400: 14.5,
    }
    
    table777 = {
        0: 11.1,
        300: 14.5,
    }
    
    table787 = {
        0: 9.1,
        10: 14.5,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            350 : (table350, 0),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetA52(aircraftData):

    table = {
        0: 0,
        321: 8.9,
        330: 8.9,
        
        757: 8.9,
    }
    
    table340 = {
        0: 8.9,
        600: 16.25,
    }
    
    table350 = {
        0: 10.9,
        1000:  16.25,
    }
    
    table747 = {
        0: 10.9,
        8: 14.6,
    }
    
    table767 = {
        0: 0,
        300: 8.9,
        400: 10.9,
    }
    
    table777 = {
        0: 8.9,
        300:  16.25,
    }
    
    table787 = {
        0: 8.9,
        10: 10.9,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            350 : (table350, 0),
            747 : (table747, 0),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetA54A58A62A66(aircraftData):

    table = {
        0: 0,
        380: 6.3,
    }
    
    table330 = {
        0: 0,
        300: 1.65,
        900: 1.65,
    }
    
    table340 = {
        0: 1.65,
        600: 6.3,
    }
    
    table350 = {
        0: 5.3,
        1000:  8.2,
    }
    
    table747 = {
        0: 1.65,
        8: 6.3,
    }
    
    table767 = {
        0: 0,
        300: 0,
        400: 5.3,
    }
    
    table777 = {
        0: 1.65,
        300: 5.3,
    }
    
    table787 = {
        0: 0,
        9: 1.65,
        10: 5.3,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            330 : (table330, 0),
            340 : (table340, 0),
            350 : (table350, 0),
            747 : (table747, 0),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetA545862B(aircraftData):

    table = {
        0: 0,
        221: -1.5,
        223: -1.5,
        318: -3.5,
        319: -3.5,
        320: -2.5,
        321: -1.5,
    }
    
    table737 = {
        0: -1.5,
        900: 0,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetA54586266A(aircraftData):

    table = {
        0: 0,
        221: -1.5,
        223: -1.5,
        318: -4,
        319: -4,
        320: -2.5,
        321: -2.5,
        
        170: -2.5,
        175: -2.5,
        190: -2.5,
        195: -2.5,
    }
    
    table737 = {
        0: -2.5,
        800: 0,
        900: 0,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetA66B(aircraftData):

    table = {
        0: 0,
        221: -2.7,
        223: -2.7,
        318: -5,
        319: -5,
        320: -4,
    }
    
    table737 = {
        0: -2.7,
        800: 0,
        900: 0,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetA69(aircraftData):

    table = {
        0: 0,
        330: 8.4,
        
        757: 8.4,
    }
    
    table340 = {
        0: 8.4,
        600: 15.5,
    }
    
    table350 = {
        0: 10.6,
        1000:  17.5,
    }
    
    table747 = {
        0: 10.6,
        8: 15.5,
    }
    
    table767 = {
        0: 0,
        300: 10.6,
        400: 10.6,
    }
    
    table777 = {
        0: 10.6,
        300:  15.5,
    }
    
    table787 = {
        0: 8.4,
        9: 10.6,
        10: 10.6,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            350 : (table350, 0),
            747 : (table747, 0),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 8),
        },
        table) )


@AlternativeStopPositions
def customOffsetB10(aircraftData):

    table = {
        0: 0,
        321: 3.6,
        350: 10,
        
        190: 1.9,
        195: 3.6,
    }
    
    table737 = {
        0: 0,
        800: 3.6,
        900: 3.6,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetB20(aircraftData):

    table = {
        0: 0,
        321: 8.1,
        350: 10,
        
        747: 8.1,
        757: 8.1,
        777: 10,
    }
    
    table330 = {
        0: 6.7,
        300: 8.1,
        900: 8.1,
    }
    
    table340 = {
        0: 8.1,
        600: 10,
    }
    
    table767 = {
        0: 0,
        300: 6.7,
        400: 10.6,
    }
    
    table787 = {
        8: 8.1,
        0: 10,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            330 : (table330, 0),
            340 : (table340, 0),
            767 : (table767, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetB22(aircraftData):

    table = {
        0: 0,
        321:7.6,
        350: 11.9,
        
        747: 8.1,
        757: 7.6,
        777: 10.9,
    }
    
    table330 = {
        0: 7.6,
        300: 10.8,
        900: 10.8,
    }
    
    table340 = {
        0: 9.05,
        600: 10.9,
    }
    
    table767 = {
        0: 0,
        300: 10.8,
        400: 10.9,
    }
    
    table787 = {
        0: 9.05,
        9: 10.9,
        10: 10.9,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            330 : (table330, 0),
            340 : (table340, 0),
            767 : (table767, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetB23(aircraftData):

    table = {
        0: 0,
        321:6.6,
        330: 5.2,
        
        747: 8.1,
        757: 5.2,
        777: 8.1,
    }
    
    table340 = {
        0: 5.2,
        600: 8.1,
    }
    
    table350 = {
        0: 8.1,
        1000: 9.2,
    }
    
    table767 = {
        0: 0,
        300: 6.6,
        400: 6.6,
    }
    
    table787 = {
        0: 8.1,
        9: 8.1,
        10: 8.1,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            350 : (table350, 0),
            340 : (table340, 0),
            767 : (table767, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetB24(aircraftData):

    table = {
        0: 0,
        321: 4.6,
        
        757: 4.6,
        767: 7.2,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetB25(aircraftData):

    table = {
        0: 0,
        321: 7.3,
        340: 9.5,
        350: 13,
        
        757: 7.3,
        777: 9.5,
    }
    
    table330 = {
        0: 7.3,
        300: 9.5,
        900: 9.5,
    }
    
    table767 = {
        0: 0,
        300: 9.5,
        400: 9.5,
    }
    
    table787 = {
        8: 8.3,
        0: 11,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            330 : (table330, 0),
            767 : (table767, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetB26(aircraftData):

    table = {
        0: 0,
        321: 13.5,
        380: 15.2,
        
        757: 13.5,
    }
    
    table330 = {
        0: 11.8,
        300: 13.5,
        900: 13.5,
    }
    
    table340 = {
        0: 13.5,
        600: 19.3,
    }
    
    table350 = {
        0: 15.2,
        1000: 19.3,
    }
    
    table747 = {
        0: 13.5,
        8: 15.2,
    }
    
    table767 = {
        0: 0,
        300: 15.2,
        400: 15.2,
    }
    
    table777 = {
        0: 13.5,
        300: 16.8,
    }
    
    table787 = {
        0: 11.8,
        9: 13.5,
        10: 15.2,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            330 : (table330, 0),
            340 : (table340, 0),
            350 : (table350, 0),
            747 : (table747, 0),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 8),
        },
        table) )


@AlternativeStopPositions
def customOffsetB27(aircraftData):

    table = {
        0: 0,
        320: 3.7,
        321: 6.9,
        
        190: 3.7,
        195: 3.7,
    }
    
    table737 = {
        0: 3.7,
        800: 5.2,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetB28(aircraftData):

    table = {
        0: 0,
        321: 7.7,
        330: 7.7,
        380: 12.2,
        
        757: 7.7,
    }
    
    table340 = {
        0: 7.7,
        600: 19.3,
    }
    
    table350 = {
        0: 9.8,
        1000: 19.3,
    }
    
    table747 = {
        0: 9.8,
        8: 12.2,
    }
    
    table767 = {
        0: 0,
        300: 9.8,
        400: 9.8,
    }
    
    table777 = {
        0: 7.7,
        300: 12.2,
    }
    
    table787 = {
        0: 8.7,
        10: 12.2,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            350 : (table350, 0),
            747 : (table747, 0),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 8),
        },
        table) )


@AlternativeStopPositions
def customOffsetB41(aircraftData):

    table = {
        0: 0,
        318: -1.7,
        319: -1.7,
        321: 3.8,
    }
    
    table737 = {
        0: 0,
        900: 3.8,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetB42(aircraftData):

    table = {
        0: 0,
        321: 4.3,
        
        747: 4.3,
        757: 4.3,
    }
    
    table330 = {
        0: 4.3,
        300: 7.7,
        900: 7.7,
    }
    
    table340 = {
        0: 4.3,
        600: 10.5,
    }
    
    table350 = {
        0: 7.7,
        1000: 10.5,
    }
    
    table767 = {
        0: 4.3,
        400: 7.7,
    }
    
    table777 = {
        0: 4.3,
        300: 7.7,
    }
    
    table787 = {
        0: 4.3,
        10: 7.7,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            330 : (table330, 0),
            340 : (table340, 0),
            350 : (table350, 0),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetB43(aircraftData):

    table = {
        0: 0,
        350: 12.8,
        
        747: 10.2,
        757: 5.7,
    }
    
    table330 = {
        0: 5.7,
        300: 7.5,
        900: 7.5,
    }
    
    table340 = {
        0: 7.5,
        600: 12.8,
    }
    
    table767 = {
        0: 0,
        300: 7.5,
        400: 7.5,
    }
    
    table777 = {
        0: 7.5,
        300: 12.8,
    }
    
    table787 = {
        0: 7.5,
        9: 10.2,
        10: 14.25,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            330 : (table330, 0),
            340 : (table340, 0),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetB44(aircraftData):

    table = {
        0: 0,
        321: 7.5,
        340: 10.6,
        350: 13.3,
        
        777: 10.6
    }
    
    table330 = {
        0: 7.5,
        300: 10.6,
        900: 10.6,
    }
    
    table757 = {
        0: 7.5,
        300: 8.5,
    }
    
    table767 = {
        0: 0,
        300: 10.6,
        400: 7.7,
    }
    
    table787 = {
        0: 8.5,
        9: 12.3,
        10: 14.25,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            330 : (table330, 0),
            757 : (table757, 0),
            767 : (table767, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetB45(aircraftData):

    table = {
        0: 0,
        321: 7.2,
        330: 7.2,
        
        747: 13.2,
        757: 7.2,
    }
    
    table340 = {
        0: 7.2,
        600: 15.1,
    }
    
    table350 = {
        0: 9.7,
        1000: 15.1,
    }
    
    table767 = {
        0: 0,
        300: 7.2,
        400: 9.7,
    }
    
    table777 = {
        0: 7.2,
        300: 15.1,
    }
    
    table787 = {
        0: 7.2,
        10: 13.2,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            350 : (table350, 0),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetB46(aircraftData):

    table = {
        0: 0,
        221: -11.4,
        223: -11.4,
        321: 3,
        350: 4.2,
        
        737: -11.4,
        747: 4.2,
        757: 3,
        767: 4.2,
        
        170: -11.4,
        175: -11.4,
        190: -11.4,
        195: -11.4,
    }
    
    table340 = {
        0: 3,
        600: 4.2,
    }
    
    table777 = {
        0: 0,
        300: 4.2,
    }
    
    table787 = {
        8: 3,
        0: 4.2,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetB47(aircraftData):

    table = {
        0: 0,
        221: 2,
        223: 2,
        320: 2,
        321: 4.5,
        
        190: 4.5,
        195: 4.5,
        }
    
    table737 = {
        0: 0,
        700: 2,
        800: 2,
        900: 4.5,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetB48(aircraftData):

    table = {
        0: 0,
        300: 7.6,
        330: 7.6,
        321: 8.4,
        
        747: 9.4,
        757: 8.4,
        767: 9.4,
    }
    
    table340 = {
        0: 7.6,
        600: 11,
    }
    
    table350 = {
        0: 9.4,
        1000: 11,
    }
    
    table777 = {
        0: 8.4,
        300: 11,
    }
    
    table787 = {
        0: 8.4,
        10: 9.4,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            350 : (table350, 9),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetC2(aircraftData):

    table = {
        0: 0,
        318: -2.1,
        319: -1,
        320: -1,
        321: -1,
        
        72: -1,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetC4(aircraftData):

    table = {
        0: 0,
        300: 6.1,
        321: 7.8,
        
        757: 7.8,
        777: 9.8,
    }
    
    table330 = {
        0: 7.8,
        300: 8.8,
        900: 8.8,
    }
    
    table340 = {
        0: 8.8,
        600: 11,
    }
    
    table767 = {
        0: 0,
        300: 8.8,
        400: 8.8,
    }
    
    table787 = {
        8: 8.8,
        0: 9.8,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            330 : (table330, 0),
            340 : (table340, 0),
            767 : (table767, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetC5(aircraftData):

    table = {
        0: 0,
        321: 5.1,
        }
    
    table737 = {
        0: 0,
        800: 5.1,
        900: 5.1,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetC6(aircraftData):

    table = {
        0: 0,
        321: 9.7,
        240: 10.9,
        350: 14.3,
        
        747: 13.1,
        757: 9.7,
        777: 10.9,
    }
    
    table330 = {
        0: 8.5,
        300: 10.9,
        900: 10.9,
    }
    
    table767 = {
        0: 0,
        300: 10.9,
        400: 14.3,
    }
    
    table787 = {
        0: 9.7,
        9: 10.9,
        10: 14.3,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            330 : (table330, 0),
            767 : (table767, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetC8(aircraftData):

    table = {
        0: 0,
        321: 3,
        350: 10.6,
        
        747: 10.6,
        757: 5.2,
    }
    
    table330 = {
        0: 5.2,
        300: 7.25,
        900: 7.25,
    }
    
    table340 = {
        0: 7.25,
        600: 10.6,
    }
    
    table767 = {
        0: 3,
        300: 7.25,
        400: 10.6,
    }
    
    table777 = {
        0: 7.25,
        300: 15,
    }
    
    table787 = {
        8: 7.25,
        0: 10.6,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            330 : (table330, 0),
            340 : (table340, 0),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetC11(aircraftData):

    table = {
        0: 0,
        300: 4.8,
        321: 6.8,
        
        747: 9.3,
        757: 4.8,
    }
    
    table330 = {
        0: 4.8,
        300: 6.8,
        900: 6.8,
    }
    
    table340 = {
        0: 6.8,
        600: 13.2,
    }
    
    table350 = {
        0: 9.3,
        1000: 15.6,
    }
    
    table767 = {
        0: 3,
        300: 6.8,
        400: 10.6,
    }
    
    table777 = {
        0: 6.8,
        300: 13.2,
    }
    
    table787 = {
        0: 6.8,
        9: 9.3,
        10: 13.2,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            330 : (table330, 0),
            340 : (table340, 0),
            350 : (table350, 0),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetC13(aircraftData):

    table = {
        0: 0,
        321: 6.9,
        
        757: 6.9,
    }
    
    table330 = {
        0: 6.9,
        300: 7.9,
        900: 7.9,
    }
    
    table340 = {
        0: 6.8,
        600: 16.6,
    }
    
    table350 = {
        0: 10,
        1000: 16.6,
    }
    
    table747 = {
        0: 10,
        8: 14.1,
    }
    
    table767 = {
        0: 0,
        300: 7.9,
        400: 10,
    }
    
    table777 = {
        200: 10,
        300: 14.1,
    }
    
    table787 = {
        8: 7.9,
        0: 10,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            330 : (table330, 0),
            340 : (table340, 0),
            350 : (table350, 0),
            747 : (table747, 0),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetC14(aircraftData):

    table = {
        0: 0,
        221: 2.5,
        223: 2.5,
        318: 2.5,
        319: 2.5,
        320: 2.5,
        321: 8.5,
        330: 8.5,
        380: 14.6,
        
        757: 8.5,
    }
    
    table340 = {
        0: 8.5,
        600: 16.6,
    }
    
    table350 = {
        0: 13.5,
        1000: 16.1,
    }
    
    table747 = {
        0: 0,
        8: 16.1,
    }
    
    table767 = {
        0: 8.5,
        400: 13.5,
    }
    
    table777 = {
        0: 8.5,
        300: 13.5,
    }
    
    table787 = {
        0: 8.5,
        10: 13.5,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            350 : (table350, 0),
            747 : (table747, 0),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetC15(aircraftData):

    table = {
        0: 0,
        321: 5.7,
        330: 6.8,
        380: 10.3,
        
        757: 6.8,
        767: 6.8,
    }
    
    table340 = {
        0: 6.8,
        600: 11.8,
    }
    
    table350 = {
        0: 11.8,
        1000: 12.8,
    }
    
    table747 = {
        0: 6.8,
        8: 10.3,
    }
    
    table777 = {
        0: 5.7,
        300: 11.8,
    }
    
    table787 = {
        0: 6.8,
        10: 11.8,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            350 : (table350, 0),
            747 : (table747, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetC15B(aircraftData):

    table = {
        0: 0,
        221: 1.6,
        223: 1.6,
        320: 1.6,
        321: 2.8,
        
        170: 1.6,
        175: 1.6,
        190: 1.6,
        195: 1.6,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetC16(aircraftData):

    table = {
        0: 0,
        321: 5.4,
        330: 7.4,
        380: 10.3,
        
        757: 7.4,
        767: 7.4,
    }
    
    table340 = {
        0: 7.4,
        600: 12.4,
    }
    
    table350 = {
        0: 11,
        1000: 12.4,
    }
    
    table747 = {
        0: 7.4,
        8: 11,
    }
    
    table777 = {
        0: 5.4,
        300: 12.4,
    }
    
    table787 = {
        0: 7.4,
        10: 12.4,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            350 : (table350, 0),
            747 : (table747, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetC16B(aircraftData):

    table = {
        0: 0,
        221: 3,
        223: 3,
        321: 3,
        
        190: 3,
        195: 3,
        }
    
    table737 = {
        0: 0,
        800: 3,
        900: 3,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetC16A(aircraftData):

    table = {
        0: 0,
        221: 2,
        223: 2,
        321: 2,
        
        190: 2,
        195: 2,
        }
    
    table737 = {
        800: 2,
        900: 2,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 800),
        },
        table) )


@AlternativeStopPositions
def customOffsetD1(aircraftData):

    table = {
        0: 0,
        
        757: -4.7,
    }
    
    table330 = {
        0: -4.7,
        300: 0,
        900: 0,
    }
    
    table340 = {
        0: 8.5,
        600: 16.6,
    }
    
    table350 = {
        0: 2,
        1000: 4.7,
    }
    
    table767 = {
        0: 0,
        300: -2,
        400: 2,
    }
    
    table777 = {
        0: 0,
        300: 3.5,
    }
    
    table787 = {
        0: -2,
        9: 0,
        10: 3.5,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            330 : (table330, 0),
            340 : (table340, 0),
            350 : (table350, 0),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetD1A(aircraftData):

    table = {
        0: 0,
        318: -1,
        319: -1,
    }
    
    table737 = {
        0: -1,
        800: 0,
        900: 0,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetD4(aircraftData):

    table = {
        0: 0,
        
        757: -4.5,
    }
    
    table330 = {
        0: -4.5,
        300: -1.8,
        900: -1.8,
    }
    
    table340 = {
        0: -1.8,
        600: 0,
    }
    
    table350 = {
        0: 0,
        1000: 1.2,
    }
    
    table747 = {
        0: -1.8,
        8 : 0,
        }
    
    table767 = {
        0: 0,
        300: -3.1,
        400: 2,
    }
    
    table777 = {
        0: -1.8,
        300: 1.2,
    }
    
    table787 = {
        0: -3.1,
        10: 0,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            330 : (table330, 0),
            340 : (table340, 0),
            350 : (table350, 0),
            757 : (table747, 0),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetD4B(aircraftData):

    table = {
        0: 0,
        221: 1,
        223: 1,
        318: -1.4,
        319: -1.4,
        321: 4.1,
        
        190: 1,
        195: 1,
        }
    
    table737 = {
        0: 0,
        900: 2.5,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetD4A(aircraftData):

    table = {
        0: 0,
        318: -2.4,
        319: -2.4,
        320: -1,
        
        }
    
    table737 = {
        0: 0,
        300: -1,
        400: -1,
        500: -1,
        600: -1,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetD5(aircraftData):

    table = {
        0: 0,
        
        757: -4.5,
    }
    
    table330 = {
        0: -4.5,
        300: 0,
        900: 0,
    }
    
    table340 = {
        0: -2.5,
        600: 0,
    }
    
    table350 = {
        0: 1.4,
        1000: 6,
    }
    
    table747 = {
        0: -2.5,
        8: 4,
    }
    
    table767 = {
        0: 0,
        300: -2.5,
    }
    
    table777 = {
        0: 0,
        300: 4,
    }
    
    table787 = {
        0: -2.5,
        10: 1.4,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            330 : (table330, 0),
            340 : (table340, 0),
            350 : (table350, 0),
            747 : (table747, 0),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetD5A(aircraftData):

    table = {
        0: 0,
        318: -1.5,
        319: -1.5,
        321: 3.3,
        
        190: 3.3,
        195: 3.3,
    }
    
    table737 = {
        0: 0,
        800: 3.3,
        900: 3.3,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetD8(aircraftData):

    table = {
        0: 0,
        318: -9.5,
        319: -9.5,
        320: -9.5,
        321: -9.5,
        
    }
    
    table330 = {
        0: -3.8,
        300: -2.7,
        900: -2.7,
    }
    
    table340 = {
        0: -2.7,
        600: 0,
    }
    
    table350 = {
        0: 0,
        1000: 2.1,
    }
    
    table757 = {
        0: -3.8,
        300: -2.7,
    }
    
    table767 = {
        0: -9.5,
        300: -2.5,
        400: 0,
    }
    
    table787 = {
        8: -2.7,
        0: 0,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            330 : (table330, 0),
            340 : (table340, 0),
            350 : (table350, 0),
            757 : (table757, 0),
            767 : (table767, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetE2(aircraftData):

    table = {
        0: 0,
        330: 4.7,
        380: 9.6,
        
        757: 4.7,
    }
    
    table340 = {
        0: 7.5,
        600: 10.6,
    }
    
    table350 = {
        0: 10.6,
        1000: 11.5,
    }
    
    table747 = {
        0: 7.5,
        8: 9.6,
    }
    
    table767 = {
        0: 0,
        0: 9.6,
    }
    
    table777 = {
        0: 7.5,
        300: 10.6,
    }
    
    table787 = {
        0: 7.5,
        10: 10.6,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            350 : (table350, 0),
            747 : (table747, 0),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetE2B(aircraftData):

    table = {
        0: 0,
        320: 2.5,
        321: 7.1,
        
        190: 2.5,
        }
    
    table737 = {
        0: 0,
        800: 2.5,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetE2A(aircraftData):

    table = {
        0: 0,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetE5(aircraftData):

    table = {
        0: 0,
        380: 3.3,
        
        757: -1.7,
    }
    
    table330 = {
        0: -1.7,
        300: 0,
        900: 0,
    }
    
    table340 = {
        0: 0,
        600: 5.3,
    }
    
    table350 = {
        0: 3.3,
        1000: 6.7,
    }
    
    table747 = {
        0: 0,
        8: 3.3,
    }
    
    table777 = {
        0: 0,
        300: 3.3,
    }
    
    table767 = {
        0: -1.7,
        300: 0,
        400: 3.3,
    }
    
    table787 = {
        0: 0,
        10: 1.7,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            330 : (table330, 0),
            340 : (table340, 0),
            350 : (table350, 0),
            747 : (table747, 0),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetE5A(aircraftData):

    table = {
        0: 0,
        318: -2.8,
        319: -2.8,
        320: -2.8,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetE5B(aircraftData):

    table = {
        0: 0,
        318: -1,
        319: -1,
        321: 3.8,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetE6(aircraftData):

    table = {
        0: 0,
        330: 6.6,
        
        757: 6.6,
    }
    
    
    table340 = {
        0: 9.6,
        600: 12,
    }
    
    table350 = {
        0: 12,
        1000: 13,
    }
    
    table747 = {
        0: 9.6,
        8: 3.3,
    }
    
    table777 = {
        0: 9.6,
        300: 12,
    }
    
    table767 = {
        0: 0,
        0: 9.6,
    }
    
    table787 = {
        0: 7.6,
        9: 9.6,
        10: 12,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            350 : (table350, 0),
            747 : (table747, 0),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetE9(aircraftData):

    table = {
        0: 0,
        318: -12,
        319: -12,
        320: -12,
        321: -10.5,
        380: -2.1,
        
        757: -6.9,
    }
    
    table330 = {
        0: -6.9,
        300: -4.1,
        900: -4.1,
    }
    
    table340 = {
        0: -2.1,
        600: 0,
    }
    
    table747 = {
        0: 9.6,
        8: 0,
    }
    
    table777 = {
        0: -2.1,
        300: 0,
    }
    
    table767 = {
        0: -10.5,
        0: -2.1,
    }
    
    table787 = {
        0: -4.1,
        10: 0,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            330 : (table330, 0),
            340 : (table340, 0),
            747 : (table747, 0),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetF211(aircraftData):

    table = {
        0: 0,
        300: 6.1,
        310: 3,
        321: 6.1,
        330: 6.1,
        340: 6.1,
        
        747: 10.3,
        757: 6.1,
        
        1000: 6.1,
        
        10: 6.1,
        11: 6.1,
        
        42: -4.6,
        72: -4.6,
        
        1008: -4.6,
        
        400: -4.6,
        130: -4.6,
        17: 3,
    }
    
    table350 = {
        0: 10.3,
        1000: 12,
    }
    
    table737 = {
        0: 0,
        800: 3,
        900: 3,
    }
    
    table777 = {
        0: 10.3,
        300: 12,
    }
    
    table767 = {
        0: 6.1,
        400: 10.3,
    }
    
    table787 = {
        0: 6.1,
        10: 12,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            350 : (table350, 0),
            737 : (table737, 0),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetF212(aircraftData):

    table = {
        0: 0,
        300: 8.4,
        310: 3,
        321: 8.4,
        330: 8.4,
        350: 12.8,
        
        747: 12.8,
        757: 8.4,
        777: 12.8,
        
        1000: 6.1,
        
        10: 8.4,
        11: 8.4,
        
        42: -3.9,
        72: -3.9,
        
        1008: -3.9,
        
        400: -3.9,
        130: -3.9,
    }
    
    table340 = {
        0: 8.4,
        500: 12.8,
    }
    
    table737 = {
        0: 0,
        800: 3,
        900: 3,
    }
    
    table767 = {
        0: 8.4,
        400: 12.8,
    }
    
    table787 = {
        0: 8.4,
        10: 12.8,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            737 : (table737, 0),
            767 : (table767, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetF213(aircraftData):

    table = {
        0: 0,
        300: 6.2,
        321: 6.2,
        330: 6.2,
        350: 12.3,
        
        747: 10.3,
        757: 6.2,
        
        1000: 6.2,
        
        10: 6.2,
        11: 6.2,
        
        42: -3.9,
        72: -3.9,
        
        1008: -3.9,
        
        400: -3.9,
        130: -3.9,
    }
    
    table340 = {
        0: 8.4,
        500: 12.8,
    }
    
    table767 = {
        0: 6.2,
        400: 10.3,
    }
    
    table777 = {
        0: 10.3,
        300: 12.3,
    }
    
    table787 = {
        0: 6.2,
        10: 12.3,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetF214(aircraftData):

    table = {
        0: 0,
        300: 6.3,
        321: 6.3,
        330: 6.3,
        340: 6.3,
        350: 11.5,
        
        747: 10.3,
        757: 6.2,
        777: 10.2,
        
        1000: 6.3,
        
        10: 6.3,
        11: 6.3,
        
        42: 4,
        72: 4,
        
        1008: 4,
        
        400: 4,
        130: 4,
    }
    
    table767 = {
        0: 6.3,
        400: 10.2,
    }
    
    table787 = {
        0: 6.2,
        10: 11.5,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            767 : (table767, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetF215(aircraftData):

    table = {
        0: 0,
        300: 6,
        321: 6,
        330: 6,
        340: 6,
        350: 11.5,
        
        747: 11.5,
        757: 6,
        
        1000: 6,
        
        10: 6,
        11: 11.5,
        
        42: -5,
        72: -5,
        
        1008: -5,
        
        400: -5,
        130: -5,
    }
    
    table350 = {
        0: 11.5,
        1000: 14,
    }
    
    table767 = {
        0: 6,
        400: 11.5,
    }
    
    table777 = {
        0: 11.5,
        300: 12.7,
    }
    
    table787 = {
        0: 6,
        10: 11.5,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            350 : (table350, 900),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetF216(aircraftData):

    table = {
        0: 0,
        300: 6.2,
        321: 6.2,
        330: 6.2,
        340: 6.2,
        350: 11.5,
        
        757: 6.2,
        
        1000: 6.2,
        
        10: 6.2,
        11: 11.5,
        
        42: -5,
        72: -5,
        
        1008: -5,
        
        400: -5,
        130: -5,
    }
    
    table350 = {
        0: 11.5,
        1000: 14,
    }
    
    table767 = {
        0: 6.2,
        400: 11.5,
    }
    
    table787 = {
        0: 6.2,
        10: 11.5,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            350 : (table350, 900),
            767 : (table767, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetF221F223F225(aircraftData):

    table = {
        0: 0,
        319: -1.7,
        319: -1.7,
        321: 3.7,
        
        900: 3.7,
        1000: 3.7,
        
        42: -4.9,
        72: -4.9,
        
        1008: -4.9,
    }
    
    table737 = {
        0: 0,
        800: 3.7,
        900: 3.7,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetF222(aircraftData):

    table = {
        0: 0,
        310: -2.3,
        
        767: 2,
        
        11: 2,
        
        17: -2.3,
        130: -10.1,
        400: -10.1,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetF224(aircraftData):

    table = {
        0: 0, #CDE
        310: -5.8,
    }
    
    table767 = {
        0: 0,
        300: 3,
        400: 3,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            767 : (table767, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetF231(aircraftData):

    table = {
        0: 0,
        300: 8,
        321: 9.7,
        330: 11.5,
        350: 14.2,
        380: 11.5,
        
        757: 9.7,
        
        1000: 8,
        
        10: 8,
        11: 8,
    }
    
    table340 = {
        0: 11.5,
        600: 13,
    }
    
    table747 = {
        0: 11.5,
        8: 14.2,
    }
    
    table767 = {
        200: 8,
        0: 11.5,
    }
    
    table777 = {
        0: 11.5,
        300: 14.2,
    }
    
    table787 = {
        0: 11.5,
        10: 14.2,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            747 : (table747, 0),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetF232(aircraftData):

    table = {
        0: 0,
        300: 7,
        321: 8.2,
        330: 10.2,
        350: 13.2,
        380: 10.2,
        
        757: 8.2,
        
        1000: 7,
        
        10: 7,
        11: 7,
    }
    
    table340 = {
        0: 10.2,
        600: 11.9,
    }
    
    table747 = {
        0: 10.2,
        8: 13.2,
    }
    
    table767 = {
        200: 7,
        0: 10.2,
    }
    
    table777 = {
        0: 10.2,
        300: 13.2,
    }
    
    table787 = {
        0: 10.2,
        10: 13.2,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            747 : (table747, 0),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetF233(aircraftData):

    table = {
        0: 0,
        300: 2,
        321: 3.5,
        330: 3.5,
        350: 11.3,
        380: 9.9,
        
        747: 11.3,
        757: 3.5,
        
        1000: 2,
        
        10: 2,
        11: 3.5,
        
        130: -1.9,
    }
    
    table340 = {
        0: 3.5,
        600: 9.9,
    }
    
    table767 = {
        200: 2,
        0: 11.3,
    }
    
    table777 = {
        0: 0,
        300: 11.3,
    }
    
    table787 = {
        0: 3.5,
        10: 11.3,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetF234(aircraftData):

    table = {
        0: 0,
        300: 6.2,
        321: 6.2,
        330: 7.9,
        350: 11.8,
        380: 9.5,
        
        757: 6.2,
        787: 7.9,
        
        1000: 6.2,
        
        10: 6.2,
        11: 6.2,
        
        130: -2.5,
        400: -2.5,
    }
    
    table340 = {
        0: 7.9,
        600: 11.8,
    }
    
    table747 = {
        0: 7.9,
        8: 11.8,
    }
    
    table767 = {
        200: 6.2,
        0: 7.9,
    }
    
    table777 = {
        0: 7.9,
        300: 11.8,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            747 : (table747, 0),
            767 : (table767, 0),
            777 : (table777, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetF235(aircraftData):

    table = {
        0: 0,
        300: 6,
        321: 6,
        330: 9.7,
        350: 13.8,
        
        757: 6,
        787: 9.7,
        
        1000: 6,
        
        10: 6,
        11: 6,
        
        130: -1.9,
        400: -1.9,
    }
    
    table340 = {
        0: 9.7,
        600: 13.8,
    }
    
    table747 = {
        0: 9.7,
        8: 11.8,
    }
    
    table767 = {
        200: 6,
        0: 9.7,
    }
    
    table777 = {
        0: 9.7,
        300: 13.8,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            747 : (table747, 0),
            767 : (table767, 0),
            777 : (table777, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetF237(aircraftData):

    table = {
        0: 0, #B
        300: 6.5,
        321: 10,
        330: 10,
        350: 14.8,
        380: 10,
        
        757: 10,
        787: 10,
        
        10: 6.5,
        11: 6.5,
        82: 6.5,
        83: 6.5,
        87: 6.5,
        88: 6.5,
        90: 6.5,
        
        1000: 6.5,
    }
    
    table340 = {
        0: 10,
        600: 13.8,
    }
    
    table747 = {
        0: 10,
        8: 13.8,
    }
    
    table767 = {
        200: 6.5,
        0: 10,
    }
    
    table777 = {
        0: 10,
        300: 14.8,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            747 : (table747, 0),
            767 : (table767, 0),
            777 : (table777, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetF238(aircraftData):

    table = {
        0: 0, #B
        300: 6.4,
        321: 10.1,
        330: 10.1,
        350: 14.9,
        380: 10.1,
        
        757: 10.1,
        787: 10.1,
        
        10: 6.4,
        11: 6.4,
        82: 6.4,
        83: 6.4,
        87: 6.4,
        88: 6.4,
        90: 6.4,
        
        1000: 6.5,
    }
    
    table340 = {
        0: 10.1,
        600: 13.5,
    }
    
    table747 = {
        0: 10.1,
        8: 13.5,
    }
    
    table767 = {
        200: 6.4,
        0: 10.1,
    }
    
    table777 = {
        0: 10.1,
        300: 14.9,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            747 : (table747, 0),
            767 : (table767, 0),
            777 : (table777, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetV266ToV270(aircraftData):

    table = {
        0: 0, #AB
        321: 1.8,
        
        1000: 1.8,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetV93(aircraftData):

    table = {
        0: 0,
        
        190: 3,
        195: 3,
        
        900: 3,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetV94(aircraftData):

    table = {
        0: 0,
        221: 2.1,
        223: 5.5,
        320: 2.1,
        
        900: 6.5,
        1000: 6.5,
        
        190: 5.5,
        195: 5.5,
    }
    
    table737 = {
        0: 2.1,
        800: 6.5,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetV95V96V97(aircraftData):

    table = {
        0: 0,
        221: 2.8,
        223: 5.5,
        320: 2.8,
        
        900: 6.5,
        1000: 6.5,
        
        190: 5.5,
        195: 5.5,
    }
    
    table737 = {
        0: 2.8,
        800: 6.5,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetV106(aircraftData):

    table = {
        0: 0,
        321: 5.2,
        
        1000: 10.65,
    }
    
    table737 = {
        0: 0,
        900: 5.2,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetV107(aircraftData):

    table = {
        0: 0,
        321: 6.15,
        
        1000: 9.1,
    }
    
    table737 = {
        0: 0,
        900: 6.15,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetV108(aircraftData):

    table = {
        0: 0, #AB
        321: 4.3,
        
        1000: 4.3,
        
        82: 4.3,
        83: 4.3,
        88: 4.3,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetV109(aircraftData):

    table = {
        0: 0,
        321: 2.5,
        
        1000: 4.1,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetV110(aircraftData):

    table = {
        0: 0,
        300: 3,
        321: 4.3,
        
        757: 4.3,
        767: 4.3,
        
        82: 4.3,
        83: 4.3,
        88: 4.3,
        
        1000: 4.3,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetV111(aircraftData):

    table = {
        0: 0,
        300: 3.25,
        321: 3.25,
        
        757: 3.25,
        767: 5.1,
        
        82: 5.1,
        83: 5.1,
        88: 5.1,
        
        1000: 5.1,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetV112(aircraftData):

    table = {
        0: 0,
        321: 2.2,
        
        1000: 7.5,
    }
    
    table737 = {
        0: 0,
        900: 2.2,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetV113(aircraftData):

    table = {
        0: 0,
        300: 2.8,
        321: 3.9,
        
        757: 3.9,
        767: 5.2,
        
        82: 5.2,
        83: 5.2,
        88: 5.2,
        
        1000: 5.2,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetV114(aircraftData):

    table = {
        0: 0,
        300: 4,
        321: 5,
        
        757: 5,
        767: 5,
        
        82: 5,
        83: 5,
        88: 5,
        
        42: -2,
        72: -2,
        
        1008: -2,
        
        1000: 5,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetV115(aircraftData):

    table = {
        0: 0, #AB
        321: 5,
        
        1000: 5,
        
        82: 5,
        83: 5,
        88: 5,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetV116(aircraftData):

    table = {
        0: 0, #B
        321: 5,
        
        1000: 5,
        
        82: 5,
        83: 5,
        88: 5,
        
        42: -2.2,
        72: -2.2,
        
        1008: -2.2,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetV117(aircraftData):

    table = {
        0: 0,
        321: 7.5,
        
        1000: 7.5,
    }
    
    table737 = {
        0: 0,
        900: 7.5,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetV118(aircraftData):

    table = {
        0: 0,
        321: 5,
        
        1000: 10.4,
    }
    
    table737 = {
        0: 0,
        900: 5,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetV119(aircraftData):

    table = {
        0: 0, #B
        300: 4.5,
        321: 4.5,
        
        757: 4.5,
        767: 4.5,
        
        82: 4.5,
        83: 4.5,
        87: 4.5,
        88: 4.5,
        
        42: -2,
        72: -2,
        
        1008: -2,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetV120(aircraftData):

    table = {
        0: 0, #FG
        330: -4.1,
        340: -4.1,
        
        757: -4.1,
    }
    
    table787 = {
        0: -4.1,
        10: 0,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetV121(aircraftData):

    table = {
        0: 0,
        321: 4.5,
        
        900: 3.4,
        1000: 3.4,
        
        757: 4.5,
        767: 5.7,
        
        82: 5.7,
        83: 5.7,
        88: 5.7,
    }
    
    table737 = {
        0: 0,
        800: 5.7,
        900: 5.7,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetV122(aircraftData):

    table = {
        0: 0,
        747: 4,
        777: 5,
    }
    
    table340 = {
        0: 0,
        600: 5,
    }
    
    table350 = {
        0: 5,
        1000: 6,
    }
    
    table767 = {
        0: 0,
        400: 5,
    }
    
    table787 = {
        0: 0,
        10: 5,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            350 : (table350, 0),
            767 : (table767, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetV123(aircraftData):

    table = {
        0: 0,
        300: 2,
        321: 3,
        
        757: 3,
        767: 4.3,
        
        82: 4.3,
        83: 4.3,
        88: 4.3,
        
        42: -4.8,
        72: -4.8,
        
        1008: -4.8,
    }
    
    table737 = {
        0: 0,
        900: 4.3,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetV124(aircraftData):

    table = {
        0: 0,
    }
    
    table350 = {
        0: 1.85,
        1000: 3.1,
    }
    
    table777 = {
        0: 0,
        300: 1.85,
    }
    
    table787 = {
        0: 0,
        10: 1.85,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            350 : (table350, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetV125(aircraftData):

    table = {
        0: 0,
        300: 5.4,
        321: 5.4,
        
        757: 5.4,
        
        82: 5.4,
        83: 5.4,
        88: 5.4,
        
        42: -2,
        72: -2,
        
        1008: -2,
    }
    
    table737 = {
        0: 0,
        900: 5.4,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetV126(aircraftData):

    table = {
        0: 0,
        221: 1.6,
        223: 1.6,
        310: 1.6,
        320: 1.6,
        321: 5.5,
        
        757: 5.5,
        
        170: 1.6,
        175: 1.6,
        190: 1.6,
        195: 1.6,
        
        82: 8.5,
        83: 8.5,
        88: 8.5,
        
        1000: 5.5,
    }
    
    table737 = {
        0: 0,
        700: 1.6,
        800: 5.5,
        900: 5.5,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetV127(aircraftData):

    table = {
        0: 0,
        330: -3.5,
    }
    
    table340 = {
        0: -3.5,
        600: 0,
    }
    
    table350 = {
        0: 0,
        1000: 1.7,
    }
    
    table767 = {
        0: 0,
        400: 1.7,
    }
    
    table777 = {
        0: 0,
        300: 1.7,
    }
    
    table787 = {
        0: -3.5,
        10: 1.7,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            350 : (table350, 0),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetV128(aircraftData):

    table = {
        0: 0,
        300: 4.2,
        320: 1.6,
        321: 5.3,
        
        757: 5.3,
        767: 5.3,
        
        82: 5.3,
        83: 5.3,
        88: 5.3,
    }
    
    table737 = {
        0: 0,
        800: 4.2,
        900: 4.2,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetV129(aircraftData):

    table = {
        0: 0,
        350: 5.95,
    }
    
    table767 = {
        0: 0,
        400: 5.95,
    }
    
    table777 = {
        0: 0,
        300: 4.75,
    }
    
    table787 = {
        0: 0,
        10: 4.75,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetV130(aircraftData):

    table = {
        0: 0, #AB
        300: 6.3,
        321: 6.3,
        
        757: 6.3,
        
        82: 6.3,
        83: 6.3,
        87: 6.3,
        88: 6.3,
        90: 6.3,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetV134V136(aircraftData):

    table = {
        0: 0, #B
        321: 4.6,
        
        1000: 3.2,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetV135V152(aircraftData):

    table = {
        0: 0, #BCDE
        350: 8.3, 
        380: 4.9,
    }
    
    table340 = {
        0: 0,
        600: 8.3,
    }
    
    table747 = {
        0: 4.9,
        8: 8.3,
    }
    
    table767 = {
        0: 0,
        400: 4.9,
    }
    
    table777 = {
        0: 4.9,
        300: 8.3,
    }
    
    table787 = {
        0: 0,
        10: 4.9,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            747 : (table747, 0),
            767 : (table767, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetV151V153(aircraftData):

    table = {
        0: 0, #B
        321: 4.7,
        
        1000: 3.2,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetV157(aircraftData):

    table = {
        0: 0, #B
        321: 6.1,
        
        1000: 6.1,
        
        42: -2.9,
        72: -2.9,
        
        1008: -2.9,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetV158(aircraftData):

    table = {
        0: 0, #B
        300: 6.6,
        321: 7.9,
        
        757: 7.9,
        767: 6.6,
        
        82: 6.6,
        83: 6.6,
        87: 6.6,
        88: 6.6,
        90: 6.6,
        
        1000: 6.6,
        
        42: -5.4,
        72: -5.4,
        
        1008: -5.4,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetV159(aircraftData):

    table = {
        0: 0, #DE
        747: 2.9,
        767: 2.9,
    }
    
    table340 = {
        0: 0,
        500: 2.9,
        600: 6,
    }
    
    table777 = {
        0: 2.9,
        300: 6,
    }
    
    table787 = {
        0: 0,
        10: 2.9,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetV160(aircraftData):

    table = {
        0: 0, #B A124
        300: 3.4,
        321: 3.4,
        380: 3.4,
        
        747: 7.45,
        757: 3.4,
        767: 3.4,
        
        1000: 3.4,
        
        82: 3.4,
        83: 3.4,
        87: 3.4,
        88: 3.4,
        90: 3.4,
        
        42: -6.4,
        72: -6.4,
        
        1008: -6.4,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetV162(aircraftData):

    table = {
        0: 0, #AB
        300: 6,
        321: 6,
        
        757: 6,
        
        1000: 6,
        
        82: 6,
        83: 6,
        88: 6,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetV163(aircraftData):

    table = {
        0: 0, #B
        300: 4.5,
        321: 4.5,
        
        757: 4.5,
        
        1000: 4.5,
        
        82: 4.5,
        83: 4.5,
        88: 4.5,
        
        42: -6.5,
        72: -6.5,
        
        1008: -6.5,
        
        130: -6.5,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetV164(aircraftData):

    table = {
        0: 0, #AB
        300: 4.5,
        321: 4.5,
        330: 4.5,
        350: 11.8,
        
        747: 9.8,
        757: 4.5,
        
        1000: 4.5,
        
        10: 4.5,
        11: 4.5,
        82: 4.5,
        83: 4.5,
        87: 4.5,
        88: 4.5,
        90: 4.5,
    }
    
    table340 = {
        0: 4.5,
        500: 9.8,
        600: 9.8,
    }
    
    table767 = {
        0: 4.5,
        300: 9.8,
    }
    
    table777 = {
        0: 9.8,
        300: 11.8,
    }
    
    table787 = {
        0: 4.5,
        10: 9.8,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )



@AlternativeStopPositions
def customOffsetV166V167(aircraftData):

    table = {
        0: 0, #AB
        300: 5.3,
        321: 5.3,
        330: 5.3,
        350: 12.5,
        
        747: 10.8,
        757: 5.3,
        
        10: 5.3,
        11: 5.3,
        82: 5.3,
        83: 5.3,
        87: 5.3,
        88: 5.3,
        90: 5.3,
    }
    
    table340 = {
        0: 5.3,
        500: 10.8,
        600: 10.8,
    }
    
    table767 = {
        0: 4.5,
        300: 10.8,
    }
    
    table777 = {
        0: 10.8,
        300: 12.5,
    }
    
    table787 = {
        0: 5.3,
        10: 10.8,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetV168V169(aircraftData):

    table = {
        0: 0, #AB
        300: 5.3,
        321: 5.3,
        330: 5.3,
        350: 12.8,
        
        747: 10.8,
        757: 5.3,
        
        10: 5.3,
        11: 5.3,
        82: 5.3,
        83: 5.3,
        87: 5.3,
        88: 5.3,
        90: 5.3,
    }
    
    table340 = {
        0: 5.3,
        500: 10.8,
        600: 10.8,
    }
    
    table767 = {
        0: 4.5,
        300: 10.8,
    }
    
    table777 = {
        0: 10.8,
        300: 12.8,
    }
    
    table787 = {
        0: 5.3,
        10: 10.8,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetV170(aircraftData):

    table = {
        0: 0, #AB
        300: 5.3,
        321: 5.3,
        330: 5.3,
        350: 13,
        
        747: 10.8,
        757: 5.3,
        
        10: 5.3,
        11: 5.3,
        82: 5.3,
        83: 5.3,
        87: 5.3,
        88: 5.3,
        90: 5.3,
    }
    
    table340 = {
        0: 5.3,
        500: 10.8,
        600: 10.8,
    }
    
    table767 = {
        0: 4.5,
        300: 10.8,
    }
    
    table777 = {
        0: 10.8,
        300: 13,
    }
    
    table787 = {
        0: 5.3,
        10: 10.8,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )



@AlternativeStopPositions
def customOffsetV171(aircraftData):

    table = {
        0: 0, #B
        300: 5.3,
        321: 8.8,
        
        757: 8.8,
        
        10: 5.3,
        11: 5.3,
        82: 5.3,
        83: 5.3,
        87: 5.3,
        88: 5.3,
        90: 5.3,
        
        42: -4.5,
        72: -4.5,
        
        1008: -4.5,
        
        130: -4.5,
    }
    
    table767 = {
        0: 5.3,
        300: 8.8,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            767 : (table767, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetV172V173V174V175V177(aircraftData):

    table = {
        0: 0, #B
        300: 5.5,
        321: 8.25,
        
        757: 8.25,
        
        10: 5.5,
        11: 5.5,
        82: 5.5,
        83: 5.5,
        87: 5.5,
        88: 5.5,
        90: 5.5,
        
        42: -4.5,
        72: -4.5,
        
        1008: -4.5,
        
        130: -4.5,
    }
    
    table767 = {
        0: 5.5,
        300: 8.25,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            767 : (table767, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetV176(aircraftData):

    table = {
        0: 0, #AB
        321: 5.1,
        
        1000: 9.2,
        
        82: 9.2,
        83: 9.2,
        87: 9.2,
        88: 9.2,
        90: 9.2,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetV178(aircraftData):

    table = {
        0: 0, #AB
        321: 6.1,
        
        1000: 10.2,
        
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetV702(aircraftData):

    table = {
        0: 0,
        321: 4.1,
    }
    
    table737 = {
        0: 0,
        900: 4.1,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetV704V706V708(aircraftData):

    table = {
        0: 0,
        321: 3.9,
    }
    
    table737 = {
        0: 0,
        900: 3.9,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetS501S503S506S507S508(aircraftData):

    table = {
        0: 0, #B, AB
        300: 6,
        321: 6,
        330: 6,
        340: 6,
        
        747: 10.45,
        757: 6,
        777: 10.45,
        
        10: 6,
        11: 6,
        82: 6,
        83: 6,
        87: 6,
        88: 6,
        90: 6,
    }
    
    table767 = {
        200: 0,
        0: 10.45,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            767 : (table767, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetS504S505(aircraftData):

    table = {
        0: 0,
        310: -6,
        319: -6,
        320: -6,
        
        737: -6,
        747: 4.4,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetS601S603(aircraftData):

    table = {
        0: 0, #AB
        300: 7.8,
        321: 7.8,
        330: 7.8,
        340: 7.8,
        350: 12.7,
        
        757: 7.8,
        777: 12.7,
        
        11: 7.8,
    }
    
    table747 = {
        0: 12.7,
        8: 19,
    }
    
    table767 = {
        200: 7.8,
        0: 12.7,
    }
    
    table787 = {
        0: 7.8,
        10: 12.7,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            747 : (table747, 0),
            767 : (table767, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetS602(aircraftData):

    table = {
        0: 0, #B
        300: 5,
        321: 7.2,
        330: 7.2,
        340: 7.2,
        350: 10.2,
        
        747: 10.2,
        757: 7.2,
        777: 10.2,
        
        11: 5,
        
        130: -2,
        #CD 5,
    }
    
    table767 = {
        200: 5,
        0: 10.2
    }
    
    table787 = {
        0: 7.2,
        10: 12.7,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            767 : (table767, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetS604(aircraftData):

    table = {
        0: 0, #AB
        300: 6.5,
        321: 6.5,
        330: 6.5,
        340: 6.5,
        350: 11.45,
        
        757: 6.5,
        777: 11.45,
        
        11: 6.5,
    }
    
    table747 = {
        0: 11.45,
        8: 17.9,
    }
    
    table767 = {
        200: 6.5,
        0: 11.45,
    }
    
    table787 = {
        0: 6.5,
        10: 11.45,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            747 : (table747, 0),
            767 : (table767, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetK2(aircraftData):

    table = {
        0: 0,
        321: 5.8,
        
        1000: 5.8,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


@AlternativeStopPositions
def customOffsetK4(aircraftData):

    table = {
        0: 0,
        300: 5.1,
        321: 9.3,
        330: 9.3,
        350: 12.5,
        
        747: 9.3,
        757: 9.3,
        767: 9.3,
        787: 9.3,
        
        1000: 5.1,
    }
    
    table340 = {
        0: 9.3,
        600: 12.5,
    }
    
    
    table777 = {
        0: 9.3,
        300: 12.5,
    }
    
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            777 : (table777, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetK6(aircraftData):

    table = {
        0: 0,
        300: 4.1,
        321: 9.3,
        330: 9.3,
        350: 12.5,
        
        757: 9.3,
        767: 9.3,
        
        1000: 4.1,
    }
    
    table340 = {
        0: 9.3,
        600: 12.5,
    }
    
    table747 = {
        0: 9.3,
        8: 12.5,
    }
    
    table777 = {
        0: 9.3,
        300: 12.5,
    }
    
    table787 = {
        0: 9.3,
        10: 12.5,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            747 : (table747, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetK8K10(aircraftData):

    table = {
        0: 0,
        300: 4.2,
        321: 8.5,
        330: 8.5,
        350: 12.5,
        
        757: 8.5,
        767: 8.5,
        
        1000: 4.2,
    }
    
    table340 = {
        0: 8.5,
        600: 12.5,
    }
    
    table747 = {
        0: 8.5,
        8: 12.5,
    }
    
    table777 = {
        0: 8.5,
        300: 12.5,
    }
    
    table787 = {
        0: 8.5,
        10: 12.5,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            747 : (table747, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )


@AlternativeStopPositions
def customOffsetV322V324V326V328(aircraftData):

    table = {
        0: 0, #B
        300: 5.1,
        321: 7.7,
        330: 7.7,
        350: 10.85,
        
        757: 7.7,
        767: 7.7,
        787: 7.7,
        
        11: 7.7,
        82: 5.1,
        83: 5.1,
        87: 5.1,
        88: 5.1,
        90: 5.1,
        
        1000: 5.1,
    }
    
    table340 = {
        0: 7.7,
        600: 10.85,
    }
    
    table747 = {
        0: 7.7,
        8: 10.85,
    }
    
    table777 = {
        0: 7.7,
        300: 10.85,
    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            747 : (table747, 0),
            777 : (table777, 0),
        },
        table) )


#Category names

Terminal1ASE = CustomizedName("Terminal 1 - A Gates [SE] (A1-A40 (V143+V144)) | Gate A#§",1)
Terminal1VSE = CustomizedName("Terminal 1 - A Gates [SE] (A1-A40 (V143+V144)) | Gate V#§",1)
Terminal1AN = CustomizedName("Terminal 1 - A Gates [N] (A50-A69) | Gate A#§",2)

Terminal1BW = CustomizedName("Terminal 1 - B Gates [W] (B10-B28) | Gate B#§",3)
Terminal1BE = CustomizedName("Terminal 1 - B Gates [E] (B41-B48) | Gate B#§",4)

Terminal1CW = CustomizedName("Terminal 1 - C Gates [W] (C2-C11) | Gate C#§",5)
Terminal2CE = CustomizedName("Terminal 2 - C Gates [E] (C13-C16) | Gate C#§",6)

Terminal2DW = CustomizedName("Terminal 2 - D Gates [W] (D1-D8) | Gate D#§",7)
Terminal2EE = CustomizedName("Terminal 2 - E Gates [E] (E2-E9) | Gate E#§",8)

LHCargo = CustomizedName("LH Cargo Ramp (F211-F225) | Stand F#§",9)
NECargoF = CustomizedName("NE Cargo Ramp (F231-V270) | Stand F#§",10)
NECargoV = CustomizedName("NE Cargo Ramp (F231-V270) | Stand V#§",10)

VRampE = CustomizedName("Victor Ramp [E] (V93-V118) | Stand V#§",11)
VRampCE = CustomizedName("Victor Ramp [Center E] (V119-V130) | Stand V#§",12)
VRampCW = CustomizedName("Victor Ramp [Center W] (V134-V163) | Stand V#§",13)
VRampW = CustomizedName("Victor Ramp [W] (V164-V178) | Stand V#§",14)

GAArea = CustomizedName("GA Area [S] (V701-V721) | Stand V#",15)

SRamp = CustomizedName("Old GA Area [S] (S401-S420) | Stand S#",16)
SHRamp = CustomizedName("Old GA Area [S] (S401-S420) | Stand S#/H#",16)

SERamp = CustomizedName("Sierra Cargo Ramp [SE] (S501-S604) | Stand S#",17)

Terminal3EJ = CustomizedName("Construction Terminal 3 (K2-K10 V322-V328) | Gate J#§",20)
Terminal3EK = CustomizedName("Construction Terminal 3 (K2-K10 V322-V328) | Gate K#§",20)

VRampSW = CustomizedName("Construction Terminal 3 (K2-K10 V322-V328) | Stand V#§",20)


parkings = {

    GATE_A : {
        None : ( ),
        1 : (Terminal1ASE, customOffsetA1, ),
        11 : (Terminal1ASE, customOffsetA11, ),
        13 : (Terminal1ASE, customOffsetA13, ),
        14 : (Terminal1ASE, customOffsetA14, ),
        15 : (Terminal1ASE, customOffsetA15, ),
        16 : (Terminal1ASE, customOffsetA16, ),
        17 : (Terminal1ASE, customOffsetA17, ),
        18 : (Terminal1ASE, customOffsetA18, ),
        19 : (Terminal1ASE, customOffsetA19, ),
        20 : (Terminal1ASE, customOffsetA20, ),
        21 : (Terminal1ASE, customOffsetA21, ),
        22 : (Terminal1ASE, customOffsetA22, ),
        23 : (Terminal1ASE, customOffsetA23, ),
        24 : (Terminal1ASE, customOffsetA24, ),
        25 : (Terminal1ASE, customOffsetA25, ),
        26 : (Terminal1ASE, customOffsetA26, ),
        28 : (Terminal1ASE, customOffsetA28, ),
        30 : (Terminal1ASE, customOffsetA30, ),
        34 : (Terminal1ASE, customOffsetA34, ),
        36 : (Terminal1ASE, customOffsetA36, ),
        38 : (Terminal1ASE, customOffsetA38, ),
        40 : (Terminal1ASE, customOffsetA40, ),
        
        50 : (Terminal1AN, customOffsetA50, ),
        52 : (Terminal1AN, customOffsetA52, ),
        54 : (Terminal1AN, customOffsetA54A58A62A66, ),
        "54A" : (Terminal1AN, customOffsetA54586266A, ),
        "54B" : (Terminal1AN, customOffsetA545862B, ),
        58 : (Terminal1AN, customOffsetA54A58A62A66, ),
        "58A" : (Terminal1AN, customOffsetA54586266A, ),
        "58B" : (Terminal1AN, customOffsetA545862B, ),
        62 : (Terminal1AN, customOffsetA54A58A62A66, ),
        "62A" : (Terminal1AN, customOffsetA54586266A, ),
        "62B" : (Terminal1AN, customOffsetA545862B, ),
        66 : (Terminal1AN, customOffsetA54A58A62A66, ),
        "66A" : (Terminal1AN, customOffsetA54586266A, ),
        "66B" : (Terminal1AN, customOffsetA66B, ),
        69 : (Terminal1AN, customOffsetA69, ),
    },

    GATE_B : {
        None : ( ),
        10 : (Terminal1BW, customOffsetB10, ),
        20 : (Terminal1BW, customOffsetB20, ),
        22 : (Terminal1BW, customOffsetB22, ),
        23 : (Terminal1BW, customOffsetB23, ),
        24 : (Terminal1BW, customOffsetB24, ),
        25 : (Terminal1BW, customOffsetB25, ),
        26 : (Terminal1BW, customOffsetB26, ),
        27 : (Terminal1BW, customOffsetB27, ),
        28 : (Terminal1BW, customOffsetB28, ),
        
        41 : (Terminal1BE, customOffsetB41, ),
        42 : (Terminal1BE, customOffsetB42, ),
        43 : (Terminal1BE, customOffsetB43, ),
        44 : (Terminal1BE, customOffsetB44, ),
        45 : (Terminal1BE, customOffsetB45, ),
        46 : (Terminal1BE, customOffsetB46, ),
        47 : (Terminal1BE, customOffsetB47, ),
        48 : (Terminal1BE, customOffsetB48, ),
    },

    GATE_C : {
        None : ( ),
        2 : (Terminal1CW, customOffsetC2, ),
        4 : (Terminal1CW, customOffsetC4, ),
        5 : (Terminal1CW, customOffsetC5, ),
        6 : (Terminal1CW, customOffsetC6, ),
        8 : (Terminal1CW, customOffsetC8, ),
        11 : (Terminal1CW, customOffsetC11, ),
        
        13 : (Terminal2CE, customOffsetC13, ),
        14 : (CustomizedName("Terminal 2 - C Gates [E] (C13-C16) | Gate C#§/S",6), customOffsetC14, ),
        "14S" :(Terminal2CE, customOffsetequal, ),
        15 : (CustomizedName("Terminal 2 - C Gates [E] (C13-C16) | Gate C#§/S",6), customOffsetC15, ),
        "15A" : (Terminal2CE, customOffsetequal, ),
        "15S" : (Terminal2CE, customOffsetequal, ),
        "15B" : (Terminal2CE, customOffsetC15B, ),
        16: (CustomizedName("Terminal 2 - C Gates [E] (C13-C16) | Gate C#§/S",6), customOffsetC16, ),
        "16S" : (Terminal2CE, customOffsetequal, ),
        "16A" : (Terminal2CE, customOffsetC16A, ),
        "16B" : (Terminal2CE, customOffsetC16B, ),
    },

    GATE_D : {
        None : ( ),
        1 : (Terminal2DW, customOffsetD1, ),
        "1A" : (Terminal2DW, customOffsetD1A, ),
        4 : (Terminal2DW, customOffsetD4, ),
        "4A" : (Terminal2DW, customOffsetD4A, ),
        "4B" : (Terminal2DW, customOffsetD4B, ),
        5 : (Terminal2DW, customOffsetD5, ),
        "5A" : (Terminal2DW, customOffsetD5A, ),
        8 : (Terminal2DW, customOffsetD8, ),
        "8A" : (Terminal2DW, customOffsetequal, ),
    },

    GATE_E : {
        None : ( ),
        2 : (Terminal2EE, customOffsetE2, ),
        "2A" : (Terminal2EE, customOffsetE2A, ),
        "2B" : (Terminal2EE, customOffsetE2B, ),
        5 : (Terminal2EE, customOffsetE5, ),
        "5A" : (Terminal2EE, customOffsetE5A, ),
        "5B" : (Terminal2EE, customOffsetE5B, ),
        6 : (Terminal2EE, customOffsetE6, ),
        "6A" : (Terminal2EE, customOffsetequal, ),
        9 : (Terminal2EE, customOffsetE9, ),
        "9A" : (Terminal2EE, customOffsetequal, ),
    },

    GATE_F : {
        None : ( ),
        211 : (LHCargo, customOffsetF211, ),
        212 : (LHCargo, customOffsetF212, ),
        213 : (LHCargo, customOffsetF213, ),
        214 : (LHCargo, customOffsetF214, ),
        215 : (LHCargo, customOffsetF215, ),
        216 : (LHCargo, customOffsetF216, ),
        221 : (LHCargo, customOffsetF221F223F225, ),
        222 : (CustomizedName("LH Cargo Ramp (F211-F225) | Stand F#§ / F221",9), customOffsetF222, ),
        223 : (LHCargo, customOffsetF221F223F225, ),
        224 : (CustomizedName("LH Cargo Ramp (F211-F225) | Stand F#§ / F225",9), customOffsetF224, ),
        225 : (LHCargo, customOffsetF221F223F225, ),
        
        231 : (NECargoF, customOffsetF231, ),
        232 : (NECargoF, customOffsetF232, ),
        233 : (NECargoF, customOffsetF233, ),
        234 : (NECargoF, customOffsetF234, ),
        235 : (NECargoF, customOffsetF235, ),
        237 : (NECargoF, customOffsetF237, ),
        238 : (NECargoF, customOffsetF238, ),
    },

    GATE_S : {
        None : ( ),
        401 : (SHRamp, customOffsetequal, ),
        402 : (SHRamp, customOffsetequal, ),
        403 : (SRamp, customOffsetequal, ),
        404 : (SRamp, customOffsetequal, ),
        405 : (SRamp, customOffsetequal, ),
        406 : (SRamp, customOffsetequal, ),
        407 : (SRamp, customOffsetequal, ),
        408 : (SRamp, customOffsetequal, ),
        409 : (SRamp, customOffsetequal, ),
        410 : (SRamp, customOffsetequal, ),
        411 : (SRamp, customOffsetequal, ),
        412 : (SRamp, customOffsetequal, ),
        413 : (SRamp, customOffsetequal, ),
        414 : (SRamp, customOffsetequal, ),
        416 : (SRamp, customOffsetequal, ),
        418 : (SRamp, customOffsetequal, ),
        420 : (SRamp, customOffsetequal, ),
        
        501 : (SERamp, customOffsetS501S503S506S507S508, ),
        503 : (SERamp, customOffsetS501S503S506S507S508, ),
        504 : (SERamp, customOffsetS504S505, ),
        505 : (SERamp, customOffsetS504S505, ),
        506 : (SERamp, customOffsetS501S503S506S507S508, ),
        507 : (SERamp, customOffsetS501S503S506S507S508, ),
        508 : (SERamp, customOffsetS501S503S506S507S508, ),
        601 : (SERamp, customOffsetS601S603, ),
        602 : (SERamp, customOffsetS602, ),
        603 : (SERamp, customOffsetS601S603, ),
        604 : (SERamp, customOffsetS604, ),
    },
    
    GATE_V : {
        None : ( ),
        93 : (VRampE, customOffsetV93, ),
        94 : (VRampE, customOffsetV94, ),
        95 : (VRampE, customOffsetV95V96V97, ),
        96 : (VRampE, customOffsetV95V96V97, ),
        97 : (VRampE, customOffsetV95V96V97, ),
        106 : (VRampE, customOffsetV106, ),
        107 : (VRampE, customOffsetV107, ),
        108 : (VRampE, customOffsetV108, ),
        109 : (VRampE, customOffsetV109, ),
        110 : (VRampE, customOffsetV110, ),
        111 : (VRampE, customOffsetV111, ),
        112 : (VRampE, customOffsetV112, ),
        113 : (VRampE, customOffsetV113, ),
        114 : (VRampE, customOffsetV114, ),
        115 : (VRampE, customOffsetV115, ),
        116 : (VRampE, customOffsetV116, ),
        117 : (VRampE, customOffsetV117, ),
        118 : (VRampE, customOffsetV118, ),
        
        119 : (VRampCE, customOffsetV119, ),
        120 : (VRampCE, customOffsetV120, ),
        121 : (VRampCE, customOffsetV121, ),
        122 : (VRampCE, customOffsetV122, ),
        123 : (VRampCE, customOffsetV123, ),
        124 : (VRampCE, customOffsetV124, ),
        125 : (VRampCE, customOffsetV125, ),
        126 : (VRampCE, customOffsetV126, ),
        127 : (VRampCE, customOffsetV127, ),
        128 : (VRampCE, customOffsetV128, ),
        129 : (VRampCE, customOffsetV129, ),
        130 : (VRampCE, customOffsetV130, ),
        
        134 : (VRampCW, customOffsetV134V136, ),
        135 : (VRampCW, customOffsetV135V152, ),
        136 : (VRampCW, customOffsetV134V136, ),
        
        143 : (Terminal1VSE, customOffsetV143, ),
        144 : (Terminal1VSE, customOffsetV144, ),
        
        151 : (VRampCW, customOffsetV151V153, ),
        152 : (VRampCW, customOffsetV135V152, ),
        153 : (VRampCW, customOffsetV151V153, ),
        157 : (VRampCW, customOffsetV157, ),
        158 : (VRampCW, customOffsetV158, ),
        159 : (VRampCW, customOffsetV159, ),
        160 : (VRampCW, customOffsetV160, ),
        161 : (VRampCW, customOffsetequal, ),
        162 : (VRampCW, customOffsetV162, ),
        163 : (VRampCW, customOffsetV163, ),
        
        164 : (VRampW, customOffsetV164, ),
        166 : (VRampW, customOffsetV166V167, ),
        167 : (VRampW, customOffsetV166V167, ),
        168 : (VRampW, customOffsetV168V169, ),
        169 : (VRampW, customOffsetV168V169, ),
        170 : (VRampW, customOffsetV170, ),
        171 : (CustomizedName("Victor Ramp [W] (V164-V178) | Stand V#§/A",14), customOffsetV171, ),
        "171A" : (VRampW, customOffsetequal, ),
        "171B" : (VRampW, customOffsetequal, ),
        172 : (VRampW, customOffsetV172V173V174V175V177, ),
        173 : (CustomizedName("Victor Ramp [W] (V164-V178) | Stand V#§/B",14), customOffsetV172V173V174V175V177, ),
        "173A" : (VRampW, customOffsetequal, ),
        "173B" : (VRampW, customOffsetequal, ),
        174 : (VRampW, customOffsetV172V173V174V175V177, ),
        175 : (VRampW, customOffsetV172V173V174V175V177, ),
        176 : (VRampW, customOffsetV176, ),
        177 : (VRampW, customOffsetV172V173V174V175V177, ),
        178 : (VRampW, customOffsetV178, ),
        
        266 : (NECargoV, customOffsetV266ToV270, ),
        267 : (NECargoV, customOffsetV266ToV270, ),
        268 : (NECargoV, customOffsetV266ToV270, ),
        269 : (NECargoV, customOffsetV266ToV270, ),
        270 : (NECargoV, customOffsetV266ToV270, ),
        
        322 : (VRampSW, customOffsetV322V324V326V328, ),
        324 : (VRampSW, customOffsetV322V324V326V328, ),
        326 : (VRampSW, customOffsetV322V324V326V328, ),
        328 : (VRampSW, customOffsetV322V324V326V328, ),
        
        701 : (GAArea, customOffsetequal, ),
        702 : (GAArea, customOffsetV702, ),
        704 : (GAArea, customOffsetV704V706V708, ),
        706 : (GAArea, customOffsetV704V706V708, ),
        708 : (GAArea, customOffsetV704V706V708, ),
        711 : (GAArea, customOffsetequal, ),
        712 : (GAArea, customOffsetequal,  ),
        713 : (GAArea, customOffsetequal, ),
        714 : (GAArea, customOffsetequal, ),
        715 : (GAArea, customOffsetequal, ),
        716 : (GAArea, customOffsetequal, ),
        717 : (GAArea, customOffsetequal, ),
        718 : (GAArea, customOffsetequal, ),
        719 : (GAArea, customOffsetequal, ),
        721 : (GAArea, customOffsetequal, ),
    },

    GATE_K : {
        None : ( ),
        2 : (Terminal3EK, customOffsetK2, ),
        4  :(Terminal3EK, customOffsetK4, ),
        6 : (Terminal3EK, customOffsetK6, ),
        8 : (Terminal3EK, customOffsetK8K10, ),
        10 :(Terminal3EK, customOffsetK8K10, ),
    },

}
