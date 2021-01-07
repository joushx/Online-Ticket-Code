from onlineticket.sections.head import HeadSectionParser
from onlineticket.sections.db_bl import DBBLSectionParser

class SectionParser:
    def parse(self, section):
        parser = self._find_parser(section.name)
        if not parser:
            return None
        
        parsed = self._parse_header(section)
        parsed['content'] = parser.parse(section)
        return parsed

    def _parse_header(self, section):
        return {
            'record_id': section.name,
            'version': section.version,
            'length': section.length
        }

    def _find_parser(self, name):
        if name == 'U_HEAD':
            return HeadSectionParser()
        elif name == '0080BL':
            return DBBLSectionParser()