import json

# Import the dish mapping
with open('dishMap.json') as menu_Data:
    menuData = json.load(menu_Data)


class Fitness:
    # Define the characteristics required to calculate the fitness function
    def __init__(self, dishes):
        self.dishes = dishes
        self.ratings = 0
        self.cost = 0
        self.cuisines = 0
        self.fitness = 0

    # Calculate Fitness for a Chromosome
    def calcFitness(self):
        cuisinePresent = {"indian": False, "afghani": False,
                          "italian": False, "chinese": False}
        totQty = 0
        for i in range(0, len(self.dishes)):
            dishId = self.dishes[i].id
            quantity = self.dishes[i].qty
            if quantity > 0:
                totQty += quantity
                self.ratings += menuData[dishId]["rating"]
                self.cost += menuData[dishId]["price"]*quantity
                if cuisinePresent[menuData[dishId]["cuisine"]] == False:
                    cuisinePresent[menuData[dishId]["cuisine"]] = True
                    self.cuisines += 1
        self.fitness = self.ratings - self.cost/float(totQty*100) + self.cuisines
        return self.fitness

    def getFitness(self):
        if self.fitness == 0:
            self.fitness = float(self.calcFitness())
        return self.fitness
