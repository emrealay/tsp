from itertools import combinations
from utilities import calc_path_distance


def two_opt_swap(route, i, j):
    """Finds an alternative route of the given route with 2-OPT."""
    new_list1 = route[0:i]
    new_list2 = route[i:j]
    new_list2.reverse()
    new_list3 = route[j:]
    return new_list1 + new_list2 + new_list3


def two_opt(route):
    """Tries all alternative 2-OPT routes of the given route."""
    copy_route = route[:]
    index_list = []
    best = calc_path_distance(copy_route)
    for i in range(len(copy_route)):
        index_list.append(i)
    comb_index = list(combinations(index_list, 2))  # all alternative 2-OPTs
    i = 0
    while i < len(comb_index):
        temp_list = (two_opt_swap(copy_route, comb_index[i][0], comb_index[i][1]))
        if calc_path_distance(temp_list) < best:
            copy_route = temp_list
            best = calc_path_distance(temp_list)
            i = 0
        i = i + 1
    copy_route.append(copy_route[0])  # add starting city to route, to create a cycle.
    return copy_route, best
