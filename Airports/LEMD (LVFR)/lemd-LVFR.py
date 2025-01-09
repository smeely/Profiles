# -- coding: utf-8 --

version = 1.0
msfs_mode = 1
icao = "lemd"

@AlternativeStopPositions
def customOffsetEqual(aircraftData):
    return Distance.fromMeters(0)
    
@AlternativeStopPositions
def customOffset4M2L(aircraftData):

    table = {
        0: 0,
        330: 5,
        737: -1,
        747: 6,
        757: 0,
        767: 0,
        777: 5,
        787: 5,
        42: -1,
        72: -1,
        170: -1,
        175: -1,
        190: -1,
        195: -1,
    }
    
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance()

@AlternativeStopPositions
def customOffset3M2L(aircraftData):

    table = {
        0: 0,
        330: 11.5,
        747: 12.5,
        777: 11.5,
        787: 11.5,
    }
    
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance()
        
@AlternativeStopPositions
def customOffset2M1L(aircraftData):

    table = {
        0: 0,
        330: 7.5,
        747: 7.5,
        757: 7.5,
        767: 7.5,
        777: 7.5,
        787: 7.5,
    }
    
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance()
                        
@AlternativeStopPositions
def customOffsetT24(aircraftData):

    table = {
        0: 0,
        318: 1.3,
        319: 1.3,
        320: 1.3,
        321: 1.3,
        42: -3.8,
        72: -3.8,
        700: -3.8,
        900: -3.8,
        1000: -3.8,
    }
    
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance()
        
@AlternativeStopPositions
def customOffsetT4Rem1(aircraftData):

    table = {
        0: 0,
        321: 2.8,
        737: 2.8,
        757: 2.8,
    }
    
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance()

@AlternativeStopPositions
def customOffsetT4Rem2(aircraftData):

    table = {
        0: 0,
        321: 3,
        737: 3,
        757: 3,
        42: -6,
        72: -6,
        700: -6,
        900: -6,
        1000: -6,
        170: -6,
        175: -6,
    }
    
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance()

@AlternativeStopPositions
def customOffsetT4Gat1(aircraftData):

    table = {
        0: 0,
        321: 3.2,
        757: 3.2,
    }
    
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance()
        
@AlternativeStopPositions
def customOffsetT4Stop1(aircraftData):

    table = {
        0: 0,
        330: 4.9,
        340: 4.9,
        380: 4.9,
        747: 4.9,
    }
    
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance()
        
@AlternativeStopPositions
def customOffsetT4Stop2(aircraftData):

    table = {
        0: 0,
        330: 2.6,
        340: 2.6,
        380: 2.6,
        747: 2.6,
    }
    
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance()
        
@AlternativeStopPositions
def customOffsetT4Stop3(aircraftData):

    table = {
        0: 0,
        777: 2.9,
        787: 2.9,
        330: 2.9,
        340: 2.9,
        380: 5.9,
        747: 6.9,
    }
    
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance()
        
@AlternativeStopPositions
def customOffsetT4Stop4(aircraftData):

    table = {
        0: 0,
        777: 3.4,
        787: 3.4,
        330: 7.6,
        340: 7.6,
        380: 7.6,
        747: 7.6,
    }
    
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance()
        
@AlternativeStopPositions
def customOffsetT4Stop5(aircraftData):

    table = {
        0: 0,
        777: 8.7,
        787: 8.7,
        330: 10.9,
        340: 10.9,
        380: 10.9,
        747: 10.9,
    }
    
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance()
        
@AlternativeStopPositions
def customOffsetT4Stop6(aircraftData):

    table = {
        0: 0,
        321: 2,
        757: 2,
        767: 2,
    }
    
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance()

@AlternativeStopPositions
def customOffsetT4Stop7(aircraftData):

    table = {
        0: 0,
        321: 1.3,
        757: 1.3,
        767: 1.3,
    }
    
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance()

