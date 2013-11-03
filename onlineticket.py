#!/usr/bin/python
# -*- coding: utf-8 -*-

import zlib

def parse_freetext(text):

	blocks = []
	
	cursor = 0

	while cursor < len(text):

		coordinates = text[cursor:cursor+13]
		
		line = int(coordinates[0:2])
		cell = int(coordinates[2:4])
		length = int(coordinates[11:13])

		block = {"line":line,"cell":cell,"length":length,"text":text[cursor+13:cursor+13+length]}

		blocks.append(block)

		cursor = cursor+13+length

	return blocks



f = open("onlineticket.bin", "rb")

try:
    byte = f.read()
    print "Ticket-Typ: " + byte[0:3] + " (UIC)"
    print "Version: " + byte[3:5]
    print "Aussteller: " + byte[5:9]
    print "Schlüsselnummer: " + byte[9:14]
    print "Signatur: " + byte[14:64].encode("hex")

    print "Padding " + byte[64:65] + " -------------------"

    print "Länge des zlib-Teils: " + byte[66:68]
    print "zlib-Header: " + byte[68:70].encode("hex")

    zlib = zlib.decompress(byte[68:])

    print "Header: " + zlib[0:6]
    print "Version: " + zlib[6:8]
    print "Länge: " + zlib[8:12]
    print "Aussteller: " + zlib[12:16]
    print "Auftragsnummer: " + zlib[16:33]
    print "Ausstellungsdatum: " + zlib[36:44]
    print "Ausstellungszeit: " + zlib[44:48]
    print "Ticket-Typ: " + zlib[48:49]
    print "Sprache: " + zlib[49:51]

    start = zlib.index("U_TLAY")
    print "Header: " + zlib[start:start+6]
    print "?: " + zlib[start+6:start+12]
    print "Typ: " + zlib[start+12:start+16]
    print "Blöcke: " + zlib[start+16:start+20]

    blocks = parse_freetext(zlib[start+20:])

    current_cell = 0
    current_line = 0

    for block in blocks:

    	if block["line"] != current_line:
    		current_cell = 0
    		print "\n",

    	

    	

    	cell = int((block["cell"] - current_cell))

    	for i in range(0,cell):
    		print " ",

    	print block["text"],

    	current_line = block["line"]
    	current_cell = cell

finally:
    f.close()
