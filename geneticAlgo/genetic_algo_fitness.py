import json
import math

# Import the dish mapping
with open('../dishMap.json') as menu_Data:
    menuData = json.load(menu_Data)

# Import genInfo of cuisines and number of dishes
with open('../genInfo.json') as gen_info:
    genInfo = json.load(gen_info)


class Object(dict):
    pass


class Fitness:
    """
    Define the characteristics required to calculate the fitness function
    and calculate the fitness of chromosome
    """

    def __init__(self, dishes, cuisineScore):
        """
        dishes = list of dishes i.e. chromosome
        cuisineScore  = the score obtained per cuisine using 
                        preferences of the group members     
        totCuisineScore = sum of all cuisine scores
        ratings = sum of all ratings for which qty > 0
        cost = cost of dishes for which qty > 0
        fitness = value of fitness for this chromosome
        """
        self.dishes = dishes
        self.ratings = 0
        self.cost = 0
        self.fitness = 0
        self.cuisineScore = cuisineScore
        self.totCuisineScore = 0
        self.fitnessSet = False
        for i in cuisineScore:
            self.totCuisineScore += cuisineScore[i]

    def calcFitness(self):
        """
        Calculate Fitness for a Chromosome
        cuisineQty = object holding individual qty per cuisine
        cuisineRating = object holding individual ratings per cuisine
        cuisineCost = object holding individual cost per cuisine
        """
        cuisineQty = Object()
        cuisineRating = Object()
        cuisineCost = Object()
        for i in genInfo["cuisines"]:
            cuisineQty[i] = 0
            cuisineRating[i] = 0
            cuisineCost[i] = 0

        totalQty = 0

        for i in range(0, len(self.dishes)):
            dishId = self.dishes[i].id
            quantity = self.dishes[i].qty
            totalQty += quantity
            if quantity > 0:
                # Copy values of this dish from menuData
                tempCuisine = menuData[dishId]["cuisine"]
                tempRating = menuData[dishId]["rating"]
                tempPrice = menuData[dishId]["price"]

                # Add quantity to respective Cuisine
                cuisineQty[tempCuisine] += quantity

                # Add rating to respective Cuisine as well as total Rating sum
                self.ratings += tempRating
                cuisineRating[tempCuisine] += tempRating

                # Add cost to respective Cuisine as well as total Rating sum
                self.cost += tempPrice*quantity
                cuisineCost[tempCuisine] += tempPrice*quantity

        # totalQty exceeds the desired number of dishes thus, assign 0 fitness
        if totalQty > genInfo["totalDishes"]:
            self.fitness = 0
            return self.fitness

        for i in genInfo["cuisines"]:
            tempQtyFit = (1/float(1+math.exp(-1*(cuisineQty[i]-1))))
            tempRatingFit = float(cuisineRating[i]/self.ratings)
            tempCostFit = float(cuisineCost[i]/self.cost)
            tempCuisineScoreFit = float(self.cuisineScore[i]/self.totCuisineScore)
            self.fitness += tempQtyFit*(tempRatingFit-tempCostFit)*tempCuisineScoreFit
            
        return self.fitness

    def getFitness(self):
        if not self.fitnessSet:
            self.fitness = float(self.calcFitness())
            self.fitnessSet = True
        return self.fitness
