# Has concurrency issues. I don't give a damn.
import os
from utils.type_checker import type_checked

class Distance:
    @type_checked(bound=True)
    def __init__(self, author: str, distance: float):
        self.author = author
        self.distance = distance

class BestDistance:

    file = 'data/best_distance.txt'

    @classmethod
    def get(cls) -> Distance:
        if not os.path.exists(cls.file):
            return Distance('Nobody', float('+inf'))

        with open(cls.file) as f:
            author, distance = f.readline().split()
            return Distance(author, float(distance))

    @classmethod
    def get_all(cls) -> list:
        if not os.path.exists(cls.file):
            return []

        with open(cls.file) as f:
            author_list = []
            for line in f:
                author, distance = line.split()
                author_list.append(Distance(author, float(distance)))

        return author_list

    @classmethod
    def set(cls, value: float, author: str):
        with open(cls.file, 'w') as f:
            f.write(f'{author} {value}')

    @classmethod
    def append(cls, value:float, author: str):
        with open(cls.file, 'a') as f:
            f.write(f'\n{author} {value}')