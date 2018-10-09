import random
from copy import deepcopy
# from genetic_algo_gene import Dish


def mutate(individual, mutationRate):
    """
    This function performs scramble mutation in an individual

    individual -> chromosome 
    mutationRate -> the rate at which mutation is supposed to occur

    returns chromosome after mutation if mutation occurs, else returns
    original chromosome
    """
    chromosomeLength = len(individual)
    k = random.random()
    # print(k)
    if(k <= mutationRate):
        startPtr = random.randint(0, chromosomeLength-1)
        # print (startPtr)
        endPtr = random.randint(0, chromosomeLength-1)
        # print (endPtr)
        if(endPtr < startPtr):
            temp = endPtr
            endPtr = startPtr
            startPtr = temp
        tempArrQty = []
        for i in range(startPtr,endPtr+1):
            tempArrQty.append(individual[i].qty)
        tempArrQty = random.sample(tempArrQty,len(tempArrQty))
        for i in range(startPtr,endPtr+1):
            individual[i].qty = tempArrQty[i-startPtr]
    return individual

def mutatePopulation ( population, noOfElite, mutationRate):
    """
    This function performs mutation on entire population

    population -> pool of chromosomes of current generation
    mutationRate -> rate at which mutation is supposed to occur

    returns new population pool after mutation of original pool
    """
    popuLen = len(population)
    newPopu = []
    for i in range(0,noOfElite):
        newPopu.append(deepcopy(population[i]))
    for i in range(noOfElite,popuLen):
        mutantIndi = mutate(population[i],mutationRate)
        newPopu.append(mutantIndi)
    return newPopu

# mutate function test
# chromo1 = []
# for i in range(1,8):
#     chromo1.append(Dish(i,i))
# newchromo = mutate(chromo1,0.5)
# print(newchromo)

# mutatePopulation function test
# popu = []
# for i in range(0,7):
#     chromo1=[]
#     for i in range(1,8):
#         chromo1.append(Dish(i,i))
#     popu.append(chromo1)
# newPopu = mutatePopulation(popu,0.7)
# print(newPopu)