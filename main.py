from utilities import txt_reader, visualize_route
from nearest_neighbor import nna_iteration
from two_opt import two_opt
import time


if __name__ == "__main__":
    city_list = txt_reader("data/51_Cities.txt")

    t0 = time.time()
    nna_result = nna_iteration(city_list)
    t1 = time.time()

    t2 = time.time()
    two_opt_result = two_opt(city_list)
    t3 = time.time()

    t4 = time.time()
    nna_result2 = nna_iteration(city_list)
    hybrid_result = two_opt(nna_result2[0])
    hybrid_result[0].pop()
    t5 = time.time()

    print("Nearest Neighbor Path: " + str(nna_result[0]) + "\nNearest Neighbor Solution: " + str(nna_result[1]) + "\nNearest Neighbor Elapsed Time: " + str(round((t1 - t0), 3)) + " seconds")
    print("----------------------------------------")
    print("2-OPT Path: " + str(two_opt_result[0]) + "\n2-OPT Solution: " + str(two_opt_result[1]) + "\n2-OPT Elapsed Time: " + str(round((t3 - t2), 3)) + " seconds")
    print("----------------------------------------")
    print("Nearest Neighbor + 2-OPT (Hybrid) Path: " + str(hybrid_result[0]) + "\nHybrid Solution: " + str(hybrid_result[1]) + "\nHybrid Elapsed Time: " + str(round((t5 - t4), 3)) + " seconds")

    visualize_route("Nearest Neighbor --- Solution: " + str(nna_result[1]), nna_result[0])
    visualize_route("2-OPT --- Solution: " + str(two_opt_result[1]), two_opt_result[0])
    visualize_route("Nearest Neighbor + 2-OPT (Hybrid) --- Solution: " + str(hybrid_result[1]), hybrid_result[0])
