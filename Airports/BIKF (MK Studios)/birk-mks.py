# -- coding: utf-8 --
# Scenery = MK Studios - BIRK Reykjavik

version = "1.3.0"
msfs_mode = 1
icao = "birk"

apron_1 = CustomizedName("Apron 1 | Stand #", 1)
apron_2 = CustomizedName("Apron 2 | Stand #", 2)
apron_3 = CustomizedName("Apron 3 | Stand #", 3)
apron_4 = CustomizedName("Apron 4 | Stand #", 4)
apron_7 = CustomizedName("Apron 7 | Stand #", 7)

@AlternativeStopPositions
def default_stops(aircraftData):
    return Distance.fromMeters(0)

parkings = {
    PARKING : {
        None : (apron_1, ),
        1 : (apron_4, default_stops),
        3 : (apron_4, default_stops),
        4 : (apron_4, default_stops),
        8 : (apron_4, default_stops),
        9 : (apron_4, default_stops),
        10 : (apron_2, ),
        20 : (apron_3, ),
        31 : (apron_7, )
    }
}