from genetic_algo_fitness import Fitness

def rankDishes(population):
    """
    Ranks the population using the Fitness class
    and the method to calculate fitness
    """
    fitnessResults = {}
    for i in population:
        fitnessResults[i] = Fitness(population[i]).calcFitness()
    return sorted(fitnessResults, key=lambda x: x[1], reverse=True)
