Parses online tickets for trains following UIC 918-3 and checks the signature

## Dependencies

```
sudo apt install kaitai-struct-compiler
```

## Usage

1. Run `bootstrap.sh` to setup the environment (python requiements, generate models, downlad keys)
2. Scan the aztec code of the online ticket e.g. using your phone and write the binary data into a file
3. Run `python3 onlineticket.py <file>`

## Example

The `example` directory contains a file that was extracted from a ticket that was once visible in a movie scene and probably contains fake data. This is the output of this script:

```
Header: #UT
Version: 01
Issuer: 0080
Key Nr: 00006
Signature: 302c02144825665130eae29c9ee2045f10c4e54701ce2a8002143b27279307cc42e43ebfd8ba689e2a92147203da00
Payload size: 0234
---
U_HEAD
---
RICS: 0080
Order: PA2B1H-5
Date: 2018-11-12 21:04
Flag: <ticket.Ticket.Payload.Head.Flags object at 0x7f53800bddd8>
Language: DE
Second language: DE
---
0080BL
---
{'_io': <kaitaistruct.KaitaiStream object at 0x7f53800b5320>, '_parent': <ticket.Ticket.Payload object at 0x7f53800b56d8>, '_root': <ticket.Ticket object at 0x7f5381dcb3c8>, 'name': '0080BL', 'version': '03', 'length': '0303', '_raw_data': b'0311911201819112018362243814\x0016S0010015Super SparpreisS00200011S0030001BS00900051-0-0S01200010S0140002S2S0150007HamburgS0160015Frankfurt(Main)S0210019HH-Hbf  8:28 IC2279S0230018Holzer-Nims SophieS026000213S0280018Sophie#Holzer-NimsS031001019.11.2018S032001019.11.2018S03500042549S03600042042', 'data': <ticket.Ticket.Payload.SectionData object at 0x7f53800bdf98>}
---
```

Note that some data specific for german railways are not parsed yet
