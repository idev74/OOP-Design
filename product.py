'''
Product inside the Department
'''

import random

class Product:
    def __init__(self, price):
        self.price = price
        self.groceries = ['Ketchup', 'Bread', 'Rice', 'Soup', 'Milk', 'Chips']
        self.clothes = ['Levi', 'Nike', 'Converse', 'Adidas']
        self.product_dept = ['groceries', 'clothing'] 
        self.product = []

    def insert_obj(self):
        self.product.append(self.name)
        return self.product

    def random_item(self):
        chosen = input('Please choose a department (Groceries or Clothing): ').lower()
        while chosen in self.product_dept:
            if chosen == self.product_dept[0]:
                item = random.choice(self.groceries)
                self.product.append(item)

            elif chosen == self.product_dept[1]:
                item = random.choice(self.clothes)
                self.product.append(item)
            return self.product

        while chosen not in self.product_dept:
            return f'Please choose from one of the listed departments.'
        
prod = Product(3)
print(prod.random_item())
