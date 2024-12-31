# -- coding: utf-8 --

msfs_mode = 1
icao = "eidw"

@AlternativeStopPositions
def customOffsetEqual(aircraftData):

    table = {
        318: 0,
        319: 0,
        320: 0,
        321: 0,
        330: 0,
        737: 0,
        747: 0,
        757: 0,
        767: 0,
        777: 0,
        787: 0,
        42: 0,
        72: 0,
        170: 0,
        175: 0,
        190: 0,
        195: 0,
    }
    
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance()
        
        

Pier1 = CustomizedName("Pier 1 | Stand #§",1)
Pier1Re = CustomizedName("Pier 1 Remote | Stand #§",2)

Pier2 = CustomizedName("Pier 2 | Stand #§",3)

Pier3 = CustomizedName("Pier 3 | Gate #§",4)

Pier4left = CustomizedName("Pier 4 | Gate #L",5)
Pier4center = CustomizedName("Pier 4 | Gate #C",5)
Pier4right = CustomizedName("Pier 4 | Gate #R",5)

Pier4PBZ = CustomizedName("Pier 4 PBZ | Stand #§",6)

NorthRe = CustomizedName("North Remote | Stand #§",7)

WestAp = CustomizedName("West Apron | Stand #§",8)

GaAp = CustomizedName("GA Apron | Stand #§",9)

Maint = CustomizedName("Maintenance | Stand #§",10)

Inop = CustomizedName("INOP DO NOT USE",11)


parkings = {
	GATE : {
        None : ( ),
        119 : (Pier1, ),
        312 : (Pier3, ),
        314 : (Pier3, ),
        315 : (Pier3, ),
        316 : (Pier3, ),
        317 : (Pier3, ),
        405 : (Pier4center, ),
    },
    
    GATE_A : {
        None : (Pier4left, ),
    },
    
    GATE_B : {
        None : (Inop, ),
    },

    GATE_C : {
        None : ( ),
        144 : (Inop, ),
        311 : (Pier3, ),
        313 : (Pier3, ),
        318 : (Pier3, ),
        400 : (Pier4center, ),
        401 : (Pier4center, ),
        402 : (Pier4center, ),
        403 : (Pier4center, ),
        404 : (Pier4center, ),
        406 : (Pier4center, ),
        407 : (Pier4center, ),
        408 : (Pier4center, ),
        409 : (Pier4center, ),
    },
    
    GATE_L : {
        None : ( ),
        144 : (Inop, ),
        400 : (Pier4left, ),
        401 : (Pier4left, ),
        402 : (Pier4left, ),
        403 : (Pier4left, ),
        404 : (Pier4left, ),
        407 : (Pier4left, ),
        408 : (Pier4left, ),
        409 : (Pier4left, ),
    },
    
    GATE_R : {
        None : ( ), 
        144 : (Inop, ),
        400 : (Pier4right, ),
        401 : (Pier4right, ),
        402 : (Pier4right, ),
        403 : (Pier4right, ),
        404 : (Pier4right, ),
        407 : (Pier4right, ),
        408 : (Pier4right, ),
        409 : (Pier4right, ),
    },
    
    PARKING : {
        None : ( ),
        1 : (Maint, ),
        2 : (Maint, ),
        50 : (NorthRe, ),
        51 : (NorthRe, ),
        52 : (NorthRe, ),
        53 : (NorthRe, ),
        105 : (Pier1Re, customOffsetEqual, ),
        106 : (Pier1Re, customOffsetEqual, ), 
        107 : (Pier1, customOffsetEqual, ),
        108 : (Pier1, customOffsetEqual, ),
        109 : (Pier1, customOffsetEqual, ),
        110 : (Pier1, customOffsetEqual, ),
        111 : (Pier1, customOffsetEqual, ),
        118 : (Pier1, customOffsetEqual, ),
        119 : (Pier1, customOffsetEqual, ),
        120 : (Pier1, customOffsetEqual, ),
        121 : (Pier1, customOffsetEqual, ),
        122 : (Pier1, customOffsetEqual, ),
        123 : (Pier1, customOffsetEqual, ),
        124 : (Pier1, customOffsetEqual, ),
        125 : (Pier1, customOffsetEqual, ),
        126 : (Pier1, customOffsetEqual, ),
        127 : (Pier1, customOffsetEqual, ),
        130 : (Pier1Re, customOffsetEqual, ),
        131 : (Pier1Re, customOffsetEqual, ),
        132 : (Pier1Re, customOffsetEqual, ),
        133 : (Pier1Re, customOffsetEqual, ),
        137 : (Pier1Re, customOffsetEqual, ),
        138 : (Pier1Re, customOffsetEqual, ),
        139 : (Pier1Re, customOffsetEqual, ),
        140 : (Pier1Re, customOffsetEqual, ),
        141 : (Pier1Re, customOffsetEqual, ),
        142 : (Pier1Re, customOffsetEqual, ),
        145 : (Inop, ),
        200 : (Pier2, ),
        201 : (Pier2, ),
        202 : (Pier2, ),
        203 : (Pier2, ),
        205 : (Pier2, ),
        206 : (Pier2, ),
        207 : (Pier2, ),
        311 : (Pier3, ),
        313 : (Pier3, ),
        315 : (Pier3, ),
        318 : (Pier3, ),
        411 : (Pier4PBZ, ),
        412 : (Pier4PBZ, ),
        413 : (Pier4PBZ, ),
        414 : (Pier4PBZ, ),
        415 : (Pier4PBZ, ),
        416 : (Pier4PBZ, ),
        417 : (Pier4PBZ, ),
        418 : (Pier4PBZ, ),
        600 : (GaAp, ),
        601 : (GaAp, ),
        602 : (GaAp, ),
        603 : (GaAp, ),
        604 : (GaAp, ),
        605 : (GaAp, ),
        606 : (GaAp, ),
        607 : (GaAp, ),
        612 : (WestAp, ),
        614 : (WestAp, ),
        615 : (WestAp, ),
        616 : (WestAp, ),
        617 : (WestAp, ),
        618 : (WestAp, ),
        619 : (WestAp, ),
        620 : (WestAp, ),
        621 : (WestAp, ),
    },

}