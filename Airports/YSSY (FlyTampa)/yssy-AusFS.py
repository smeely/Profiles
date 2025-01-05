# -- coding: utf-8 --
version = 1.2.0
msfs_mode = 1
icao = "yssy"

default_parking_type = "Bay"

# -- UIGrouping Definitions --
#
# (Priority, GroupingName)
# Priority is UI Order (1 is top of list)
# GroupingName is UI Grouping
Intl   = (1, "T1 International")
IntlCargo = (2, "International Cargo")
DomQFA = (3, "T3 Domestic (Qantas)")
DomQLK = (4, "T3 Domestic (QantasLink Bussing)")
DomCUT = (5, "T2 Domestic (Other)")
DomCUTBussing = (6, "T2 Domestic (Other Bussing)")
GA = (7, "General Aviation Apron")
PASth = (8, "Parking Apron - Airport South")
PASthE = (9, "Parking Apron - Airport South East")
PANorth = (10, "Parking Apron - Airport North")
PAEast = (11, "Parking Apron - Airport East")
QFHangar = (12, "Qantas Jet Base")

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

def HandleAircraftOffsets(aircraftData, specificTables, genericTable):
	try:
		# Try to get the value using idMinor
		return specificTables[aircraftData.idMajor][0].get(aircraftData.idMinor)
	except:
		try:
			# Fallback to the default key (second item in the tuple) if idMinor lookup fails
			return specificTables[aircraftData.idMajor][0].get(specificTables[aircraftData.idMajor][1])
		except:
			# If both lookups fail, use the generic table with a default value of 0 if idMajor isn't found
			return genericTable.get(aircraftData.idMajor, 0)

def subtract_from_result(result, value_to_subtract):
    if isinstance(result, tuple):
        new_first_element = Distance.fromMeters(result[0] - value_to_subtract)
        new_second_element = Distance.fromMeters(result[1])
        return (new_first_element, new_second_element)
    else:
        return Distance.fromMeters(result - value_to_subtract)


@AlternativeStopPositions
def customOffsetDOM1(aircraftData):
	table = {
		0: 0,
        737: 12.5,
        320: 12.5,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetQLK(aircraftData):
	table = {
		0: 0,
        1008: 4.6,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetIntlCargo3to5(aircraftData):
	table = {
		0: 0,
		737: 0,
		320: 0,
        330: 2.5,
        767: 2.5,
        11: 5.4,
        342: 5.4,
        345: 5.4,
        747: 8,
        380: 8,
        346: 12.6,
	}

	table777 = {
		0: 12.6,
		200: 8.0,
		300: 12.6,
	}

	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, {777 : (table777, 0)},table) - 0.25 )

@AlternativeStopPositions
def customOffsetIntlCargo1(aircraftData):
	table = {
		0: 0,
		737: 0,
		320: 0,
        11: 0,
        300: 0,
        310: 0,
        747: 4.1,
        380: 4.1,
        346: 8.5,
	}

	table777 = {
		0: 8.5,
		200: 4.1,
		300: 8.5,
	}
    
	table787 = {
		0: 4.1,
		8: 0,
		9: 4.1,
	}

	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, {777 : (table777, 0),787 : (table787, 0),},table) - 0.25 )



@AlternativeStopPositions
def customOffsetIntlCargo2(aircraftData):
	table = {
		0: 0,
        767: 2.2,
        330: 2.2,
        11: 4.7,
        342: 4.7,
        345: 4.7,
        747: 7.4,
        380: 7.4,
        346: 12.6,
	}

	table777 = {
		0: 12.6,
		200: 7.4,
		300: 12.6,
	}

	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, {777 : (table777, 0)},table) - 0.25 )
    
