import random, math

def breed(chromosome1, chromosome2):
    """
    This crossover function performs uniform crossover between
    two chromosomes
    """
    for i in range(0,len(chromosome1)):
        k = random.random()
        # print (k)
        if(k>=0.5):
            temp = chromosome1[i]
            chromosome1[i] = chromosome2[i]
            chromosome2[i] = temp
    # print (chromosome1)
    # print (chromosome2)
    

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
        newChromosome.append(origChromosomes[matingPool[i]])
    upperBoundForCrossover = (int)((sizeOfMatingPool-noOfElite)/2)+1
    for i in range(0,upperBoundForCrossover):
        # print ("%d,%d\n" %(chromo1,chromo2))
        ind1 = matingPool[noOfElite+i]
        ind2 = matingPool[sizeOfMatingPool-1-i]
        tempChromo1 = origChromosomes[ind1]
        tempChromo2 = origChromosomes[ind2]
        breed(tempChromo1,tempChromo2)
        newChromosome.append(tempChromo1)
        newChromosome.append(tempChromo2)
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

