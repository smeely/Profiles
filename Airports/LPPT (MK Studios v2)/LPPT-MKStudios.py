# -- coding: utf-8 --

msfs_mode = 1
icao = "lppt"
version = 1.2

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
def MyCustomOffsets104(aircraftData):

    table = {
        0: 0,
        321: 2.2,

        757: 2.2,
        
        190: -3.2,
        195: -3.2,
        170: -3.2,

        42: 4.7,
        72: 4.7,
        }

    table737 = {
        0: 0,
        300: -2.1,
        700: -2.1,
        900: 2.2,
        }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsets105to106(aircraftData):

    table = {
        0: 0,
        321: 2.5,

        757: 4.7,
        
        190: -1.2,
        195: -1.2,
        170: -1.2,

        42: 6.4,
        72: 6.4,
        }

    table737 = {
        0: 0,
        300: 0,
        700: 1.2,
        800: 2.4,
        900: 4.7,
        }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsets107(aircraftData):

    table = {
        0: 0,
        321: 0.9,

        757: 2.3,
        
        190: -1,
        195: -1,
        170: -1,
        }

    table737 = {
        0: 0,
        300: -1,
        700: -1,
        800: 0.9,
        900: 0.9,
        }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsets108(aircraftData):

    table = {
        0: 0,

        42: -4.1,
        72: 0,
        }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets(aircraftData=aircraftData, specificTables={}, genericTable=table))

@AlternativeStopPositions
def MyCustomOffsets114to123(aircraftData):

    table = {
        0: 0,
        190: 0.6,

        90: 2.1,
        }

    table737 = {
        0: 0,
        700: 1.3,
        }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsets124(aircraftData):

    table = {
        0: 0,
        321: 2,

        190: -1.1,

        90: 3.1,
    }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets(aircraftData=aircraftData, specificTables={}, genericTable=table))

@AlternativeStopPositions
def MyCustomOffsets125to126(aircraftData):

    table = {
        0: 0,
        321: 1.2,
        190: -1.5,

        90: 3.2,
        }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets(aircraftData=aircraftData, specificTables={}, genericTable=table))

@AlternativeStopPositions
def MyCustomOffsets141(aircraftData):

    table = {
        0: 0,
        319: -0.9, 
        321: 1.3,   

        190: -4.9,
        195: -4.9,

        90: 2.9,    
    }

    table737 = {
        0: 1.3,
        300: -2.9,
        400: -2.9,
        700: -0.9,
        800: 1.3,
        }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsets142(aircraftData):

    table = {
        0: 0,
        319: -2.2,
        330: 4.5,
        340: 4.5,

        737: -2.2,
        757: 1.5,
        767: 7.4,
        777: 7.4,

        170: -5.5,
        175: -5.5,
        190: -4.3,
        195: -4.3,
        }

    table787 = {
        0: 4.5,
        8: 1.5,
        9: 4.5,
        10: 5.5,
        }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            787 : (table787, 8),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsets143(aircraftData):

    table = {
        0: 0,
        319: -4.4,
        330: -2.1,

        757: -2.1,
        747: 7.6,

        190: -5.4,
        195: -5.4,
        }

    table787 = {
        0: 0,
        8: -2.1,
        9: 0,
        10: 0,
        }
    
    table737 = {
        0: 0,
        700: -2.1,
        800: 0,
    }

    table777 = {
        0: 3.5,
        200: 0,
        300: 3.5,
    }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            787 : (table787, 8),
            737 : (table737, 0),
            777 : (table777, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsets144(aircraftData):

    table = {
        0: 0,
        319: -1.9,
        330: 5.5,
        340: 5.5,

        747: 7.5,
        757: 1.5,
        767: 7.5,

        170: -5.5,
        175: -5.5,
        190: -4.2,
        195: -4.2,
        }


    table777 = {
        0: 7.5,
        200: 5.5,
        300: 7.5,
        }
    
    table737 = {
        0: 0,
        700: -1.9,
    }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            777 : (table777, 0),
            737 : (table737, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsets145(aircraftData):

    table = {
        0: 0,
        319: -4.5,
        321: -2,
        330: -2,

        757: -2,
        747: 7.7,

        190: -5.4,
        195: -5.4,
        }


    table777 = {
        0: 0,
        200: 0,
        300: 3.8,
        }
    
    table737 = {
        0: 0,
        700: -2,
        800: 0,
    }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            777 : (table777, 0),
            737 : (table737, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsets146(aircraftData):

    table = {
        0: 0,
        319: -6.3,
        330: 2.1,
        340: 6,

        747: 8.5,
        787: 6,

        190: -6.3,
        195: -6.3,
        }


    table777 = {
        0: 6,
        200: 4,
        300: 6,
        }
    
    table737 = {
        0: 0,
        700: -1.2,
        800: 0,
    }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            777 : (table777, 0),
            737 : (table737, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsets147(aircraftData):

    table = {
        0: 0,
        
        330: 3.3,
        340: 5.3,
        321: 1,
        
        747: 10.7,
        757: 3.3,
        }


    table777 = {
        0: 6,
        200: 5.3,
        300: 8.3,
        }

    table787 = {
        0: 5.3,
        8: 3.3,
        9: 5.3,
        }
    
    table737 = {
        0: 1,
        700: 0,
        800: 1,
    }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            777 : (table777, 0),
            787 : (table787, 8),
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def MyCustomOffsets201(aircraftData):

    table = {
        0: 0,
        321: 1,
        
        747: 14,
        777: 3,
        }
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets(aircraftData=aircraftData, specificTables={}, genericTable=table))

@AlternativeStopPositions
def MyCustomOffsets203p6p8(aircraftData):

    table = {
        0: 0,

        90: 5.8,
        }
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets(aircraftData=aircraftData, specificTables={}, genericTable=table))


@AlternativeStopPositions
def MyCustomOffsets204p207(aircraftData):

    table = {
        0: 0,
        321: 1.1,
        
        330: -3,
        340: -1.9,
        
        777: 2.9,

        90: 7.3,
        }
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets(aircraftData=aircraftData, specificTables={}, genericTable=table))


@AlternativeStopPositions
def MyCustomOffsets505p503(aircraftData):

    table = {
        0: 0,

        777: 4.1,
        
        }
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets(aircraftData=aircraftData, specificTables={}, genericTable=table))


