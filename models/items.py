from models.item import *

item1 = Item("Milk", 1, 1, False)
item2 = Item("Jelly", 2, 4, False)
item3 = Item("Carton of Eggs", 3, 2, True)

list_of_items = [item1, item2, item3]

def add_new_item(item):
    list_of_items.append(item)

def total_cost_items(list):
    res = 0
    for item in list:
        if item.discounted == 0:
            res += item.total
        else:
            res += (item.discounted * item.quantity)
    return res

def total_number(list):
    return len(list)



def show_bought(list):
    bought = []
    for item in list:
        if item.bought_status == True:
            bought.append(item)
    return bought

def show_not_bought(list):
    not_bought = []
    for item in list:
        if item.bought_status == False:
            not_bought.append(item)
    return not_bought

def delete_item(name):
    item_to_delete = None
    for item in list_of_items:
        if item.name_of_item == name:
            item_to_delete = item
            break
    list_of_items.remove(item_to_delete)\

def apply_discount(list):
    for item in list:
        if item.quantity >= 5: 
            item.discounted = int(item.price_of_item)*.8
