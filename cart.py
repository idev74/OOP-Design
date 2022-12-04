import random
from store import Store, store 

class Cart():
    def __init__(self, quantity, item, id =''):
        self.quantity = quantity
        self.item = item
        self.id = id

    def order_id(self):
        for i in range(5):
            self.id.append(random.randint(0,9))
            return self.id.join('')

    def add_item(self):
        
        pass

    def receipt(self):
        print(f"Here's your order info from {store.name} {self.id}")

hi = Cart(10, 'item')
hi.receipt()