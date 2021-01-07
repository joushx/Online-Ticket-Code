Parses online tickets for trains following UIC 918-3

## Dependencies

```
sudo apt install kaitai-struct-compiler
```

## Usage

1. Run `bootstrap.sh` to generate the parsing code from the model
2. Scan the aztec code of the online ticket e.g. using your phone and write the binary data into a file
3. Run `python3 onlineticket.py <file>`
