'''
Product inside the Department
'''

import random

class Product:
    def __init__(self, price):
        self.price = price


    def _insert_obj(self):
        self.product.append(self.name)
        return self.product

    def random_item(self):
        groceries = ['Ketchup', 'Bread', 'Rice', 'Soup', 'Milk', 'Chips']
        clothes = ['Levi', 'Nike', 'Converse', 'Adidas']
        product_dept = ['Groceries', 'Clothing'] 
        product = []
        chosen = input('Please choose a department (Groceries or Clothing):')
        
        for num, department in enumerate(product_dept):
            chosen += f'{num+1}) {department}\n'
            # chosen += f'{num+1}) {department}\n'

            chosen += f'Getting your items from the {department} department...'

            if department == product_dept[0]:
                item = random.choice(groceries)
                product.append(item)
                return product

            elif department == product_dept[1]:
                item = random.choice(clothes)
                product.append(item)
                return product

        while user_input.lower() not in product_dept:
            user_input = input(chosen)

prod = Product(3)
print(prod.random_item())
