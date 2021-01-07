from onlineticket.generated.ticket import Ticket
from onlineticket.section import SectionParser

class TicketParser:
    def parse(self, filename):
        parsed = self._parse_kaitai(filename)
        return self._map(parsed)

    def _parse_kaitai(self, filename):
        return Ticket.from_file(filename)

    def _map(self, parsed):
        p = parsed
        return {
            'header': {
                'version': p.version,
                'issuer': p.issuer,
                'signature_key_id': p.key_id,
                'signature': p.signature.hex(),
                'payload_size': p.payload_size
            },
            'payload': self._map_payload(parsed)
        }

    def _map_payload(self, parsed):
        section_parser = SectionParser()
        return list(map(lambda section: section_parser.parse(section), parsed.payload.section))