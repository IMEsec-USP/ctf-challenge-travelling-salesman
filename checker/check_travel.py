from utils.type_checker import type_checked
from utils.point import Point
from model.best_distance import BestDistance

THRESHOLD = 260

def is_valid_travel(cities: dict, travel: list) -> bool:
    if len(set(travel)) != len(travel):
        return False
    return all(city in travel for city in cities)

def calculate_distance(cities: dict, travel: list) -> float:
    distance = 0
    for a, b in zip(travel[:-1], travel[1:]):
        distance += cities[a].distance_to(cities[b])
    return distance

def is_good_travel(distance: float) -> bool:
    return distance <= THRESHOLD
