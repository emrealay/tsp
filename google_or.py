"Simple Travelling Salesperson Problem (TSP) between cities."""

from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
from main import *


def compute_distance_matrix(cities):
    """Creates the distance matrix for the problem."""
    final_data = []
    for city1 in cities:
        initial_data = []
        for city2 in cities:
            initial_data.append(city1.distance(city2))

        final_data.append(initial_data)
    return final_data


def create_data_model():
    """Stores the data for the problem."""
    data = {}
    cities = txt_reader("data/51_Cities.txt")
    distance_matrix = compute_distance_matrix(cities)
    data['distance_matrix'] = distance_matrix  # yapf: disable
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data, cities


def print_solution(manager, routing, solution):
    """Prints solution on console."""
    print('Objective: {} miles'.format(solution.ObjectiveValue()))
    index = routing.Start(0)
    plan_output = 'Route for vehicle 0:\n'
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += ' {} ->'.format(manager.IndexToNode(index ))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += ' {}\n'.format(manager.IndexToNode(index))
    plan_output += 'Route distance: {}miles\n'.format(route_distance)


def get_routes(solution, routing, manager):
  """Get vehicle routes from a solution and store them in an array."""
  # Get vehicle routes and store them in a two dimensional array whose
  # i,j entry is the jth location visited by vehicle i along its route.
  routes = []
  for route_nbr in range(routing.vehicles()):
    index = routing.Start(route_nbr)
    route = [manager.IndexToNode(index)]
    while not routing.IsEnd(index):
      index = solution.Value(routing.NextVar(index))
      route.append(manager.IndexToNode(index))
    routes.append(route)
  return routes


def main():
    """Entry point of the program."""
    # Instantiate the data problem.
    data = create_data_model()[0]

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)


    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.SAVINGS)

    # Changing the search strategy
    # search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    # search_parameters.local_search_metaheuristic = (
    #     routing_enums_pb2.LocalSearchMetaheuristic.GENERIC_TABU_SEARCH)
    # search_parameters.time_limit.seconds = 30
    # search_parameters.log_search = True

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    routes = get_routes(solution, routing, manager)[0]
    city_list = create_data_model()[1]
    route = []
    for c1 in routes:
        for c2 in city_list:
            if c2.get_city_id() == str(c1 + 1):
                route.append(c2)
    print("Google OR (SAVINGS) Path: " + str(route), "\nGoogle OR (SAVINGS) Solution: " + str(solution.ObjectiveValue()))
    visualize_route("Google OR (SAVINGS) --- Solution: " + str(solution.ObjectiveValue()), route)


if __name__ == '__main__':
    main()
