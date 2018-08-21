from genetic_algo_fitness import Fitness

def rankDishes(population):
    """
    Ranks the population using the Fitness class
    and the method to calculate fitness
    """
    fitnessResults = {}
    for i in population:
        fitnessResults[i] = Fitness(population[i]).calcFitness()
    return sorted(fitnessResults.items(), key=lambda x: x[1], reverse=True)

# Testing sorted()
# import json

# with open('../dishMap.json') as dish_map:
#     dishMap = json.load(dish_map)

# tempData = {}

# for i in dishMap:
#     tempData[dishMap[i]["dishName"]] = int(i)

# print (sorted(tempData.items(),key = lambda x:x[1], reverse= True))