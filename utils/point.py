from utils.type_checker import type_checked

class Point:

    @type_checked(bound=True)
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @type_checked(bound=True)
    def distance_to(self, other) -> float:
        if not isinstance(other, Point):
            raise Exception(f'{other} is not a Point')
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __str__(self):
        return f'<Point x={self.x} y={self.y}>'

    __repr__ = __str__