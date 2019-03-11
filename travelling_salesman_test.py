from utils.data_parser import parse_cities
from checker.check_travel import is_valid_travel, is_best_travel, calculate_distance
import random as r


# Test
if __name__ == '__main__':
    with open('./data/texas.txt') as f:
        cities = parse_cities(f)
        travel = list(cities.keys())
        r.shuffle(travel)
        print({'cities': cities, 'travel': travel})
        print(is_valid_travel(cities, travel))
        distance = calculate_distance(cities, travel)
        print()
        for city in travel:
            print(city)