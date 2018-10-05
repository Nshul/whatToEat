from genetic_algo_chromosome import createChromosome


def createInitialPopu(maxDishes, initialPopuSize):
    """
    Creates initial set of population

    maxDishes -> total number of dishes that are to be ordered

    initialPopuSize -> Size of initial population pool
    """
    population = []
    for i in range(1, initialPopuSize+1):
        population.append(createChromosome(maxDishes))
    return population
