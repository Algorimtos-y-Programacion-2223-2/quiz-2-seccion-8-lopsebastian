class Productos(): 
    def __init__(self, name, type, stock, price): 
        self.name = name
        self.type = type
        self.stock = stock
        self.price = price

    def show(self): 
        print(f" Nombre: {self.name}, Tipo = {self.type}, Stock = {self.stock}, Precio = {self.price}")