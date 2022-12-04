import random

class Store:
    def __init__(self, name, employee_name, sq_ft):
        self.name = name
        self.employee_name = employee_name
        self.sq_ft = sq_ft


    """
    Need to retrieve and set the store/employee names in order to print a message when initialized.
    """
    def get_names(self):
        return self.name, self.employee_name
    
    """
    Introducing the employee name and store name
    """
    def get_cart(self):
        cart = input('Do you want a shopping cart? Y/N: ')
        if cart.lower() == 'y':
            return f'Welcome to {self.name}, {self.employee_name} hands you a cart!'
        else:
            return f'Hi! I am {self.employee_name}. Here is a basket, then? Welcome to {self.name}!'
    
    """
    Capacity of the store
    """
    def get_capacity(self): 
        max_capacity = round(int(self.sq_ft) / 36) 
        customers = random.randint(5, max_capacity * 2)
        if customers > max_capacity:
            return f"Currently, {self.name}'s max capacity is {max_capacity} people ...since we recently got 'sued'.\nYou are going to have to wait in the storage room until some more people leave."
        else:
             return f"Currently, {self.name}'s max capacity is {max_capacity} people. Let me know if you see {max_capacity + 1}\n...I will take care of them"

        

store = Store('Target', 'Marty', 130000)
print(store.get_cart())
print(store.get_capacity())