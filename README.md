# Traveling Salesman Problem

The traveling salesman problem (also called the traveling salesperson problem or TSP) asks the following question: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?"

In this project, I have solved different TSPs with different approaches. I have three different problem sets with 51 cities, 101 cities, and 130 cities.

I have used following approaches to solve the TSPs:

* Nearest Neighbor
* 2-OPT
* Nearest Neighbor + 2-OPT (Hybrid)
* Particle Swarm Optimization
* COTS Solution (Google OR Tools)

You can find the results, and their comparisons according to their accuracy and complexity in the Jupyter Notebook (*Traveling Salesman Problem.ipynb*) file.

## How to run it?

* Clone repository into a directory.
* Open the *Traveling Salesman Problem.ipynb* with Jupyter Notebook(Python 3).

or
* Clone repository into a directory.
* Run the main.py -with Python 3- for *Nearest Neighbor*, *2-OPT*, and *Hybrid* solution.
* Run the particle_swarm_optimization.py -with Python 3- for *Particle Swarm Optimization.*
* Run the google_or.py -with Python 3- for all COTS solutions by changing the appropriate parameters. Do not forget to install ortools.
