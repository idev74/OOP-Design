from store import Store, store
import random

#Department
class Technology(Store):
    def __init__(self, name, employee_name, sq_ft, employee_num, stock):
        super().__init__(name, employee_name, sq_ft)
        self.employee_num = employee_num # protected; used in both groceries and technology
        self.stock = stock # protected; used in both groceries and technology

    """
    Returns a random coffee that the worker may or may not have spilled on the job
    """

    def cleaning(self): # private; unique list attribute
        drink = ['Pumpkin Spice Frappuccino', 'Salted Cream Cold Brew', 'Vanilla Latte', 'Medium Roast', 'Cappuccino']
        drink = random.choice(drink)
        return f'Wow, that worker really has to clean a {drink} off the phone display? Customers can be so messy.\n'
        
    """
    Introducing the employee name and store name
    """
    def intro(self): # protected; used in both groceries and technology
        return f"Welcome. My name is {self.employee_name}. Please do not abuse the {self.name} products.\nIf you do I won't hesistate to throw my coffee at you. I only have {self.stock} phones in the back.\n"
    
    """
    Capacity of the store
    """
    def get_capacity(self):  # protected; used in store, groceries, and product
        max_capacity = round(int(self.sq_ft) / 36) 
        customers = random.randint(5, max_capacity * 2)
        
        if customers > max_capacity:
            return f'Attention ladies and germs only {max_capacity} people are allowed in the {self.name} Department!\nWe already have {self.employee_num} employees helping my mom pick a phone case. Please come back later.\n'
        else:
            return f"{store.name}'s {self.name} department rarely restocks on airpod pros. As much as\nI want some, it's out of my control. Plus I don't get paid much for this.\n"
     

technology = Technology('electronics', 'Dani', 5000, 22, 5)
print(technology.cleaning())
print(technology.intro())
print(technology.get_capacity())