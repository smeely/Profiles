# -- coding: utf-8 --

version = 1.5
msfs_mode = 1
icao = "lepa"

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
    return Distance.fromMeters(0)

PaxPierA=CustomizedName('Terminal A (08-22) | Stand #§', 1)
PaxPierB=CustomizedName('Terminal B (30-36) | Stand #§', 2)
PaxPierC=CustomizedName('Terminal C (38-72) | Stand #§', 3)
PaxPierD=CustomizedName('Terminal D (80-98) | Stand #§', 4)
ApronR6=CustomizedName('Terminal A East Remotes (23-25) | Stand #§', 5)
ApronR5=CustomizedName('Terminal A North Remotes (104-108) | Stand #§', 6)
ApronR16=CustomizedName('Terminal D Remotes (150-159) | Stand #§', 7)
ApronR1=CustomizedName('Apron R1 (301-318) | Stand #§', 8)
ApronR3=CustomizedName('Apron R3 (02-06, 100-103) | Stand #§', 9)
ApronR7=CustomizedName('Apron R7 (114-118) | Stand #§', 10)
ApronR8=CustomizedName('Apron R8 (26-29, 119-123) | Stand #§', 11)
ApronR17=CustomizedName('Apron R17 (200-247) | Stand #§', 12)

parkings = {
    PARKING : {
        200 : (ApronR17, ),
        201 : (ApronR17, ),
        202 : (ApronR17, ),
        203 : (ApronR17, ),
        204 : (ApronR17, ),
        205 : (ApronR17, ),
        206 : (ApronR17, ),
        207 : (ApronR17, ),
        208 : (ApronR17, ),
        209 : (ApronR17, ),
        210 : (ApronR17, ),
        211 : (ApronR17, ),
        212 : (ApronR17, ),
        213 : (ApronR17, ),
        214 : (ApronR17, ),
        215 : (ApronR17, ),
        216 : (ApronR17, ),
        217 : (ApronR17, ),
        218 : (ApronR17, ),
        219 : (ApronR17, ),
        220 : (ApronR17, ),
        221 : (ApronR17, ),
        222 : (ApronR17, ),
        223 : (ApronR17, ),
        224 : (ApronR17, ),
        225 : (ApronR17, ),
        226 : (ApronR17, ),
        227 : (ApronR17, ),
        228 : (ApronR17, ),
        229 : (ApronR17, ),
        230 : (ApronR17, ),
        231 : (ApronR17, ),
        232 : (ApronR17, ),
        233 : (ApronR17, ),
        234 : (ApronR17, ),
        235 : (ApronR17, ),
        236 : (ApronR17, ),
        237 : (ApronR17, ),
        238 : (ApronR17, ),
        239 : (ApronR17, ),
        240 : (ApronR17, ),
        241 : (ApronR17, ),
        242 : (ApronR17, ),
        243 : (ApronR17, ),
        244 : (ApronR17, ),
        245 : (ApronR17, ),
        246 : (ApronR17, ),
        247 : (ApronR17, ),
        2 : (ApronR3, ),
        3 : (ApronR3, ),
        4 : (ApronR3, ),
        5 : (ApronR3, ),
        6 : (ApronR3, ),
        100 : (ApronR3, ),
        101 : (ApronR3, ),
        102 : (ApronR3, ),
        103 : (ApronR3, ),
        114 : (ApronR7, ),
        115 : (ApronR7, ),
        116 : (ApronR7, ),
        117 : (ApronR7, ),
        118 : (ApronR7, ),
        119 : (ApronR8, ),
        120 : (ApronR8, ),
        121 : (ApronR8, ),
        122 : (ApronR8, ),
        123 : (ApronR8, ),
        23 : (ApronR6, ),
        24 : (ApronR6, ),
        25 : (ApronR6, ),
        23 : (ApronR6, ),
        24 : (ApronR6, ),
        25 : (ApronR6, ),
        26 : (ApronR8, ),
        27 : (ApronR8, ),
        28 : (ApronR8, ),
        29 : (ApronR8, ),
        301 : (ApronR1, ),
        302 : (ApronR1, ),
        303 : (ApronR1, ),
        155 : (ApronR17, ),
        156 : (ApronR17, ),
        157 : (ApronR17, ),
        158 : (ApronR17, ),
        159 : (ApronR17, ),
        104 : (ApronR5, ),
        105 : (ApronR5, ),
        106 : (ApronR5, ),
        107 : (ApronR5, ),
        108 : (ApronR5, ),
        109 : (ApronR5, ),
        150 : (ApronR16, ),
        151 : (ApronR16, ),
        152 : (ApronR16, ),
        153 : (ApronR16, ),
        154 : (ApronR16, ),
        306 : (ApronR1, ),
        307 : (ApronR1, ),
        308 : (ApronR1, ),
        309 : (ApronR1, ),
        310 : (ApronR1, ),
        311 : (ApronR1, ),
        312 : (ApronR1, ),
        313 : (ApronR1, ),
        314 : (ApronR1, ),
        315 : (ApronR1, ),
        316 : (ApronR1, ),
        317 : (ApronR1, ),
        318 : (ApronR1, ),
    },
    GATE_A : {
        8 : (PaxPierA, ),
        10 : (PaxPierA, ),
        12 : (PaxPierA, ),
        14 : (PaxPierA, ),
        16 : (PaxPierA, ),
        18 : (PaxPierA, ),
        20 : (PaxPierA, ),
        22 : (PaxPierA, )
    },
    GATE_B : {
        30 : (PaxPierB, ),
        32 : (PaxPierB, ),
        34 : (PaxPierB, ),
        36 : (PaxPierB, )
    },
    GATE_C : {
        38 : (PaxPierC, ),
        40 : (PaxPierC, ),
        42 : (PaxPierC, ),
        44 : (PaxPierC, ),
        46 : (PaxPierC, ),
        48 : (PaxPierC, ),
        50 : (PaxPierC, ),
        52 : (PaxPierC, ),
        54 : (PaxPierC, ),
        56 : (PaxPierC, ),
        58 : (PaxPierC, ),
        60 : (PaxPierC, ),
        62 : (PaxPierC, ),
        64 : (PaxPierC, ),
        66 : (PaxPierC, ),
        68 : (PaxPierC, ),
        70 : (PaxPierC, ),
        72 : (PaxPierC, )
    },
    GATE_D : {
       80 : (PaxPierD, ),
        82 : (PaxPierD, ),
        84 : (PaxPierD, ),
        86 : (PaxPierD, ),
        88 : (PaxPierD, ),
        90 : (PaxPierD, ),
        92 : (PaxPierD, ),
        94 : (PaxPierD, ),
        96 : (PaxPierD, ),
        98 : (PaxPierD, )
    }
}