@AlternativeStopPositions
def customOffsetDom2to6(aircraftData):
	table = {
		0: 0,
        737: 0,
        767: 6.7,
        330: 6.7,
        787: 6.7,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetDom11(aircraftData):
	table = {
		0: 0,
        737: 0,
        320: 13.7,
        787: 15.5,
        330: 17.2,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetDom13(aircraftData):
	table = {
		0: 0,
        737: 0,
        320: 0,
        787: 1.7,
        330: 3.35,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )
	
@AlternativeStopPositions
def customOffsetDom12(aircraftData):
	table = {
		0: 0,
        737: 8.3,
        320: 8.9,
		321: 8.9,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )
	
@AlternativeStopPositions
def customOffsetDom49(aircraftData):
	table = {
		0: 0,
        737: 0,
        320: 1.5,
        321: 1.5,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetDom52to57(aircraftData):
	table = {
		0: 0,
        320: 0,
        321: 0,
        737: 0.7,
        717: 2.2,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetDom5355(aircraftData):
	table = {
		0: 0,
        320: 0,
        321: 0,
        737: 0.4,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetDom58(aircraftData):
	table = {
		0: 0,
        320: 2.3,
        717: 3.6,
        737: 3.6,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetDom59(aircraftData):
	table = {
		0: 0,
        737: 0.8,
        320: 2.3,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetDom32(aircraftData):
	table = {
		0: 0,
        190: 1.0,
        170: 1.0,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetDom33(aircraftData):
	table = {
		0: 0,
        737: 1.0,
        170: 1.9,
        190: 1.9,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetDom34(aircraftData):
	table = {
		0: 0,
        737: 0.7,
        170: 0.7,
        190: 0.7,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetDom39(aircraftData):
	table = {
		0: 0,
        330: 0,
        320: 1.0,
        737: 1.0,
        190: 2.1,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetDom40(aircraftData):
	table = {
		0: 0,
        737: 0.8,
        190: 0.8,
        170: 0.8,
        330: 8.3,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetDom42(aircraftData):
	table = {
		0: 0,
        738: 2.2,
        321: 2.2,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetDom43(aircraftData):
	table = {
		0: 0,
        320: 2.0,
        190: 2.0,
	}
    
	table737 = {
		0: 0,
		700: 0,
		800: 2.0,
	}

	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, {737 : (table737, 0)},table) - 0.25 )

@AlternativeStopPositions
def customOffsetIntl8(aircraftData):
	table = {
		0: 0,
        747: 3.5,
        380: 5.4,
        777: 8.0,
       
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetIntl9(aircraftData):
	table = {
		0: 0,
        330: 1.6,
        747: 3.9,
        777: 5.0,
        380: 6.0,
        346: 7.3, 
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetIntl11(aircraftData):
	table = {
		0: 0,
        320: 1.7,
        737: 1.7,
        321: 5.0,
        757: 11.0,
        767: 12.6,
        330: 12.6,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetIntl12(aircraftData):
	table = {
		0: 0,
        320: 5.7,
        737: 5.7,
        100: 7.0,
        738: 8.8,
        321: 13.0,
        767: 13.0,
        330: 13.0,
        757: 13.0,
	}

	table737 = {
		0: 8.8,
		700: 5.7,
		800: 8.8,
	}

	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, {737 : (table737, 0)},table) - 0.25 )

@AlternativeStopPositions
def customOffsetIntl24(aircraftData):
	table = {
		0: 0,
        787: 6.3,
        330: 7.5,
        747: 9.7,
        380: 11.5,
        777: 14.3,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetIntl25(aircraftData):
	table = {
		0: 0,
        787: 2.2,
        747: 2.2,
        330: 4.8,
        777: 7.6,
        380: 8.7,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetIntl30(aircraftData):
	table = {
		0: 0,
        300: 0,
        310: 0,
        787: 2.6,
        11: 4.4,
        330: 5.5,
        340: 5.5,
        767: 6.6,
        747: 8.5,
        777: 8.5,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetIntl31(aircraftData):
	table = {
		0: 0,
        11: 5.6,
        300: 8.0,
        310: 8.0,
        330: 9.0,
        777: 10.6,
        787: 10.6,
        747: 11.7,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetIntl33(aircraftData):
	table = {
		0: 0,
        330: 2.2,
        777: 4.6,
        787: 4.6,
        747: 5.8,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetIntl34(aircraftData):
	table = {
		0: 0,
        11: 2.6,
        330: 3.7,
        340: 3.7,
        767: 3.7,
        787: 4.7,
        777: 6.3,
        787: 6.3,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetIntl36(aircraftData):
	table = {
		0: 0,
        11: 6.5,
        330: 8.7,
        340: 10.7,
        787: 10.7,
        777: 12.0,
        747: 13.6,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetIntl50(aircraftData):
	table = {
		0: 0,
        777: 19.0,
        747: 19.0,
        787: 19.0,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetIntl51(aircraftData):
	table = {
		0: 0,
        737: 0,
        310: 3.2,
        320: 3.2,
        321: 3.2,
        300: 15.0,
        330: 15.0,
        340: 15.0,
        777: 16.3,
        787: 16.3,
        747: 17.5,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetIntl54(aircraftData):
	table = {
		0: 0,
        737: 0,
        330: 3.3,
        767: 3.3,
        787: 6.3,
        777: 7.7,
        747: 7.7,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetIntl57(aircraftData):
	table = {
		0: 0,
        330: 9.7,
        747: 11.6,
        777: 12.7,
        380: 13.0,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetIntl58(aircraftData):
	table = {
		0: 0,
        11: 5.8,
        300: 8.7,
        310: 8.7,
        787: 10.5,
        747: 12.4,
        330: 12.4,
        777: 14.7,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetIntl60(aircraftData):
	table = {
		0: 0,
        300: 7.7,
        787: 8.6,
        747: 11.3,
        330: 11.3,
        777: 13.9,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetIntl62(aircraftData):
	table = {
		0: 0,
        330: 1.5,
        380: 3.7,
        777: 3.7,
        787: 3.7,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffsetIntl63(aircraftData):
	table = {
		0: 0,
        330: 2.2,
        787: 4.9,
        777: 4.9,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )



parkings = {
    GATE_D : {
        None : ( ),
        1    : (PresetNames(DomQFA), customOffsetDOM1),
        2    : (PresetNames(DomQFA), customOffsetDom2to6),
        3    : (PresetNames(DomQFA), customOffsetDom2to6),
        5    : (PresetNames(DomQFA), customOffsetDom2to6),
        6    : (PresetNames(DomQFA), customOffsetDom2to6),
        7    : (PresetNames(DomQFA), ),
        8    : (PresetNames(DomQFA), ),
        9    : (PresetNames(DomQFA), ),
        10    : (PresetNames(DomQFA), ),
        11    : (PresetNames(DomQFA), customOffsetDom11),
        12    : (PresetNames(DomQFA), customOffsetDom12),
        14    : (ManualNames(DomQFA, "Bay 13"), customOffsetDom13),
        15    : (PresetNames(DomQFA), ),
        16    : (PresetNames(DomQFA), ),
        17    : (PresetNames(DomQFA), ),
        18    : (PresetNames(DomQFA), ),
        19    : (PresetNames(DomQFA), ),
        31    : (PresetNames(DomCUT), ),
        32    : (PresetNames(DomCUT), customOffsetDom32),
        33    : (PresetNames(DomCUT), customOffsetDom33),
        34    : (PresetNames(DomCUT), customOffsetDom34),
        35    : (PresetNames(DomCUT), customOffsetDom33),
        36    : (PresetNames(DomCUT), customOffsetDom34),
        38    : (PresetNames(DomCUT), customOffsetDom34),
        39    : (PresetNames(DomCUT), customOffsetDom39),
        40    : (PresetNames(DomCUT), customOffsetDom40),
        41    : (PresetNames(DomCUT), ),
        42    : (PresetNames(DomCUT), customOffsetDom42),
        43    : (PresetNames(DomCUT), customOffsetDom43),
        44   : (ManualNames(DomCUT, "Bay 44A"), ),
        45   : (ManualNames(DomCUT, "Bay 45A"), ),
        49    : (PresetNames(DomCUT), customOffsetDom49),
        52    : (PresetNames(DomCUT), customOffsetDom52to57),
        53    : (PresetNames(DomCUT), customOffsetDom5355),
        54    : (PresetNames(DomCUT), customOffsetDom52to57),
        55    : (PresetNames(DomCUT), customOffsetDom5355),
        56    : (PresetNames(DomCUT), customOffsetDom52to57),
        57    : (PresetNames(DomCUT), customOffsetDom52to57),
        58    : (PresetNames(DomCUT), customOffsetDom58),
        59    : (PresetNames(DomCUT), customOffsetDom59),
        64    : (PresetNames(DomQLK), customOffsetQLK),
        65    : (PresetNames(DomQLK), customOffsetQLK),
        66    : (PresetNames(DomQLK), customOffsetQLK),
        67    : (PresetNames(DomQLK), customOffsetQLK),
        68    : (PresetNames(DomQLK), customOffsetQLK),
        69    : (PresetNames(DomQLK), customOffsetQLK),
        70    : (PresetNames(DomQLK), customOffsetQLK),
        71    : (PresetNames(QFHangar), ),
    },
    
    GATE_E : {
        None : ( ),
        4    : (PresetNames(DomQFA), customOffsetDom2to6),
    },
    GATE : {
        None  : ( ),
        6     : (PresetNames(IntlCargo), ),
        8     : (PresetNames(Intl), customOffsetIntl8),
        9     : (PresetNames(Intl), customOffsetIntl9),
        10    : (PresetNames(Intl), customOffsetIntl9),
        11    : (PresetNames(Intl), customOffsetIntl11),
        12    : (PresetNames(Intl), customOffsetIntl12),
        24    : (PresetNames(Intl), customOffsetIntl24),
        25    : (PresetNames(Intl), customOffsetIntl25),
        30    : (PresetNames(Intl), customOffsetIntl30),
        31    : (PresetNames(Intl), customOffsetIntl31),
        32    : (PresetNames(Intl), customOffsetIntl30),
        33    : (PresetNames(Intl), customOffsetIntl33),
        34    : (PresetNames(Intl), customOffsetIntl34),
        35    : (PresetNames(Intl), customOffsetIntl33),
        36    : (PresetNames(Intl), customOffsetIntl36),
        37    : (PresetNames(Intl), customOffsetIntl36),
        50    : (PresetNames(Intl), customOffsetIntl50),
        51    : (PresetNames(Intl), customOffsetIntl51),
        53    : (PresetNames(Intl), customOffsetIntl51),
        54    : (PresetNames(Intl), customOffsetIntl54),
        55    : (PresetNames(Intl), ),
        56    : (PresetNames(Intl), customOffsetIntl54),
        57    : (PresetNames(Intl), customOffsetIntl57),
        58    : (PresetNames(Intl), customOffsetIntl58),
        59    : (PresetNames(Intl), customOffsetIntl58),
        60    : (PresetNames(Intl), customOffsetIntl60),
        61    : (PresetNames(Intl), customOffsetIntl62),
        63    : (PresetNames(Intl), customOffsetIntl63),
        71    : (PresetNames(PASth), ),
        72    : (PresetNames(PASth), ),
        73    : (PresetNames(PASth), ),
        74    : (PresetNames(PASth), ),
        75    : (PresetNames(PASth), ),
        77    : (PresetNames(PASth), ),
        83    : (ManualNames(PANorth, "Bay 85"), ), # Correct FT Error
        84    : (PresetNames(PANorth), ),
        85    : (ManualNames(PANorth, "Bay 83"), ), # Correct FT Error
        97    : (ManualNames(PAEast, "Bay 97A"), ), # Correct FT Error
        98    : (ManualNames(PAEast, "Bay 98A"), ), # Correct FT Error
        99    : (ManualNames(PAEast, "Bay 99A"), ), # Correct FT Error
        121   : (PresetNames(QFHangar), ),
        124   : (PresetNames(QFHangar), ),
        125   : (PresetNames(QFHangar), ),
        126   : (PresetNames(QFHangar), ),
        127   : (PresetNames(QFHangar), ),
    },   
    
    GATE_F : {
        None : ( ),
        1   : (ManualNames(DomCUTBussing, "Bay F1"), ),
        2   : (ManualNames(DomCUTBussing, "Bay F2"), ),
        3   : (ManualNames(DomCUTBussing, "Bay F3"), ),
        4   : (ManualNames(DomCUTBussing, "Bay F4"), ),
        5   : (ManualNames(DomCUTBussing, "Bay F5"), ),
        6   : (ManualNames(DomCUTBussing, "Bay F6"), ),
        7   : (ManualNames(DomCUTBussing, "Bay F7"), ),
        8   : (ManualNames(DomCUTBussing, "Bay F8"), ),
        9   : (ManualNames(DomCUTBussing, "Bay F9"), ),
        10   : (ManualNames(DomCUTBussing, "Bay F10"), ),
        11   : (ManualNames(DomCUTBussing, "Bay F11"), ),
        12   : (ManualNames(DomCUTBussing, "Bay F12"), ),
        13   : (ManualNames(DomCUTBussing, "Bay F13"), ),
        14   : (ManualNames(DomCUTBussing, "Bay F14"), ),
        15   : (ManualNames(DomCUTBussing, "Bay F15"), ),
        16   : (ManualNames(DomCUTBussing, "Bay F16"), ),
    },  
    PARKING : {
        None : ( ),
        1    : (PresetNames(IntlCargo), customOffsetIntlCargo1),
        2    : (PresetNames(IntlCargo), customOffsetIntlCargo2),
        3    : (PresetNames(IntlCargo), customOffsetIntlCargo3to5),
        4    : (PresetNames(IntlCargo), customOffsetIntlCargo3to5),
        5    : (PresetNames(IntlCargo), customOffsetIntlCargo3to5),
        90   : (ManualNames(PAEast, "Bay 90A"), ), # Correct FT Error
        91   : (ManualNames(PAEast, "Bay 91A"), ), # Correct FT Error
        92   : (ManualNames(PAEast, "Bay 92A"), ), # Correct FT Error
        93   : (ManualNames(PAEast, "Bay 93A"), ), # Correct FT Error
        94   : (ManualNames(PAEast, "Bay 94A"), ), # Correct FT Error
        100   : (PresetNames(GA), ),
        101   : (PresetNames(GA), ),
        102   : (PresetNames(GA), ),
        103   : (PresetNames(GA), ),
        104   : (ManualNames(GA, "REX Hangar"), ), # Correct FT Error
        105   : (PresetNames(GA), ),
        106   : (PresetNames(GA), ),
        107   : (PresetNames(GA), ),
        108   : (ManualNames(GA, "NSW Ambulance Service Hangar"), ), # Correct FT Error
        109   : (PresetNames(GA), ),
        110   : (ManualNames(GA, "Jet Aviation 1"), ), # Correct FT Error
        111   : (ManualNames(GA, "Jet Aviation 2"), ), # Correct FT Error
        112   : (ManualNames(GA, "ExecuJet"), ), # Correct FT Error
        113   : (PresetNames(GA), ),
        114   : (PresetNames(GA), ),
        115   : (PresetNames(GA), ),
        116   : (PresetNames(GA), ),
        117   : (PresetNames(GA), ),
        118   : (PresetNames(GA), ),
        119   : (PresetNames(GA), ),
        120   : (PresetNames(GA), ),
        121   : (PresetNames(GA), ),
        122   : (PresetNames(GA), ),
        123   : (PresetNames(GA), ),
        124   : (PresetNames(GA), ),
    },  
    
    S_PARKING : {
        None : ( ),
        120   : (ManualNames(PASthE, "Bay 120B"), ), # Correct FT Error
        121   : (ManualNames(PASthE, "Bay 121B"), ), # Correct FT Error
    },  
}
