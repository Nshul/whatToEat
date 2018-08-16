import json
#from pprint import pprint

with open('sampleMenu.json') as menu_Data:
    menuData = json.load(menu_Data)


class Object(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
    pass


dishMap = Object()

for i in menuData:
    for j in menuData[i]:
        temp = j["dishID"]
        dishMap[temp] = {"dishName": j["dishName"], "restName": j["restName"],
                         "cuisine": i, "price": j["price"], "rating": j["rating"]}

# print dishMap

with open('dishMap.json', 'w') as outfile:
    json.dump(dishMap, outfile)
