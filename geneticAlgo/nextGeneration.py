from genetic_algo_ratePopu import rankDishes
from selection import selection
from crossover import crossover
from mutate import mutatePopulation

def nextGeneration ( currentPopulation, cuisineScore, noOfElite, mutationRate ):
    populationRanked = rankDishes(currentPopulation, cuisineScore)
    selectedPopulationPool = selection( populationRanked, noOfElite)
    populationAfterCrossover = crossover( selectedPopulationPool, currentPopulation, noOfElite)
    nextGen = mutatePopulation( populationAfterCrossover, mutationRate )
    return nextGen

