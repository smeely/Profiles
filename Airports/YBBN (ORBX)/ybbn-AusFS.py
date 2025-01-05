# -- coding: utf-8 --

version = 1.3.0
msfs_mode = 1
icao = "ybbn"

default_parking_type = "Bay"

# -- UIGrouping Definitions --
#
# (Priority, GroupingName)
# Priority is UI Order (1 is top of list)
# GroupingName is UI Grouping
Intl   = (1, "International")

DomQLK = (2, "Domestic North (QantasLink)")
DomQFA = (3, "Domestic North (Qantas)")
DomCUT = (4, "Domestic Central (Common User)")
DomVOZ = (5, "Domestic South (Virgin Australia)")

GA = (6, "General Aviation Apron")
Logist = (7, "Logistics Apron")
Hangar = (8, "Hangars")

PADomN = (8, "Parking Apron - Domestic North")
PADomS = (9, "Parking Apron - Domestic South")
PASth = (10, "Parking Apron - Airport South")

# -- Function Definitions --
#
# ManualNames - Used when scenery naming is incorrect
#    UIGrouping + Position Name
#        UIGrouping can be UIGrouping or manually defined. e.g. (1, "Test Terminal")
#        positionName must be entire name. e.g. "Bay 1L"

def ManualNames((priority, groupingName), positionName):
    return CustomizedName( "%s|%s" % (groupingName, positionName), priority )

# PresetNames - StandardUIGrouping + extraSuffix + parkingType
#    UIGrouping can be UIGrouping or manually defined. e.g. (1, "Test Terminal")
#    extraSuffix. Defaults to empty. Value is appendix to end of default sim name. e.g. "Left" to "Bay 1" creates "Bay 1 Left"
#    parking_type. Defaults to predefined value. By default set to "Bay"

def PresetNames((priority, groupingName), extraSuffix = "", parkingType = default_parking_type):
    return CustomizedName( "%s|%s #§ %s" % (groupingName, parkingType, extraSuffix), priority )

