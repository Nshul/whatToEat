from genetic_algo_initial_popu import createInitialPopu
from genetic_algo_ratePopu import rankDishes
from nextGeneration import nextGeneration

import matplotlib.pyplot as plt

def geneticAlgorithm( maxDishes, initialPopulationSize, cuisineScore, noOfElite, mutationRate, generations ):
    popu = createInitialPopu( maxDishes, initialPopulationSize)

    graphPoints = []

    for i in range(0, generations):
        popu = nextGeneration( popu, cuisineScore , maxDishes, noOfElite, mutationRate, graphPoints ) 

    lastGenRanked = rankDishes(popu, cuisineScore, maxDishes)
    graphPoints.append(lastGenRanked[0][1])

    plt.plot(graphPoints)
    plt.ylabel('Best Fitness')
    plt.xlabel('Generation')
    plt.show()
    print( popu[0] )
    return popu[0]