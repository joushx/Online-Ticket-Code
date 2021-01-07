meta:
  id: ticket
  file-extension: ticket
  encoding: iso8859-1
seq:
  - id: header
    type: str
    size: 3
  - id: version
    size: 2
    type: str
  - id: issuer
    size: 4
    type: str
  - id: key_id
    size: 5
    type: str
  - id: signature
    size: 47
  - id: payload_size
    size: 7
    type: str
  - id: payload
    process: zlib
    size-eos: true
    type: payload
types:
  payload:
    seq:
    - id: section
      type: section
      repeat: expr
      repeat-expr: 2
    types:
      section:
        seq:
        - id: name
          type: str
          size: 6
        - id: version
          size: 2
          type: str
        - id: length
          size: 4
          type: str
        - id: data
          size: length.to_i - 12