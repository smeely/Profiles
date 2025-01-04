# -- coding: utf-8 --

version = "1.3.1"
msfs_mode = 1
icao = "lpfr"

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
def customOffsetApronNWSWLarge1(aircraftData):

    table = {
        0: 0,
        319 : -3.4,
        757 : 8.15,
        767 : 8.15,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )
    
@AlternativeStopPositions
def customOffsetApronNWSWLarge2(aircraftData):

    table = {
        0: 0,
        319 : -10.5,
        190 : -8,
        195 : -8,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )
    
@AlternativeStopPositions
def customOffsetApronNWSWSmall1(aircraftData):

    table = {
        0: 0,
        190 : 4.15,
        195 : 4.15,
        757 : 4.2,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )
    
@AlternativeStopPositions
def customOffsetApronNWSWSmall2(aircraftData):

    table = {
        0: 0,
        757 : 2.9,
        767 : 2.9,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )    
    
@AlternativeStopPositions
def customOffsetApronNWSWSmall3(aircraftData):

    table = {
        0: 0,
        319 : -5.5,
        190 : -3.25,
        195 : -3.25,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )    
    
@AlternativeStopPositions
def customOffsetApronNWSWSmall4(aircraftData):

    table = {
        0: 0,
        319 : -3.3,
        757 : 3.55,
        767 : 3.55,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )

@AlternativeStopPositions
def customOffsetApronS(aircraftData):

    table = {
        0: 0,
        330 : 9.1,
        340 : 9.1,
        350 : 9.1,
        767 : 9.1,
        777 : 9.1,
        10 : 9.1,
        11 : 9.1,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )    

@AlternativeStopPositions
def customOffsetApronNGate314(aircraftData):

    table = {
        0: 0,
        319 : -3.0,
        330 : 4.0,
        340 : 4.0,
        350 : 5.4,
        747 : 5.4,
        757 : 7.25,
        767 : 7.25,
        777 : 9.0,
        787 : 9.0,
        10 : 7.25,
        11 : 7.25,
        190 : -3.0,
        195 : -3.0,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )    

@AlternativeStopPositions
def customOffsetApronNGate316(aircraftData):

    table = {
        0: 0,
        330 : 5.0,
        340 : 5.0,
        350 : 5.0,
        757 : 5.0,
        767 : 5.0,
        10 : 5.0,
        11 : 5.0,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )    

@AlternativeStopPositions
def customOffsetApronNGate318(aircraftData):

    table = {
        0: 0,
        330 : 2.05,
        340 : 2.05,
        350 : 3.7,
        757 : 3.7,
        767 : 3.7,
        10 : 3.7,
        11 : 3.7,
        190 : -2.5,
        195 : -2.5,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )    

@AlternativeStopPositions
def customOffsetApronNGate320(aircraftData):

    table = {
        0: 0,
        330 : 4.0,
        340 : 4.0,
        350 : 4.0,
        747 : 6.5,
        757 : 2.5,
        767 : 2.5,
        777 : 7.5,
        787 : 7.5,
        10 : 5.2,
        11 : 5.2,
        190 : -2.5,
        195 : -2.5,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )    

@AlternativeStopPositions
def customOffsetApronNGate322(aircraftData):

    table = {
        0: 0,
        330 : -3.0,
        340 : -3.0,
        350 : 1.2,
        747 : 1.2,
        757 : -7.2,
        767 : -7.2,
        777 : 1.2,
        787 : 1.2,
        10 : -3.0,
        11 : -3.0,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )    

@AlternativeStopPositions
def customOffsetApronNGate324(aircraftData):

    table = {
        0: 0,
        330 : 7.2,
        340 : 7.2,
        350 : 7.2,
        757 : 7.2,
        767 : 7.2,
        10 : 7.2,
        11 : 7.2,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )    

@AlternativeStopPositions
def customOffsetApronNE432(aircraftData):

    table = {
        0: 0,
        321 : 4.0,
        747 : 6.0,
        757 : 4.0,
        767 : 4.0,
        10 : 6.0,
        11 : 6.0,
    }
 
    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )   

@AlternativeStopPositions
def customOffsetApronNE434(aircraftData):

    table = {
        0: 0,
        747 : 13.0,
        777 : 13.0,
        787 : 13.0,
        190 : 2.1,
        195 : 2.1,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )    

@AlternativeStopPositions
def customOffsetApronNE436(aircraftData):

    table = {
        0: 0,
        321 : 6.1,
        737 : 4.2,
        757 : 6.1,
        767 : 6.1,
        190 : 1.9,
        195 : 1.9,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )    

@AlternativeStopPositions
def customOffsetApronNE442(aircraftData):

    table = {
        0: 0,
        321 : 5.75,
        737 : 3.8,
        757 : 5.75,
        767 : 5.75,
        190 : 2,
        195 : 2,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )
    
@AlternativeStopPositions
def customOffsetApronNE444(aircraftData):

    table = {
        0: 0,
        321 : 8.0,
        757 : 8.0,
        767 : 8.0,
        747 : 16.0,
        777 : 16.0,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )
    
@AlternativeStopPositions
def customOffsetApronNE446(aircraftData):

    table = {
        0: 0,
        321 : 17.9,
        737 : 5.9,
        757 : 17.9,
        767 : 17.9,
        190 : 5.9,
        195 : 5.9,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )
    
@AlternativeStopPositions
def customOffsetApronNE452(aircraftData):

    table = {
        0: 0,
        321 : 7.9,
        757 : 7.9,
        767 : 7.9,
        190 : 2.2,
        195 : 2.2,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )
    
