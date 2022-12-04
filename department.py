# Isabella
from store import Store
from product import Product, new

class Department:
    prod = new.products

    dept_names = {
            'clothing': prod,
            'shoes': prod, 
            'baby items': prod,
            'groceries': prod,
            'electronics': prod, 
            'toys': prod,
            'customer service': None
    }

    def __init__(self, name, item_quantity):
        super(Store).__init__(name)
        self.item_quantity = item_quantity

    def selectName(self):
        selection = input('Choose a department')

    def get_quantity(self):
        pass

for dept in Department.dept_names:
    print(dept)
