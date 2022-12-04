# Isabella

import random

class Cart:
    def __init__(self, quantity, id):
        self.quantity = quantity
        self.id = id

    def order_id(self):
        item = random.randint(0,9)
        return item

    def add_items(self):
        pass

    def receipt(self):
        print(f'')