import json

with open('dishMap.json') as menu_Data:
    menuData = json.load(menu_Data)

class Dish:
    def __init__(self, id, qty):
        self.id = id
        self.qty = qty
        

    def __repr__(self):
        return "Dish Name:"+str(menuData[self.id]["dishName"])+" Restaurant Name:"+str(menuData[self.id]["restName"])+" Price:"+str(menuData[self.id]["price"])+" Rating:"+str(menuData[self.id]["rating"])
