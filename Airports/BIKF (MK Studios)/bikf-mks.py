# -- coding: utf-8 --
# Scenery = MK Studios - BIKF Keflavik

version: "1.3.0"
msfs_mode = 1
icao = "bikf"

terminal_apron = CustomizedName("Terminal Apron | Gate #§", 1)
terminal_west_remote = CustomizedName("Terminal Remote West Apron | Stand #§", 2)
terminal_east_remote = CustomizedName("Terminal Remote East Apron | Stand #§", 3)
remote_k = CustomizedName("Remote Apron K | Stand #§", 4)
east_apron = CustomizedName("East Apron | Stand #§", 5)
k = CustomizedName("Taxiway K | Stand #§", 6)
military = CustomizedName("Military | Stand #§", 7)
maint = CustomizedName("Maintenance Area | Stand #§", 8)
do_not_use = CustomizedName("Do Not Use | N/A", 9)

@AlternativeStopPositions
def default_stops(aircraftData):
    return Distance.fromMeters(0)

@AlternativeStopPositions
def custom_stops_3(aircraftData):
    return Distance.fromMeters(6.1 if aircraftData.aircraftGroup == "ARC-D" else 0)

@AlternativeStopPositions
def custom_stops_4(aircraftData):
    distances = {
        "ARC-D": 7.1,
        "ARC-E": 13.2
    }

    return Distance.fromMeters(distances.get(aircraftData.aircraftGroup, 0))

@AlternativeStopPositions
def custom_stops_5(aircraftData):
    return Distance.fromMeters(2.5 if aircraftData.aircraftGroup == "ARC-D" else 0)

@AlternativeStopPositions
def custom_stops_8(aircraftData):
    return Distance.fromMeters(4.25 if aircraftData.aircraftGroup == "ARC-D" else 0)

@AlternativeStopPositions
def custom_stops_9(aircraftData):
    return Distance.fromMeters(5.4 if aircraftData.aircraftGroup == "ARC-D" else 0)

@AlternativeStopPositions
def custom_stops_10_12(aircraftData):
    distances = {
        "ARC-D": 4,
        "ARC-E": 4,
        "ARC-F": 4
    }

    return Distance.fromMeters(distances.get(aircraftData.aircraftGroup, 0))

@AlternativeStopPositions
def custom_stops_11(aircraftData):
    distances = {
        "ARC-D": 3.25,
        "ARC-E": 5.3,
        "ARC-F": 5.3
    }

    return Distance.fromMeters(distances.get(aircraftData.aircraftGroup, 0))

@AlternativeStopPositions
def custom_stops_14(aircraftData):
    distances = {
        "ARC-D": 4,
        "ARC-E": 7.5,
        "ARC-F": 7.5
    }

    return Distance.fromMeters(distances.get(aircraftData.aircraftGroup, 0))

@AlternativeStopPositions
def custom_stops_40(aircraftData):
    return Distance.fromMeters(5.4 if aircraftData.aircraftGroup == "ARC-D" else 0)

@AlternativeStopPositions
def custom_stops_42(aircraftData):
    return Distance.fromMeters(4 if aircraftData.aircraftGroup == "ARC-D" else 0)

@AlternativeStopPositions
def custom_stops_44(aircraftData):
    return Distance.fromMeters(8.05 if aircraftData.aircraftGroup == "ARC-D" else 0)

@AlternativeStopPositions
def custom_stops_46(aircraftData):
    distances = {
        "ARC-D": 2.2,
        "ARC-E": 7.15,
        "ARC-F": 7.15
    }

    return Distance.fromMeters(distances.get(aircraftData.aircraftGroup, 0))

@AlternativeStopPositions
def custom_stops_70(aircraftData):
    distances = {
        "ARC-D": 6.6,
        "ARC-E": 10.4,
        "ARC-F": 10.4
    }

    return Distance.fromMeters(distances.get(aircraftData.aircraftGroup, 0))

@AlternativeStopPositions
def custom_stops_70L(aircraftData):
    return Distance.fromMeters(4.7 if aircraftData.aircraftGroup == "ARC-D" else 0)

@AlternativeStopPositions
def custom_stops_71(aircraftData):
    distances = {
        "ARC-D": 5,
        "ARC-E": 9.5,
        "ARC-F": 9.5
    }

    return Distance.fromMeters(distances.get(aircraftData.aircraftGroup, 0))

@AlternativeStopPositions
def custom_stops_72(aircraftData):
    distances = {
        "ARC-D": 6.95,
        "ARC-E": 10.85,
        "ARC-F": 10.85
    }

    return Distance.fromMeters(distances.get(aircraftData.aircraftGroup, 0))

@AlternativeStopPositions
def custom_stops_73(aircraftData):
    distances = {
        "ARC-D": 5.1,
        "ARC-E": 10.5,
        "ARC-F": 10.5
    }

    return Distance.fromMeters(distances.get(aircraftData.aircraftGroup, 0))

