meta:
  id: bl
  file-extension: bl
  encoding: ascii
seq:
  - id: unknown
    size: 3
  - id: valid_from
    type: str
    size: 8
  - id: valid_to
    type: str
    size: 8
  - id: serial
    type: str
    size: 9
  - id: padding
    size: 1
  - id: pair_count
    type: str
    size: 2
  - id: name_value_pairs
    type: name_value_pair
    repeat: expr
    repeat-expr: pair_count.to_i
types:
  name_value_pair:
    seq:
      - id: start
        contents: 'S'
      - id: id
        type: str
        size: 3
      - id: length
        type: str
        size: 4
      - id: content
        type: str
        size: length.to_i
  