# Marty

class Store:
    def __init__(self, name, sq_ft):
        self.name = name
        self.sq_ft = sq_ft
        self.max_capacity = round(self.sq_ft / 36) 

    # Department has products
    def get_name(self):
        print('Please enter your store name: ')
        return self.name
        
    def get_capacity(self): 
        return f"{self.name}'s max capacity is {self.max_capacity}"


store = Store('Target', 50000)
print(store.get_name())
print(store.get_capacity())