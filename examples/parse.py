#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pprint
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "onlineticket")))
from ticketparser import TicketParser

def print_keys(dict):
    for key in dict:
        print(key + ": " + str(dict[key]))

parsed = TicketParser().parse(sys.argv[1])

print("== HEADER ==")
print_keys(parsed['header'])

print("== PAYLOAD ==")
for section in parsed['payload']:
    print("-- " + section['record_id'] + " --")
    print('Version: ' + section['version'])

    if(section['record_id'] == 'U_HEAD'):
        print_keys(section['content'])
    elif(section['record_id'] == '0080BL'):
        print("Valid from: " + section['content']['valid_from'])
        print("Valid to: " + section['content']['valid_to'])
        print("Serial: " + section['content']['serial'])
        print("Pairs:")
        for pair in section['content']['pairs']:
            print(pair['id'] + ": " + pair['content'])
print("== RAW ==")
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(parsed)