@AlternativeStopPositions
def customOffsetT4Stop8(aircraftData):

    table = {
        0: 0,
        321: 2,
        757: 2,
        767: 2,
        777: 3.3,
        787: 3.3,
        330: 7.6,
        340: 7.6,
        380: 7.6,
        747: 7.6,
    }
    
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance()

@AlternativeStopPositions
def customOffsetT4Stop9(aircraftData):

    table = {
        0: 0,
        321: 4.3,
        757: 4.3,
        767: 4.3,
        700: -1.5,
        900: -1.5,
        1000: -1.5,
    }
    
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance()

@AlternativeStopPositions
def customOffsetT4Stop10(aircraftData):

    table = {
        0: 0,
        321: 1,
        757: 1,
        767: 2.5,
        777: 2.5,
        787: 2.5,
        330: 5.5,
        340: 5.5,
    }
    
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance()
        
@AlternativeStopPositions
def customOffsetT4Stop11(aircraftData):

    table = {
        0: 0,
        777: 7.5,
        787: 7.5,
        330: 7.5,
        340: 7.5,
        380: 7.5,
        747: 7.5,
    }
    
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance()
        
@AlternativeStopPositions
def customOffsetT4SRem1(aircraftData):

    table = {
        0: 0,
        777: 1.4,
        787: 1.4,
        330: 3,
        340: 3,
    }
    
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance()
        
@AlternativeStopPositions
def customOffsetT4SRem2(aircraftData):

    table = {
        0: 0,
        321: 1.2,
        777: 2.9,
        787: 2.9,
        330: 2.9,
        340: 2.9,
    }
    
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance()
        
@AlternativeStopPositions
def customOffsetT4SRem3(aircraftData):

    table = {
        0: 0,
        321: 2.1,
        777: 5.9,
        787: 5.9,
        330: 3.8,
        340: 3.8,
    }
    
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance()
        
@AlternativeStopPositions
def customOffsetCargo1(aircraftData):

    table = {
        0: 0,
        767: 5.1,
        777: 5.1,
        300: 5.1,
        330: 5.1,
    }
    
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance()
        
@AlternativeStopPositions
def customOffsetCargo2(aircraftData):

    table = {
        0: 0,
        747: 10.6,
        767: 5.1,
        777: 5.1,
        300: 5.1,
        330: 5.1,
    }
    
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance()
        
@AlternativeStopPositions
def customOffsetCargo3(aircraftData):

    table = {
        0: 0,
        747: 16.6,
        767: 6,
        777: 6,
        300: 6,
        330: 6,
    }
    
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance()
        
@AlternativeStopPositions
def customOffsetCargo4(aircraftData):

    table = {
        0: 0,
        321: 10,
        767: 7.5,
        777: 10,
        300: 7.5,
        330: 10,
    }
    
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance()
        
@AlternativeStopPositions
def customOffsetGA1(aircraftData):

    table = {
        0: 0,
        319: 7.5,
        320: 7.5,
        737: 7.5,
    }
    
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance()
        
@AlternativeStopPositions
def customOffsetGA2(aircraftData):

    table = {
        0: 0,
        319: 7,
        320: 7,
        737: 7,
    }
    
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance()
        
@AlternativeStopPositions
def customOffsetRamp0(aircraftData):

    table = {
        0: 0,
        321: 3,
    }
    
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance()
           
Terminal1 = CustomizedName("Terminal 1 | Gate T#",1)
Terminal1Re = CustomizedName("Terminal 1 Remote | Stand #",2)
Terminal1Sat = CustomizedName("Terminal 1 Satelite | Gate #",3)

Terminal2 = CustomizedName("Terminal 2 | Gate T#",4)
Terminal2Re = CustomizedName("Terminal 2 Remote | Stand #",5)

Terminal3 = CustomizedName("Terminal 3 | Gate T#",6)
Terminal3Re = CustomizedName("Terminal 3 Remote (Terrain Issues) | Stand T#",7)

Terminal4Nor = CustomizedName("Terminal 4 North | Gate #",8)
Terminal4Sou = CustomizedName("Terminal 4 South | Gate #",9)
Terminal4Re = CustomizedName("Terminal 4 Remote | Stand #",10)
Terminal4ReN = CustomizedName("Terminal 4 Remote North | Stand #",11)

