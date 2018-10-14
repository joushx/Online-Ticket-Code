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

result = [" "*300]*15
def set_text(line, column, text):
	length = len(text)
	before = result[line][:column]
	after = result[line][column + length:]
	result[line] = before + text + after

t = Ticket.from_file(sys.argv[1])

print("Header: {}".format(t.header))
print("Version: {}".format(t.version))
print("Issuer: {}".format(t.issuer))
print("Key Nr: {}".format(t.key_id))
print("Signature: {}".format(t.signature))
print("Payload size: {}".format(t.payload_size))
print("---")
print("Name: {}".format(t.payload.header.name))
print("Version: {}".format(t.payload.header.version))
print("Length: {}".format(t.payload.header.length))
print("Issuer: {}".format(t.payload.header.issuer))
print("Order: {}".format(t.payload.header.order))
print("Date: {}-{}-{} {}:{}".format(t.payload.header.date.year,t.payload.header.date.month,t.payload.header.date.day, t.payload.header.date.hour, t.payload.header.date.minute))
print("Flag: {}".format(t.payload.header.flag))
print("Language: {}".format(t.payload.header.lang))
print("Second language: {}".format(t.payload.header.lang2))
print("---")
s = t.payload.text
print("Name: {}".format(s.name))
print("Version: {}".format(s.version))
print("Length: {}".format(s.length))
print("Type: {}".format(s.type))
print("Blocks: {}".format(s.n_blocks))

print("---")

for b in s.blocks:
	line = int(b.line)
	column = int(b.column)
	length = int(b.length)

	for part in b.text.split("\n"):
		set_text(line, column, part)
		line += 1

print("\n".join(result))

print("---")

keys = xmltodict.parse(open("uic-keys/keys.xml").read())
key = list(filter(lambda k: k["issuerCode"] == t.issuer, keys["keys"]["key"]))

if len(key) == 0:
	print("Cannot find public key")
	os.exit()

key = key[0]
print("Found key of {}".format(key["issuerName"]))

der = base64.b64decode(key["publicKey"])
print(der.hex())
key = load_der_public_key(der, backend=default_backend())

print(key)

hash = hashlib.sha1(b"!")
result = key.verify(hash, t.signature)
print(result)
