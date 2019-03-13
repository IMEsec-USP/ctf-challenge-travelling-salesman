import random as r

THRESHOLD = 240.0
DATA_FILE = 'data/texas.txt'

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, other) -> float:
        if not isinstance(other, Point):
            raise Exception(f'{other} is not a Point')
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __str__(self):
        return f'<Point x={self.x} y={self.y}>'

    __repr__ = __str__

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

def calculate_distance(points: list) -> float:
    distance = 0
    for a, b in zip(points[:-1], points[1:]):
        distance += a.distance_to(b)
    return distance


def brute_force(cities: list, threshold: float) -> list:
    distance = float('+inf')
    while distance > threshold:
        r.shuffle(cities)
        points = [x[1] for x in cities]
        distance = calculate_distance(points)
        print('.', end='', flush=True)

    return [x[0] for x in cities]

with open(DATA_FILE) as f:
    cities = parse_cities(f)
    cities_list = []
    for city, location in cities.items():
        cities_list.append((city, location))
    
    result = brute_force(cities_list, THRESHOLD)
    print('found an answer:\n')
    for i in result:
        print(i)
