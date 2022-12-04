import random

class Store:
    def __init__(self, name, sq_ft, employee_name):
        self.name = name
        self.sq_ft = sq_ft
        self.max_capacity = round(self.sq_ft / 36) 
        self.employee_name = employee_name
        self.cart = input('Do you want a shopping cart? Y/N: ')
        self.customers = random.randint(5, self.max_capacity * 2)


    """
    Need to retrieve and set the store/employee names in order to print a message when initialized.
    """
    def get_names(self):
        return self.name, self.employee_name
    
    """
    Introducing the employee name and store name
    """
    def get_cart(self):
        if self.cart.lower() == 'y':
            return f'Welcome to {self.name}, {self.employee_name} hands you a cart!'
        else:
            return f'Hi! I am {self.employee_name}. Here is a basket, then? Welcome to {self.name}!'
    
    """
    Capacity of the store
    """
    def get_capacity(self): 
        if self.customers > self.max_capacity:
            return f"Currently, {self.name}'s max capacity is {self.max_capacity} people ...since we recently got 'sued'.\nYou are going to have to wait in the storage room until some more people leave."
        else:
             return f"Currently, {self.name}'s max capacity is {self.max_capacity} people. Let me know if you see {self.max_capacity + 1}\n...I will take care of them"

        

store = Store('Target', 130000, 'Marty')
print(store.get_cart())
print(store.get_capacity())