import random
from store import store
from product import prod

class Cart():
    def __init__(self, location_num, order_id = ['#']):
        self.location_num = location_num # private; only used in cart
        self.order_id = order_id # private; only used in cart

    def get_items(self): # protected; shared between product and cart only
        order = prod.product
        return f'Your Items: {order}'

    def order_num(self): # private; uses unique order_id attribute
        for i in range(5):
            self.order_id.append(random.randint(0,9))
        self.order_id = (''.join(str(num) for num in self.order_id))
        return self.order_id

    def receipt(self): # protected; uses unique order_id attribute, but also takes from store
         return f"~ Order {self.order_id} from {store.name} location {self.location_num} is confirmed. Thank you for choosing us! ~"

new_order = Cart(10)
print(new_order.get_items())
new_order.order_num()
print(new_order.receipt())