parkings = {
    GATE : {
        None : ( ),
        16    : (PresetNames(DomQFA), ),
        17    : (PresetNames(DomQFA), ),
        18    : (PresetNames(DomQFA), ),
        19    : (PresetNames(DomQFA), ),
        20    : (PresetNames(DomQFA), ),
        21    : (PresetNames(DomQFA), ),
        22    : (ManualNames(DomQFA, "Bay 22"), ), # Correct Orbx Error
        23    : (PresetNames(DomQFA), ),
        24    : (PresetNames(DomQFA), ),

        25    : (PresetNames(DomCUT), ),
        26    : (PresetNames(DomCUT), ),
        27    : (PresetNames(DomCUT), ),
        28    : (PresetNames(DomCUT), ),
        29    : (PresetNames(DomCUT), ),
        30    : (PresetNames(DomCUT), ),
        31    : (PresetNames(DomCUT), ),
        32    : (PresetNames(DomCUT), ),
        38    : (PresetNames(DomCUT), ),
        39    : (PresetNames(DomCUT), ),

        40    : (PresetNames(DomVOZ), ),
        41    : (PresetNames(DomVOZ), ),
        "41B" : (ManualNames(DomVOZ, "Bay 41"), ), # Correct Orbx Error
        43    : (PresetNames(DomVOZ), ),
        44    : (PresetNames(DomVOZ), ),
        45    : (PresetNames(DomVOZ), ),
        46    : (PresetNames(DomVOZ), ),
        47    : (PresetNames(DomVOZ), ),
        48    : (PresetNames(DomVOZ), ),
        49    : (PresetNames(DomVOZ), ),
        50    : (PresetNames(DomVOZ), ),

        72    : (PresetNames(Intl), ),
        73    : (PresetNames(Intl), ),
        74    : (PresetNames(Intl), ), # Orbx have 74 as RAMP
        75    : (PresetNames(Intl), ),
        76    : (PresetNames(Intl), ),
        77    : (PresetNames(Intl), ),
        78    : (PresetNames(Intl), ),
        79    : (PresetNames(Intl), ),
        80    : (PresetNames(Intl), ),
        81    : (PresetNames(Intl), ),
        82    : (PresetNames(Intl), ),
        83    : (PresetNames(Intl), ),
        84    : (PresetNames(Intl), ),
        85    : (PresetNames(Intl), ),
        86    : (PresetNames(Intl), ),
        87    : (PresetNames(Intl), ),
    },
    PARKING : {
        None : ( ),
        1     : (PresetNames(DomQLK), ),
        3     : (PresetNames(DomQLK), ),
        4     : (PresetNames(DomQLK), ),
        5     : (PresetNames(DomQLK), ),
        6     : (PresetNames(DomQLK), ),


        53    : (PresetNames(PADomS), ),
        54    : (PresetNames(PADomS), ),
        55    : (PresetNames(PADomS), ),
        56    : (PresetNames(PADomS), ),
        57    : (PresetNames(PADomS), ),
        60    : (PresetNames(PADomS), ),
        61    : (PresetNames(PADomS), ),
        62    : (PresetNames(PADomS), ),
        63    : (PresetNames(PADomS), ),
        64    : (PresetNames(PADomS), ),

        69    : (PresetNames(Intl), ),
        70    : (PresetNames(Intl), ),
        71    : (PresetNames(Intl), ),
        72    : (PresetNames(Intl), ),

        15    : (PresetNames(PADomN), ),
        100   : (PresetNames(PADomN), ),
        101   : (PresetNames(PADomN), ),
        102   : (PresetNames(PADomN), ),
        103   : (PresetNames(PADomN), ),
        108   : (PresetNames(PADomN), ),
        109   : (PresetNames(PADomN), ),
        110   : (PresetNames(PADomN), ),
        111   : (PresetNames(PADomN), ),
    },
    DOCK : {
        None : ( ),
        1 : (ManualNames(Logist, "L1"), ),
        2 : (ManualNames(Logist, "L1A"), ), # Correct Orbx Error
        3 : (ManualNames(Logist, "L3"), ),
        4 : (ManualNames(Logist, "L4"), ),
        5 : (ManualNames(Logist, "L5"), ),
        6 : (ManualNames(Logist, "L6"), ),
    },

    
    SE_PARKING : {
        None : ( ),
        1    : (ManualNames(Logist, "Avcair 1"), ),
        2    : (ManualNames(Logist, "Avcair 2"), ),
    },
    
    
    E_PARKING : {
        None : ( ),
        1    : (ManualNames(Hangar, "Northrop Grumman | Parking 1"), ),
        2    : (ManualNames(Hangar, "Northrop Grumman | Parking 2"), ),
        3    : (ManualNames(Hangar, "Hangar 2 (Qantas) | Parking 1"), ),
        4    : (ManualNames(Hangar, "Hangar 2 (Qantas) | Parking 2"), ),
        5    : (ManualNames(Hangar, "Hangar 3 (Qantas) | Parking 1"), ),
        6    : (ManualNames(Hangar, "Hangar 3 (Qantas) | Parking 2"), ),
    },
    
    NE_PARKING : {
        None : ( ),
        1    : (ManualNames(Hangar, "LifeFlight"), ),
        2    : (ManualNames(Hangar, "QantasLink"), ),
        3    : (ManualNames(Hangar, "Airbus Helicopters | Parking 1"), ),
        4    : (ManualNames(Hangar, "Airbus Helicopters | Parking 2"), ),
        5    : (ManualNames(Hangar, "Unity Aviation Maintenance | Parking 1"), ),
        6    : (ManualNames(Hangar, "Unity Aviation Maintenance | Parking 2"), ),
        7    : (ManualNames(Hangar, "Alliance Airlines"), ),
        8    : (ManualNames(Hangar, "Virgin Australia"), ),
        9    : (ManualNames(Hangar, "Nauru Airlines"), ),
    },
    
    N_PARKING : {
        None : ( ),
        1    : (PresetNames(GA, ), ),
        2    : (PresetNames(GA, ), ),
        3    : (PresetNames(GA, ), ),
        4    : (PresetNames(GA, ), ),
        5    : (PresetNames(GA, ), ),
        6    : (PresetNames(GA, ), ),
        7    : (PresetNames(GA, ), ),
        8    : (PresetNames(GA, ), ),
        9    : (PresetNames(GA, ), ),
        10   : (PresetNames(GA, ), ),
        11   : (PresetNames(GA, ), ),
        12   : (PresetNames(GA, ), ),
        13   : (PresetNames(GA, ), ),
        14   : (PresetNames(GA, ), ),
        15   : (PresetNames(GA, ), ),
        16   : (PresetNames(GA, ), ),
        17   : (PresetNames(GA, ), ),
        18   : (PresetNames(GA, ), ),
        19   : (PresetNames(GA, ), ),
        20   : (PresetNames(GA, ), ),
        21   : (PresetNames(GA, ), ),
        22   : (PresetNames(GA, ), ),
        23   : (PresetNames(GA, ), ),
    },
    
    SW_PARKING : {
        None : ( ),
        1    : (PresetNames(PASth, ), ),
        2    : (PresetNames(PASth, ), ),
        3    : (PresetNames(PASth, ), ),
        4    : (PresetNames(PASth, ), ),
        7    : (PresetNames(PASth, ), ),
    },
    
    0 : { # TO BE FIXED
        None : ( ),
        74    : (PresetNames(Intl), ),
    },
}