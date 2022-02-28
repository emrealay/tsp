from sys import maxsize
from City import City
from utilities import calc_path_distance, visualize_route, txt_reader
import random
import time


t0 = time.time()

# Constants
c1 = 1.494  # self confidence
c2 = 1.494  # swarm confidence
w = 0.729  # inertia weight

# Iteration number and swarm size
maxIter = 1000
swarmSize = 500

# lists for particles, their positions, and their velocities.
p = []  # particles
x = []  # positions of the particles
v = []  # velocities of the particles

best = [maxsize for i in range(swarmSize)]  # best values for each particle, maxsize at inital
g = 0  # index of the global best

org_city_list = txt_reader('data/51_Cities.txt')
num_city = len(org_city_list)

for i in range(swarmSize):
    route1 = []
    route2 = []
    route3 = []
    for c in range(num_city):
        org_city = org_city_list[c]
        city1 = City(org_city.get_city_id(), org_city.get_x(), org_city.get_y())
        city2 = City(org_city.get_city_id(), org_city.get_x(), org_city.get_y())
        city3 = City(org_city.get_city_id(), org_city.get_x(), org_city.get_y())
        rand = random.random() * 50

        # added a random value to create variation between initial routes of particles
        city1.z = rand + i
        city2.z = rand + i
        city3.z = 0  # velocity is zero at the beginning.

        route1.append(city1)
        route2.append(city2)
        route3.append(city3)

    p.append(route1)
    x.append(route2)
    v.append(route3)

for n in range(maxIter):

    # algorithm can be improved by using a dynamic inertia weight
    # if n < maxIter/2:
    #     w = (0.85 - 0.55) * (maxIter/2 - n) / (maxIter/2) + 0.55
    # else:
    #     w = (0.85 - 0.55) * (maxIter - n) / (maxIter/2) + 0.55
    # w = min(max(w + 0.0004,0.69),0.8)

    for i in range(swarmSize):

        res = calc_path_distance(sorted(x[i]))
        if res < min(best):  # finds the global best
            for c in range(num_city):
                p[g][c].z = x[i][c].z
            g = i

            print('New cost: ', str(res))
        if res < best[i]:  # finds the personal best
            best[i] = res
            for c in range(num_city):
                p[i][c].z = x[i][c].z
        for c in range(num_city):  # finds the next velocity and position of the particles
            rand1 = random.random()
            rand2 = random.random()
            v[i][c].z = w * v[i][c].z + c1 * rand1 * (p[i][c].z - x[i][c].z) + c2 * rand2 * (p[g][c].z - x[i][c].z)  #next velocities
            x[i][c].z = x[i][c].z + v[i][c].z  # next positions

p[g].sort()  # sort the particles by their z value.
p[g].append(p[g][0])  # add starting city to route, to create a cycle.

t1 = time.time()

print("Particle Swarm Optimization Path: " + str(p[g]) + "\nParticle Swarm Optimization Solution: " + str(calc_path_distance(p[g])) + "\nParticle Swarm Optimization Elapsed Time: " + str(round((t1 - t0), 3)) + " seconds")
visualize_route("Particle Swarm Optimization --- Solution: " + str(calc_path_distance(p[g])), p[g])
