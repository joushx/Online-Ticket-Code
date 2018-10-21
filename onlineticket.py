#!/usr/bin/python3
# -*- coding: utf-8 -*-

import zlib
import sys
import gzip
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives.serialization import load_der_public_key
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_public_key
import base64
import hashlib
import xmltodict
import os

from ticket import Ticket

def render_tlay(tlay):
	result = [" "*77]*18

	def set_text(line, column, text):
		length = len(text)
		before = result[line][:column]
		after = result[line][column + length:]
		result[line] = before + text + after

	set_text(4, 1, "DATUM")
	set_text(5, 1, "DATE")

	set_text(4, 7, "ZEIT")
	set_text(5, 7, "TIME")

	set_text(4, 14, "VON/DE/FROM")
	set_text(4, 31, "->")
	set_text(4, 35, "NACH/A/TO")
	set_text(4, 52, "DATUM")
	set_text(5, 52, "DATE")
	set_text(4, 58, "ZEIT")
	set_text(5, 58, "TIME")
	set_text(4, 66, " KL.")
	set_text(5, 66, " CL.")

	for b in tlay.blocks:
		line = int(b.line)
		column = int(b.column)
		length = int(b.length)

		for part in b.text.split("\n"):
			set_text(line, column, part)
			line += 1

	return "\n".join(result)



t = Ticket.from_file(sys.argv[1])

print("Header: {}".format(t.header))
print("Version: {}".format(t.version))
print("Issuer: {}".format(t.issuer))
print("Key Nr: {}".format(t.key_id))
print("Signature: {}".format(t.signature.hex()))
print("Payload size: {}".format(t.payload_size))
print("---")
for section in t.payload.section:
	print(section.name)
	print("---")

	if hasattr(section.data, 'head'):
		print("RICS: {}".format(section.data.head.rics))
		print("Order: {}".format(section.data.head.ticket_id))
		print("Date: {}-{}-{} {}:{}".format(section.data.head.edition_time.year,section.data.head.edition_time.month,section.data.head.edition_time.day, section.data.head.edition_time.hour, section.data.head.edition_time.minute))
		print("Flag: {}".format(section.data.head.flag))
		print("Language: {}".format(section.data.head.lang))
		print("Second language: {}".format(section.data.head.lang2))
	elif hasattr(section.data, 'tlay'):
		print(render_tlay(section.data.tlay))
	else:
		print(section.__dict__)
	print("---")
