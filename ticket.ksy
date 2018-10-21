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
          type: section_data
      section_data:
        seq:
        - id: head
          type: head
          if: _parent.name == "U_HEAD"
        - id: tlay
          type: tlay
          if: _parent.name == "U_TLAY"
      head:
        seq:
        - id: rics
          size: 4
          type: str
        - id: ticket_id
          size: 20
          type: str
        - id: edition_time
          type: date
        - id: flag
          type: flags
          size: 1
        - id: lang
          type: str
          size: 2
        - id: lang2
          type: str
          size: 2
        types:
          flags:
            seq:
              - id: international
                type: b1
              - id: test
                type: b1
      tlay:
        seq:
          - id: type
            size: 4
            type: str
          - id: n_blocks
            size: 4
            type: str
          - id: blocks
            type: block
            repeat: expr
            repeat-expr: n_blocks.to_i
      block:
        seq:
          - id: line
            size: 2
            type: str
          - id: column
            size: 2
            type: str
          - id: height
            size: 2
            type: str
          - id: width
            size: 3
            type: str
          - id: format
            size: 1
            type: str
          - id: length
            size: 3
            type: str
          - id: text
            size: length.to_i
            type: str
      date:
        seq:
          - id: day
            type: str
            size: 2
          - id: month
            type: str
            size: 2
          - id: year
            size: 4
            type: str
          - id: hour
            size: 2
            type: str
          - id: minute
            size: 2
            type: str