@AlternativeStopPositions
def custom_stops_73L(aircraftData):
    return Distance.fromMeters(5.9 if aircraftData.aircraftGroup == "ARC-D" else 0)

@AlternativeStopPositions
def custom_stops_74_6_8(aircraftData):
    return Distance.fromMeters(6 if aircraftData.aircraftGroup == "ARC-D" else 0)

@AlternativeStopPositions
def custom_stops_75(aircraftData):
    distances = {
        "ARC-D": 5.1,
        "ARC-E": 10.5,
        "ARC-F": 10.5
    }

    return Distance.fromMeters(distances.get(aircraftData.aircraftGroup, 0))

@AlternativeStopPositions
def custom_stops_77R(aircraftData):
    return Distance.fromMeters(6.1 if aircraftData.aircraftGroup == "ARC-D" else 0)

@AlternativeStopPositions
def custom_stops_77(aircraftData):
    distances = {
        "ARC-D": 6.1,
        "ARC-E": 11.6,
        "ARC-F": 11.6
    }

    return Distance.fromMeters(distances.get(aircraftData.aircraftGroup, 0))

@AlternativeStopPositions
def custom_stops_79(aircraftData):
    distances = {
        "ARC-D": 6,
        "ARC-E": 11.5,
        "ARC-F": 11.5
    }

    return Distance.fromMeters(distances.get(aircraftData.aircraftGroup, 0))

parkings = {
    0 : {
        None : (military, )
    },
    GATE : {
        None : (),
        1 : (terminal_apron, default_stops),
        3 : (terminal_apron, custom_stops_3),
        4 : (terminal_apron, custom_stops_4),
        5 : (terminal_apron, custom_stops_5),
        7 : (terminal_apron, default_stops),
        8 : (terminal_apron, custom_stops_8),
        9 : (terminal_apron, custom_stops_9),
        10 : (CustomizedName("Terminal Apron | Stand 10", 1), custom_stops_10_12),
        11 : (terminal_apron, custom_stops_11),
        12 : (terminal_apron, custom_stops_10_12),
        14 : (terminal_apron, custom_stops_14),
        40 : (terminal_west_remote, custom_stops_40),
        42 : (terminal_west_remote, custom_stops_42),
        44 : (terminal_west_remote, custom_stops_44),
        46 : (terminal_west_remote, custom_stops_46),
        70 : (terminal_east_remote, custom_stops_70),
        71 : (terminal_east_remote, custom_stops_71),
        72 : (terminal_east_remote, custom_stops_72),
        73 : (terminal_east_remote, custom_stops_73),
        74 : (terminal_east_remote, custom_stops_74_6_8),
        75 : (terminal_east_remote, custom_stops_75),
        76 : (terminal_east_remote, custom_stops_74_6_8),
        77 : (terminal_east_remote, custom_stops_77),
        78 : (terminal_east_remote, custom_stops_74_6_8),
        79 : (terminal_east_remote, custom_stops_79),
        84 : (k, ),
        112 : (east_apron, ),
        113 : (east_apron, )
    },
    GATE_L : {
        None : (),
        46 : (CustomizedName("Terminal Remote West Apron | Stand 46L", 2), default_stops),
        70 : (CustomizedName("Terminal Remote East Apron | Stand 70L", 3), custom_stops_70L),
        72 : (CustomizedName("Terminal Remote East Apron | Stand 72L", 3), default_stops),
        73 : (CustomizedName("Terminal Remote East Apron | Stand 73L", 3), custom_stops_73L),
        75 : (CustomizedName("Terminal Remote East Apron | Stand 75L", 3), default_stops)
    },
    GATE_R : {
        None : (),
        46 : (CustomizedName("Terminal Remote West Apron | Stand 46R", 2), default_stops),
        71 : (do_not_use, ),
        72 : (do_not_use, ),
        73 : (CustomizedName("Terminal Remote East Apron | Stand 73R", 3), default_stops),
        75 : (CustomizedName("Terminal Remote East Apron | Stand 75R", 3), default_stops),
        77 : (CustomizedName("Terminal Remote East Apron | Stand 77R", 3), custom_stops_77R),
        79 : (CustomizedName("Terminal Remote East Apron | Stand 79R", 3), default_stops)
    },
    PARKING : {
        None : (east_apron, ),
        51 : (k, ),
        52 : (k, ),
        53 : (k, ),
        54 : (k, ),
        55 : (remote_k, default_stops),
        56 : (k, ),
        57 : (remote_k, default_stops),
        58 : (k, ),
        59 : (remote_k, default_stops),
        61 : (remote_k, default_stops),
        63 : (maint, ),
        64 : (maint, ),
        65 : (maint, ),
        67 : (k, ),
        69 : (k, ),
        112 : (CustomizedName("East Apron | Stand 114", 5), )
    }
}