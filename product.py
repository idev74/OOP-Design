'''
Product inside the Department
'''

import random

class Product:
    def __init__(self, price, product = []):
        self.price = price
        self.product = product

    def insert_obj(self):
        object = input('Enter the name of your item and we will add that to your order: ')
        self.product.append(object)
        return f'{self.product}\n'

    def random_item(self):
        groceries = ['Ketchup', 'Bread', 'Rice', 'Soup', 'Milk', 'Chips', 'Beans', 'Sparkling Water', 'Soda', 'Lettuce', 'Grapes', 'Bottled Water']
        clothes = ['Levi Shorts', 'Tank Top', 'Graphic Tee', 'Leggings', 'Mom Jeans', 'Crew Socks', 'Button Up', 'Pajama Pants', 'Baseball Cap', 'Belt']
        product_dept = ['groceries', 'clothing'] 
        chosen = input('Please choose a department (Groceries or Clothing): ').lower()
        while chosen in product_dept:
            if chosen == product_dept[0]:
                item = random.choice(groceries)
                self.product.append(item)

            elif chosen == product_dept[1]:
                item = random.choice(clothes)
                self.product.append(item)
            return self.product

        while chosen not in product_dept:
            return f'Please choose from one of the listed departments.'
        
prod = Product(3)
print(prod.insert_obj())
print(prod.random_item())
