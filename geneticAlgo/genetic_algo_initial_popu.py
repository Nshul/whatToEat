from genetic_algo_chromosome import createChromosome


def createInitialPopu(maxDishes, initialPopuSize):
    """
    Creates initial set of population
    """
    population = []
    for i in range(1, initialPopuSize+1):
        population.append(createChromosome(maxDishes))
    return population
