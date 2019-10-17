import random
from copy import deepcopy

def breed(chromosome1, chromosome2):
    """
    This crossover function performs uniform crossover between
    two chromosomes
    """
    for i in range(0,len(chromosome1)):
        k = random.random()
        # print (k)
        if(k>=0.5):
            chromosome1[i], chromosome2[i] = chromosome2[i], chromosome1[i]
    

def crossover( matingPool, origChromosomes, noOfElite):
    """
    This crossover function performs uniform crossover between
    two chromosomes

    matingPool -> list consisting of indices from original Chromosomes
    origChromosomes -> consists of list of original Chromosomes
    noOfElite -> number of times we need to perform breed function

    returns list containing chromosome pool of new generation
    """
    sizeOfMatingPool = len(matingPool)
    sizeOfChromosome = len(origChromosomes[0])
    newChromosome = []
    # Copy the elite chromosomes and persist them to next generation
    for i in range(0, noOfElite):
        newChromosome.append(deepcopy(origChromosomes[matingPool[i]]))
    LowerPtrForCrossover = noOfElite
    UpperPtrForCrossover = sizeOfMatingPool-1
    while (LowerPtrForCrossover<UpperPtrForCrossover):
        ind1 = matingPool[LowerPtrForCrossover]
        ind2 = matingPool[UpperPtrForCrossover]
        tempChromo1 = deepcopy(origChromosomes[ind1])
        tempChromo2 = deepcopy(origChromosomes[ind2])
        breed(tempChromo1,tempChromo2)
        newChromosome.append(tempChromo1)
        newChromosome.append(tempChromo2)
        LowerPtrForCrossover+=1
        UpperPtrForCrossover-=1
    if(LowerPtrForCrossover==UpperPtrForCrossover):
        ind1 = matingPool[LowerPtrForCrossover]
        tempChromo1 = deepcopy(origChromosomes[ind1])
        newChromosome.append(tempChromo1)

    return newChromosome

# Breed function test
# cr1 = [1,2,3,4,5]
# cr2 = [6,7,8,9,10]
# breed(cr1,cr2)
# print(cr1)

# crossover function test
# orig_chr = [[1,2,3,4,5,6,7],[8,9,10,11,12,13,14],[15,16,17,18,19,20,21],[22,23,24,25,26,27,28]]
# matingPool = [1,2,0,3]
# new_popu = crossover(matingPool,orig_chr,0)
# print(new_popu)

