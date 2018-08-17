"""
Create Allele of Dish for Chromosome
"""
import json

# Load the dishMap file so as to map dishes with id
with open('../dishMap.json') as menu_Data:
    menuData = json.load(menu_Data)


class Dish:
    """
    Allele in chromosome consists of this Dish which has
    id -> Dish ID
    qty -> Quantity of this Dish
    """
    # Assign the Allele with DishID and Quantity in suggestion
    def __init__(self, id, qty):
        self.id = id
        self.qty = qty

    # Return Quantity of current Dish
    def Quantity(self):
        return self.qty

    # Return the information of the dish
    def __repr__(self):
        dishId = "Dish Id:"+str(self.id)
        dishname = "Dish Name:"+str(menuData[self.id]["dishName"])
        restname = "Restaurant Name:"+str(menuData[self.id]["restName"])
        price = "Price:"+str(menuData[self.id]["price"])
        rating = "Rating:"+str(menuData[self.id]["rating"])
        quantity = "Quantity:" + str(self.qty)
        totCost = "Total Cost:" + str(menuData[self.id]["price"]*self.qty)
        return '%s %s %s %s %s %s %s'%(dishId,dishname,restname,price,rating,quantity,totCost)
