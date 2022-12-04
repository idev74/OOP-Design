
from store import Store
# from product import Product

#Department
class Groceries(Store):
    def __init__(self, name, employee_num, stock, employee_name):
        super().__init__(name, employee_name)
        self.employee_num = employee_num
        self.stock = stock

    
#  both groceries and clothes are inheriting from the store class

    """
    Need to retrieve and set the store/employee names in order to print a message when initialized.
    """
    def get_names(self):
        return self.name, self.employee_name, self.employee_num, self.max_capacity
    
    """
    Introducing the employee name and store name
    """
    # def 

    # def get_cart(self):
    #     if cart.lower() == 'y':
    #         return f'Welcome to {self.name}, {self.employee_name} hands you a cart!'
    #     else:
    #         return f'Hi! I am {self.employee_name}. Here is a basket, then? Welcome to {self.name}!'
    
    # def intro(self):
        


    """
    Capacity of the store
    """
    def get_capacity(self): 
        if self.customers > self.max_capacity:
            return f"Currently, {self.name}'s max capacity is {self.max_capacity} people ...since we recently got 'sued'.\nYou are going to have to wait in the storage room until some more people leave."
        else:
             return f"Currently, {self.name}'s max capacity is {self.max_capacity} people. Let me know if you see {self.max_capacity + 1}\n...I will take care of them"
        

# store = Store('Target', 50000, 'Marty')
groceries = Groceries('hi', 'Marty', 1234, 5)
# groceries = Groceries('dairy', 'Isabella', 12, 50)
# print(groceries.get_capacity())
# print(groceries)

# class Department:
#     prod = new.products

#     dept_names = {
#             'clothing': prod,
#             'shoes': prod, 
#             'baby items': prod,
#             'groceries': prod,
#             'electronics': prod, 
#             'toys': prod,
#             'customer service': None
#     }

#     def __init__(self, name, item_quantity):
#         super(Store).__init__(name)
#         self.item_quantity = item_quantity

#     def selectName(self):
#         selection = input('Choose a department')

#     def get_quantity(self):
#         pass

# for dept in Department.dept_names:
#     print(dept)
