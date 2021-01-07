from kaitaistruct import KaitaiStream, BytesIO
from onlineticket.generated.bl import Bl

class DBBLSectionParser:
    def parse(self, section):
        parsed = Bl(KaitaiStream(BytesIO(section.data)))
        return {
            'valid_from': parsed.valid_from,
            'valid_to': parsed.valid_to,
            'serial': parsed.serial,
            'pairs': self._parse_pairs(parsed.name_value_pairs)
        }

    def _parse_pairs(self, pairs):
        return list(map(lambda pair: {'id': pair.id, 'content': pair.content}, pairs))