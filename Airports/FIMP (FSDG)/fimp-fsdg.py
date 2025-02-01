# -- coding: utf-8 --
# Scenery = FSDG - FIMP Mauritius

msfs_mode = 1
icao = "fimp"
version = "2.0.0"

terminal = CustomizedName("Terminal | Gate #§",1)
ga_apron = CustomizedName("GA Apron | Parking #§",2)

@AlternativeStopPositions
def custom_offset_small(aircraftData):
	distances = {
		0: 0,
		319: 2.8,
		320: 2.8,
		321: 2.8,
		737: 2.8
	}

	return Distance.fromMeters(distances.get(aircraftData.idMajor, 0))

@AlternativeStopPositions
def custom_offset(aircraftData):
	distances = {
		0: 0,
		300: 4.45,
		310: 4.45,
		319: 0,
		320: 0,
		321: 1.5,
		737: 1.5,
		787: 4.45,
		330: 4.45,
		340: 6,
		767: 4.45,
		747: 7.4
	}

	distances_777 = {
		0: 7.4,
		200: 7.4,
		300: 10.3
	}

	if aircraftData.idMajor == 777:
		return Distance.fromMeters(distances_777.get(aircraftData.idMinor, 0))
	else:
		return Distance.fromMeters(distances.get(aircraftData.idMajor, 0))


parkings = {
	GATE : {
        None : (),
        2 : (terminal, custom_offset_small),
        3 : (terminal, ),
        5 : (terminal, ),
        7 : (terminal, ),
        8 : (terminal, ),
        9 : (terminal, ),
        12 : (terminal, custom_offset),
        13 : (terminal, custom_offset),
        14 : (terminal, custom_offset),
        16 : (terminal, custom_offset),
        42 : (ga_apron, ),
        43 : (ga_apron, ),
        44 : (ga_apron, ),
        45 : (ga_apron, ),
        47 : (ga_apron, ),
        48 : (ga_apron, )
	}
}