"""
This program create a chromosome
"""
import json
import random

from genetic_algo_allele import Dish

with open('../dishMap.json') as menu_Data:
    menuData = json.load(menu_Data)

def createChromosome():
    chromosome = []

print "hi"