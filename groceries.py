
from store import Store, store
import random

#Department
class Groceries(Store):
    def __init__(self, name, employee_name, sq_ft, employee_num, stock):
        super().__init__(name, employee_name, sq_ft)
        self.employee_num = employee_num
        self.stock = stock

    
#  both groceries and clothing are inheriting from the store class

    """
    Need to retrieve and set the store/employee names in order to print a message when initialized.
    """
    def get_names(self):
        return self.name, self.employee_name, self.employee_num
   
    """
    Introducing the employee name and store name
    """
    def intro(self):
        return f'Welcome. My name is {self.employee_name}. Please do not throw our {self.name} PREMIUM tomatoes at me.\nWe only have {self.stock} in stock and I get hungry.\n'
    
    """
    Capacity of the store
    """
    def get_capacity(self): 
        max_capacity = round(int(self.sq_ft) / 36) 
        customers = random.randint(5, max_capacity * 2)
        if customers > max_capacity:
            return f'Out of the {self.employee_num} people working this department, not one of them has told you \nthat this area has a max capacity of {max_capacity} shoppers?! Get in the storage warehouse...\n'
        else:
                return f"{store.name} {store.name} really prides itself on its grocery department. Almost as much as we\npride ourselves on fire safety! Seriously, only {max_capacity} people allowed in these food aisles.\nLet me know if you spot any rebels.\n"
   

        
  

groceries = Groceries('produce', 'Isabella', 1234, 20, 5)
print(groceries.intro())
print(groceries.get_capacity())
