Parses online tickets for trains following UIC 918-3 and checks the signature

## Dependencies

```
sudo apt install kaitai-struct-compiler
```

## Usage

1. Run `bootstrap.sh` to setup the environment (python requiements, generate models, downlad keys)
2. Scan the aztec code of the online ticket e.g. using your phone and write the binary data into a file
3. Run `python examples/parse.py examples/ticket-visible-in-a-movie-scene`

## Example

The `example` directory contains a file that was extracted from a ticket that was once visible in a movie scene and probably contains fake data. This is the output of this script:

```
== HEADER ==
version: 01
issuer: 0080
signature_key_id: 00006
signature: 302c02144825665130eae29c9ee2045f10c4e54701ce2a8002143b27279307cc42e43ebfd8ba689e2a92147203da00
payload_size: 0234
== PAYLOAD ==
-- U_HEAD --
Version: 01
company: 0080
ticket_id: PA2B1H-5
edition_time: {'year': '2018', 'month': '11', 'day': '12', 'hour': '21', 'minute': '04'}
flags: {'international': False, 'test': False}
languages: ['DE', 'DE']
-- 0080BL --
Version: 03
Valid from: 19112018
Valid to: 19112018
Serial: 362243814
Pairs:
001: Super Sparpreis
002: 1
003: B
009: 1-0-0
012: 0
014: S2
015: Hamburg
016: Frankfurt(Main)
021: HH-Hbf  8:28 IC2279
023: Holzer-Nims Sophie
026: 13
028: Sophie#Holzer-Nims
031: 19.11.2018
032: 19.11.2018
035: 2549
036: 2042
== RAW ==
{ 'header': { 'issuer': '0080',
              'payload_size': '\x00\x00\x000234',
              'signature': '302c02144825665130eae29c9ee2045f10c4e54701ce2a8002143b27279307cc42e43ebfd8ba689e2a92147203da00',
              'signature_key_id': '00006',
              'version': '01'},
  'payload': [ { 'content': { 'company': '0080',
                              'edition_time': { 'day': '12',
                                                'hour': '21',
                                                'minute': '04',
                                                'month': '11',
                                                'year': '2018'},
                              'flags': {'international': False, 'test': False},
                              'languages': ['DE', 'DE'],
                              'ticket_id': 'PA2B1H-5\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'},
                 'length': '0053',
                 'record_id': 'U_HEAD',
                 'version': '01'},
               { 'content': { 'pairs': [ { 'content': 'Super Sparpreis',
                                           'id': '001'},
                                         {'content': '1', 'id': '002'},
                                         {'content': 'B', 'id': '003'},
                                         {'content': '1-0-0', 'id': '009'},
                                         {'content': '0', 'id': '012'},
                                         {'content': 'S2', 'id': '014'},
                                         {'content': 'Hamburg', 'id': '015'},
                                         { 'content': 'Frankfurt(Main)',
                                           'id': '016'},
                                         { 'content': 'HH-Hbf  8:28 IC2279',
                                           'id': '021'},
                                         { 'content': 'Holzer-Nims Sophie',
                                           'id': '023'},
                                         {'content': '13', 'id': '026'},
                                         { 'content': 'Sophie#Holzer-Nims',
                                           'id': '028'},
                                         {'content': '19.11.2018', 'id': '031'},
                                         {'content': '19.11.2018', 'id': '032'},
                                         {'content': '2549', 'id': '035'},
                                         {'content': '2042', 'id': '036'}],
                              'serial': '362243814',
                              'valid_from': '19112018',
                              'valid_to': '19112018'},
                 'length': '0303',
                 'record_id': '0080BL',
                 'version': '03'}]
```
