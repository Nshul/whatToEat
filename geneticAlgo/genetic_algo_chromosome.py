"""
This program create a chromosome
"""
import json
import random

from genetic_algo_allele import Dish

with open('../dishMap.json') as menu_Data:
    menuData = json.load(menu_Data)

with open('../genInfo.json') as gen_Info:
    genInfo = json.load(gen_Info)

# NOT USING THIS FUNCTION CURRENTLY
# This function limits to starting dishes more so I am not using it currently
def randSeq(n, a, b, sum):
    """
    Generate the random sequence of quantities for the dishes
    """
    found = False
    while not found:
        totalNum = 0
        numSum = 0
        sequence = []
        while totalNum < n and numSum < sum:
            r = random.randint(a,b)
            numSum += r
            totalNum += 1
            sequence.append(r)
        if numSum == sum:
            while totalNum < n:
                sequence.append(0)
                totalNum+=1
            found = True 
    return sequence

# This function gives a more distributed result so using this currently
def randSeq2(n, sum):
    """
    Generate the random sequence of quantities for the dishes
    """
    sequence = [0]*n
    i=0
    while i < sum:
        r = random.randint(1,n)
        sequence[r-1]+=1
        i+=1
    return sequence


def createChromosome( totQty ):
    """
    Creates the chromosome with Qty assigned to Each Dish such that
    sum of all Qty equals to the number of dishes to be ordered

    totQty = Number of Dishes to be Ordered
    """
    chromosome = []
    qtySeq = randSeq2(genInfo["totalDishes"],totQty)
    i=0
    for key in menuData:
        chromosome.append(Dish(key,qtySeq[i]))
        i+=1
    return chromosome