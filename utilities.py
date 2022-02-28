import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from City import *


def visualize_route(title, route):
    """Visualizes the route for the TSP."""
    fig = plt.figure()
    fig.suptitle(title)
    x = []
    y = []
    for city in route:
        x.append(city.get_x())
        y.append(city.get_y())
    x.append(route[0].get_x())
    y.append(route[0].get_y())
    graph, = plt.plot(x, y, 'ko')
    graph, = plt.plot(x, y, 'darkorange')

    def animate(i):
        graph.set_data(x[:i + 1], y[:i + 1])
        return graph

    ani = FuncAnimation(fig, animate, frames=len(route) + 10, interval=500)
    plt.show()
    plt.show(block=True)


def txt_reader(file_name):
    """Reads the given input files and store the cities."""
    city_list = []
    txt_file = open(file_name, "r")
    txt_file.readline()  # skip the header line
    for line in txt_file:
        temp_list = line.rstrip().split(" ")
        temp_city = City(temp_list[0], int(float(temp_list[1])), int(float(temp_list[2])))
        city_list.append(temp_city)
    return city_list


def calc_path_distance(city_list):
    """Calculates the distance of the TSP route."""
    path_distance = 0
    for i in range(len(city_list) - 1):
        path_distance += city_list[i].distance(city_list[i + 1])
    path_distance += city_list[-1].distance(city_list[0])  # adds the arc between starting city & ending city.
    return path_distance
