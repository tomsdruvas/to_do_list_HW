class Item():
    def __init__(self, name_of_item, price_of_item, quantity, bought_status):
        self.name_of_item = name_of_item
        self.price_of_item = price_of_item
        self.quantity = int(quantity)
        self.bought_status = bought_status
        self.total = int(price_of_item)*int(quantity)
        self.discounted = int(0)