@AlternativeStopPositions
def customOffsetApronNE454(aircraftData):

    table = {
        0: 0,
        321 : 4,
        737 : 2.1,
        757 : 4,
        767 : 4,
        190 : 2.1,
        195 : 2.1,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )
    
@AlternativeStopPositions
def customOffsetApronNE456(aircraftData):

    table = {
        0: 0,
        321 : 5.9,
        737 : 2.9,
        757 : 5.9,
        767 : 5.9,
        190 : 2.9,
        195 : 2.9,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )
    
@AlternativeStopPositions
def customOffsetApronNE462p466(aircraftData):

    table = {
        0: 0,
        321 : 8,
        737 : 4,
        757 : 8,
        767 : 8,
        190 : 4,
        195 : 4,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )
    
@AlternativeStopPositions
def customOffsetApronNE464(aircraftData):

    table = {
        0: 0,
        321 : 5.9,
        737 : 1.9,
        747 : 13.5,
        757 : 5.9,
        767 : 5.9,
        777 : 13.5,
        787 : 13.5,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )
    
@AlternativeStopPositions
def customOffsetApronSECommon(aircraftData):

    table = {
        0: 0,
        321 : 3.1,
        757 : 6.1,
        767 : 6.1,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )
    
@AlternativeStopPositions
def customOffsetApronSE453(aircraftData):

    table = {
        0: 0,
        321 : 3,
        747 : 9,
        757 : 3,
        767 : 3,
        777 : 9,
        787 : 9,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )
    
@AlternativeStopPositions
def customOffsetApronSE463(aircraftData):

    table = {
        0: 0,
        321 : 3.1,
        737 : 1.6,
        747 : 11.3,
        757 : 3.1,
        767 : 3.1,
        777 : 11.3,
        787 : 11.3,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )
    
@AlternativeStopPositions
def customOffsetApronSE471(aircraftData):

    table = {
        0: 0,
        321 : 6,
        757 : 6,
        767 : 6,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )
    
@AlternativeStopPositions
def customOffsetApronSE473(aircraftData):

    table = {
        0: 0,
        321 : 3.3,
        737 : 1.5,
        747 : 14.4,
        757 : 3.3,
        767 : 3.3,
        777 : 14.4,
        787 : 14.4,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )

ApronNWSW = CustomizedName("Apron NW/SW | Stand #",1)

ApronN = CustomizedName("Apron N (Terminal) | Gate #",2)
ApronS = CustomizedName("Apron S | Stand #",3)

ApronNESE = CustomizedName("Apron NE/SE | Stand #",4)

ApronM = CustomizedName("Apron M | Stand #",5)

parkings = {

    PARKING : {
        None : ( ),
        202 : (ApronNWSW, customOffsetApronNWSWLarge1, ),
        203 : (ApronNWSW, customOffsetApronNWSWSmall1, ),
        205 : (ApronNWSW, customOffsetApronNWSWSmall3, ),
        206 : (ApronNWSW, customOffsetApronNWSWLarge1, ),
        207 : (ApronNWSW, customOffsetApronNWSWSmall1, ),
        208 : (ApronNWSW, customOffsetApronNWSWLarge2, ),
        209 : (ApronNWSW, customOffsetApronNWSWSmall2, ),
        210 : (ApronNWSW, customOffsetApronNWSWLarge2, ),
        211 : (ApronNWSW, customOffsetApronNWSWSmall4, ),
        212 : (ApronNWSW, customOffsetApronNWSWLarge2, ),
        213 : (ApronNWSW, customOffsetequal, ),
    
        314 : (ApronN, customOffsetApronNGate314, ),
        316 : (ApronN, customOffsetApronNGate316, ),
        318 : (ApronN, customOffsetApronNGate318, ),
        320 : (ApronN, customOffsetApronNGate320, ),
        321 : (ApronS, customOffsetApronS, ),
        322 : (ApronN, customOffsetApronNGate322, ),
        323 : (ApronS, customOffsetApronS, ),
        324 : (ApronN, customOffsetequal, ),
        325 : (ApronS, customOffsetApronS, ),
    
        432 : (ApronNESE, customOffsetApronNE432, ),
        434 : (ApronNESE, customOffsetApronNE434, ),
        436 : (ApronNESE, customOffsetApronNE436, ),
        442 : (ApronNESE, customOffsetApronNE442, ),
        444 : (ApronNESE, customOffsetApronNE444, ),
        446 : (ApronNESE, customOffsetApronNE446, ),
        451 : (ApronNESE, customOffsetApronSECommon, ),
        453 : (ApronNESE, customOffsetApronSE453, ),
        454 : (ApronNESE, customOffsetApronNE454, ),
        455 : (ApronNESE, customOffsetApronSECommon, ),
        456 : (ApronNESE, customOffsetApronNE456, ),
        461 : (ApronNESE, customOffsetApronSECommon, ),
        462 : (ApronNESE, customOffsetApronNE462p466, ),
        463 : (ApronNESE, customOffsetApronSE463, ),
        464 : (ApronNESE, customOffsetApronNE464, ),
        465 : (ApronNESE, customOffsetApronSECommon, ),
        466 : (ApronNESE, customOffsetApronNE462p466, ),
        471 : (ApronNESE, customOffsetApronSE471, ),
        473 : (ApronNESE, customOffsetApronSE473, ),
        475 : (ApronNESE, customOffsetApronSECommon, ),
    
        500 : (ApronM, customOffsetequal, ),
    },

    0 : {
        None : ( ),
        201 : (ApronNWSW, customOffsetApronNWSWSmall1, ),
        204 : (ApronNWSW, customOffsetApronNWSWLarge1, ),
        452 : (ApronNESE, customOffsetApronNE452, ),
    },

} 