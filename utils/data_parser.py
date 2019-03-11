from utils.point import Point

class ParseException(Exception):
    def __init__(self, line_no: int, reason: str):
        super().__init__(reason)
        self.reason = reason
        self.line_no = line_no

    def __str__(self):
        return f'Could not parse line {self.line_no}: {self.reason}'

def parse_cities(reader) -> dict:
    cities = {}
    for line_no, line in enumerate(reader):
        try:
            city, x, y = line.split()
            x = float(x)
            y = float(y)
            cities[city] = Point(x, y)
        except Exception as e:
            raise ParseException(line_no, str(e))

    return cities