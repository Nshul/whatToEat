from genetic_algo_fitness import Fitness
# from genetic_algo_initial_popu import createInitialPopu

def rankDishes(population, cuisineScore):
    """
    Ranks the population using the Fitness class
    and the method to calculate fitness

    population -> initial population of chromosomes
    cuisineScore -> object consisting of score that is rated
                    by users with key as cuisine name

    returns array consisting of (chromosome index,fitness) pairs
    in sorted order (chromosome with max fitness at 0th index)
    """
    fitnessResults = {}
    for i in range(0,len(population)):
        fitnessResults[i] = Fitness(population[i], cuisineScore).calcFitness()
    return sorted(fitnessResults.items(), key=lambda x: x[1], reverse=True)

# temp = createInitialPopu(4, 10)
# print ("***")
# print (temp)
# print ("***")
# cuisineScore = {"indian":0.33,"italian":0.45,"afghani":0.08,"chinese":0.14}
# temp1 = rankDishes(temp, cuisineScore)
# print ("/*/*")
# print (temp1)
# print ("/*/*")