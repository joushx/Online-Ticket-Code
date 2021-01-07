from kaitaistruct import KaitaiStream, BytesIO
from onlineticket.generated.head import Head

class HeadSectionParser:
    def parse(self, section):
        parsed = Head(KaitaiStream(BytesIO(section.data)))

        return {
            'company': parsed.rics,
            'ticket_id': parsed.ticket_id,
            'edition_time': {
                'year': parsed.edition_time.year,
                'month': parsed.edition_time.month,
                'day': parsed.edition_time.day,
                'hour': parsed.edition_time.hour, 
                'minute': parsed.edition_time.minute
            },
            'flags': {
                'international': parsed.flag.international,
                'test': parsed.flag.test
            },
            'languages': [
                parsed.lang,
                parsed.lang2
            ]
        }