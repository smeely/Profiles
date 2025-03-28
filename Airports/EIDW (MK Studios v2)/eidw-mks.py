# -- coding: utf-8 --

version = "2.0.0"
msfs_mode = 1
icao = "eidw"        

pier_1 = CustomizedName("Pier 1 | Stand #§", 1)
pier_1_l = CustomizedName("Pier 1 | Stand #L", 1)
pier_1_c = CustomizedName("Pier 1 | Stand #C", 1)
pier_1_r = CustomizedName("Pier 1 | Stand #R", 1)

pier_1_remote = CustomizedName("Pier 1 Remote | Stand #§", 2)

pier_2 = CustomizedName("Pier 2 | Stand #§", 3)

pier_3c = CustomizedName("Pier 3 | Gate #C", 4)
pier_3 = CustomizedName("Pier 3 | Gate #", 4)

pier_4l = CustomizedName("Pier 4 | Gate #L", 5)
pier_4c = CustomizedName("Pier 4 | Gate #C", 5)
pier_4r = CustomizedName("Pier 4 | Gate #R", 5)

south_apron = CustomizedName("South Apron | Stand #§", 6)

north_remote = CustomizedName("North Remote | Stand #§", 7)

apron_west_cargo = CustomizedName("West Apron (Cargo) | Stand #§", 8)
apron_west = CustomizedName("West Apron | Stand #§", 9)

ga = CustomizedName("GA Apron | Stand #§", 10)

maintenance = CustomizedName("Maintenance | Stand #§", 11)

inop = CustomizedName("INOP", 12)

@AlternativeStopPositions
def default_stop(aircraftData):
    return Distance.fromMeters(0)

