# -- coding: utf-8 --

version = 1
msfs_mode = 1
icao = "lphr"

def TerminalName(name, letter, priority):
	return CustomizedName( "%s | Gate #§%s" % (name, letter), priority )

def StandName(name, letter, priority):
	return CustomizedName( "%s | Stand #§%s" % (name, letter), priority )
	
MainApronNameGate1 = TerminalName("Main Apron | Enter via A Only", "", 1)
MainApronNameGate2 = TerminalName("Main Apron | Enter via B Only", "", 1)
MainApronNameGate3 = TerminalName("Main Apron | Enter via B Only", "", 1)
GAApronNames = StandName("GA Apron", "", 2)

parkings = {
	PARKING : {
		None : ( ),
		1 : (MainApronNameGate1, ),
		2 : (MainApronNameGate2, ),
		3 : (MainApronNameGate3, ),
	},
	0 : {
		None : ( ),
		"1A" : (GAApronNames, ),
		"2A" : (GAApronNames, ),
	},
}