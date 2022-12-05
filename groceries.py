from store import Store, store
import random

#Department
class Groceries(Store):
    def __init__(self, name, employee_name, sq_ft, employee_num, stock):
        super().__init__(name, employee_name, sq_ft)
        self.employee_num = employee_num # protected; used in both groceries and technology
        self.stock = stock; # protected; used in both groceries and technology


    """
    Picks a random place for the worker to take a break.
    """    
    def on_break(self): # private; unique list attribute
        room = ['Storage', 'Fitting Room', 'Break Room', 'Bathroom', 'Dollar Section']
        room = random.choice(room)
        return f"Man, I can't wait to go to {room} and take my break..."

    """
    Introducing the employee name and store name
    """
    def intro(self): # protected; used in both groceries and technology
        return f'Welcome. My name is {self.employee_name}. Please do not throw our {self.name} PREMIUM tomatoes at me.\nWe only have {self.stock} in stock and I get hungry.\n'
    
    """
    Capacity of the store
    """
    def get_capacity(self): # protected; used in store, groceries, and product
        max_capacity = round(int(self.sq_ft) / 36) 
        customers = random.randint(5, max_capacity * 2)
        if customers > max_capacity:
            return f'Out of the {self.employee_num} people working this department, not one of them has told you \nthat this area has a max capacity of {max_capacity} shoppers?! Get in the storage warehouse...\n'
        else:
            return f"{store.name} grocery really prides itself on its {self.name} department. Almost as much as we\npride ourselves on fire safety! Seriously, only {max_capacity} people allowed in these food aisles.\nLet me know if you spot any rebels.\n"
    

groceries = Groceries('produce', 'Isabella', 1234, 20, 5)
print(groceries.on_break())
print(groceries.intro())
print(groceries.get_capacity())