Terminal4SNor = CustomizedName("Terminal 4S North | Gate #",12)
Terminal4SSou = CustomizedName("Terminal 4S South | Gate #",13)
Terminal4SRe = CustomizedName("Terminal 4S Remote | Stand #",14)

CargoSouth = CustomizedName("Cargo Area South | Stand #",15)
CargoEast = CustomizedName("Cargo Area East | Stand #",16)

GAApron = CustomizedName("GA Ramp | Stand #",17)
LongPark = CustomizedName("Longterm Parking | Stand #",18)

Ramp0 = CustomizedName("Ramp 0 | Stand #",19) 

parkings = {
	GATE : {
		None : ( ),
        1 : (Ramp0, customOffsetRamp0, ),
        2 : (Ramp0, customOffsetRamp0, ),
        3 : (Ramp0, customOffsetRamp0, ),
        4 : (Ramp0, customOffsetRamp0, ),
        5 : (Ramp0, customOffsetRamp0, ),
        6 : (Ramp0, customOffsetEqual, ),
        7 : (Ramp0, customOffsetEqual, ),
        8 : (Ramp0, customOffsetEqual, ),
        9 : (Ramp0, customOffsetEqual, ),
        10 : (Terminal2Re,customOffsetEqual, ),
        11 : (Terminal2Re,customOffsetEqual, ),
        12 : (Terminal2Re,customOffsetEqual, ),
        13 : (Terminal2Re,customOffsetEqual, ),
        14 : (Terminal2Re,customOffsetEqual, ),
        15 : (Terminal2Re,customOffsetEqual, ),
        16 : (Terminal2Re,customOffsetEqual, ),
        17 : (Terminal2Re,customOffsetEqual, ),
        22 : (Terminal1Re,customOffsetEqual, ),
        23 : (Terminal1Re,customOffsetEqual, ),
        24 : (Terminal1Re,customOffsetEqual, ),
        25 : (Terminal1Re,customOffsetEqual, ),
        26 : (Terminal1Re,customOffsetEqual, ),
        27 : (Terminal1Re,customOffsetEqual, ),
        30 : (Terminal1Re,customOffsetEqual, ),
        31 : (Terminal1Re,customOffsetEqual, ),
        32 : (Terminal1Re,customOffsetEqual, ),
        33 : (Terminal1Re,customOffsetEqual, ),
        34 : (Terminal1Re,customOffsetEqual, ),
        35 : (Terminal1Re,customOffsetEqual, ),
        36 : (Terminal1Re,customOffsetEqual, ),
        37 : (Terminal1Re,customOffsetEqual, ),
        41 : (Terminal1Re,customOffset2M1L, ),
        42 : (Terminal1Re,customOffset2M1L, ),
        43 : (Terminal1Re,customOffset2M1L, ),
        44 : (Terminal1Re,customOffsetEqual, ),
        50 : (Terminal1Re,customOffsetEqual, ),
        52 : (Terminal1Re,customOffsetEqual, ),
        54 : (Terminal1Re,customOffsetEqual, ),
        56 : (Terminal1Re,customOffsetEqual, ),
        58 : (Terminal1Re,customOffsetEqual, ),
        59 : (Terminal1Re, ),
        60 : (Terminal1Re,customOffsetEqual, ),
        62 : (Terminal1Re,customOffsetEqual, ),
        64 : (Terminal1Re,customOffsetEqual, ),
        66 : (Terminal1Re,customOffsetEqual, ),
        68 : (Terminal1Re,customOffsetEqual, ),
        69 : (Terminal1Re, ),
        70 : (Terminal1Sat, customOffsetEqual, ),
        71 : (Terminal1Sat, customOffsetEqual, ),
        72 : (Terminal1Sat, customOffsetEqual, ),
        73 : (Terminal1Sat, customOffsetEqual, ),
        74 : (Terminal1Sat, customOffsetEqual, ),
        75 : (GAApron, customOffsetEqual, ),
        80 : (GAApron, customOffsetGA1, ),
        81 : (GAApron, customOffsetGA1, ),
        82 : (GAApron, customOffsetGA1, ),
        83 : (GAApron, customOffsetGA1, ),
        84 : (GAApron, customOffsetGA1, ),
        85 : (GAApron, customOffsetGA1, ),
        90 : (GAApron, customOffsetEqual, ),
        91 : (GAApron, customOffsetEqual, ),
        92 : (GAApron, customOffsetEqual, ),
        93 : (GAApron, customOffsetEqual, ),
        94 : (GAApron, customOffsetEqual, ),
        95 : (GAApron, customOffsetEqual, ),
        96 : (GAApron, customOffsetEqual, ),
        97 : (GAApron, customOffsetEqual, ),
        98 : (GAApron, customOffsetGA2, ),
        99 : (GAApron, customOffsetGA2, ),
        100 : (GAApron, customOffsetEqual, ),
        101 : (GAApron, customOffsetEqual, ),
        102 : (GAApron, customOffsetEqual, ),
        103 : (GAApron, customOffsetEqual, ),
        104 : (GAApron, customOffsetEqual, ),
        105 : (GAApron, customOffsetEqual, ),
        111 : (GAApron, customOffsetEqual, ),
        112 : (GAApron, customOffsetGA2, ),
        113 : (GAApron, customOffsetGA2, ),
        114 : (GAApron, customOffsetGA2, ),
        115 : (GAApron, customOffsetGA2, ),
        116 : (GAApron, customOffsetGA2, ),
        120 : (GAApron, customOffsetEqual, ),
        121 : (GAApron, customOffsetEqual, ),
        122 : (GAApron, customOffsetEqual, ),
        123 : (GAApron, customOffsetEqual, ),
        124 : (GAApron, customOffsetEqual, ),
        125 : (GAApron, customOffsetEqual, ),
        126 : (GAApron, customOffsetEqual, ),
        145 : (CargoSouth, customOffsetCargo1, ),
        146 : (CargoSouth, customOffsetEqual, ),
        148 : (CargoSouth, customOffsetEqual, ),
        151 : (CargoSouth, customOffsetCargo2, ),
        152 : (CargoSouth, customOffsetEqual, ),
        154 : (CargoSouth, customOffsetEqual, ),
        155 : (CargoSouth, customOffsetCargo2, ),
        157 : (CargoSouth, customOffsetCargo3, ),
        159 : (CargoSouth, customOffsetCargo2, ),
        160 : (CargoSouth, customOffsetEqual, ),
        162 : (CargoSouth, customOffsetEqual, ),
        200 : (CargoEast, customOffsetEqual, ),
        201 : (CargoEast, customOffsetEqual, ),
        202 : (CargoEast, customOffsetEqual, ),
        203 : (CargoEast, customOffsetEqual, ),
        204 : (CargoEast, customOffsetEqual, ),
        205 : (CargoEast, customOffsetEqual, ),
        206 : (CargoEast, customOffsetEqual, ),
        207 : (CargoEast, customOffsetEqual, ),
        208 : (CargoEast, customOffsetEqual, ),
        215 : (CargoEast, customOffsetCargo4, ),
        217 : (CargoEast, customOffsetCargo4, ),
        220 : (LongPark, customOffsetEqual, ),
        221 : (LongPark, customOffsetCargo4, ),
        222 : (LongPark, customOffsetEqual, ),
        223 : (LongPark, customOffsetCargo4, ),
        225 : (LongPark, customOffsetCargo4, ),
        300 : (Terminal4Nor, customOffsetEqual, ),
        302 : (Terminal4Nor, customOffsetEqual, ),
        304 : (Terminal4Nor, customOffsetEqual, ),
        306 : (Terminal4Nor, customOffsetEqual, ),
        308 : (Terminal4Nor, customOffsetEqual, ),
        310 : (Terminal4Nor, customOffsetEqual, ),
        312 : (Terminal4Nor, customOffsetT4Rem2, ),
        320 : (Terminal4Nor, customOffsetT4Rem1, ),
        322 : (Terminal4Nor, customOffsetT4Rem1, ),
        324 : (Terminal4Nor, customOffsetT4Rem1, ),
        326 : (Terminal4Nor, customOffsetT4Rem1, ),
        328 : (Terminal4Nor, customOffsetT4Rem1, ),
        329 : (Terminal4Nor, customOffsetEqual, ),
        330 : (Terminal4Nor, customOffsetT4Rem2, ),
        332 : (Terminal4Nor, customOffsetT4Gat1, ),
        334 : (Terminal4Nor, customOffsetT4Gat1, ),
        336 : (Terminal4Nor, customOffsetT4Gat1, ),
        338 : (Terminal4Nor, customOffsetT4Gat1, ),
        340 : (Terminal4Nor, customOffsetT4Gat1, ),
        342 : (Terminal4Nor, customOffsetT4Gat1, ),
        344 : (Terminal4Nor, customOffsetT4Gat1, ),
        346 : (Terminal4Nor, customOffsetT4Gat1, ),
        348 : (Terminal4Nor, customOffsetT4Gat1, ),
        350 : (Terminal4Nor, customOffsetT4Gat1, ),
        352 : (Terminal4Sou, customOffsetT4Gat1, ),
        354 : (Terminal4Sou, customOffsetT4Gat1, ),
        356 : (Terminal4Sou, customOffsetT4Gat1, ),
        358 : (Terminal4Sou, customOffsetT4Gat1, ),
        360 : (Terminal4Sou, customOffsetT4Gat1, ),
        362 : (Terminal4Sou, customOffsetT4Gat1, ),
        364 : (Terminal4Sou, customOffsetT4Gat1, ),
        366 : (Terminal4Sou, customOffsetT4Gat1, ),
        368 : (Terminal4Sou, customOffsetT4Gat1, ),
        370 : (Terminal4Sou, customOffsetT4Gat1, ),
        373 : (Terminal4Sou, customOffsetEqual, ),
        377 : (Terminal4Sou, customOffsetEqual, ),
        380 : (Terminal4Sou, customOffsetEqual, ),
        382 : (Terminal4Sou, customOffsetEqual, ),
        384 : (Terminal4Sou, customOffsetEqual, ),
        386 : (Terminal4Sou, customOffsetEqual, ),
        388 : (Terminal4Sou, customOffsetEqual, ),
        384 : (Terminal4Sou, customOffsetEqual, ),
        386 : (Terminal4Sou, customOffsetEqual, ),
        390 : (Terminal4Sou, customOffsetEqual, ),
        392 : (Terminal4Sou, customOffsetEqual, ),
        394 : (Terminal4Sou, customOffsetEqual, ),
        400 : (Terminal4ReN, customOffsetT4Rem2, ),
        402 : (Terminal4ReN, customOffsetT4Rem2, ),
        404 : (Terminal4ReN, customOffsetT4Rem2, ),
        406 : (Terminal4ReN, customOffsetT4Rem2, ),
        408 : (Terminal4ReN, customOffsetT4Rem2, ),
        410 : (Terminal4ReN, customOffsetT4Rem2, ),
        411 : (Terminal4ReN, customOffsetT4Rem2, ),
        412 : (Terminal4ReN, customOffsetT4Rem1, ),
        413 : (Terminal4ReN, customOffsetT4Rem1, ),
        414 : (Terminal4ReN, customOffsetT4Rem1, ),
        415 : (Terminal4ReN, customOffsetT4Rem1, ),
        416 : (Terminal4ReN, customOffsetT4Rem1, ),
        417 : (Terminal4ReN, customOffsetT4Rem1, ),
        418 : (Terminal4ReN, customOffsetT4Rem1, ),
        419 : (Terminal4ReN, customOffsetT4Rem1, ),
        420 : (Terminal4Re, customOffsetT4Rem1, ),
        424 : (Terminal4Re, customOffsetT4Rem1, ),
        426 : (Terminal4Re, customOffsetT4Rem1, ),
        428 : (Terminal4Re, customOffsetT4Rem1, ),
        430 : (Terminal4Re, customOffsetT4Rem1, ),
        432 : (Terminal4Re, customOffsetT4Rem1, ),
        434 : (Terminal4Re, customOffsetT4Rem1, ),
        436 : (Terminal4Re, customOffsetT4Rem1, ),
        438 : (Terminal4Re, customOffsetT4Rem1, ),
        442 : (Terminal4Re, customOffsetT4Rem1, ),
        444 : (Terminal4Re, customOffsetT4Rem1, ),
        446 : (Terminal4Re, customOffsetT4Rem1, ),
        448 : (Terminal4Re, customOffsetT4Rem1, ),
        501 : (Terminal4SNor, customOffsetT4Stop1, ),
        505 : (Terminal4SNor, customOffsetT4Stop2, ),
        510 : (Terminal4SNor, customOffsetT4Stop2, ),
        515 : (Terminal4SNor, customOffsetT4Stop2, ),
        519 : (Terminal4SNor, customOffsetT4Stop3, ),
        522 : (Terminal4SNor, customOffsetT4Stop3, ),
        525 : (Terminal4SNor, customOffsetT4Stop3, ),
        529 : (Terminal4SNor, customOffsetT4Stop1, ),
        533 : (Terminal4SNor, customOffsetT4Stop1, ),
        536 : (Terminal4SNor, customOffsetT4Stop3, ),
        538 : (Terminal4SNor, customOffsetEqual, ),
        541 : (Terminal4SNor, customOffsetEqual, ),
        545 : (Terminal4SNor, customOffsetT4Stop4, ),
        549 : (Terminal4SNor, customOffsetT4Stop4, ),
        553 : (Terminal4SNor, customOffsetT4Stop5, ),
        556 : (Terminal4SNor, customOffsetT4Stop6, ),
        559 : (Terminal4SNor, customOffsetT4Stop4, ),
        562 : (Terminal4SSou, customOffsetT4Stop7, ),
        565 : (Terminal4SSou, customOffsetT4Stop4, ),
        569 : (Terminal4SSou, customOffsetT4Stop4, ),
        572 : (Terminal4SSou, customOffsetT4Stop8, ),
        576 : (Terminal4SSou, customOffsetT4Stop9, ),
        578 : (Terminal4SSou, customOffsetEqual, ),
        580 : (Terminal4SSou, customOffsetT4Stop10, ),
        582 : (Terminal4SSou, customOffsetT4Stop7, ),
        585 : (Terminal4SSou, customOffsetT4Stop11, ),
        601 : (Terminal4SRe, customOffsetEqual, ),
        604 : (Terminal4SRe, customOffsetEqual, ),
        609 : (Terminal4SRe, customOffsetEqual, ),
        614 : (Terminal4SRe, customOffsetT4SRem1, ),
        616 : (Terminal4SRe, customOffsetT4Gat1, ),
        618 : (Terminal4SRe, customOffsetEqual, ),
        620 : (Terminal4SRe, customOffsetT4Gat1, ),
        622 : (Terminal4SRe, customOffsetEqual, ),
        624 : (Terminal4SRe, customOffsetT4SRem2, ),
        627 : (Terminal4SRe, customOffsetT4SRem3, ),
        938 : (CustomizedName("Terminal 3 Remote (Terrain Issues) | Stand T38",7), ),
	},    
    GATE_T : {
        None : ( ),
        1 : (Terminal1,customOffset4M2L, ),
        2 : (Terminal1,customOffset4M2L, ),
        3 : (Terminal1,customOffset3M2L, ),
        4 : (Terminal1,customOffset3M2L, ),
        5 : (Terminal1,customOffset3M2L, ),
        6 : (Terminal1,customOffsetEqual, ),
        7 : (Terminal1, ),
        8 : (Terminal1, ),
        9 : (Terminal1,customOffsetEqual, ),
        10 : (Terminal1,customOffsetEqual, ),
        11 : (Terminal1,customOffsetEqual, ),
        12 : (Terminal1, ),
        13 : (Terminal1, ),
        14 : (Terminal2, ),
        15 : (Terminal2,customOffsetEqual, ),
        16 : (Terminal2,customOffsetEqual, ),
        17 : (Terminal2,customOffset4M2L, ),
        18 : (Terminal2,customOffset4M2L, ),
        19 : (Terminal2,customOffset4M2L, ),
        20 : (Terminal2,customOffsetEqual, ),
        21 : (Terminal2, ),
        22 : (Terminal2, ),
        24 : (Terminal3,customOffsetT24, ),
        25 : (Terminal3,customOffsetEqual, ),
        26 : (Terminal3,customOffsetEqual, ),
        27 : (Terminal3,customOffsetEqual, ),
        28 : (Terminal3,customOffsetEqual, ),
        29 : (Terminal3,customOffsetT24, ),
        30 : (Terminal3,customOffsetEqual, ),
        31 : (Terminal3,customOffsetT24, ),
        32 : (Terminal3,customOffsetEqual, ),
        33 : (Terminal3,customOffsetEqual, ),
        34 : (Terminal3,customOffsetEqual, ),
        35 : (Terminal3,customOffsetEqual, ),
        36 : (Terminal3Re,customOffsetEqual, ),
        37 : (Terminal3Re,customOffsetEqual, ),
        39 : (Terminal3Re,customOffsetEqual, ),
        40 : (Terminal3Re,customOffsetEqual, ),
	},    
    PARKING : {
        None : ( ),
        107 : (GAApron, customOffsetEqual, ),
        108 : (GAApron, customOffsetGA2, ),
        109 : (GAApron, customOffsetGA2, ),
        110 : (GAApron, customOffsetGA2, ),
        117 : (GAApron, customOffsetEqual, ),
        118 : (GAApron, customOffsetEqual, ),
        130 : (GAApron, customOffsetEqual, ),
        132 : (GAApron, customOffsetEqual, ),
        133 : (GAApron, customOffsetEqual, ),
        134 : (GAApron, customOffsetEqual, ),
        135 : (GAApron, customOffsetEqual, ),
        138 : (GAApron, customOffsetEqual, ),
        140 : (GAApron, customOffsetEqual, ),
        210 : (CargoEast, customOffsetEqual, ),
        211 : (CargoEast, customOffsetCargo4, ),
        212 : (CargoEast, customOffsetEqual, ),
        216 : (CargoEast, customOffsetEqual, ),
        218 : (CargoEast, customOffsetEqual, ),
        230 : (LongPark, customOffsetEqual, ),
        231 : (LongPark, customOffsetEqual, ),
        232 : (LongPark, customOffsetEqual, ),
        233 : (LongPark, customOffsetEqual, ),
        234 : (LongPark, customOffsetEqual, ),
        235 : (LongPark, customOffsetEqual, ),
        236 : (LongPark, customOffsetEqual, ),
        237 : (LongPark, customOffsetEqual, ),
        238 : (LongPark, customOffsetEqual, ),
        239 : (LongPark, customOffsetEqual, ),
        240 : (LongPark, customOffsetEqual, ),
        241 : (LongPark, customOffsetEqual, ),
        242 : (LongPark, customOffsetEqual, ),
        243 : (LongPark, customOffsetEqual, ),
        244 : (LongPark, customOffsetEqual, ),
        245 : (LongPark, customOffsetEqual, ),
        246 : (LongPark, customOffsetEqual, ),
        247 : (LongPark, customOffsetEqual, ),
        248 : (LongPark, customOffsetEqual, ),
        249 : (LongPark, customOffsetEqual, ),
        915 : (CustomizedName("Terminal 4 PE Parking | Stand PE15",11), customOffsetEqual, ),
        920 : (CustomizedName("Terminal 4 PE Parking | Stand PE20",11), customOffsetEqual, ),
        930 : (CustomizedName("Terminal 4 PE Parking | Stand PE30",11), customOffsetEqual, ),
    },     
}