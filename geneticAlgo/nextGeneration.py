from genetic_algo_ratePopu import rankDishes
from selection import selection
from crossover import crossover
from mutate import mutatePopulation
from genetic_algo_fitness import Fitness
from copy import deepcopy

def nextGeneration(currentPopulation, cuisineScore, maxQtyToBeOrdered, noOfElite, mutationRate, graphPoints, answer):
    """
    This function applies genetic operators over current generation to produce 
    new generation

    currentPopulation -> current pool of chromosomes of current generation
    cuisineScore -> Object consisting of cuisine score as rated by the users
    noOfElite -> no of Elite chromosomes that are to be persisted in next generation
    mutationRate -> rate at which mutation is to take place

    returns new generation of chromosomes
    """
    populationRanked = rankDishes(currentPopulation, cuisineScore, maxQtyToBeOrdered)
    graphPoints.append(populationRanked[0][1])
    
    if(answer.fitness<populationRanked[0][1]):
        answer.ans = deepcopy(currentPopulation[populationRanked[0][0]])
        answer.fitness = populationRanked[0][1]

    selectedPopulationPool = selection(populationRanked, noOfElite)
    populationAfterCrossover = crossover(
        selectedPopulationPool, currentPopulation, noOfElite)
    nextGen = mutatePopulation(populationAfterCrossover, noOfElite, mutationRate)
    return nextGen
