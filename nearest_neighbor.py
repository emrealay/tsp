from sys import maxsize
from utilities import calc_path_distance


def nearest_neighbor(city, city_list):
    """Finds the nearest neighbor of a given city."""
    min_distance = maxsize
    nearest_city = None
    for c in city_list:
        temp_distance = city.distance(c)
        if temp_distance < min_distance:
            min_distance = temp_distance
            nearest_city = c
    return nearest_city, min_distance


def nearest_neighbor_algorithm(next_city, city_list):
    """Creates a route by starting with the given city."""
    copy_city_list = city_list[:]
    path = [next_city]
    copy_city_list.remove(next_city)
    while copy_city_list:
        next_step = nearest_neighbor(next_city, copy_city_list)
        next_city = next_step[0]
        path.append(next_city)
        copy_city_list.remove(next_city)
    path_distance = calc_path_distance(path)
    path.append(path[0])  # add starting city to route, to create a cycle.
    return path, path_distance


def nna_iteration(city_list):
    """Finds the best route by changing the starting city & following the nearest neighbors."""
    best_path = []
    best_distance = maxsize
    for city in city_list:
        result = nearest_neighbor_algorithm(city, city_list)
        if best_distance > result[1]:
            best_path = result[0]
            best_distance = result[1]
    return best_path, best_distance
