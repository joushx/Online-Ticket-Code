meta:
  id: head
  encoding: iso8859-1
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
