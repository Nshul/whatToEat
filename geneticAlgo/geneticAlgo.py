from genetic_algo_initial_popu import createInitialPopu
from nextGeneration import nextGeneration

def geneticAlgorithm( maxDishes, initialPopulationSize, cuisineScore, noOfElite, mutationRate, generations ):
    popu = createInitialPopu( maxDishes, initialPopulationSize)
    for i in range(0, generations):
        popu = nextGeneration( popu, cuisineScore , maxDishes, noOfElite, mutationRate )    
    print( popu[0] )
    return popu[0]