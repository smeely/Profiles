# -- coding: utf-8 --

msfs_mode = 1
icao = "eddk"

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
def MyCustomOffsetsA30(aircraftData):

    table = {
        0: 0,
        321: 9.5,
        757: 9.5,

    }

    table737 = {
        0: 0,
        800: 4.8,
        900: 9.5,
        }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsetsA28(aircraftData):

    table = {
        0: 0,
        321: 4.4,
        757: 4.4,

    }

    table737 = {
        0: 0,
        800: 4.4,
        900: 4.4,
        }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsetsA26(aircraftData):

    table = {
        0: 0,
        321: 9.5,
        757: 9.5,

    }

    table737 = {
        0: 0,
        800: 5.1,
        900: 9.5,
        }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsetsA24(aircraftData):

    table = {
        0: 0,
        321: 9.7,
        757: 9.7,

    }

    table737 = {
        0: 0,
        800: 5.1,
        900: 9.7,
        }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsetsA21(aircraftData):

    table = {
        0: 0,
        321: 7.3,
        757: 7.3,

    }

    table737 = {
        0: 0,
        800: 5.3,
        900: 7.3,
        }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsetsA18(aircraftData):

    table = {
        0: 0,
        321: 5,
        757: 5,

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
def MyCustomOffsetsB30(aircraftData):

    table = {
        0: 0,
        319: -4

    }

    table737 = {
        0: -4,
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
def MyCustomOffsetsB20to22(aircraftData):

    table = {
        0: 0,
        321: 4,
        757: 4,

    }

    table737 = {
        0: 0,
        800: 4,
        900: 4,
        }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsetsB26(aircraftData):

    table = {
        0: 0,
        321: 3.8,
        757: 3.8,

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
def MyCustomOffsetsB18(aircraftData):

    table = {
        0: 0,
        321: 3.4,
        757: 3.4,

    }

    table737 = {
        0: 0,
        800: 3.4,
        900: 3.4,
        }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsetsB16(aircraftData):

    table = {
        0: 0,
        319: -4.5,

    } 
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsetsC06(aircraftData):

    table = {
        0: 0,
        321: 5.6,
        757: 5.6,

    }

    table737 = {
        0: 0,
        900: 5.6,
        }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsetsC10(aircraftData):

    table = {
        0: 0,
        757: 4,

    }

    table737 = {
        0: 0,
        900: 4,
        }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsetsC12(aircraftData):

    table = {
        0: 0,
        321: 3.6,
        757: 3.6,

    }

    table737 = {
        0: 0,
        900: 3.6,
        }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsetsC14(aircraftData):

    table = {
        0: 0,
        757: 3.8,

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
def MyCustomOffsetsD24(aircraftData):

    table = {
        0: 0,
        321: 5,
        757: 5,

    }

    table737 = {
        0: 0,
        900: 5
        }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsetsD26(aircraftData):

    table = {
        0: 0,
        321: 4,
        757: 7.1,

    }

    table737 = {
        0: 0,
        900: 4,
        }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsetsD36(aircraftData):

    table = {
        0: 0,
        321: 3.8,
        757: 3.8,

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
def MyCustomOffsetsD42(aircraftData):

    table = {
        0: 0,
        321: 6.6,
        757: 6.6,

    }

    table737 = {
        0: 0,
        900: 6.6,
        }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsetsD64(aircraftData):

    table = {
        0: 0,
        321: 4.7,
        757: 4.7,

    }

    table737 = {
        0: 0,
        800: 4.7,
        900: 4.7,
        }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsetsE09(aircraftData):

    table = {
        0: 0,
        747: 4.2,
        330: 4.2,

    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsetsE13to46(aircraftData):

    table = {
        0: 0,
        747: 12.7,
        757: 5,
        777: 5,
        330: 5,
        321: 5,
        737: 5,

    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsetsF21(aircraftData):

    table = {
        0: 0,
        747: 10.6,
        757: 5.3,
        330: 5.3,
        777: 5.3,
        321: 5.3,
        737: 5.3,

    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsetsF34(aircraftData):

    table = {
        0: 0,
        747: 3,
        757: 3,
        777: 3,
        330: 3,
        321: 3,
        737: 3,

    }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
        },
        table) )


ApronA = CustomizedName("Apron A | Stand A#", 1)
ApronB = CustomizedName("Apron B | Stand B#", 2)
ApronC = CustomizedName("Apron C | Stand C#", 3)
ApronD = CustomizedName("Apron D | Stand D#", 4)
ApronE = CustomizedName("Apron E | Stand E#", 5)
ApronF = CustomizedName("Apron F | Stand F#", 6)
ApronU = CustomizedName("Apron U | Stand U#", 7)
ApronV = CustomizedName("Apron V | Stand V#", 8)
ApronW = CustomizedName("Apron W | Stand W#", 9)
InoperableE = CustomizedName("Apron E | Stand E# INOP", 5)
InoperableF = CustomizedName("Apron F | Stand F# INOP", 6)





parkings = {
    GATE_A : {
        None : ( ),
     
        1 : (ApronA, ),
        3 : (ApronA, ),
        5 : (ApronA, ),
        10 : (ApronA, MyCustomOffsetsA18, ),
        11 : (ApronA, MyCustomOffsetsA21, ),
        12 : (ApronA, MyCustomOffsetsA18, ),
        14 : (ApronA, MyCustomOffsetsA18, ),
        16 : (ApronA, MyCustomOffsetsA18, ),
        17 : (ApronA, MyCustomOffsetsA21, ),
        18 : (ApronA, MyCustomOffsetsA18, ),
        21 : (ApronA, MyCustomOffsetsA21, ),
        24 : (ApronA, MyCustomOffsetsA24, ),
        26 : (ApronA, MyCustomOffsetsA26, ),
        28 : (ApronA, MyCustomOffsetsA28, ),
        30 : (ApronA, MyCustomOffsetsA30, ),
        32 : (ApronA, MyCustomOffsetsA30, ),
        34 : (ApronA, MyCustomOffsetsA30, ),

        },

    GATE_B : {
        None : ( ),
    
        10 : (ApronB, MyCustomOffsetsB26, ),
        12 : (ApronB, ),
        14 : (ApronB, ),
        16 : (ApronB, MyCustomOffsetsB16, ),
        18 : (ApronB, MyCustomOffsetsB18, ),
        20 : (ApronB, MyCustomOffsetsB20to22, ),
        22 : (ApronB, MyCustomOffsetsB20to22, ),
        24 : (ApronB, MyCustomOffsetsB26, ),
        26 : (ApronB, MyCustomOffsetsB26, ),
        28 : (ApronB, ),
        30 : (ApronB, MyCustomOffsetsB30, ),

        },

    GATE_C : {
        None : ( ),
    
        1 : (ApronC, MyCustomOffsetsB18, ),
        2 : (ApronC, MyCustomOffsetsA28, ),
        3 : (ApronC, MyCustomOffsetsB26, ),
        4 : (ApronC, ),
        5 : (ApronC, MyCustomOffsetsB26, ),
        6 : (ApronC, MyCustomOffsetsC06, ),
        10 : (ApronC, MyCustomOffsetsC10, ),
        12 : (ApronC, MyCustomOffsetsC12, ),
        14 : (ApronC, MyCustomOffsetsC14, ),

        },

    GATE_D : {
        None : ( ),
    
        10 : (ApronD, ),
        12 : (ApronD, ),
        14 : (ApronD, ),
        16 : (ApronD, ),
        18: (ApronD, ),
        20 : (ApronD, ),
        22 : (ApronD, ),
        24 : (ApronD, MyCustomOffsetsD24, ),
        26 : (ApronD, MyCustomOffsetsD26, ),
        28 : (ApronD, MyCustomOffsetsD24, ),
        30 : (ApronD, MyCustomOffsetsD24, ),
        32 : (ApronD, MyCustomOffsetsD24, ),
        34 : (ApronD, MyCustomOffsetsD24,),
        36 : (ApronD, MyCustomOffsetsD36, ),
        38 : (ApronD, MyCustomOffsetsD24, ),
        40 : (ApronD, MyCustomOffsetsB18, ),
        42 : (ApronD, ),
        50 : (ApronD, ),
        51 : (ApronD, MyCustomOffsetsC12, ),
        52 : (ApronD, MyCustomOffsetsD24, ),
        53 : (ApronD, MyCustomOffsetsC06, ),
        54 : (ApronD, MyCustomOffsetsD24, ),
        56 : (ApronD, MyCustomOffsetsD24, ),
        57 : (ApronD, MyCustomOffsetsC06, ),
        58 : (ApronD, MyCustomOffsetsD24, ),
        60 : (ApronD, MyCustomOffsetsD24, ),
        62 : (ApronD, MyCustomOffsetsD24, ),
        64 : (ApronD, MyCustomOffsetsD64, ),

        },

GATE_E : {
        None : ( ),
    
        9 : (ApronE, MyCustomOffsetsE09, ),
        10 : (InoperableE, ),
        12 : (InoperableE, ),
        13 : (ApronE, MyCustomOffsetsE13to46, ),
        14 : (InoperableE, ),
        15 : (ApronE, MyCustomOffsetsE13to46, ),
        16 : (InoperableE, ),
        17 : (ApronE, MyCustomOffsetsE13to46, ),
        20 : (InoperableE, ),
        21 : (ApronE, MyCustomOffsetsE13to46, ),
        22 : (InoperableE, ),
        23 : (ApronE, MyCustomOffsetsE13to46, ),
        30 : (InoperableE, ),
        31 : (ApronE, MyCustomOffsetsE13to46, ),
        32 : (InoperableE, ),
        33 : (ApronE, MyCustomOffsetsE13to46, ),
        34 : (InoperableE, ),
        35 : (ApronE, MyCustomOffsetsE13to46, ),
        36 : (InoperableE, ),
        40 : (InoperableE, ),
        41 : (ApronE, MyCustomOffsetsE13to46, ),
        42 : (InoperableE, ),
        43 : (ApronE, MyCustomOffsetsE13to46, ),
        44 : (InoperableE, ),
        45 : (ApronE, MyCustomOffsetsE13to46, ),
        46 : (InoperableE, ),

        },

        GATE_F : {
        None : ( ),
    
        20 : (InoperableF, ),
        21 : (ApronF, MyCustomOffsetsF21, ),
        22 : (InoperableF, ),
        23 : (ApronF, MyCustomOffsetsF21, ),
        24 : (InoperableF, ),
        25 : (ApronF, MyCustomOffsetsF21, ),
        26 : (InoperableF, ),
        31 : (ApronF, ),
        32 : (ApronF, ),
        34 : (ApronF, MyCustomOffsetsF34),

        },

        GATE_U : {
        None : ( ),
    
        8 : (ApronU, ),
        10 : (ApronU, ),
        22 : (ApronU, ),
        26 : (ApronU, ),
        30 : (ApronU, ),
        31 : (ApronU, ),
        32 : (ApronU, ),

        },

        GATE_V : {
        None : ( ),
    
        10 : (ApronV, ),
        11 : (ApronV, ),
        12 : (ApronV, ),
        13 : (ApronV, ),
        14 : (ApronV, ),
        20 : (ApronV, ),
        21 : (ApronV, ),
        22 : (ApronV, ),
        23 : (ApronV, ),
        30 : (ApronV, ),
        31 : (ApronV, ),
        32 : (ApronV, ),
        33 : (ApronV, ),
        43 : (ApronV, ),
        44 : (ApronV, ),
        51 : (ApronV, ),
        53 : (ApronV, ),
        56 : (ApronV, ),
        411 : (ApronV, ),

        },

        GATE_W : {
        None : ( ),
    
        10 : (ApronW, ),
        12 : (ApronW, ),
        14 : (ApronW, ),
        16 : (ApronW, ),
        18 : (ApronW, ),
        20 : (ApronW, ),
        22 : (ApronW, ),
        24 : (ApronW, ),
        26 : (ApronW, ),
        28 : (ApronW, ),
        30 : (ApronW, ),
        32 : (ApronW, ),
        34 : (ApronW, ),

        },

    PARKING : {
        None : ( ),

    }
    }