parkings = {
	GATE : {
        None : ( ),
        119 : (pier_1_c, default_stop),
        312 : (pier_3, default_stop),
        314 : (pier_3, default_stop),
        315 : (CustomizedName("Pier 3 | Gate 315C", 4), default_stop),
        316 : (pier_3, default_stop),
        317 : (pier_3, default_stop),
        405 : (CustomizedName("Pier 4 | Gate 405", 5), )
    },
    GATE_A : {
        None : (CustomizedName("Pier 4 | Gate 406L", 5), )
    },
    GATE_B : {
        None : (CustomizedName("Pier 4 | Gate 406R", 5), )
    },
    GATE_C : {
        None : (),
        144 : (CustomizedName("Pier 1 Remote | Stand 144C", 2), default_stop),
        311 : (pier_3c, default_stop),
        313 : (pier_3c, default_stop),
        318 : (pier_3c, default_stop),
        400 : (pier_4c, ),
        401 : (pier_4c, ),
        402 : (pier_4c, ),
        403 : (pier_4c, ),
        404 : (pier_4c, ),
        406 : (pier_4c, ),
        407 : (pier_4c, ),
        408 : (pier_4c, ),
        409 : (pier_4c, ),
    },
    
    GATE_L : {
        None : ( ),
        144 : (CustomizedName("Pier 1 Remote | Stand 144L", 2), default_stop),
        400 : (pier_4l, ),
        401 : (pier_4l, ),
        402 : (pier_4l, ),
        403 : (pier_4l, ),
        404 : (pier_4l, ),
        407 : (pier_4l, ),
        408 : (pier_4l, ),
        409 : (pier_4l, )
    },
    GATE_R : {
        None : ( ), 
        144 : (CustomizedName("Pier 1 Remote | Stand 144R", 2), default_stop),
        400 : (pier_4r, ),
        401 : (pier_4r, ),
        402 : (pier_4r, ),
        403 : (pier_4r, ),
        404 : (pier_4r, ),
        407 : (pier_4r, ),
        408 : (pier_4r, ),
        409 : (pier_4r, )
    },
    PARKING : {
        None : (),
        1 : (maintenance, ),
        2 : (maintenance, ),
        50 : (north_remote, ),
        51 : (north_remote, ),
        52 : (north_remote, ),
        53 : (north_remote, ),
        105 : (pier_1_remote, default_stop),
        106 : (pier_1_remote, default_stop), 
        "107L" : (pier_1_l, default_stop),
        "107C" : (pier_1_c, default_stop),
        "107R" : (pier_1_r, default_stop),
        108 : (pier_1_l, default_stop),
        "108C" : (pier_1_c, default_stop),
        "108R" : (pier_1_r, default_stop),
        109 : (pier_1_l, default_stop),
        "109C" : (pier_1_c, default_stop),
        "109R" : (pier_1_r, default_stop),
        110 : (pier_1_l, default_stop),
        "110C" : (pier_1_c, default_stop),
        "110R" : (pier_1_r, default_stop),
        111 : (pier_1_l, default_stop),
        "111C" : (pier_1_c, default_stop),
        "111R" : (pier_1_r, default_stop), 
        118 : (pier_1, default_stop),
        "119L" : (pier_1_l, default_stop),
        "119R" : (pier_1_r, default_stop),
        "120L" : (pier_1_l, default_stop),
        "120C" : (pier_1_c, default_stop),
        "120R" : (pier_1_r, default_stop),
        "121L" : (pier_1_l, default_stop),
        121 : (pier_1, default_stop),   
        122 : (pier_1, default_stop),
        123 : (pier_1, default_stop),
        124 : (pier_1, default_stop),
        125 : (pier_1, default_stop),
        126 : (pier_1, default_stop),
        127 : (pier_1, default_stop),
        130 : (pier_2, default_stop),
        "131S" : (pier_2, default_stop),
        "132L" : (pier_2, default_stop),
        "132C" : (pier_2, default_stop),
        "132R" : (pier_2, default_stop),
        "133L" : (pier_2, default_stop),
        "133C" : (pier_2, default_stop),
        137 : (pier_1_remote, default_stop),
        138 : (pier_1_remote, default_stop),
        139 : (pier_1_remote, default_stop),
        140 : (pier_1_remote, default_stop),
        141 : (pier_1_remote, default_stop),
        142 : (pier_1_remote, default_stop),
        145 : (pier_1_remote, default_stop),
        "200L" : (pier_2, default_stop),
        "200C" : (pier_2, default_stop),
        "200R" : (pier_2, default_stop),
        201 : (pier_2, default_stop),
        202 : (pier_2, default_stop),
        "203L" : (pier_2, default_stop),
        "203C" : (pier_2, default_stop),
        "203R" : (pier_2, default_stop),
        "205T" : (pier_2, default_stop),
        "205L" : (pier_2, default_stop),
        "205R" : (pier_2, default_stop),
        "206T" : (pier_2, default_stop),
        207 : (CustomizedName("Pier 2 | Stand 207T", 3), default_stop),
        "311L" : (CustomizedName("Pier 3 | Stand 311L", 4), default_stop),
        "311R" : (inop, ),
        "313L" : (CustomizedName("Pier 3 | Stand 313L", 4), default_stop),
        "313R" : (CustomizedName("Pier 3 | Stand 313R", 4), default_stop),
        "315L" : (CustomizedName("Pier 3 | Stand 315L", 4), default_stop),
        "315R" : (inop, ),
        "318L" : (CustomizedName("Pier 3 | Stand 318L", 4), default_stop),
        "318R" : (CustomizedName("Pier 3 | Stand 318R", 4), default_stop),
        "411T" : (inop, ),
        "411L" : (south_apron, default_stop),
        "411C" : (south_apron, default_stop),
        "411R" : (south_apron, default_stop),
        412 : (south_apron, default_stop),
        413 : (south_apron, default_stop),
        414 : (south_apron, default_stop),
        415 : (south_apron, default_stop),
        416 : (south_apron, default_stop),
        417 : (south_apron, default_stop),
        418 : (south_apron, default_stop),
        600 : (ga, ),
        601 : (ga, ),
        602 : (ga, ),
        603 : (ga, ),
        604 : (ga, ),
        605 : (ga, ),
        606 : (ga, ),
        607 : (ga, ),
        "614L" : (inop, ),
        "614C" : (apron_west_cargo, default_stop),
        "614R" : (inop, ),
        "615L" : (inop, ),
        "615C" : (apron_west_cargo, default_stop),
        "615R" : (inop, ),
        "616L" : (inop, ),
        "616C" : (apron_west_cargo, default_stop),
        "616R" : (inop, ),
        "617L" : (inop, ),
        "617C" : (apron_west_cargo, default_stop),
        "617R" : (inop, ),
        "618L" : (inop, ),
        "618C" : (apron_west_cargo, default_stop),
        "618R" : (inop, ),
        "619L" : (inop, ),
        "619C" : (apron_west_cargo, default_stop),
        "619R" : (inop, ),
        "620L" : (inop, ),
        "620C" : (apron_west_cargo, default_stop),
        "620R" : (inop, ),
        "621L" : (inop, ),
        "621C" : (apron_west_cargo, default_stop),
        "621R" : (inop, )
    }
}