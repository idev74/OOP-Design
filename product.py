# Marty

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.products = []

    def _insert_obj(self):
        self.products.append(self.name)
        return self.products

new = Product('toy', 4)
print(new._insert_obj())