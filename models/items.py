from models.item import *

item1 = Item("Milk", 1, 1, False)
item2 = Item("Jelly", 2, 4, False)
item3 = Item("Carton of Eggs", 3, 2, False)

items = [item1, item2, item3]

def add_new_item(item):
    items.append(item)

