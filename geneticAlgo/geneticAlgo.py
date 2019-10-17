from genetic_algo_initial_popu import createInitialPopu
from genetic_algo_ratePopu import rankDishes
from nextGeneration import nextGeneration

import matplotlib.pyplot as plt

class DotDict(dict):
    def __getattr__(self, key):
        return self[key]
    def __setattr__(self, key, val):
        if key in self.__dict__:
            self.__dict__[key] = val
        else:
            self[key] = val

def geneticAlgorithm( maxDishes, initialPopulationSize, cuisineScore, noOfElite, mutationRate, generations ):
    popu = createInitialPopu( maxDishes, initialPopulationSize)

    graphPoints = []
    answer = DotDict([("ans",-1),("fitness",0)])
    for i in range(0, generations):
        popu = nextGeneration( popu, cuisineScore , maxDishes, noOfElite, mutationRate, graphPoints, answer ) 

    lastGenRanked = rankDishes(popu, cuisineScore, maxDishes)
    graphPoints.append(lastGenRanked[0][1])

    if(answer.fitness<lastGenRanked[0][1]):
        answer.ans = popu[lastGenRanked[0][0]].copy()
        answer.fitness = lastGenRanked[0][1]

    plt.plot(graphPoints)
    plt.ylabel('Best Fitness')
    plt.xlabel('Generation')
    plt.show()
    print( answer.ans )
    print("Fitness: %s" %str(answer.fitness))
    return answer.ans