@AlternativeStopPositions
def MyCustomOffsets506(aircraftData):

    table = {
        0: 0,
        321: 0.9,
        
        330: 6.3,

        }
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets(aircraftData=aircraftData, specificTables={}, genericTable=table))


@AlternativeStopPositions
def MyCustomOffsets600p607(aircraftData):

    table = {
        0: 0,
        319: -1.3,
        321: 6.5,

        90: 10.9,

        }

    table737 = {
        0: 2.8,
        300: 0,
        400: 1.3,
        700: 2.8,
        800: 5.6,

        }
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def MyCustomOffsets602(aircraftData):

    table = {

        777: 3.9,
        310: -2.9,

        }

    table340 = {
        0: 2.9,
        200: 0.9,
        300: 2.9,

    }

    table330 = {
        0: 2.9,
        200: 0,
        300: 2.9,
        800: 2.9,
        900: 2.9,
    }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            330 : (table330, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsets605(aircraftData):

    table = {
        350: -3,

        747: 0.9,
        767: 2.9,
        }

    table340 = {
        0: 0,
        200: -2,
        300: 0,
    }

    table777 = {
        0: 0,
        200: 0,
        300: 7.1,
    }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            777 : (table777, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsets608(aircraftData):

    table = {
        310: -6,

        767: 2.8,
        }

    table340 = {
        0: 0,
        200: -3,
        300: 0,
    }

    table777 = {
        0: 0,
        200: 0,
        300: 7.1,
    }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            777 : (table777, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsets609(aircraftData):

    table = {
        319: -1.3,
        321: 6.5,

        90: 10.9,
 
        }

    table737 = {
        0: 2.7,
        400: 5.1,
        800: 2.7,
    }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )


@AlternativeStopPositions
def MyCustomOffsets801(aircraftData):

    table = {
            319: -1.5,

            757: 3.5,
            767: 6.5,

            190: -3,
            195: -3,
            170: -3,
        }

    table737 = {
        0: 0,
        700: -1.5,
        800: 0,
    }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsets802(aircraftData):

    table = {
            319: -1.5,
            321: 1.5,

            757: 4.9,
            767: 8,

            190: -1.5,
            195: -1.5,
            170: -1.5,
        }

    table737 = {
        0: 0,
        700: -1.5,
        800: 0,
    }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsets803(aircraftData):

    table = {
            319: -0.9,
            321: 0.9,

            757: 4.2,
            767: 7.3,

            190: -1.5,
            195: -1.5,
            170: -1.5,
        }

    table737 = {
        0: 0,
        700: -1.5,
        800: 0,
    }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsets804to806(aircraftData):

    table = {
            319: -1.5,
            321: 3.5,

            190: -3,
            195: -3,
            170: -3,
        }

    table737 = {
        0: 0,
        300: -1.5,
        700: 0,
        800: 1.5,
    }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )
        
GateNames = CustomizedName("Gates (114-147) | Gate #", 1)
Apron10Names = CustomizedName("Apron 10 (104-108) | Stand #", 2)
Apron20Names = CustomizedName("Apron 20 (200-209) | Stand #", 3)
Apron22Names = CustomizedName("Apron 22 (221-225) | Stand #", 4)
Apron30Names = CustomizedName("Apron 30 (301-302) | Stand #", 5)
Apron40Names = CustomizedName("Arpon 40 (401-405) | Stand #", 6)
Apron41Names = CustomizedName("Apron 41 (411-416) | Stand #", 7)
Apron42Names = CustomizedName("Apron 42 (421-426) | Stand #", 8)
Apron50Names = CustomizedName("Apron 50 (501-506) | Stand #", 9)
Apron60Names = CustomizedName("Apron 60 (600-609) | Stand #", 10)
Apron70Names = CustomizedName("Apron 70 (701-706) | Stand #", 11)
Apron80Names = CustomizedName("Apron 80 (801-806) | Stand #", 12)



parkings = {
    GATE : {
        None : ( ),
        107 : (Apron10Names, MyCustomOffsets107, ),
        114 : (GateNames, MyCustomOffsets114to123, ),
        115 : (GateNames, MyCustomOffsets114to123, ),
        116 : (GateNames, MyCustomOffsets114to123, ),
        117 : (GateNames, MyCustomOffsets114to123, ),
        122 : (GateNames, MyCustomOffsets114to123, ),
        123 : (GateNames, MyCustomOffsets114to123, ),
        124 : (GateNames, MyCustomOffsets124, ),
        125 : (GateNames, MyCustomOffsets125to126, ),
        126 : (GateNames, MyCustomOffsets125to126, ),
        141 : (GateNames, MyCustomOffsets141, ),
        142 : (GateNames, MyCustomOffsets142, ),
        143 : (GateNames, MyCustomOffsets143, ),
        144 : (GateNames, MyCustomOffsets144, ),
        145 : (GateNames, MyCustomOffsets145, ),
        146 : (GateNames, MyCustomOffsets146, ),
        147 : (GateNames, MyCustomOffsets147, ),



        104 : (Apron10Names, MyCustomOffsets104, ),
        105 : (Apron10Names, MyCustomOffsets105to106, ),
        106 : (Apron10Names, MyCustomOffsets105to106, ),
        108 : (Apron10Names, MyCustomOffsets108, ),

        200 : (Apron20Names, ),
        201 : (Apron20Names, MyCustomOffsets201, ),
        202 : (Apron20Names, ),
        203 : (Apron20Names, MyCustomOffsets203p6p8, ),
        204 : (Apron20Names, MyCustomOffsets204p207, ),
        205 : (Apron20Names, ),
        206 : (Apron20Names, MyCustomOffsets203p6p8, ),
        207 : (Apron20Names, MyCustomOffsets204p207, ),
        208 : (Apron20Names, MyCustomOffsets203p6p8, ),
        209 : (Apron20Names, ),

        221 : (Apron22Names, ),
        222 : (Apron22Names, ),
        223 : (Apron22Names, ),
        224 : (Apron22Names, ),
        225 : (Apron22Names, ),


        301 : (Apron30Names, ),
        302 : (Apron30Names, ),

        401 : (Apron40Names, ),
        402 : (Apron40Names, ),
        403 : (Apron40Names, ),
        404 : (Apron40Names, ),
        405 : (Apron40Names, ),

        411 : (Apron41Names, ),
        412 : (Apron41Names, ),
        413 : (Apron41Names, ),
        414 : (Apron41Names, ),
        415 : (Apron41Names, ),
        416 : (Apron41Names, ),

        421 : (Apron42Names, ),
        422 : (Apron42Names, ),
        423 : (Apron42Names, ),
        424 : (Apron42Names, ),
        425 : (Apron42Names, ),
        426 : (Apron42Names, ),

        501 : (Apron50Names, MyCustomOffsets505p503, ),
        502 : (Apron50Names, MyCustomOffsets505p503, ),
        503 : (Apron50Names, MyCustomOffsets505p503, ),
        504 : (Apron50Names, MyCustomOffsets505p503, ),
        505 : (Apron50Names, MyCustomOffsets505p503, ),
        506 : (Apron50Names, MyCustomOffsets506, ),

        600 : (Apron60Names, MyCustomOffsets600p607, ),
        601 : (Apron60Names, MyCustomOffsets600p607, ),
        602 : (Apron60Names, MyCustomOffsets602, ),
        603 : (Apron60Names, MyCustomOffsets600p607, ),
        604 : (Apron60Names, MyCustomOffsets600p607,),
        605 : (Apron60Names, MyCustomOffsets605, ),
        606 : (Apron60Names, MyCustomOffsets600p607, ),
        607 : (Apron60Names, MyCustomOffsets600p607, ),
        608 : (Apron60Names, MyCustomOffsets608, ),
        609 : (Apron60Names, MyCustomOffsets609, ),

        801 : (Apron80Names, MyCustomOffsets801, ),
        802 : (Apron80Names, MyCustomOffsets802, ),
        803 : (Apron80Names, MyCustomOffsets803, ),
        804 : (Apron80Names, MyCustomOffsets804to806, ),
        805 : (Apron80Names, MyCustomOffsets804to806, ),
        806 : (Apron80Names, MyCustomOffsets804to806, ),
        },

    PARKING : {
        None : ( ),



        701 : (Apron70Names, ),
        702 : (Apron70Names, ),
        703 : (Apron70Names, ),
        704 : (Apron70Names, ),
        705 : (Apron70Names, ),
        706 : (Apron70Names, ),


    }
    }